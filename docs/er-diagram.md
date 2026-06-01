# E/R Diagram

```mermaid
ASSETS ||--o{ RECOMMENDATION_ITEMS : contains
    RECOMMENDATION_REQUESTS ||--o{ RECOMMENDATION_ITEMS : generates

    ASSETS {
        int asset_id PK
        varchar ticker UK
        varchar name
        varchar asset_type
        varchar country
        varchar sector
        integer risk_level
        numeric expense_ratio
    }

    RECOMMENDATION_REQUESTS {
        int request_id PK
        numeric amount
        integer risk_level
        varchar asset_type
        varchar country
        varchar sector
        varchar search_pattern
        timestamp created_at
    }

    RECOMMENDATION_ITEMS {
        int item_id PK
        integer request_pk FK
        integer asset_pk FK
        numeric allocated_amount
    }
```

## Description

The database has three main tables:

- `Assets` stores the available investment assets.
- `RecommendationRequests` stores each user request for an investment suggestion.
- `RecommendationItems` stores the generated allocation lines for each request.

Each recommendation request can generate many recommendation items. Each recommendation item points to one asset and one recommendation request.

The database also defines the SQL view `vw_assets`, which exposes the asset fields used by the filtering page.
