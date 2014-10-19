RPi-to-windows-shell
====================

Here you find some scripts to let the RPi start programs/tasks on windows.


Server.py
  - Running on the windows side.
  - First time run by clicking on it. And view IP adrres.
  - Later you can run it using command prompt "pythonw server.py". Now the script will run in background
  

client.py + index.php + .htaccess
  - On RPi in the /var/www/ folder
  - Browse to the website of your pi and try it out!

The .htaccess file is important for enabeling CGI and to protect your webpage because from this page anyone can access your computer without the .htaccess file.


<b>! For these files to work you'll need some libraries !</b>
The most libraries are included in python but Pygoogle is not so be sure you download it first.


If you have some questions feel free to contact me at laurens.wuyts@gmail.com
