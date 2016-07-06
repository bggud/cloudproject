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
a = 0#form.getvalue('counter')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
b = form.getvalue('receivedId')
#print b
port = form.getvalue('portB')
#print "hello"
#print port
action = form.getvalue('action')
#print ",,,"+action+";;;;"
id = b[3]
id = int(id)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();

try:
	x = commands.getstatusoutput("sudo ps -aux | grep "+port+" | grep websockify.py | awk '{print $15;}' | awk -F: '{print $2;}'")
#	print "<br />"
#	print x[1]
	w = commands.getstatusoutput("sudo chmod 777 /etc/libvirt/  -R")
#	print w[1]

	myvl = x[1].strip("\n")
#	print "..."+myvl+".."
	v = commands.getstatusoutput("sudo grep "+ myvl+" /etc/libvirt/qemu/* | sudo awk -F/ {'print $5;'}|sudo awk -F: {'print $1;'}")
#	print "<META HTTP-EQUIV=refresh>\n";
	print "Are You sure to perform the chosen Action ? Press Ctrl + F5 "

	myList= []
	myList = v[1].split("\n")
	name =  myList[1]
	name = name[:-4]
	if action == "Reboot" :
		
		print "I am here in Reboot"
		
		print """<body style=\"background-image: url('Cloud.jpg');\"><script>
					function alertMsg(){

						alert('Rebooting in progress ... ');
					}
					alertMsg();
					</script>
					</body>"""

		s = commands.getstatusoutput("sudo virsh reboot " + name)
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/vnc/index.html?host=192.168.42.151&port="+port+"\">\n";

	elif action == "Reset" :
		print "I am here in Reset"
		s = commands.getstatusoutput("sudo virsh reset " + name)
		
		print """<body style=\"background-image: url('Cloud.jpg');\"><script>
					function alertMsg(){

						alert('Resetting in progress ... ');
					}
					alertMsg();
					</script>
					</body>"""
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/vnc/index.html?host=192.168.42.151&port="+port+"\">\n";

	elif action == "Shut Down" :
		print "I am here in Shut Down"
		s = commands.getstatusoutput("sudo virsh shutdown " + name)
		print s
		print """<body style=\"background-image: url('Cloud.jpg');\"><script>
					function alertMsg(){

						alert('Shutting Down ... ');
					}
					alertMsg();
					</script>
					</body>"""
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";
	elif action == "Force off" :
		print "I am here in Force Off"
		s = commands.getstatusoutput("sudo virsh destroy " + name)
		
		print """<body style=\"background-image: url('Cloud.jpg');\"><script>
					function alertMsg(){

						alert('Shut Down ... ');
					}
					alertMsg();
					</script>
					</body>"""
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";

	elif action == "Save" :
		print "I am here in Save"
		id='1'
		s = commands.getstatusoutput("sudo virsh save " + name + " " + id + "-" +name + " --running")
		
		print """<body style=\"background-image: url('Cloud.jpg');\"><script>
					function alertMsg(){

						alert('Saving in progress ... ');
					}
					alertMsg();
					</script>
					</body>"""
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/vnc/index.html?host=192.168.42.151&port="+port+"\">\n";

	print "Successful"
	db.commit()
except:
#	print "hello"
	db.rollback()
finally:
	db.close()
