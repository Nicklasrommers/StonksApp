import csv
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


if __name__ == '__main__':
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'InvestmentHelper'),
        user=os.getenv('DB_USERNAME', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres'),
    )

    base_dir = os.path.dirname(__file__)
    dataset_path = os.path.join(base_dir, '..', 'dataset', 'assets.csv')

    with conn.cursor() as cur:
        with open(os.path.join(base_dir, "schema.sql"), encoding='utf-8') as db_file:
            cur.execute(db_file.read())

        with open(dataset_path, newline='', encoding='utf-8') as csv_file:
            rows = list(csv.DictReader(csv_file))

        values = [
            (
                row['ticker'],
                row['name'],
                row['asset_type'],
                row['country'],
                row['sector'],
                int(row['risk_level']),
                float(row['expense_ratio']),
            )
            for row in rows
        ]
        args = ','.join(cur.mogrify("(%s, %s, %s, %s, %s, %s, %s)", value).decode('utf-8') for value in values)
        cur.execute("""
            INSERT INTO Assets(ticker, name, asset_type, country, sector, risk_level, expense_ratio)
            VALUES
        """ + args)
        conn.commit()

    conn.close()
