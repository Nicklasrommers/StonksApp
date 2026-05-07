#!/bin/bash

cd /code/InvestmentHelper/utils

python init_db.py

cd /code/InvestmentHelper

flask run --host=0.0.0.0
