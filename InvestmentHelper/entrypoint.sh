#!/bin/sh

set -eu

python /app/InvestmentHelper/utils/init_db.py

python -m flask --app InvestmentHelper.app run --host=0.0.0.0 --port=8000
