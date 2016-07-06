#! /usr/bin/python2
import os,commands
import mysql.connector as mariadb
import cgi
import cgitb

cgitb.enable()

print "content-type:text/html"

form = cgi.FieldStorage()
x = form.getvalue('USER') 
password= form.getvalue('PASSWORD')

commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
#print "hello"
existence = 'select * from USER where NAME = "%s"  ; ' % (x)
try:
	cursor.execute(existence)
	psswd = 'eefe2435665778  ./././l/.,'


	if cursor.fetchall():

		passkey = 'select PASSWORD from USER where NAME = "%s"  ; ' % (x)
		
		cursor.execute(passkey)

		r = cursor.fetchall()

		for i in r:
			psswd= i[0]

			#print psswd
		db.commit()

		if password == psswd :
			id = 'select ID from USER where  NAME = "%s"  ; ' % (x)
			cursor.execute(id)
			y = cursor.fetchall()
			for w in y :
				
				if w[0] == 0 :
					print "Set-Cookie:id={0};Path=/;\r\n".format(w[0])
					print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/adminProfile.html\">\n";
					print ""
			
				else :
					qw = w[0]
 					print "Set-Cookie:id={0};Path=/;\r\n".format(qw)
					print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";

		else :
			print ""
			print """<body style=\"background-image: url('Cloud.jpg');\"><script>
					function alertMsg(){

						alert('Invalid Credentials. please try again');
					}
					alertMsg();
					</script>
					</body>"""
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/index.html\">\n";

	else:
		print ""
		print """<script>
				function alertMsg(){
					alert('User does not exist. Please Sign Up !');
				}
				alertMsg();
				</script>
				"""
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/register.php\">\n";
except:
	db.rollback()
finally:
	db.close()
print ""
