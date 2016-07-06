#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import random
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print "Set-Cookie:cookie=abcd;Path=/;\r\n"
print ""	# it indicates the termination of header.

id = 2
print id

commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	values = "select *from USER where id = %d " % (id)
	cursor.execute(values)
	for y in cursor.fetchall():

		print "hello"
		print y[20]
		for a in range(y[20]):
			print '''<html>
			<form method="post"  action="hybrid2.cgi">
			

			<input type="hidden" name="counter" value={1} />
			<input type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			</html>'''.format(str(id),str(a))

			print "<br />"
		print """
		<html>
		<head>
			<title> I am </title>

		</head>
		<body>
			<h2> I am the one </h2>
			<a > REDHAT </a>
			{0}
		</body>
		</html>
		""".format(id)
		db.commit()
except:
	db.rollback()
finally:
	db.close()
