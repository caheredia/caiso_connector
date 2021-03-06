FROM python:3.8.3-slim-buster
COPY ["pyproject.toml", "poetry.lock" , "./"]
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install gcc
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN pip install --upgrade pip
RUN pip install poetry==1.0.3
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi
EXPOSE 80
CMD uvicorn --host 0.0.0.0 --port 80 app.main:app
