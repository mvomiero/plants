# Database

### to do:
move pw and user and the informations to the hidden .env file. That means that the server then has to be recreated (when you access the pgAdmin broswer page)

## Usage 

### Access pg admin broswer:   
_http://localhost:5050_

### Access DataBase CLI and execute queries

* access the CLI of the database, from here you can do whatever query
```bash
psql -h localhost -U postgres -d postgres -p 5432 -W

```
* see for example the existing tables 
```bash
\dt
```

* exit
```bash
\q
``````



### start and stop the containers:

```bash
docker-compose up -d
```
```bash
docker-compose down
```

## Reference project:

[Medium project containers db + pg Admin web interface](https://medium.com/@jewelski/quickly-set-up-a-local-postgres-database-using-docker-5098052a4726)

## Settings

*from chatGPT*

### Setttings when creating a new server in pgAdmin


To view your PostgreSQL database and the example table you created in pgAdmin, follow these steps:

Access pgAdmin:

Open your web browser and navigate to http://localhost:5050. Log in with the email and password you provided in the docker-compose.yml file.

Add PostgreSQL Server:

In pgAdmin, on the left sidebar, right-click on "Servers" and choose "Create" > "Server..."
In the "General" tab, provide a name for the connection.
In the "Connection" tab:
Hostname/address: postgres
Port: 5432
Maintenance database: postgres
Username: postgres
Password: mysecretpassword (or the password you set)
Click "Save" to add the PostgreSQL server.

View Database and Table:

On the left sidebar, expand "Servers" and your newly added server.
Navigate to "Databases" and select the postgres database.
Expand "Schemas" > "public" > "Tables" to see your tables.



