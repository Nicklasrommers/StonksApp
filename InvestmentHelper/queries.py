from InvestmentHelper import conn, db_cursor
from InvestmentHelper.models import Asset, RecommendationItem, RecommendationRequest


def _empty_to_none(value):
    return value if value not in (None, '', 'all') else None


def get_assets_by_filters(asset_type=None, country=None, sector=None, risk_level=None, search_pattern=None, limit=None):
    sql = """
    SELECT *
    FROM vw_assets
    WHERE (%s IS NULL OR asset_type = %s)
      AND (%s IS NULL OR country = %s)
      AND (%s IS NULL OR sector = %s)
      AND (%s IS NULL OR risk_level <= %s)
      AND (%s IS NULL OR ticker ~* %s OR name ~* %s OR sector ~* %s)
    ORDER BY risk_level, expense_ratio, ticker
    """
    params = (
        _empty_to_none(asset_type), _empty_to_none(asset_type),
        _empty_to_none(country), _empty_to_none(country),
        _empty_to_none(sector), _empty_to_none(sector),
        _empty_to_none(risk_level), int(risk_level) if _empty_to_none(risk_level) else None,
        _empty_to_none(search_pattern), _empty_to_none(search_pattern),
        _empty_to_none(search_pattern), _empty_to_none(search_pattern),
    )
    if limit:
        sql += " LIMIT %s"
        params += (limit,)
    db_cursor.execute(sql, params)
    return [Asset(row) for row in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []


def insert_recommendation_request(request_data):
    request_model = RecommendationRequest(request_data)
    sql = """
    INSERT INTO RecommendationRequests(amount, risk_level, asset_type, country, sector, search_pattern)
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING pk
    """
    db_cursor.execute(sql, (
        request_model.amount,
        request_model.risk_level,
        _empty_to_none(request_model.asset_type),
        _empty_to_none(request_model.country),
        _empty_to_none(request_model.sector),
        _empty_to_none(request_model.search_pattern),
    ))
    conn.commit()
    return db_cursor.fetchone()['pk']


def insert_recommendation_item(request_pk, asset_pk, allocated_amount):
    sql = """
    INSERT INTO RecommendationItems(request_pk, asset_pk, allocated_amount)
    VALUES (%s, %s, %s)
    """
    db_cursor.execute(sql, (request_pk, asset_pk, allocated_amount))
    conn.commit()


def create_recommendation(request_data):
    request_pk = insert_recommendation_request(request_data)
    assets = get_assets_by_filters(
        asset_type=request_data.get('asset_type'),
        country=request_data.get('country'),
        sector=request_data.get('sector'),
        risk_level=request_data.get('risk_level'),
        search_pattern=request_data.get('search_pattern'),
        limit=4,
    )
    if not assets:
        return []

    allocation = round(float(request_data.get('amount')) / len(assets), 2)
    for asset in assets:
        insert_recommendation_item(request_pk, asset.pk, allocation)
    return get_recommendation_items(request_pk)


def get_recommendation_items(request_pk):
    sql = """
    SELECT ri.pk, ri.request_pk, ri.asset_pk, ri.allocated_amount,
           a.ticker, a.name, a.asset_type, a.country, a.sector, a.risk_level
    FROM RecommendationItems ri
    JOIN Assets a ON a.pk = ri.asset_pk
    WHERE ri.request_pk = %s
    ORDER BY ri.allocated_amount DESC, a.ticker
    """
    db_cursor.execute(sql, (request_pk,))
    return [RecommendationItem(row) for row in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
