sudo apt-get update
sudo apt-get -y install python-pip python-dev build-essential libfreetype6 libfontconfig1 libpq-dev
sudo apt-get -y install postgresql-9.3 postgresql-client-9.3
sudo echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf
sudo echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf
sudo service postgresql start &&\
    sudo -u postgres psql --command "CREATE USER onhands WITH SUPERUSER PASSWORD 'onhands';" &&\
    sudo -u postgres createdb -O onhands onhands &&\
    service postgresql stop

sudo pip install -r requirements.txt
