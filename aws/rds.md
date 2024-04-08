# Aws RDS with postgresql

## Connect

* install psql
```bash
holawhich psql
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

* check service name and start it 
```bash
sudo systemctl list-unit-files | grep postgres
sudo systemctl start <service-name>
# Enable automatic start
sudo systemctl enable <service-name>
```

* connect to the sql database from EC2
```
psql -h <rds-endpoint> -U <username> -d <database>
```

* change psql configurations to allow access from everywhere
```
# version is normally 14
sudo nano /etc/postgresql/<version>/main/postgresql.conf
# comment out and change the following line to
listen_addresses = '*'
sudo systemctl restart postgresql
```

* check the status:
```
sudo systemctl status postgresql
```

## Problem connecting with users:

* you have to add at this path:
`sudo nano /etc/postgresql/14/main/pg_hba.conf` this line: `host  all       postgres       93.70.92.176/32        md5`

in order to allow login from the ip address specified (my local machine)

* then default login is:
`local   all     postgres   peer`, that means you first have to change to user postgres before the log in (sudo -i -u postgres). Then you have to change from peer to md5 to be able to connect with another password, from another user. The problem is if the password is not set, because it will require a password, but none is set. In this case, when logged in the database, you have to reset the password: `ALTER ROLE postgres PASSWORD 'your_password';`

* Always remember to restart the service with systemctl

* to log in from your local machine:
```
psql -h ec2-3-79-39-126.eu-central-1.compute.amazonaws.com -U postgres -d postgres
```

* new pw and db and user are:
postgres


 