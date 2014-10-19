#!/usr/bin/env python2.7

import socket
import cgi
import cgitb
from pygoogle import pygoogle

cgitb.enable()

print('Content-Type: text/html; charset=utf-8\n')

print """
<head>
	<title>Control my PC</title>				
	<link rel="shortcut icon" href="../images/home.ico" type="image/x-icon" />
	<link rel="stylesheet" type="text/css" href="../style.css">
	<script src="jquery-1.11.1.js"></script>	
	<script> 
		$(function(){
			$("#header").load("../header.html"); 
			$("#footer").load("../footer.html"); 
		});
	</script>
</head>
<body onLoad="document.forms.form.submit.focus()">
<div id="wrapper">
		<div id="header"></div>
		<div id="content">	
			<center>"""

form=cgi.FieldStorage()

if "submit1" in form:
	if "post" not in form:					
		print "<h1>Chrome is started empty</h1>"
		value=''
	else:									
		value = form["post"].value			
		print "<h1>Chrome is started at " + value + "</h1>"
	send = "start chrome " + value
	
elif "MNM" in form:
	print "<h1>Chrome is started at MNM</h1>"
	send = "start chrome http://be.radioonline.fm/luisteren/mnm"

elif "MNM-hits" in form:
	print "<h1>Chrome is started at MNM-hits</h1>"
	send = "start chrome http://be.radioonline.fm/luisteren/mnm-hits"

elif "youtube" in form:
	if "post" not in form:					
		print "<h1>Chrome is started empty</h1>"
		value=''
	else:									
		value = form["post"].value			
		print "<h1>Chrome is started at youtube</h1>"
	g = pygoogle(value)
	g.pages = 1
	url = g.get_urls()
	link = url[0]
	send = "start chrome " + link

else:
	print "Couldn't determine which button was pressed."
	send = " "

print """</center>"""

HOST = '192.168.1.137'		  # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(send)
# data = s.recv(1024)
s.close()

print """
			<form name="form" action="client.py" method="POST" autocomplete="off">

				<h1>Text to send:</h1><br>
				<input type="text" name="post" >
				<input type="submit" value="Send" name="submit1">
				<input type="submit" value="YouTube" name="youtube"> <br><br>
				<input type="submit" value="   MNM   " name="MNM"> 
				<input type="submit" value="MNM-hits" name="MNM-hits"> 

			</form>
		</div>
	</div>
	<div id="footer"></div>
</body>"""
