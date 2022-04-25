FROM python:3.10

ENV ENV_FOR_DYNACONF docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /weather

COPY Pipfile Pipfile.lock /weather/
RUN pip install pipenv && pipenv install --system

COPY . /weather/

RUN chmod +x ./psql-migrations.sh
ENTRYPOINT [ "./psql-migrations.sh" ]