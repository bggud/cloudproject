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
activity = form.getvalue('activity')

#print a
receivedId= a[3]
#print receivedId
receivedId = int(receivedId)
x = commands.getstatusoutput("sudo virsh list")
y = x[1]
#print y
y = y.split("\n")
z = y[2:-1]
print z
#z = z.split()
if activity == "Migrate" :
	for r in z :
		c = r.split()
		if c[2] == 'running' :
			print "coffee"
			name = c[1]
			n = commands.getstatusoutput("sudo chmod 777 /data -R")
			n = commands.getstatusoutput("sudo chmod 777 /var /var/lib /var/lib/libvirt/ /var/lib/libvirt/images -R")
			w = commands.getstatusoutput("sudo sshpass -p 'redhat' virsh migrate --live "+name + " qemu+ssh://192.168.0.120/system ")
			print w
			while True :
				q = commands.getstatusoutput("sudo free -m | awk '{print $3;}' | head -n 2 | tail -n 1")
				print q
				print q[1]
				s = int(q[1])
				if s < 1000  :
					break
			print "migration successful"
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/adminProfile.html\">\n";

elif activity == "VG-Extend" :
	# default increment size 2GB
	s = commands.getstatusoutput("sudo pvs | awk '{print $1;}'")
	r = commands.getstatusoutput("sudo pvs | awk '{print $2;}'")
	print "<br />"
	q = s[1]
	p = r[1]
	q = q.split("\n")
	p = p.split("\n")
	q = q[2:-1]
	p = p[2:-1]
	o= -1
	for e in p :
		print e
		print "<br />"
		if e != "vg1" and e!="rhel":
			o = p.index(e)
			print o
			print q[o]
			break 
	if o == -1 :
		print '''
				<script>
					function alertMsg(){
							alert(" No Physical Volume Available !")

					}
					alertMsg();
				</script>
			'''
		print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/adminProfile.html\">\n";

	else :
		x = commands.getstatusoutput("sudo vgdisplay vg1 ")
		print x[1]
		x = commands.getstatusoutput("sudo vgextend vg1 "+ q[o] )
		if x[0] == 0 :
			print '''
				<script>
					function alertMsg(){
							alert(" Entended Successfully !")

					}
					alertMsg();
				</script>
			'''
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/adminProfile.html\">\n";

		else:
			print '''
				<script>
					function alertMsg(){
							alert(" Entension Unsuccessful !")

					}
					alertMsg();
				</script>
			'''
			x = commands.getstatusoutput("sudo vgdisplay vg1 ")
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/adminProfile.html\">\n";

else :
	print "error"
