# E/R Diagram

![1780310677306](image/er-diagram/1780310677306.png)

## Description

The database consists of three main tables:

* Assets stores the available investment assets and their metadata such as ticker, sector, country, and risk level.
* Recommendation_Request stores each investment recommendation request made by the user.
* Recommendation_Items stores the generated allocation items for each request.

Each recommendation request can generate multiple recommendation items.
Each recommendation item references exactly one asset and one recommendation request.

The database also defines the SQL view vw_assets, which exposes the asset fields used by the filtering page.
