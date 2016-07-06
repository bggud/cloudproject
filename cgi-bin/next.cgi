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
x =   form.getvalue('pycode')
f = open("a.py","w")
f.write(x)
f.close()
d = commands.getstatusoutput('sudo touch x.txt; sudo chmod 777 x.txt;sudo chmod 777 a.py')
print d
d = commands.getstatusoutput('sudo python a.py &> x.txt')
f1 = open("x.txt")
t=""
for x in f1.readlines():
	t = t + x
f1.close()
#print t
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
	<div class="abc" style="margin-left:400px;margin-top:100px;"> <textarea style="z-index:2"rows="15px" cols="40px" name="pycode"
	>'''+t+'''
	

		</textarea></div>
		
		</form>
	<p >'''