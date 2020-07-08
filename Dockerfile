FROM python:3.7.3-slim-stretch AS base

MAINTAINER Shin Eunju <eunjuoi0515@gmail.com>

ENV RUN_ENV prod
ENV SERVICE_NAME samoyed
ENV DATABASE_URL $DATABASE_URL
ENV JWT_SECRET_KEY $JWT_SECRET_KEY

COPY . .
WORKDIR .

RUN apt-get update && \
    apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    gcc

RUN pip install -r requirements.txt

CMD ["-m", "samoyed"]
EXPOSE 80
ENTRYPOINT ["python"]