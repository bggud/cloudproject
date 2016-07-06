<html>
	<head>
		<title>	Welcome to our CLoud Services </title>
	</head>
<style>
body {
	background-image: url("Cloud.jpg");
	background-repeat: no-repeat;
	position:absolute;
	z-index:0;
	left:0;
	top:0;
	width:100%;
	height:100% ;
	background-size : 100% ;

}
video#bgVideo {
position: fixed;
right: 0;
bottom: 0;
width: auto;
min-width: 100%;
height: auto;
min-height: 100%;
z-index: -100;    
background-size: cover;
}

}
#borderStyle {
	
	margin-top:80px;
	font-family: "Serif";
	border-color: black;
	border-style:inset ;
	border-width:10px;
	margin-left: 200px;
	margin-right:300px;
	border-radius:10px;
	padding:20px 20px 20px 20px;
	width:450px;
	height:275px;
	box-sizing:border-box;
}

</style>
<body >

	<p ><center>
		<font color="#C0C0C0" >
		<h1 > Welcome to our CLOUD SERVICES   </h1>
		<div id="borderStyle" >
		<form  method="post" action="../cgi-bin/register.cgi">
			<b>
			
			USERNAME : <input type="text" pattern="[a-zA-Z0-9]{1,}" title="Only AlphaNumeric are allowed"  name="USERNAME" required />	<br /> <br />
			PASSWORD : <input type="password" pattern="{5,}" title="Minimum 5 characters"  name="PASSWORD" required/>	<br /><br />
				   
				EMAIL	:  <input type="email" value="example@my.com" title="Improper Format" name="EMAIL" required>	<br /><br/>
			CONTACT No. : <input type="text" value="" title="Invalid Number"  name="NUMBER" required> <br /><br />
			<input type="submit" value ="Sign Up">	<br /><br />
		</b>
		</form>
		</div>
		</font>
	</center></p>
	
</body>
</html>

