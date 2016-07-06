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

hello = "abcd"


form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
CPUCores = form.getvalue('CPUCores')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
receivedId=form.getvalue('receivedId')
receivedId = int(receivedId)
CPUCores = int(CPUCores)

commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	insertion = 'update  USER set CPUCORES =%d where ID =%d;' % (CPUCores,receivedId)
	
	cursor.execute(insertion)
	values = 'select *from USER where ID =%d;' % (receivedId)
	cursor.execute(values)
	
	for y in cursor.fetchall():
		print y[9]
		print y[10]
		print y[11]
		print y[12]
		print y[1]
		print y[16]
		type = y[0]
		ram = y[1]
		hdd = y[2]
		cores = y[3]
		print y[20]	#windows counter
		print y[21]	#debian counter
	###########################################################################################
	####################################### IAAS	ALLOCATION ################################
	###########################################################################################
		

		if y[9] == 'Redhat':
			name = "Redhat-" + y[1]+'-' +str(y[16])
			insertion = 'update  USER set COUNTER = COUNTER +1 where ID =%d;' % (receivedId)
	
			cursor.execute(insertion)
			print name
			x = commands.getstatusoutput("sudo virsh destroy "+name)
			x = commands.getstatusoutput("sudo chmod 777 /etc/libvirt/qemu/ -R ;sudo touch /etc/libvirt/qemu/"+name+".xml;sudo cp /etc/libvirt/qemu/trial.xml	/etc/libvirt/qemu/"+name+".xml")
#			print x
			#lets replace the name first
			x = commands.getstatusoutput("sudo cat /etc/libvirt/qemu/{0}.xml  | sudo grep name | sudo sed -i 's/<name>trial</<name>{0}</' /etc/libvirt/qemu/{0}.xml".format(name))
#			print x
			x = random.sample('1234567890abcdef1234567890abcdef1234567890acbdef',6)
#			print x
			mac ="30:f9:ed:"	
#			print x
			i=0 
			for z in x :
				mac = mac + z;
				i += 1 ;
				if i%2 == 0 and i < 6:
					mac = mac+ ":";
			mac = "'"+mac+"'"

			x = random.sample('1234567890abcdef1234567890abcdef1234567890acbdef',32)
			uuid=""
#			print x
			i =0
			for z in x:
				uuid = uuid + z ;
				i=i +1 ;
				if i==8 or i == 12 or i==16 or i==20 :
					uuid = uuid +"-" ;
#			print uuid+"***"
			newVar = commands.getstatusoutput("sudo  grep  /etc/libvirt/qemu/"+name+".xml -e mac\ address| awk -F= '{print $2;}' | awk -F/ '{print $1;}'")
#			print newVar[1] ;
#			print "jeko"
			newVar2 = commands.getstatusoutput("sudo sed -i 's/"+newVar[1]+"/"+mac+"/' /etc/libvirt/qemu/"+name+".xml > sudo /etc/libvirt/qemu/"+name+".xml")
#			print "tamatar"
#			print newVar2
#			print "hii"
			uidNewVar = commands.getstatusoutput("sudo grep  /etc/libvirt/qemu/"+name+".xml -e uuid | awk -Fuuid '{print $2;}' ")
		#	print uidNewVar
			uidVar = uidNewVar[1]
#			print "<br/>"
#			print uidVar
	#		print uidVar
			e = uidVar[1:-1]
#			print "<br />"
#			print "<br />"
#			print e
#			print "<br />"
#			print  e + "..........................."

			x = commands.getstatusoutput("sudo sed -i 's/"+e+"/"+uuid+"</' /etc/libvirt/qemu/"+name+".xml > sudo /etc/libvirt/qemu/"+name+".xml")
#			print x
#			print name
#			print "sudo grep /etc/libvirt/qemu/"+name+".xml -e source\ file |sudo awk -F/ '{print $6}'"
			x = commands.getstatusoutput("sudo grep /etc/libvirt/qemu/"+name+".xml -e source\ file |sudo awk -F/ '{print $6}'")
#			print x
#			print x[1]
			p = x[1]
#			print p
			receivedId = str(receivedId)
			#print "sudo sed -i 's/"+p+"/redhat-"+receivedId+".qcow2/' /etc/libvirt/qemu/"+name+".xml > sudo /etc/libvirt/qemu/"+name+".xml"
#			print x
			x = commands.getstatusoutput("sudo sed -i 's/"+p+"/redhat-"+receivedId+"-"+str(y[16])+".qcow2'/' /etc/libvirt/qemu/"+name+".xml > sudo /etc/libvirt/qemu/"+name+".xml")
##			print x
#			print "hii"
#			print "<br /><br />"
			x = commands.getstatusoutput("sudo grep /etc/libvirt/qemu/"+name+".xml -e path | awk -F/ '{print $8}'")
			c = x[1]
			print c
			qwe = commands.getstatusoutput("sudo sed -i 's/"+c+"/domain-"+name+"/' /etc/libvirt/qemu/"+name+".xml > sudo /etc/libvirt/qemu/"+name+".xml")
			#print qwe
			e =random.randint(5900,65535)
			f = int(e)
			f1 = str(f)
			print "prakshi"
			print f1
			zuts = commands.getstatusoutput("sudo replace \"listen='192.168.0.129'\" \"listen='0.0.0.0'\" -- /etc/libvirt/qemu/"+name+".xml")
			zuts = commands.getstatusoutput("sudo replace \"address='192.168.0.129'\" \"address='0.0.0.0'\" -- /etc/libvirt/qemu/"+name+".xml")
			print zuts
			v =commands.getstatusoutput("sudo grep /etc/libvirt/qemu/"+name+".xml -e 'vnc' | awk '{print $3;}'")
			x = commands.getstatusoutput("sudo replace \""+v[1]+"\" \"port='"+f1+"'\" -- /etc/libvirt/qemu/"+name+".xml")
			print x
			print v[1]
			print "<br />"
			print "<br />"
			
#			print x
#			print x
			x = commands.getstatusoutput("sudo virsh define /etc/libvirt/qemu/"+name+".xml")
			print x
			x = commands.getstatusoutput("sudo virsh start "+name)
#			print x
			x = commands.getstatusoutput("sudo virsh setmem --size "+y[10] + "M "+name)
#			print x
			x = commands.getstatusoutput("sudo virsh define /etc/libvirt/qemu/"+name+".xml")
			
			print "hello"
#			print x
#
			
#	x = commands.getstatusoutput("sudo virt-install --name " +y[1]+"-"+x[1] + "  --ram " + y[10] + " --vcpu " + y[12] + " --disk path=/var/lib/libvirt/images/rhel7.qcow2,size=" +y[10]+ " --cdrom /root/Downloads/rhel-server-7.2-x86_64-dvd.iso --noautoconsole " )
#	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.0.129/basicProfile.html\">\n";
#	x = commands.getstatusoutput("virsh setmem --size " + )
#	x = commands.getstatusoutput("virsh start trail")
			s =random.randint(2000,65535)
			f4 = int(s)
			f5 = str(f4)

			x = commands.getstatusoutput("sudo /root/Downloads/websockify-master/websockify.py -D "+f5+" 192.168.0.129:"+f1)
			print f1

			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.0.129/vnc/index.html?host=192.168.0.129&port="+f5+"\">\n";
	#		print x
	
			db.commit()

		

	#		print x
			db.commit()
except:
	db.rollback()
finally:
	db.close()
