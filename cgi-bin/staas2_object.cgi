#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
serviceType = form.getvalue('SERVICE_TYPE')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
a = form.getvalue('receivedId')
#print a
receivedId= a[3]
print receivedId
receivedId = int(receivedId)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	if serviceType== "glusterfs":
		insertion = 'update USER set SERVICE_TYPE = "glusterfs"  where ID = %d ;' % (receivedId)
		cursor.execute(insertion)
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/stass3.html\">\n";
		db.commit()
	elif serviceType == "nfs":
		insertion = 'update USER set SERVICE_TYPE = "nfs" where ID = %d ;' % (receivedId)
		cursor.execute(insertion)
		print "hello"
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/stass3.html\">\n";
		db.commit()
	elif serviceType == "sshfs": 
		insertion = 'update USER set SERVICE_TYPE = "sshfs"  where ID = %d ;' % (receivedId)
		cursor.execute(insertion)
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/stass3.html\">\n";
		db.commit()
	elif serviceType == "samba": 
		insertion = 'update USER set SERVICE_TYPE = "samba"  where ID = %d ;' % (receivedId)
		cursor.execute(insertion)
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/stass3.html\">\n";
		db.commit()
except:
	db.rollback()
finally:
	db.close()
