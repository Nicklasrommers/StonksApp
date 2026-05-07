DROP TABLE IF EXISTS RecommendationItems;
DROP TABLE IF EXISTS RecommendationRequests;
DROP TABLE IF EXISTS Assets CASCADE;

CREATE TABLE IF NOT EXISTS Assets(
    pk serial PRIMARY KEY,
    ticker varchar(20) UNIQUE NOT NULL,
    name varchar(120) NOT NULL,
    asset_type varchar(30) NOT NULL,
    country varchar(40) NOT NULL,
    sector varchar(60) NOT NULL,
    risk_level integer NOT NULL CHECK (risk_level BETWEEN 1 AND 5),
    expense_ratio numeric(6, 4) NOT NULL DEFAULT 0
);

CREATE INDEX IF NOT EXISTS assets_filter_index
ON Assets(asset_type, country, sector, risk_level);

CREATE TABLE IF NOT EXISTS RecommendationRequests(
    pk serial PRIMARY KEY,
    amount numeric(12, 2) NOT NULL CHECK (amount > 0),
    risk_level integer NOT NULL CHECK (risk_level BETWEEN 1 AND 5),
    asset_type varchar(30),
    country varchar(40),
    sector varchar(60),
    search_pattern varchar(120),
    created_at timestamp NOT NULL DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS RecommendationItems(
    pk serial PRIMARY KEY,
    request_pk integer NOT NULL REFERENCES RecommendationRequests(pk) ON DELETE CASCADE,
    asset_pk integer NOT NULL REFERENCES Assets(pk) ON DELETE CASCADE,
    allocated_amount numeric(12, 2) NOT NULL CHECK (allocated_amount > 0)
);

CREATE OR REPLACE VIEW vw_assets
AS
SELECT pk, ticker, name, asset_type, country, sector, risk_level, expense_ratio
FROM Assets;
