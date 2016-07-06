#! /usr/bin/python2
import cgitb # its traceback for displaying the errors on web browser
import cgi
import commands,os
import mysql.connector as mariadb
cgitb.enable() # enabling  the traceback

print "content-type:text/html" # browser understands HTML only , we need to tell this
print ""	# it indicates the termination of header.

form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
receivedId = form.getvalue('receivedId')
receivedId = int(receivedId)
commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');

cursor = db.cursor();
try:
	values = "select *from USER where id = %d " % (receivedId)
	cursor.execute(values)
	for y in cursor.fetchall() :
		print y[6]
		print y[7]
		print y[8]
		print y[15]
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
		background-image: url("Cloud.jpg");
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
		width: 150px;
		font-size: 20px;
		font-weight: bold;
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
	}
	th,td,tr{
		
		border-radius: 20px;
		border-spacing: 18px;
		border-width: 5px;
		padding: 10px;
		border-collapse: no-collapse;
		color: #C0C0C0;
		border-bottom: 2px solid;
	}
	tr{
		text-align: center;
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
		.three:hover{
			height:100%;
			width:100%;
			margin-left:0px;
			margin-top:0px;
			transition:all 2s;
			transform:rotate(360deg);		
			z-index:2;

		}
	</style>
</head>
<body>
	

	<ul>
		<li> <div><img src="cld1.jpg" alt="DisplayPicture" height="150px" width="150px" 	/> </div></li>
		<li> <a href="profile.html">	Profile 	</a>	</li>
		<li> <a href="history.html">	History	</a>	</li>
		<li> <a href="saas.html">	SAAS 	</a>	</li>
		<li> <a href="staas.html">	Staas </a>	</li>
		<li> <a href="iaas1.html">	IAAS	</a>	</li>
		<li> <a href="security.html">	Security	</a>	</li>
		<li> <a href="feature.html">	Other Features	</a>	</li>
		<li> <a href="help.html">	Help	</a>	</li>
		<li> <a href="contact.html">	Contact Us	</a>	</li>
		<li> <a href="logout.html">	Log Out	</a>	</li>
	</ul>
	
	<p >
			<div class="history">
				<h2>IAAS History :</h2>
					<div class="historyP" width="300px" height="800px">
						All Instances :  <Names of all the instances --- with a Launch Button on its right><button>Launch me !</button><br/><br />
						Currently Running Instances : <Currently Running with the corresponding OS Gallery>
						<div class="one" >
		<a href="kali.html">
		
		<img height="100%" width="100%"  src="kali.png"></img>
		</a>
	</div>
	<div class="two">
		<a href="ubuntu.html">
		
		<img height="100%" width="100%"  src="ubuntu.png"></img>
		</a>
		
	</div>
	<div class="three" >
		<a href="rhel7.html">
		
		<img height="100%" width="100%"  src="rhel7.png"></img>
		</a>
	</div>
						<br/><br />

					</div>
					<br />
					<h2>Staas Information :</h2>
					<div class="historyP" width="300px">
					<!--	Total Storage : <Folder - Wise with Mount location of the corresponding folder and te type of service used><br/><br />

						Available Storage : <MOBILE NUMBER><br /><br />

						Instance Information : <DATE OF BIRTH><br /><br />-->'''

		print '''	<table >
							<thead>
								<th>Folder-Name</th>
								<th>Folder-Location</th>
								<th>Total-Space</th>
								<th>Available-Space</th>
								<th>Service-Used</th>
							</thead>
							<tr>
								<td>
									{0}
								</td>'''.format(y[8])
		print '''					<td>
		
									<script type="text/javascript">
									function hello(){
										if({1} == "Global"){
											<a href = "www.google.com">{1}</a>
										}
										else{
											{1}
										}
									}
									hello();
									</script>
								</td>
								<td>
									{2}
								</td>
								<td>
									1
								</td>
								<td>
									{3}
								</td>
							</tr>
						</table>
					</div>
					<h2>SAAS Information :</h2>
					<div class="historyP" width="300px">
						Available Softwares for your account :

					</div>
			</div>
			
		</p>
		</center>
	</body>
</html>
		
</html>		'''.format(y[15],y[7],y[6])

	db.commit()
except:
	db.rollback()
finally:
	db.close()
