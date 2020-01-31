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

CMD cron \
    # add cron job
    && python3 -m src.cron_jobs.run_cron >> /etc/cron.d/date_cron \
    # apply cron job
    && crontab /etc/cron.d/date_cron \
    && echo $(/etc/init.d/cron status) \
    && uvicorn --host 0.0.0.0 --port 80 app.main:app