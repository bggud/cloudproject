#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
a = form.getvalue('receivedId')
receivedId=a[3]
receivedId = int(receivedId)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');
print "helllo"
cursor = db.cursor();
try:
	x = 'delete from USER where ID=%d;' % (receivedId)
	print x
	cursor.execute(x)
	db.commit()
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/index.html\">\n";
except:
	db.rollback()
finally:
	db.close()
