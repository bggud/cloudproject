#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
hdd = form.getvalue('HDD')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
a = form.getvalue('receivedId')
#print a
receivedId= a[3]
print receivedId
receivedId = int(receivedId)
hdd = int(hdd)


commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	insertion = 'update USER set HDD = %d where ID =%d;' % (hdd,receivedId)
	cursor.execute(insertion)
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/iaas.html\">\n";
	db.commit()
except:
	db.rollback()
finally:
	db.close()
