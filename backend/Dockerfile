FROM python:3.12-slim

# Zainstaluj systemowe zależności dla psycopg2 (Postgres)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Katalog roboczy
WORKDIR /app

# Kopiujemy plik requirements.txt i instalujemy zależności
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Informacyjnie — Django będzie nasłuchiwał na porcie 8000
EXPOSE 8000

