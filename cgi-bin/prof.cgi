#!/usr/bin/python2
import os,commands
import mysql.connector as mariadb
import cgi
import cgitb

print "content-type:text/html" # browser understands HTML only , we need to tell this

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
a = form.getvalue('receivedId')
#print a
receivedId= a[3]
print receivedId
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');
values = 'select *from USER where ID =%d;' % (receivedId)
cursor.execute(values)
	
for y in cursor.fetchall():
	name=y[1]
	email=y[2]
	password1=y[3]
	phoneno=y[4]
