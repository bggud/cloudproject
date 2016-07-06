#! /usr/bin/python2
import os,commands,time
import mysql.connector as mariadb
import cgi
import cgitb

cgitb.enable()

print "content-type:text/html"

form = cgi.FieldStorage()
username = form.getvalue('USERNAME');
password = form.getvalue('PASSWORD');
email = form.getvalue('EMAIL')
contact = form.getvalue('NUMBER');

db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
#print username, password, email, contact ;
check = 'select * from USER where NAME = "%s" OR EMAIL = "%s"' % (username, email)
try:
	cursor.execute(check)
	#print cursor.fetchall()	
	if cursor.fetchall():
		#print "User already exists with this name . Please try any other name"
		#time.sleep(2)
		print ""
		print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('User already exists with this username or email . please try another one');
				}
				alertMsg();
				</script>
				</body>"""
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/register.php\">\n";
	else:
		insertion = 'INSERT INTO USER(NAME,EMAIL,PASSWORD,CONTACT_NUMBER) VALUES("%s","%s","%s","%s")' % (username,email,password,contact);
		cursor.execute(insertion)
		id = 'select ID from USER where  NAME = "%s"  ; ' % (username)
		cursor.execute(id)
		y = cursor.fetchall()
		for w in y:
			qw = w[0]
			print "Set-Cookie:id={0};Path=/;\r\n".format(qw)
			print ""
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";
		db.commit()
except:
	db.rollback()
db.close()
#print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";
