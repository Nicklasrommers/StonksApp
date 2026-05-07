FROM python:3.9-alpine
WORKDIR /code
RUN mkdir InvestmentHelper
RUN apk add --no-cache gcc musl-dev linux-headers postgresql postgresql-contrib libpq-dev bash musl-dev gcc libffi-dev g++
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["./InvestmentHelper/entrypoint.sh"]
