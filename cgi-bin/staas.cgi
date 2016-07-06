#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
storageType = form.getvalue('STORAGE_TYPE')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
a = form.getvalue('receivedId')
receivedId=a[3]
receivedId = int(receivedId)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	if storageType== "object":
		insertion = 'update USER set STORAGE_TYPE = "object" where ID = %d ;' % (receivedId)
		cursor.execute(insertion)
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/staas2_object.html\">\n";
		db.commit()
	elif storageType == "block":
		insertion = 'update USER set STORAGE_TYPE = "block" where ID = %d ;' % (receivedId)
		cursor.execute(insertion)
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/staas2_block.html\">\n";
		db.commit()
except:
	db.rollback()
finally:
	db.close()
