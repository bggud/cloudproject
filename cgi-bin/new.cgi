#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
receivedId=form.getvalue('receivedId')
receivedId = int(receivedId)
fileitem = form['FILE']
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');
name= ""
cursor = db.cursor();
try:
	values = 'select *from USER where ID =%d;' % (receivedId)
#	print values
	cursor.execute(values)
	for y in cursor.fetchall():
#		print y[1]
		t= commands.getstatusoutput("sudo lvcreate --name " + y[1] + " --size 1G vg1")
#		print t

		t= commands.getstatusoutput("sudo mkfs.ext4 /dev/mapper/vg1-" + y[1])
#		print t
		t= commands.getstatusoutput("sudo mkdir /var/www/"+y[1])
#		print t
		t= commands.getstatusoutput("sudo mount /dev/mapper/vg1-" + y[1] + " /var/www/"+y[1])
#		print t
		t =commands.getstatusoutput("sudo chmod 777 /var/www/"+y[1])
#		print t
#		print "\n"
		name = y[1]
# Test if the file was uploaded

	db.commit()
except:
	db.rollback()
finally:
	if fileitem.filename :

# strip leading path from file name
# to avoid directory traversal attacks
  		fn = os.path.basename(fileitem.filename)
		open('../'+name+'/' + fn, 'wb').write(fileitem.file.read())
		message = 'The file "' + fn + '" was uploaded successfully'
		print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('File uploaded Successfully :D ');
				}
				alertMsg();
				</script>
				</body>"""

	else:
		print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('Upload Failed. Please  try again later');
				}
				alertMsg();
				</script>
				</body>"""
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";
	db.close()
