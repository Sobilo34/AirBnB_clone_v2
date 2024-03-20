-- A Script that prepares a MySQL server for the project

-- firstly creare the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- then update the database with the user, password and host
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Then Grant privilege to the expected database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
