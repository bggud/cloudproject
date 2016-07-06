#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
storageName = form.getvalue('DIR_NAME')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
a = form.getvalue('receivedId')
#print a
receivedId= a[3]
print receivedId
receivedId = int(receivedId)

commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	insertion = 'update  USER set STORAGE_NAME ="%s" where ID =%d;' % (storageName,receivedId)
	
	cursor.execute(insertion)
	values = 'select *from USER where ID =%d;' % (receivedId)
	cursor.execute(values)
	
	for y in cursor.fetchall():
		print y[5]
		print y[6]
		print y[7]
		print y[8]
		if y[5] == "block" :
	
			t= commands.getstatusoutput("sudo lvcreate --name " + y[8] + " --size " + y[7] + "G vg1")
			print t
			iqn = """
						<target {0}>
						backing-store /dev/mapper/vg1-{0} 
						</target>
				""".format(y[8])

			t = commands.getstatusoutput("sudo chmod 777 /etc/tgt/conf.d/ -R")
			t = commands.getstatusoutput("touch /etc/tgt/conf.d/"+y[8]+".conf")
			print t
			t = commands.getstatusoutput("sudo echo '" + iqn + "' > /etc/tgt/conf.d/" + y[8]+".conf")
			print t
			print "#######}"
			t = commands.getstatusoutput("sudo systemctl restart tgtd ")
				
			print t
			f = open("/var/www/html/iscsiC.py","w")
			f.write('''#!/usr/bin/python2	\n

import commands	\n

x = commands.getstatusoutput("sudo yum install iscsi-initiator-utils")\n
p = commands.getstatusoutput("iscsiadm --mode discoverydb --type sendtargets --portal 192.168.42.151 --discover") \n
x = commands.getstatusoutput("iscsiadm --mode node --targetname {0} --portal 192.168.42.151:3260 --login")\n
raw_input() \n
			'''.format(y[8]))
			f.close()
			commands.getstatusoutput("sudo chmod +x ../html/iscsiC.py")
#	print a
			b =	commands.getstatusoutput("tar -cf ISCSI.tar --directory='/var/www/html' iscsiC.py ; mv ISCSI.tar ../html/")
					
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/staasLastISCSI.html\">\n";
		elif y[5] == "object" :
			if y[6] == "nfs" :
				yn = str(receivedId)+"_" + y[8]
				print yn
				print "<br /><br />"
				t= commands.getstatusoutput("sudo lvcreate --name " + yn + " --size " + y[7] + "G vg1")
				print t
				t= commands.getstatusoutput("sudo mkfs.ext4 /dev/mapper/vg1-" + yn)
				t= commands.getstatusoutput("sudo mkdir /mnt/"+yn)
				print y[8]
				t= commands.getstatusoutput("sudo mount /dev/mapper/vg1-" + yn + " /mnt/"+yn)
				print t
				print "\n"
				t= commands.getstatusoutput("sudo echo \"/mnt/"+yn +"	*(rw,no_root_squash)\" > /etc/exports")
				print t
				t= commands.getstatusoutput("sudo systemctl restart nfs")
				f = open("/var/www/html/nfsC.py","w")
				f.write('''#! /usr/bin/python2	\n

import commands,os	\n

z = commands.getstatusoutput("showmount -e 192.168.42.151");	\n
yt = z[1]	\n
yt = yt[:-2]	\n
yt=yt.split(":")	\n
yt=yt[1]	\n
yt=yt.strip()	\n
os.system("mkdir /home/{0}")	\n
os.system("mount 192.168.42.151:"+yt+" /home/{0}")	\n
			'''.format(yn))
	###########################################################################################
	####################################### IAAS	ALLOCATION ################################
	###########################################################################################
#	x = commands.getstatusoutput("virt-install --ram " + ram + " --vcpu " + cores + " --disk path =/var/lib/libvirt/images/rhel7.qcow2,size=" +hdd+ " --location ftp://192.168.0.254/pub/Softwares/ -hvm arch=x86_64 --os-variant rhel7 --os-type "+ type +" --vnc --vnc-listen=192.168.0.100 --vnc-port=5900" )
#	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/basicProfile.html\">\n";
				f.close()
				commands.getstatusoutput("sudo chmod +x ../html/nfsC.py")
#	print a
				b =	commands.getstatusoutput("tar -cf NFS.tar --directory='/var/www/html' nfsC.py ; mv NFS.tar ../html/")
				print b
				print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/staasLast.html\">\n";

#	print c
#	commands.getstatusoutput("tar -cf /var/www/html/hello1.tar /var/www/html/nfsC.py")
			elif y[6] == "sshfs" :
				yn = str(receivedId)+"_" + y[8]
				t= commands.getstatusoutput("sudo lvcreate --name " + yn + " --size " + y[7] + "G vg1")
				print t
				t= commands.getstatusoutput("sudo mkfs.ext4 /dev/mapper/vg1-" + yn)
				print t
				t = commands.getstatusoutput("sudo useradd " + yn)
				print t
				t = commands.getstatusoutput("echo \""+ y[3]+ "\" | sudo passwd " + yn + " --stdin")
				print t
				t= commands.getstatusoutput("sudo mkdir /home/"+yn +"/sshfs")
				print t
				print y[8]
				t= commands.getstatusoutput("sudo mount -o rw /dev/mapper/vg1-"+yn + " /home/"+yn+"/sshfs")
				print t
				print "\n"
				t = commands.getstatusoutput("chmod 777 /home/"+yn+"/sshfs/ -R ")
				t= commands.getstatusoutput("sudo systemctl restart sshfs")
				print t
				f = open("/var/www/html/sshfsC.py","w")
				f.write('''#!/usr/bin/python2	\n

import commands,os	\n
os.system("mkdir /home/{0}")	\n
a = commands.getstatusoutput("sshfs -o nonempty,rw {0}@192.168.42.151:/home/{0}/sshfs /home/{0}")	\n
print a  \n
raw_input() \n
			'''.format(yn))
				f.close()
				commands.getstatusoutput("sudo chmod +x ../html/sshfsC.py")
#	print a
				b =	commands.getstatusoutput("tar -cf SSHFS.tar --directory='/var/www/html' sshfsC.py ; mv SSHFS.tar ../html/")
				print b
				t = commands.getstatusoutput("sudo chmod 777 /home/"+y[8]+"/sshfs/ -R ")
				print  t
				print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/staasLastSSHFS.html\">\n";

			elif y[6] == "glusterfs":
				r = int(y[7]) 

				print y[7]  
				print r 
				s = r*512 
				print s 
				print "**"
				q = str(s) 
				print q
				print "**"
				print("sudo lvcreate --name " + y[8] + "1 --size " + q + "M vg1")
				t= commands.getstatusoutput("sudo lvcreate --name " + y[8] + "1 --size " + q + "M vg1")
				print t
				t= commands.getstatusoutput("sudo mkfs.ext4 /dev/mapper/vg1-" + y[8]+"1")
				print t
				t= commands.getstatusoutput("sudo mkdir /mnt/"+y[8] +"1")
				print t
				t= commands.getstatusoutput("sudo mount /dev/mapper/vg1-" + y[8] + "1 /mnt/"+y[8]+"1")
				print t
				print "\n"
				t= commands.getstatusoutput("sudo lvcreate --name " + y[8] + "2 --size " + q + "M vg1")
				print t
				t= commands.getstatusoutput("sudo mkfs.ext4 /dev/mapper/vg1-" + y[8]+"2")
				print t
				t= commands.getstatusoutput("sudo mkdir /mnt/"+y[8] +"2")
				print t
				t= commands.getstatusoutput("sudo mount /dev/mapper/vg1-" + y[8] + "2 /mnt/"+y[8]+"2")
				print t
				print "\n"
				t = commands.getstatusoutput("sudo systemctl restart glusterd")
				print t
				t = commands.getstatusoutput("sudo gluster  volume create " + y[8] + " 192.168.42.151:/mnt/"+y[8]+"1 192.168.42.151:/mnt/" + y[8] + "2 force")
				print t
				t = commands.getstatusoutput("sudo gluster volume start " + y[8])
				print t
				f = open("/var/www/html/glusterfsC.py","w")
				f.write('''#!/usr/bin/python2	\n
import commands,os	\n
os.system("mkdir /media/{0}")	\n
os.system("mount -o rw 192.168.42.151:/{0} /media/{0}")	\n
raw_input()	\n
			'''.format(y[8]))
				f.close()
				commands.getstatusoutput("sudo chmod +x ../html/glusterfsC.py")
#	print a
				b =	commands.getstatusoutput("tar -cf GLUSTER.tar --directory='/var/www/html' glusterfsC.py ; mv GLUSTER.tar ../html/")
				print b
				t = commands.getstatusoutput("sudo chmod 777 /mnt/"+y[8]+"1 -R")
				t = commands.getstatusoutput("sudo chmod 777 /mnt/"+y[8]+"2 -R")
				print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/staasLastGluster.html\">\n";

			elif y[6] == "samba" :
				t= commands.getstatusoutput("sudo lvcreate --name " + y[8] + " --size " + y[7] + "G vg1")
				print t
				t= commands.getstatusoutput("sudo mkfs.ext4 /dev/mapper/vg1-" + y[8])
				print t
				t= commands.getstatusoutput("sudo chmod +w /etc/samba/smb.conf")
				print t
				smbinfo = """[{0}]	\n
path=/media/{0}	\n
writable = yes	\n
				""".format(y[8])
				t = commands.getstatusoutput("sudo echo '"+smbinfo+"' >> /etc/samba/smb.conf")
				t = commands.getstatusoutput("sudo useradd -s /sbin/nologin " + y[8])
				print t
				t = commands.getstatusoutput("sudo systemctl restart smb")
				print t
				t = commands.getstatusoutput("sudo systemctl enable smb")
				print t
				t = commands.getstatusoutput("iptables -F ; setenforce 0")
				t = commands.getstatusoutput("echo -e \"{0}\n{0}\" | sudo smbpasswd -a ".format(y[3]) + y[8])
				print t
				t = commands.getstatusoutput("sudo mkdir /media/"+y[8])
				t = commands.getstatusoutput("sudo chmod g+w /media/" + y[8])
				t = commands.getstatusoutput("sudo chmod o+w /media/" + y[8])
				print t
				print y[8]
				t= commands.getstatusoutput("sudo mount -o rw /dev/mapper/vg1-"+y[8] + " /media/"+y[8])
				print t
				print "\n"
				t = commands.getstatusoutput("sudo chmod 777 /media/"+y[8]+" -R ")
				
				f = open("/var/www/html/sambaC.py","w")
				f.write('''#!/usr/bin/python2	\n

import commands,os	\n
os.system("mkdir /media/{0}")	\n
a = commands.getstatusoutput("mount -o username={0} //192.168.42.151/{0} /media/{0}")	\n
print a  \n
raw_input() \n
			'''.format(y[8]))
				f.close()
				commands.getstatusoutput("sudo chmod +x ../html/sambaC.py")
#	print a
				b =	commands.getstatusoutput("tar -cf SAMBA.tar --directory='/var/www/html' sambaC.py ; mv SAMBA.tar ../html/")
				print b
				t = commands.getstatusoutput("sudo chmod 777 /media/"+y[8]+" -R ")
				print  t
				print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/staasLastSAMBA.html\">\n";

	db.commit()
except:
	db.rollback()
finally:
	db.close()
