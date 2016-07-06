elif y[9] == 'Debian':
			name = "Debian-" + y[1]+'-' +str(y[21])
			insertion = 'update  USER set Debian_COUNTER = Debian_COUNTER +1 where ID =%d;' % (receivedId)
	
			cursor.execute(insertion)
			print name
			x = commands.getstatusoutput("sudo virsh destroy "+name)
			x = commands.getstatusoutput("sudo chmod 777 /etc/libvirt/qemu/ -R ;sudo touch /etc/libvirt/qemu/"+name+".xml;sudo cp /etc/libvirt/qemu/debian.xml	/etc/libvirt/qemu/"+name+".xml")
#			print x
			#lets replace the name first
			x = commands.getstatusoutput("sudo cat /etc/libvirt/qemu/{0}.xml  | sudo grep name | sudo sed -i 's/<name>debian</<name>{0}</' /etc/libvirt/qemu/{0}.xml".format(name))
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
			print y[21]
			var = "debian-"+receivedId+"-"+str(y[21])+".qcow2"
			print var
			x = commands.getstatusoutput("sudo replace \"debian.qcow2\" \""+var+"\" -- /etc/libvirt/qemu/"+name+".xml")
			print x
#			print "hii"
#			print "<br /><br />"
			e =random.randint(5900,65535)
			f = int(e)
			f1 = str(f)
			print "prakshi"
			print f1
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





			<form class action onsubmit="document.getElementById('cookieweds').value=document.cookie">

			<input type="textfield"  type="hidden" id="cookieweds" >