#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
ram = form.getvalue('RAM')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
ram=int(ram)

a = form.getvalue('receivedId')
#print a
receivedId= a[3]
print receivedId

receivedId = int(receivedId)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	insertion = 'update USER set RAM = %d where ID =%d;' % (ram,receivedId)
	
	cursor.execute(insertion)
	db.commit()
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/iaas3.html\">\n";

except:
	db.rollback()
finally:
	db.close()
