FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /app
COPY . /app

RUN "./dependencies.sh"

COPY postgresql/configuration/pg_hba.conf /etc/postgresql/14/main/pg_hba.conf
COPY postgresql/configuration/postgresql.conf /etc/postgresql/14/main/postgresql.conf

CMD service postgresql start && /bin/bash