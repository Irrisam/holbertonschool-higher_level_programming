-- create database and user 
CREATE DATABASE IF NOT EXISTS htbn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON '.' TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
