#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
software = form.getvalue('SOFTWARE')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
a = form.getvalue('receivedId')
#print a
receivedId= a[3]
print receivedId
receivedId = int(receivedId)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	insertion = 'update USER set SOFTWARE = "%s" where ID = %d ;' % (software,receivedId)
	cursor.execute(insertion)
	values = 'select *from USER where ID =%d;' % (receivedId)
	cursor.execute(values)
	
	for y in cursor.fetchall():
		print y[3]
		print y[8]
		print y[13]
		a=y[13].lower()
		x = commands.getstatusoutput("sudo userdel -r {0}".format(y[1]))
		print x
		x = commands.getstatusoutput("sudo useradd -s /usr/bin/{0} {1}".format(a,y[1]))
		db.commit()
		print "echo '"+ y[3]+ "' | sudo passwd " + y[1] + " --stdin"
		t = commands.getstatusoutput("echo '"+ y[3]+ "' | sudo passwd " + y[1] + " --stdin")
		print t
		f = open("/var/www/html/saasC.py","w")
		f.write('''#!/usr/bin/python2	\n

import commands	\n
x = commands.getstatusoutput("ssh -X  {0}@192.168.42.151 {1}")\n
raw_input() \n
			'''.format(y[1],a))
		f.close()
		b = commands.getstatusoutput("sudo chmod +x ../html/saasC.py ; iptables -F")
#	print a
		b =	commands.getstatusoutput("tar -cf SAAS.tar --directory='/var/www/html' saasC.py ; mv SAAS.tar ../html/")
					
		if a == "gnome-terminal":
			x = commands.getstatusoutput(" sudo echo '/usr/bin/gnome-terminal\nexit' >> sudo /home/"+y[1]+"/.bash_profile ")
			print x
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/saasLast.html\">\n";

		db.commit()
except:
	db.rollback()
finally:
	db.close()
