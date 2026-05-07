from typing import Dict


class ModelMixin(dict):
    """Dictionary-backed model with attribute access for templates."""

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as exc:
            raise AttributeError(item) from exc


class Asset(ModelMixin):
    def __init__(self, asset_data: Dict):
        super().__init__(asset_data)
        self.pk = asset_data.get('pk')
        self.ticker = asset_data.get('ticker')
        self.name = asset_data.get('name')
        self.asset_type = asset_data.get('asset_type')
        self.country = asset_data.get('country')
        self.sector = asset_data.get('sector')
        self.risk_level = asset_data.get('risk_level')
        self.expense_ratio = asset_data.get('expense_ratio')


class RecommendationRequest(ModelMixin):
    def __init__(self, request_data: Dict):
        super().__init__(request_data)
        self.pk = request_data.get('pk')
        self.amount = request_data.get('amount')
        self.risk_level = request_data.get('risk_level')
        self.asset_type = request_data.get('asset_type')
        self.country = request_data.get('country')
        self.sector = request_data.get('sector')
        self.search_pattern = request_data.get('search_pattern')


class RecommendationItem(ModelMixin):
    def __init__(self, item_data: Dict):
        super().__init__(item_data)
        self.pk = item_data.get('pk')
        self.request_pk = item_data.get('request_pk')
        self.asset_pk = item_data.get('asset_pk')
        self.allocated_amount = item_data.get('allocated_amount')
        self.ticker = item_data.get('ticker')
        self.name = item_data.get('name')
        self.asset_type = item_data.get('asset_type')
        self.country = item_data.get('country')
        self.sector = item_data.get('sector')
        self.risk_level = item_data.get('risk_level')
