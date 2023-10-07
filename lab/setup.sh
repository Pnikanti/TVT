# !/bin/bash

echo "> Setting up a lab environment"
echo ">> Installing dependencies"

apt-get update && \
apt-get install -y --fix-missing \
    python3 \
    python3-pip \
    git \
    postgresql \
    postgresql-contrib \
    build-essential \
    nano \
    net-tools

echo ">> Setting symlinks"
ln -s /usr/bin/python3 /usr/bin/python

echo ">> Installing Python packages"
python -m pip install -r requirements.txt

echo ">> Copying predefined settings"
cp -r -t /etc/postgresql/14/main/ postgresql/configuration/*

echo ">> Copying scripts"
mkdir /opt/psql && cp -r -t /opt/psql postgresql/*

#echo ">> Copying cron jobs"
#cp -r -t cron/* /etc/cron.hourly && chmod -R +x /etc/cron.hourly

echo ">> Running psql bootstrap"
python /opt/psql/bootstrap.py iknowwhatiamdoing d13ict || true
