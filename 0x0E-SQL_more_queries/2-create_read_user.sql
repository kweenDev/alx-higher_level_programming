-- SQL script to create database and user with SELECT privilege
-- Create database hbtn_0d_2 if not exists
-- Create user_0d_2 if not exists
-- Grant SELECT privilege to user_0d_2 on hbtn_0d_2 database

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
