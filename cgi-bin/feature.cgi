#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import random
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.


form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
instanceName = form.getvalue('INSTANCE_NAME')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
instanceName = instanceName.lower()
a=form.getvalue('receivedId')
#print a
receivedId= a[3]
receivedId = int(receivedId)

totalInstance = form.getvalue("TOTAL_INSTANCES")
totalInstance = int(totalInstance)
a = commands.getstatusoutput("sudo systemctl restart mariadb")
#print a

#a = commands.getstatusoutput(" sudo  docker daemon -H tcp://192.168.42.151:2375 &")

db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	
	insertion = 'update  USER set INSTANCE_NAME ="%s" where ID =%d;' % (instanceName,receivedId)
	cursor.execute(insertion)
	insertion = 'update  USER set TOTAL_INSTANCE =%d where ID =%d;' % (totalInstance,receivedId)
	cursor.execute(insertion)
	db.commit()
	values = "select * from USER where ID=%d;" % (receivedId)
	cursor.execute(values)
	for y in cursor.fetchall():
#		a = commands.getstatusoutput("sudo systemctl restart docker")
	#	a = commands.getstatusoutput("export DOCKER_HOST=tcp://192.168.42.151:2375")	
		print a
		x = commands.getstatusoutput("sudo docker images | awk '{print $1 ;}' | grep -i project_" + y[17])
#		print x[1]
		l = []
		k = int(y[18])
#		print k
		d = commands.getstatusoutput("sudo chmod 777 docker/ -R")
		f = open("docker/"+str(receivedId)+".txt","w") 
		for j in range(k):
#			print j
#			print k
#			print "hello"
			r = commands.getstatusoutput("sudo docker run -dti -p 1000"+str(j)+":22 " + x[1] + " bash")
#			print r[1]
#			print x[1]
			l.append(r[1])
			f.write(l[j]+"\n")
		print l
#			print "vye"
		
		f.close()
		print "hello"
		print '''<form  method="post"  action="http://192.168.42.151/cgi-bin/featureLast.cgi">
			
						<script type="text/javascript">
						 a = document.cookie
						 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
						 document.write("<input type=\'submit\' value=\'Submit\'   >")
						</script>

						</form>
	'''
		print "--hello--"
	#	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/cgi-bin/featureLast.cgi\">\n";

except:
	db.rollback()
finally:
	db.close()
