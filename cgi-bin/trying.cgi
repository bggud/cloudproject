#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import random
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.
form = cgi.FieldStorage()
a = form.getvalue('receivedId')
#print a
id= a[3]
print id
id=int(id)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	values = "select *from USER where id = %d " % (id)
	cursor.execute(values)
	
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
	<p >'''
	print '''
			<div class=\'history\'>
				<h2>IAAS History :</h2>
					<div class=\'historyP\' width="300px" height="800px">
						All Instances :  <Names of all the instances --- with a Launch Button on its right>
						&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button>Redhat </button>'''

	for y in cursor.fetchall():

		for a in range(y[16]):

			print'''			<form  method="post"  action="hybrid3.cgi">
			
						<script type="text/javascript">
						 a = document.cookie
						 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
						</script>

			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:5px;" type="submit" value = "Redhat-{0}-{1}" ></input>
			</form>'''.format(str(id),str(a))
		if y[16] == 3:	
			print '''
							 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
							<button   style="margin-top:-193px;margin-left:350px;"  >Debian</button>'''
			for a in range(y[21]):
				print'''
							<form  method="post"  action="hybrid4.cgi">
							<script type="text/javascript">
					 a = document.cookie
					 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
				</script>


				<input type="hidden" name="counter" value={1} />
				<input style="margin-top:-143px;margin-left:250px;" type="submit" value = "Debian-{0}-{1}" ></input>
				</form>'''.format(str(id),str(a))
			if y[21] == 3 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-332px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-300px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
			elif y[21] == 2 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-297px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-265px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
			elif y[21] == 1 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-262px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-230px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))

			elif y[21] == 0 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-212px;margin-left:630px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-160px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
		elif y[16] == 2:	
			print '''
							 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
							<button   style="margin-top:-153px;margin-left:350px;"  >Debian</button>'''
			for a in range(y[21]):
				print'''
							<form  method="post"  action="hybrid4.cgi">
							<script type="text/javascript">
					 a = document.cookie
					 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
				</script>


				<input type="hidden" name="counter" value={1} />
				<input style="margin-top:-103px;margin-left:250px;" type="submit" value = "Debian-{0}-{1}" ></input>
				</form>'''.format(str(id),str(a))

			if y[21] == 3 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-292px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-260px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
			elif y[21] == 2 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-257px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-225px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
			elif y[21] == 1 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-222px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-190px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))

			elif y[21] == 0 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-172px;margin-left:630px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-120px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))




		elif y[16] == 1:	
			print '''
							 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
							<button   style="margin-top:-123px;margin-left:350px;"  >Debian</button>'''
			for a in range(y[21]):
				print'''
							<form  method="post"  action="hybrid4.cgi">
							<script type="text/javascript">
					 a = document.cookie
					 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
				</script>


				<input type="hidden" name="counter" value={1} />
				<input style="margin-top:-73px;margin-left:250px;" type="submit" value = "Debian-{0}-{1}" ></input>
				</form>'''.format(str(id),str(a))


			if y[21] == 3 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-262px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-230px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
			elif y[21] == 2 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-227px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-195px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
			elif y[21] == 1 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-192px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-160px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))

			elif y[21] == 0 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-142px;margin-left:630px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-90px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))

		elif y[16] == 0:	
			print '''
							 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
							<button   style="margin-top:-86px;margin-left:400px;"  >Debian</button>'''
			for a in range(y[21]):
				print'''
							<form  method="post"  action="hybrid4.cgi">
							<script type="text/javascript">
					 a = document.cookie
					 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
				</script>


				<input type="hidden" name="counter" value={1} />
				<input style="margin-top:-33px;margin-left:250px;" type="submit" value = "Debian-{0}-{1}" ></input>
				</form>'''.format(str(id),str(a))


			if y[21] == 3 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-222px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-190px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
			elif y[21] == 2 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-187px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-155px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
			elif y[21] == 1 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-152px;margin-left:550px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-120px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))

			elif y[21] == 0 :

				print '''
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<button   style="margin-top:-102px;margin-left:630px;"  >Windows</button><br/><br />
		'''
				for a in range(y[20]):
					print '''
						
						<form method="post"  action="hybrid2.cgi">
						<script type="text/javascript">
				 a = document.cookie
				 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
			</script>


			<input type="hidden" name="counter" value={1} />
			<input  style="margin-top:-50px;margin-left:450px;" type="submit" value = "Windows-{0}-{1}" ></input>
			</form>
			'''.format(str(id),str(a))
		c= commands.getstatusoutput(" sudo ls -la /mnt |awk '{print $9;}' | grep ^"+str(id) +"_")
#		print c
		m = c[1]
		names = m.split("\n")

		c= commands.getstatusoutput(" sudo df -hT | grep /mnt | grep ext4 | grep "+str(id) +"_ | awk '{print $3;}'")
#		print c
		n = c[1]
		n = n.split("\n")
#		print n
		total = n
#		print total
		c= commands.getstatusoutput(" sudo df -hT | grep ext4 | grep "+str(id) +"_ | awk '{print $5;}'")
		b = c[1]
		b = b.split("\n")
		available = b
#		print available
		print '''			
	
	
						<br/><br />

					</div>
					<br />
					<h2>Staas Information :</h2>
					<div class=\'historyP\' style="height:800px;" width="300px">
					<!--	Total Storage : <Folder - Wise with Mount location of the corresponding folder and te type of service used><br/><br />

						Available Storage : <MOBILE NUMBER><br /><br />

						Instance Information : <DATE OF BIRTH><br /><br />-->
						<table height="800px" >
							<thead>
								<th>Folder-Name</th>
								<th>Action</th>
								<th>Total-Space</th>
								<th>Available-Space</th>
								<th>Service-Used</th>
							</thead>'''
		for z in range(len(available)):
			if len(available) == 0:
				break
			print '''
							<thead>
								<th>
									'''+names[z]+'''
								</th>
								<th>
											<form  method="post"  action="extend.cgi">
			
						<script type="text/javascript">
						 a = document.cookie
						 document.write("<input type=\'hidden\' value="+a+" name=\'receivedId\'  >")
						 document.write("<input type=\'hidden\' value='''+names[z]+''' name=\'name\'>")
						</script>
						<center>
						<input  class="me" type = "submit" name="extend" value="Extend" />
						</center>
						</form>
								</th>
								<th>
									'''+ total[z]+'''
								</th>
								<th>
									'''+available[z]+'''
								</th>
								<th>
									NFS
								</th>
							</thead>'''
		print '''
						</table>
					</div>
			</div>
			
		</p>
		</center>
	</body>
</html>
		
</html>

'''

		db.commit()
except:
	db.rollback()
finally:
	db.close()

