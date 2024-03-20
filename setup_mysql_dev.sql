-- A Script that prepares a MySQL server for the project

-- firstly creare the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
-- then update the database with the user and password and host
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Then Grant privilege to the expected database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT SHOW DATABASES ON *.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
