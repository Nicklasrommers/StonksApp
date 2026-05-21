import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask
from psycopg2.extras import RealDictCursor

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

conn = psycopg2.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    port=os.getenv('DB_PORT', '5432'),
    database=os.getenv('DB_NAME', 'InvestmentHelper'),
    user=os.getenv('DB_USERNAME', 'postgres'),
    password=os.getenv('DB_PASSWORD', 'postgres'),
)

db_cursor = conn.cursor(cursor_factory=RealDictCursor)

from InvestmentHelper import filters
from InvestmentHelper.blueprints.investment.routes import investment

app.register_blueprint(investment)
