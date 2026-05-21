FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY InvestmentHelper/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY InvestmentHelper /app/InvestmentHelper

ENTRYPOINT ["sh", "/app/InvestmentHelper/entrypoint.sh"]
