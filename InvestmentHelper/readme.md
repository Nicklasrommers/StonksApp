# Investment Helper

Investment Helper is a small Flask + PostgreSQL web app for the DIS database project.
It stores a small universe of investment assets and generates simple allocation suggestions
from amount, maximum risk, investment type, country, sector and an optional regex search pattern.

## Setup

Install dependencies:

``` shell
pip install -r requirements.txt
```

Create a PostgreSQL database named `InvestmentHelper`, then configure `.env`:

``` text
SECRET_KEY=dev-secret-key
DB_USERNAME=postgres
DB_PASSWORD=<your_password>
DB_NAME=InvestmentHelper
```

Initialize the database:

``` shell
python utils\init_db.py
```

Run the app from this folder:

``` shell
flask --app app run
```

## Routes

- `/` and `/home`: front page
- `/assets`: filter assets in the database
- `/recommendations`: generate and store an investment suggestion
- `/about`: short project description

## Database

The schema is in `utils/schema.sql` and the seed data is in `dataset/assets.csv`.
The app uses SQL `SELECT` and `INSERT`, plus the PostgreSQL regex operator `~*` in the asset search.
It also defines the view `vw_assets`.

## AI Declaration

AI assistance was used to help restructure the starting example into this project skeleton.
