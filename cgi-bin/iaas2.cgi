#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
osType = form.getvalue('OS_TYPE')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
a = form.getvalue('receivedId')
#print a
receivedId= a[3]
print receivedId
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');
print "sdjsasnj"
cursor = db.cursor();
receivedId = int(receivedId)
try:
	if osType == "redhat":
		insertion = 'update  USER set OS_TYPE = "Redhat" where ID = %d;' % (receivedId)
		print insertion
	elif osType == "windows":
		insertion = 'update  USER set OS_TYPE = "Windows" where ID = %d;' % (receivedId)
	elif osType == "debian":
		insertion = 'update  USER set OS_TYPE = "Debian" where ID = %d;' % (receivedId)
	cursor.execute(insertion);
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/iaas2.html\">\n";
	db.commit()
except:
	db.rollback()
finally:
	db.close()
