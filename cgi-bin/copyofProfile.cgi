#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import random
import commands,os,time
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
print '''
	b = document.cookie
'''
#b = form.getvalue('receivedId')
id = b[3]
print id
receivedId = int(id)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
print '''
<html>
<head>
	<title>Cloud - USER1</title>
	<style type="text/css">
	body{
		background-image: url(\'Cloud.jpg\');
		background-repeat:repeat;
		background-size: cover ;
		margin-top: 0px;
		margin-left: 0;
	}
	ul{
		list-style-type: none;
		margin-top: 0px;
		padding: 0;
		width: 150px;
		background-color: #2C3E50;
		height: 100%;
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
		.one{
			margin-top:75px;
			height:300px;
			width:300px;
			position:absolute;
			margin-left:300px;

		}
		.two{
			margin-top:75px;
			height:300px;
			width:300px;
			position:absolute;
			margin-left:650px;

		}
		.three{
			margin-top:75px;
			height:300px;
			width:300px;
			position:absolute;
			margin-left:1000px;

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
		.three:hover{
			height:100%;
			width:100%;
			margin-left:0px;
			margin-top:0px;
			transition:all 2s;
			transform:rotate(360deg);		
			z-index:2;

		}
		img.toshift{
			margin-top: 50px;
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

	</style>
</head>
<body>
	<script type="text/javascript">
		 a = document.cookie
		 
		function cread() {
		document.write("<input type=\'text\' placeholder="+a + " name=\'cookie\'  >")
	}
	</script>

	<div class="one" >
		<a href="saas.html">
		
		<img class="toshift" height="100%" width="100%"  src="saas.jpg"></img>
		</a>
	</div>
	<div class="two">
		<a href="staas.html">
		
		<img class="toshift" height="100%" width="100%"  src="imagesh.jpg"></img>
		</a>
		
	</div>
	<div class="three" >
		<a href="iaas1.html">
		
		<img class="toshift" height="100%" width="100%"  src="iaas.jpg"></img>
		</a>
	</div>
	
	<ul>
	'''
x = 'select * from USER where id = %d;' % (receivedId)
cursor.execute(x)
for q in cursor.fetchall():
	print q[0]
	print q[1]
	print '''
		<li> <div><img src="http://192.168.42.151/prfPic/'''+q[1]+"/"+q[22]+'''" alt="DisplayPicture" height="150px" width="150px" 	/> 
	'''
print '''			



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
		
		<li class="special"> <a href="../cgi-bin/final.cgi"> </a>
		<FORM enctype="multipart/form-data" action="../cgi-bin/final.cgi" method="post">
				<script type="text/javascript">
				a = document.cookie
				document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
				</script>
				<INPUT type=\'submit\'value="Profile" class="special" ></INPUT>
				</li>
		<li> <a href="http://192.168.42.151/cgi-bin/trying.cgi">	History	</a>	</li>
		<li> <a href="security.html">	Security	</a>	</li>
		<li> <a href="feature.html">	Other Features	</a>	</li>
		<li> <a href="help.html">	Help	</a>	</li>
		<li> <a href="contact.html">	Contact Us	</a>	</li>
		<li> <a href="logout.html">	Log Out	</a>	</li>
	</ul>
</body>
</html>
'''
