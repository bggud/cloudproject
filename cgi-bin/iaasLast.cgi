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
#CPUCores = form.getvalue('CPUCores')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
#receivedId=form.getvalue('receivedId')
receivedId = 1
CPUCores = 1
receivedId = int(receivedId)
CPUCores = int(CPUCores)
print "set-cookie:bhagyashreeCookie=1;Path=/;\r\n"
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	insertion = 'update  USER set CPUCORES =%d where ID =%d;' % (CPUCores,receivedId)
	
	cursor.execute(insertion)
	values = 'select *from USER where ID =%d;' % (receivedId)
	cursor.execute(values)
	
	for y in cursor.fetchall():
		type = y[0]
		ram = y[1]
		hdd = y[2]
		cores = y[3]
	###########################################################################################
	####################################### IAAS	ALLOCATION ################################
	###########################################################################################
		name = y[1]+'-' +str(y[16])
		print name
		print y[9]
		if y[9] == 'Redhat':
			
#			print name
#			print "sudo grep /etc/libvirt/qemu/"+name+".xml -e source\ file |sudo awk -F/ '{print $6}'"
			x = commands.getstatusoutput("sudo grep /etc/libvirt/qemu/"+name+".xml -e source\ file |sudo awk -F/ '{print $6}'")
#			print x
#			print x[1]
			p = x[1]
#			print p
			receivedId = str(receivedId)
			print "sudo sed -i 's/"+p+"/redhat-"+receivedId+".qcow2/' /etc/libvirt/qemu/"+name+".xml > sudo /etc/libvirt/qemu/"+name+".xml"
#			print x
			x = commands.getstatusoutput("sudo sed -i 's/"+p+"/redhat-"+receivedId+".qcow2/' /etc/libvirt/qemu/"+name+".xml > sudo /etc/libvirt/qemu/"+name+".xml")
			print x
			print "hii"
			x = commands.getstatusoutput("sudo grep /etc/libvirt/qemu/"+name+".xml -e path | awk -F/ '{print $8}'")
			c = x[1]
			x = commands.getstatusoutput("sudo sed -i 's/"+c+"/domain-"+name+"/' /etc/libvirt/qemu/"+name+".xml > sudo /etc/libvirt/qemu/"+name+".xml")
			print x
			x = commands.getstatusoutput("sudo virsh destroy "+name)
			print x
			print x
			x = commands.getstatusoutput("sudo virsh define /etc/libvirt/qemu/"+name+".xml")
			print x
			x = commands.getstatusoutput("sudo virsh start "+name)
			print x
			x = commands.getstatusoutput("sudo virsh setmem --size "+y[10] + "M "+name)
			print x
			x = commands.getstatusoutput("sudo virsh define /etc/libvirt/qemu/"+name+".xml")
			
			print "hello"
			print x
#	x = commands.getstatusoutput("sudo virt-install --name " +y[1]+"-"+x[1] + "  --ram " + y[10] + " --vcpu " + y[12] + " --disk path=/var/lib/libvirt/images/rhel7.qcow2,size=" +y[10]+ " --cdrom /root/Downloads/rhel-server-7.2-x86_64-dvd.iso --noautoconsole " )
#	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";
#	x = commands.getstatusoutput("virsh setmem --size " + )
#	x = commands.getstatusoutput("virsh start trail")
			x = commands.getstatusoutput("/root/Downloads/websockify-master/./websockify.py -D 192.168.42.151:2424 192.168.42.151:5910")
			
#			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/vnc/index.html?host=192.168.42.151&port=2222\">\n";
	#		print x
	db.commit()
except:
	db.rollback()
finally:
	db.close()
