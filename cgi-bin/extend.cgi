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
b = form.getvalue('receivedId')
name = form.getvalue('name')
id = b[3]
print id
print name
id = int(id)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();

x = commands.getstatusoutput("sudo lvextend --size +1G /dev/mapper/vg1-"+name)
print x
if x[0] == 0:
	x = commands.getstatusoutput("sudo resize2fs /dev/mapper/vg1-"+name)
	if x[0] == 0:
		print '''
		<script>
			function alertMsg(){
				alert("Size increased , please refresh")
			}
			alertMsg();
		</script>
		'''
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";
