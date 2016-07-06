#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import random
import commands,os,time
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
a = form.getvalue('counter')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
b = form.getvalue('receivedId')
print a
id = b[3]
print id
id = int(id)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');
t=""
cursor = db.cursor();
try:
	values = "select *from USER where id = %d " % (id)
	cursor.execute(values)
#	print "hello"
	for y in cursor.fetchall():
#		print "hello"
		d = commands.getstatusoutput("sudo chmod +r docker/ -R")
		f = open("docker/"+str(id)+".txt")
#		print f
#		print f
		k = int(y[18])
#		print k
		for  i in range(k):
			t = f.readline()
#			print t
#			print i
			if i == int(a):
				break;

		f.close()
		print t
		db.commit()
except:
	db.rollback()
finally:
	db.close()
