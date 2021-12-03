CREATE DATABASE flaskapp_dev CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER user@localhost IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON flaskapp_dev.* TO user@localhost;
FLUSH PRIVILEGES;
