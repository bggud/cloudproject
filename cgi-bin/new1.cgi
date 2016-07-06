#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
a = form.getvalue('receivedId')
print a
receivedId=a[3]
receivedId = int(receivedId)
print receivedId
fileitem = form['FILE']
imgName = fileitem.filename
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
values = 'select *from USER where ID =%d;' % (receivedId)
cursor.execute(values)
for y in cursor.fetchall():

	print y[1]
	name=y[1]
	commands.getstatusoutput("sudo mkdir ../prfPic/"+y[1])
	commands.getstatusoutput("sudo chmod o+w ../prfPic/"+y[1])
	commands.getstatusoutput("sudo chmod g+w ../prfPic/"+y[1])


#a = form.getvalue('receivedId')
#receivedId=a[3]
#receivedId = int(receivedId)
if ".jpg" not in imgName:
	print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('Format not supported');
				}
				alertMsg();
				</script>
				</body>"""
elif fileitem.filename :
# strip leading path from file name
# to avoid directory traversal attacks
  	fn = os.path.basename(fileitem.filename)
	open('../html/prfPic/'+str(receivedId)+'.jpg' , 'wb').write(fileitem.file.read())
	message = 'The file "' + fn + '" was uploaded successfully'
	print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('File uploaded Successfully :D ');
				}
				alertMsg();
				</script>
				</body>"""
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";
	print imgName
	insertion = 'update USER set DISPLAYIMG = "%s"  where ID = %d ;' % (imgName,receivedId)
	cursor.execute(insertion)
	db.commit()
	db.rollback()
	db.close()


else:
	print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('Upload Failed. Please  try again later');
				}
				alertMsg();
				</script>
				</body>"""
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";
	
