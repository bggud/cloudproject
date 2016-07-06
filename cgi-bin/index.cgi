#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands

cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
username = form.getvalue(USERNAME')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
password = form.getvalue('PASSWORD')
email = form.getvalue('EMAIL')
number = form.getvalue('NUMBER')
file1 =open("Register.txt","a")
file1.write(username +"\t\t\t\t" + password + "\t\t\t\t"+ email +"\t\t\t\t"+number)

