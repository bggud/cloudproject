#! /usr/bin/python2
import os,commands
import mysql.connector as mariadb
import cgi
import cgitb

cgitb.enable()

print "content-type:text/html"
print ""

form = cgi.FieldStorage()
x = form.getvalue('name') 
password= form.getvalue('PASSWORD')


db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();

passkey = 'select PASSWORD from USER where NAME = "'+x+'" ;'
cursor.execute(passkey)
print passkey

db.close()
#print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.google.com\">\n";
