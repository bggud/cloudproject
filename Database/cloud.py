#! /usr/bin/python2

import os,commands
import cgi
import cgitb
import mysql.connector as mariadb

cgitb.enable()

db = mariadb.connect(user='root',password='redhat',database='cloud')

cursor = db.cursor();

cursor.execute('DROP TABLE IF EXISTS USER')
cursor.execute('DROP TABLE IF EXISTS STAAS');
cursor.execute('DROP TABLE IF EXISTS SAAS');
cursor.execute('DROP TABLE IF EXISTS IAAS');

sql = """create table USER(
     ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
     NAME CHAR(30) NOT NULL,
     EMAIL CHAR(40) NOT NULL,
     PASSWORD CHAR(80) NOT NULL,
     CONTACT_NUMBER CHAR(20) NOT NULL ,
     STORAGE_TYPE CHAR(20) NOT NULL,
     SERVICE_TYPE CHAR(20) NOT NULL,
     STORAGE_SIZE CHAR(10) NOT NULL,
     STORAGE_NAME CHAR(30) NOT NULL ,
     OS_TYPE CHAR(20) NOT NULL,
     RAM CHAR(20) NOT NULL,
     HDD CHAR(10) NOT NULL,
     CPUCORES CHAR(30) NOT NULL ,
     SOFTWARE CHAR(30) NOT NULL,
     AVAILABLE_SIZE CHAR(10) NOT NULL,
     FOLDER_LOCATION CHAR(20) NOT NULL,
     COUNTER INT(10) DEFAULT 0 ,
     INSTANCE_NAME CHAR(20) NOT NULL,
     TOTAL_INSTANCE INT(3) NOT NULL,
     DOCKER_VOLUME CHAR(20) NOT NULL,
     Win_COUNTER INT(10) NOT NULL,
     Debian_COUNTER INT(10) NOT NULL,
     DISPLAYIMG CHAR(40) NOT NULL
     		 );
	"""
cursor.execute(sql);

db.close()

raw_input()
