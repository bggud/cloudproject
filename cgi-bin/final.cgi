#!/usr/bin/python2
import os,commands
import mysql.connector as mariadb
import cgi
import cgitb
cgitb.enable()

print "content-type:text/html" # browser understands HTML only , we need to tell this
print""
form = cgi.FieldStorage()	#all data captured via  browser will be stored in this variable , whole data will be captured
a = form.getvalue('receivedId')
print len(a)
receivedId=a[3]
receivedId = int(receivedId)
#print receivedId


commands.getstatusoutput("systemctl restart mariadb")
db = mariadb.connect(user='root',password='redhat',database='cloud');
cursor = db.cursor();
values = 'select *from USER where ID =%d;' % (receivedId)
cursor.execute(values)
	
for y in cursor.fetchall():
	name1=y[1]
	email=y[2]
	password1=y[3]
	phoneno=y[4]

#print name1
#print email

print '''
<html>
<head>
	<title>Cloud - USER1</title>
	<style type="text/css">
	body{
		background-image: url(\'http://192.168.42.151/cloud.jpg\');
		background-repeat: no-repeat;
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
		position: absolute;
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
	li form input {
		background-color: #2C3E50;
   		 display: block;
   		 text-decoration: none;
   		 color: #C0C0C0;
   		 font-weight: bbackold;
   		 padding:8px 0 8px 16px;
   		 padding-bottom: 0px ;
   		 font-size: 17px;
   		 font-style: Arial ;
   		 border-style: none;
	}
	.me :hover {
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
	.personal{
		font-size: 15px;
		margin-top: 30px;
		margin-left: 200px;
		position: absolute;
		color: #C0C0C0;
   		 font-weight: bold;
	}
	.Internalp{
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
	}
	button{
		color: #2C3E50;
		text-align: center;
		padding: 3px;
		font-size: 10px;
		width: 120px;
		font-size: 20px;
		font-weight: bold;
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
	.account{
		width: 250px;
	}
	.aSize{
		height: 100px;
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
	
	<p >
			<div class="personal">
				<h2>Personal Information :</h2>
					<div class="Internalp" width="300px">
						Name : '''+name1+''' <br/><br />
'''

print'''

						Contact No. : ''' +phoneno+'''<br /><br />
'''

print '''
						E-mail : '''+email+''' <br /><br />
					</div><br />

					<h2>Account Information :</h2>
					<div class="Internalp" width="300px">
						Password : ********** <button >Edit</button><USERNAME> <br/><br />

						Balance Amount. : <MOBILE NUMBER><br /><br />

						Instance Information : <DATE OF BIRTH><br /><br />
					</div>
			</div>
			
	</p>
		</center>
		</body>
		
</html>
'''
print""
