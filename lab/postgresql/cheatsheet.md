
## EXAMPLE SYNTAX 

CREATE USER "admin" WITH SUPERUSER PASSWORD 'admin';
CREATE DATABASE "ITVP23" OWNER "admin";
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    post_timestamp TIMESTAMP NOT NULL,
    post_data JSON NOT NULL
);

## LIST DATABASE TABLES
\dt  
## LIST DATABASE USERS       
\du       
## LIST DATABASES 
\l     
## SWITCH DATABASE
\c <database_name>     
