#!/usr/bin/python2
import os,commands
import mysql.connector as mariadb
import cgi
import cgitb
cgitb.enable()

print "content-type:text/html" # browser understands HTML only , we need to tell this
print""
form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
a = form.getvalue('receivedId')
#print a
receivedId= a[3]

receivedId = int(receivedId)
#print receivedId
currentPass=form.getvalue('current_passkey')
newPass=form.getvalue('new_passkey')
confirmPass=form.getvalue('confirm_passkey')

commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');
cursor = db.cursor();
values = 'select *from USER where ID =%d;' % (receivedId)
cursor.execute(values)
	
for y in cursor.fetchall():
	name1=y[1]
	email=y[2]
	password1=y[3]


#print password1
#print currentPass
#print newPass
#print confirmPass

if password1 == currentPass :
	
	if newPass == confirmPass :

		insertion = 'update USER set PASSWORD = "%s"  where ID = %d ;' % (newPass,receivedId)
		cursor.execute(insertion)
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/security.html\">\n";

	else:
		print """ <script>
			function alertMsg(){
			alert('Please enter confirmed password correctly');
			}
			alertMsg();
			</script> """
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/security.html\">\n";
else : 
	print """ <script>
			function alertMsg(){
			alert('Please enter current password correctly');
			}
			alertMsg();
			</script> """
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/security.html\">\n";


db.commit()
db.rollback()
db.close()

