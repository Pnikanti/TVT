FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /app
COPY ./ /app/

RUN "./setup.sh"
CMD service postgresql start && /bin/bash