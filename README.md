RPi-to-windows-shell
====================

Here you find some scripts to let the RPi start programs/tasks on windows.


Server.py
  - Running on the windows side.
  - First time run by clicking on it. And view IP adrres.
  - Later you can run it using command prompt "pythonw server.py". Now the script will run in background
  

client.py + index.php + .htaccess + .htpasswd
  - On RPi in the /var/www/ folder
  - Browse to the website of your pi and try it out!

The .htaccess file is important for enabeling CGI. It is also to protect your webpage because without this file anyone could access your computer.

In the .htpasswd file are the usernames and passwords saved. The username and password now are "pi" and "raspberry". 
<b>! Change certainly !</b> 

To make a passwd use http://www.htaccesstools.com/htpasswd-generator/


<b>! For these files to work you'll need some libraries !</b>
The most libraries are included in python but Pygoogle is not so be sure you download it first.


If you have some questions feel free to contact me at laurens.wuyts@gmail.com
