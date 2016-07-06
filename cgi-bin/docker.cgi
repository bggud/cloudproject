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
application = form.getvalue('app')	# filters the value of  "name=USERNAME" from the whole data captured in the above variable
a=form.getvalue('receivedId')
print a
receivedId= a[3]
receivedId = int(receivedId)

a = commands.getstatusoutput("sudo systemctl restart mariadb")
print a
a = commands.getstatusoutput("sudo systemctl stop docker")
print a
#a = commands.getstatusoutput("sudo docker daemon -H tcp://192.168.42.151:2375")
print a
a = commands.getstatusoutput("sudo systemctl restart docker")
print a
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	
	insertion = 'update  USER set INSTANCE_NAME ="%s" where ID =%d;' % (application,receivedId)
	cursor.execute(insertion)

	db.commit()
#	r = commands.getstatusoutput("touch /dockerFile/user.sh ")
	values = "select * from USER where ID=%d;" % (receivedId)
	cursor.execute(values)
	for y in cursor.fetchall():
		print y[17]
		print "sudo echo 'echo -e \'"+y[3]+"\n"+y[3]+"\' | passwd  "+y[1]+" --stdin\n' >> /dockerFile/user.sh"
		if y[17] == "shellinabox":
			r = commands.getstatusoutput("sudo touch /dockerFile/user.sh ")
			print r
			r = commands.getstatusoutput("sudo chmod 777 /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput("sudo echo '#!/bin/bash\n useradd "+y[1]+"\n'  >  /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput('sudo echo "echo \''+y[3]+'\' | passwd  '+y[1]+' --stdin\n" >> /dockerFile/user.sh')
			print r

			a = commands.getstatusoutput("sudo systemctl restart docker")
			print a			
			a = commands.getstatusoutput("sudo docker run -ti -d  --privileged -v /dockerFile/user.sh:/dockerFile/user.sh  -p "+str(receivedId)+"999:4200 hunt_d/centos6   bash");
			print a
			d = commands.getstatusoutput("sudo docker start "+a[1])
			print d
			ip = commands.getstatusoutput("sudo docker exec -t "+a[1]+" hostname -i")
			print ip
			myip = ip[1].strip("\r")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" sed -i 's/172.17.0.2/"+myip+"/'  /etc/sysconfig/shellinaboxd")
			print i

			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/shellinaboxd restart")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/sshd restart")

			print i
			i = commands.getstatusoutput('sudo docker exec -t '+a[1]+'    /dockerFile/user.sh')
			print i
#			i = commands.getstatusoutput("sudo docker attach " +a[1])

			print i
			print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('use your Cloud Username and Password to login the shell');
				}
				alertMsg();
				</script>
				</body>"""
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=https://192.168.42.151:"+str(receivedId)+"999\">\n";

		elif y[17] == "apache":

			r = commands.getstatusoutput("sudo touch /dockerFile/user.sh ")
			print r
			r = commands.getstatusoutput("sudo chmod 777 /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput("sudo echo '#!/bin/bash\n groupadd abcd\n mkdir /home/abcd \n chown root:abcd /home/abcd\n chmod 775 /home/abcd -R '  >  /dockerFile/user.sh")
			print r

			r = commands.getstatusoutput("sudo echo ' useradd -g abcd -d /home/abcd "+y[1]+"\n '  >>  /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput('sudo echo "echo \''+y[3]+'\' | passwd  '+y[1]+' --stdin\n" >> /dockerFile/user.sh')
			print r
#
			r = commands.getstatusoutput("sudo echo 'chown root:abcd /var/www/html\nchmod 775 /var/www/html\n mount  --bind /home/abcd /var/www/html\n cp /var/www/html2/* /home/abcd/ \niptables -F'  >>  /dockerFile/user.sh")

			a = commands.getstatusoutput("sudo systemctl restart docker")
			print a			
			a = commands.getstatusoutput("sudo docker run -ti -d -v /dockerFile/user.sh:/dockerFile/user.sh -v /var/www/"+y[1]+":/var/www/html2 --privileged  -p "+str(receivedId)+"998:4200  -p  "+str(receivedId)+"992:80 bhagyashree/apacheftpcentos6   bash");
			print a
			d = commands.getstatusoutput("sudo docker start "+a[1])
			print d
			ip = commands.getstatusoutput("sudo docker exec -t "+a[1]+" hostname -i")
			print ip
			myip = ip[1].strip("\r")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" sed -i 's/172.17.0.2/"+myip+"/'  /etc/sysconfig/shellinaboxd")
			print i
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/shellinaboxd restart")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/sshd restart")

			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/httpd restart")

			print i
			i = commands.getstatusoutput('sudo docker exec -t '+a[1]+' /dockerFile/user.sh')

			print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('use your Cloud Username and Password to login the shell');
				}
				alertMsg();
				</script>
				</body>"""
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=https://192.168.42.151:"+str(receivedId)+"998\">\n";

		elif y[17] == "mysql":
			r = commands.getstatusoutput("sudo touch /dockerFile/user.sh ")
			print r
			r = commands.getstatusoutput("sudo chmod 777 /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput("sudo echo '#!/bin/bash\n useradd  "+y[1]+"\n'  >  /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput('sudo echo "echo \''+y[3]+'\' | passwd  '+y[1]+' --stdin\n" >> /dockerFile/user.sh')
			print r
			r = commands.getstatusoutput('sudo echo "echo \' mysql -u root -predhat\nexit \'>> /home/'+y[1]+'/.bashrc " >> /dockerFile/user.sh')
			print r
#

			a = commands.getstatusoutput("sudo systemctl restart docker")
			print a			
			a = commands.getstatusoutput("sudo docker run -ti -d  --privileged -v /dockerFile/user.sh:/dockerFile/user.sh -p "+str(receivedId)+"997:4200 bhagyashree/mysqlcentos6   bash");
			print a
			d = commands.getstatusoutput("sudo docker start "+a[1])
			print d
			ip = commands.getstatusoutput("sudo docker exec -t "+a[1]+" hostname -i")
			print ip
			myip = ip[1].strip("\r")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" sed -i 's/172.17.0.2/"+myip+"/'  /etc/sysconfig/shellinaboxd")
			print i
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/shellinaboxd restart")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/sshd restart")

			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" service mysqld restart")

			print i
			i = commands.getstatusoutput('sudo docker exec -t '+a[1]+'    /dockerFile/user.sh')
			print i
#			i = commands.getstatusoutput("sudo docker attach " +a[1])

			print i
			print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('use your Cloud Username and Password to login the shell');
				}
				alertMsg();
				</script>
				</body>"""
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=https://192.168.42.151:"+str(receivedId)+"997\">\n";
		elif y[17] == "textbased":
			print '''

<html>
<head>
	<title>Cloud - USER1</title>
	
	<style type="text/css">
	li div img{
		width: 100px;
		height: 100px;
		background-position: center;
		border-radius: 150px ;
		border-color : #C0C0C0;;
		border-style: solid;
		border-width: 3px;
		margin-left: 20px;
		margin-top: 20px;
	}
	body{
		background-image: url(\'http://192.168.42.151/cloud.jpg\');
		background-repeat: repeat;
		background-size: cover ;
		margin-top: 0px;
		margin-left: 0;
		
	}
	li div img{
		width: 100px;
		height: 100px;
		background-position: center;
		border-radius: 150px ;
		border-color : #C0C0C0;;
		border-style: solid;
		border-width: 3px;
		margin-left: 20px;
		margin-top: 20px;
	}
	ul{
		list-style-type: none;
		margin-top: 0px;
		padding: 0;
		width: 150px;
		background-color: #2C3E50;
		height: 100%;
		position: fixed;
	}
	li a {

   		 display: block;
   		 text-decoration: none;
   		 color: #C0C0C0;
   		 font-weight: bold;
   		 padding:8px 0 8px 16px;
	}
	li a:hover {
    	background-color: #555;
    	color: white;
	}
	li div{

		width: 100px;
		height: 150px;
		border-radius: 50px;
		background-repeat: no-repeat;
		background-position: center;
		background-size: cover
	}
	.history{
		font-size: 15px;
		margin-top: 30px;
		margin-left: 200px;
		position: absolute;
		color: #C0C0C0;
   		 font-weight: bold;
	}
	.historyP{
		width: 900px;
		position: relative;
		margin-top: 10px;
		color: #C0C0C0;
   		border-width: 10px;
		background-color: #2C3E50;
		border-style: solid;
		border-color: #C0C0C0;
		border-radius: 20px;
		padding: 15px 15px 15px 15px ;
		padding-left: 10px;
		height: 200px;
	}
	button{
		color: #2C3E50;
		text-align: center;
		padding: 3px;
		font-size: 10px;
		width: 200px;
		font-size: 20px;
		font-weight: bold;
		background-color: #2C3E50;
	}
	table{
		border-style: solid;
		border-radius: 20px;
		border-spacing: 18px;
		border-width: 5px;
		padding: 10px;
		border-collapse: no-collapse;
		color: #C0C0C0;
		width: 100%;
		height : 200px;
	}
	button,th{
		
		border-radius: 20px;
		border-spacing: 18px;
		border-width: 5px;
		padding: 10px;
		border-collapse: no-collapse;
		color: #C0C0C0;
		border-bottom: 2px solid;
	}
	tr{
		position: relative;
		text-align: center;
	}
	.me{
		border-radius: 20px;
		border-spacing: 18px;
		border-width: 5px;
		padding: 10px;
		border-collapse: no-collapse;
		color: #C0C0C0;
		border-bottom: 5px solid;
		position: absolute;
		text-align: center;	
		margin-top:0px;
		margin-left:-150px;
		width:100px;
		background-color: #2C3E50;
		border-style:none;
		font-weight:bold;
		font-size:18px;
	}
	.me :hover {
		margin-left:2px;
    	background-color: #555;
    	color: white;
	}
	.one{
			margin-top:25px;
			height:100px;
			width:100px;
			position:absolute;
			margin-left:300px;
			border-bottom: solid;
		}
		.two{
			margin-top:25px;
			height:100px;
			width:100px;
			position:absolute;
			margin-left:450px;
			border-bottom: solid;
		}
		.three{
			margin-top:25px;
			height:100px;
			width:100px;
			position:absolute;
			margin-left:600px;
			border-bottom: solid;
		}
		.one:hover{
			height:100%;
			width:100%;
			margin-left:0px;
			margin-top:0px;
			transition:all 2s;
			transform:rotate(360deg);		
			z-index:2;
		}
		.two:hover{
			height:100%;
			width:100%;
			margin-left:0px;
			transition:all 2s;
			transform:rotate(360deg);		
			margin-top:0px;
			z-index:2;
		}
			.my{
		background-color: #2C3E50;
		border-bottom:1px solid;
		text-align: center;
		padding: 10px 10px 10px 5px;
		border-top-width: medium;
	border-right-width: medium;
	border-bottom-width: 1px;
	border-left-width: medium;
	border-top-style: none;
border-right-style: none;
border-bottom-style: solid;
border-left-style: none;
border-top-color: -moz-use-text-color;
border-right-color: -moz-use-text-color;
border-bottom-color: #CBCBCB;
border-left-color: -moz-use-text-color;
color: #C0C0C0;
	}
		.three:hover{
			height:100%;
			width:100%;
			margin-left:0px;
			margin-top:0px;
			transition:all 2s;
			transform:rotate(360deg);		
			z-index:2;

		}
				li form input.special {
		background-color: #2C3E50;
   		 display: block;
   		 text-decoration: none;
   		 color: #C0C0C0;
   		 font-weight: bold;
   		 padding:8px 0 8px 16px;
   		 padding-bottom: 0px ;
   		 font-size: 17px;
   		 font-style: Arial ;
   		 margin-top : 50px;
		 border-style: none;
	}
	iframe{

		position:relative;
		height:500px;
		width:500px;
	}
		form {
			margin-left :200px;
			margin-top : 0px;
			padding : 0px;
			height : 20px;
			width : 10px;
		}

.my{
		background-color: #2C3E50;
		text-align: center;

border-style: none;
width: 50px;
color: #C0C0C0;
	}

	.my1{
		background-color: #2C3E50;
		text-align: center;
		font-weight: bold;
		font-size: 20px;
border-style: none;
width: 100px;
color: #C0C0C0;
	}
				li div img{
		width: 100px;
		height: 100px;
		background-position: center;
		border-radius: 150px ;
		border-color : #C0C0C0;;
		border-style: solid;
		border-width: 3px;
		margin-left: 20px;
		margin-top: 20px;
	}		li form input.special {
		background-color: #2C3E50;
   		 display: block;
   		 text-decoration: none;
   		 color: #C0C0C0;
   		 font-weight: bold;
   		 padding:8px 0 8px 16px;
   		 padding-bottom: 0px ;
   		 font-size: 17px;
   		 font-style: Arial ;
   		 margin-top : 50px;
		 border-style: none;
	}	

	</style>
</head>
<body>
	

	<ul>
		<li> <div>
		<script type="text/javascript">
		var ai
		ai = document.cookie
		document.write("<img src=\'/prfPic/"+ai[3]+".jpg\' alt=\'DisplayPicture\' height=\'150px\' width=\'150px\' 	/>") 

		</script>
			



			<FORM enctype="multipart/form-data" action="../cgi-bin/new1.cgi" method="post">
				<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
				</script>
				<input  type="file" name="FILE" required>
				<center>
				<INPUT type=\'submit\'value="Upload"></INPUT>
				</center>
			</form>



			
		</div></li>


		<li> 

<FORM enctype="multipart/form-data" action="../cgi-bin/final.cgi" method="post">
							<script type="text/javascript">
							a = document.cookie
							 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
							</script>
							<input class="me" type="submit" value="Profile">
							</form>

			</li>
		<li> 

<FORM enctype="multipart/form-data" action="../cgi-bin/trying.cgi" method="post">
							<script type="text/javascript">
							a = document.cookie
							 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
							</script>
							<input class="me" type="submit" value="History">
							</form>

			</li>

		<li> <a href="../saas.html">	SAAS 	</a>	</li>
		<li> <a href="../staas.html">	Staas </a>	</li>
		<li> <a href="../iaas1.html">	IAAS	</a>	</li>
		<li> <a href="../security.html">	Security	</a>	</li>
		<li> <a href="../docker.html">	Other Features	</a>	</li>
		<li> <a href="../help.html">	Help	</a>	</li>
		<li> <a href="../contact.html">	Contact Us	</a>	</li>
		<li> <a href="../logout.html">	Log Out	</a>	</li>
	</ul>
	<form target="_blank" action="next.cgi" method="post">
	<div class="abc" style="margin-left:400px;margin-top:100px;"> <textarea style="z-index:2"rows="15px" cols="40px" name="pycode">

		</textarea></div>
		<input type="submit" value="Go" />
		</form>
	<p >'''

		elif y[17] == "python":
			r = commands.getstatusoutput("sudo touch /dockerFile/user.sh ")
			print r
			r = commands.getstatusoutput("sudo chmod 777 /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput("sudo echo '#!/bin/bash\n useradd -s /usr/bin/python "+y[1]+"\n'  >  /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput('sudo echo "echo \''+y[3]+'\' | passwd  '+y[1]+' --stdin\n" >> /dockerFile/user.sh')
			print r
#
			a = commands.getstatusoutput("sudo systemctl restart docker")
			print a			
			a = commands.getstatusoutput("sudo docker run -ti -d  --privileged -v /dockerFile/user.sh:/dockerFile/user.sh -p  "+str(receivedId)+"996:4200 hunt_d/centos6 bash");
			print a
			d = commands.getstatusoutput("sudo docker start "+a[1])
			print d
#			u = commands.getstatusoutput("sudo docker attach "+a[1])
#			print u
#			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" ifconfig")
#			print i
#			d = commands.getstatusoutput("sudo docker exec "+ a[1] +" sed -i 's/172.17.0.2/192.168.42.151/' /etc/sysconfig/shellinaboxd")
#			print d
			ip = commands.getstatusoutput("sudo docker exec -t "+a[1]+" hostname -i")
			print ip
			myip = ip[1].strip("\r")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" sed -i 's/172.17.0.2/"+myip+"/'  /etc/sysconfig/shellinaboxd")
			print i
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/shellinaboxd restart")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/sshd restart")

			print i
			i = commands.getstatusoutput('sudo docker exec -t '+a[1]+'   /dockerFile/user.sh')
			print i
#			i = commands.getstatusoutput("sudo docker attach " +a[1])

			print i
			print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('use root as  Username and your Password to login the shell');
				}
				alertMsg();
				</script>
				</body>"""
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=https://192.168.42.151:"+str(receivedId)+"996\">\n";

		elif y[17] == "ftp":
			r = commands.getstatusoutput("sudo touch /dockerFile/user.sh ")
			print r
			r = commands.getstatusoutput("sudo chmod 777 /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput("sudo echo '#!/bin/bash\n groupadd abcd\n mkdir /home/abcd \n chown root:abcd /home/abcd\n chmod 775 /home/abcd -R '  >  /dockerFile/user.sh")
			print r

			r = commands.getstatusoutput("sudo echo ' useradd -g abcd -d /home/abcd "+y[1]+"\n '  >>  /dockerFile/user.sh")
			print r
			r = commands.getstatusoutput('sudo echo "echo \''+y[3]+'\' | passwd  '+y[1]+' --stdin\n" >> /dockerFile/user.sh')
			print r
#
			r = commands.getstatusoutput("sudo echo 'chown root:abcd /var/ftp/pub\nchmod 775 /var/ftp/pub\n mount --bind /home/abcd /var/ftp/pub \niptables -F'  >>  /dockerFile/user.sh")
			print r


#			r = commands.getstatusoutput('sudo echo "echo \' sftp '+y[1]+'@localhost \'>> /home/'+y[1]+'/.bashrc " >> /dockerFile/user.sh')
			print r
#

			a = commands.getstatusoutput("sudo systemctl restart docker")
			print a			
			a = commands.getstatusoutput("sudo docker run -ti -d  --privileged -v /dockerFile/user.sh:/dockerFile/user.sh   -p "+str(receivedId)+"995:4200 -p "+str(receivedId)+"994:21 bhagyashree/ftpcentos6  ");
			print a
			d = commands.getstatusoutput("sudo docker start "+a[1])
			print d
			ip = commands.getstatusoutput("sudo docker exec -t "+a[1]+" hostname -i")
			print ip
			myip = ip[1].strip("\r")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" sed -i 's/172.17.0.2/"+myip+"/'  /etc/sysconfig/shellinaboxd")
			print i
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/shellinaboxd restart")
			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/sshd restart")

			i = commands.getstatusoutput("sudo docker exec -t "+a[1]+" /etc/init.d/vsftpd restart")

			print i
			i = commands.getstatusoutput('sudo docker exec -t '+a[1]+' /dockerFile/user.sh')
			print i
#			i = commands.getstatusoutput("sudo docker attach " +a[1])

			print i
			print """<body style=\"background-image: url('Cloud.jpg');\"><script>
				function alertMsg(){
					alert('use root as  Username and your Password to login the shell');
				}
				alertMsg();
				</script>
				</body>"""
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=https://192.168.42.151:"+str(receivedId)+"995\">\n";
		elif y[17]=="cli":
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.42.151/feature.html\">\n";

except:
	db.rollback()
finally:
	db.close()
