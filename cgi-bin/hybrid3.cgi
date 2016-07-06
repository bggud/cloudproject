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

cursor = db.cursor();
try:
	values = "select *from USER where id = %d " % (id)
	cursor.execute(values)
	for y in cursor.fetchall():
		print y[16]
		print y[2]
		print y[3]
		print y[20]
		print y[21]
		print y[1]


		x = commands.getstatusoutput("sudo grep /etc/libvirt/qemu/Redhat-"+y[1]+"-"+a+".xml -e autoport | awk '{print $3;}'| awk -F= '{print $2 ;}'" )
		c = x[1]
		d = c[1:-1]
		s =random.randint(2000,65535)
		f4 = int(s)
		f5 = str(f4)
		x = commands.getstatusoutput("sudo virsh start Redhat-"+y[1]+"-"+a)
		print d
		print "hello1"
		print f5
		print "hello2"
		x = commands.getstatusoutput("sudo /root/Downloads/websockify-master/websockify.py -D "+f5+" 192.168.42.151:"+d)	
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/vnc/index.html?host=192.168.42.151&port="+f5+"\">\n";

		db.commit()
except:
	db.rollback()
finally:
	db.close()
