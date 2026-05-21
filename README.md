# Investment Helper

Investment Helper is a small Flask and PostgreSQL web app for the DIS database project.
It stores a small universe of investment assets and generates simple allocation suggestions
from amount, maximum risk, investment type, country, sector and an optional regex search pattern.

## Dataset

The asset data is stored in `InvestmentHelper/dataset/assets.csv`.

The data comes from Yahoo Finance and JustETF. We manually collected the data and combined it
into one CSV file, where we adapted it to the fields required by the application.

## Recommended Setup

Requirements:

- Git
- Docker Desktop, or Docker Engine with Docker Compose

Clone the repository:

```shell
git clone https://github.com/Nicklasrommers/StonksApp.git
cd StonksApp
```

Start the app:

```shell
docker compose up --build
```

Open the web app at:

```text
http://127.0.0.1:8000
```

Stop the app with `CTRL+C`. To remove the stopped containers afterwards:

```shell
docker compose down
```

The database is initialized automatically from `InvestmentHelper/utils/schema.sql` and
`InvestmentHelper/dataset/assets.csv` when the web container starts.

The environment variables used by Docker are defined in `docker-compose.yml`. A matching example
is available in `InvestmentHelper/.env.example` for reference.

If the browser shows a blank page, make sure you are opening `http://127.0.0.1:8000`.
The Flask app runs on port `8000` inside Docker and Docker publishes the same port on your computer.

## How To Use The App

- `/` and `/home`: front page
- `/assets`: filter assets in the database
- `/recommendations`: generate and store an investment suggestion
- `/about`: short project description

On the assets page, users can filter by investment type, country, sector, maximum risk and a
regular expression search pattern. On the recommendations page, users enter an amount and
preferences, and the app returns up to four suggested assets with weighted allocations.

## Database Model

The E/R diagram is in [`docs/er-diagram.md`](docs/er-diagram.md).

The schema is in `InvestmentHelper/utils/schema.sql`. It defines:

- `Assets`
- `RecommendationRequests`
- `RecommendationItems`
- the SQL view `vw_assets`

The web app interacts with the database through SQL in `InvestmentHelper/queries.py`.
It uses `SELECT` queries to filter assets and `INSERT` queries to store recommendation requests
and generated recommendation items.

The app also performs regular expression matching through PostgreSQL's case-insensitive regex
operator `~*` in the asset search.

## AI Declaration

AI assistance was used to help restructure the starting example into this project skeleton.
