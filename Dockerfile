FROM python:3.7-slim-buster
COPY . .
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install gcc \
    && apt-get -y install cron \
    && apt-get -y install nano \
    && apt-get install -y sqlite3 libsqlite3-dev \
    && pip install --upgrade pip \
    && pip install poetry==0.12.17 \
    && poetry config settings.virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
EXPOSE 80
CMD cron
CMD python3 -m src.cron_jobs.run_cron
CMD uvicorn --host 0.0.0.0 --port 80 app.main:app