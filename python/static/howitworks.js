howitworks_text = "\
<i>Last updated Mar 27th, 2013</i>\
<h3>First Some History...</h3>\
\
<p>This particular webcam has been active in some form continuously \
since December of 1996.  It was originally running on a Windows PC in \
a dorm room.  In October of 1997, the webcam officially moved to the \
lounge on our hall where it remains today.  The webcam server has been \
running the RedHat Linux operating system since the fall of 1998.  We \
believe that this may possibly make it the oldest webcam on the \
internet that is still operating and features human subjects (not fish \
or coffeepots).</p> <p> There used to be, in ancient times, a hacked \
together mechanism using old parts from floppy disk drives and a \
pulley mechanism with weights and string and a parallel interface, \
that could control movement (panning) of the webcam from the website. \
There was also at one point a failed experiment in which we allowed \
visitors of the page to enter text into a form and have speakers in \
the lounge sound out the words of our visitors. A new motion-capable \
camera has been installed, and perhaps, in the fullness of time, some \
of these functions will be restored, or new ones developed.  </p>\
\
<h3>The System</h3>\
\
<p>The domain name \"www.mitwebcam.com\" points to this web server, \
webcam.mit.edu, located in the lounge on our hall.  Webcam is a \
cobbled-together Intel Celeron system that replaced an AMD Athlon \
XP-class system that was installed in late February 2007, which itself \
replaced a 7-year old 200mhz dell workstation.  The camera hooked up \
to this server's USB port is a Logitech Quickcam Orbit. There are also \
several Android phones running <a href=/apk>custom</a> <a \
href=https://play.google.com/store/apps/details?id=com.pas.webcam> \
software</a> that act as wireless cameras throughout hall (see the \
kitchen cam at <a\
href=\"http://www.collegecoedsgonewildinthekitchen.com\" \
>http://www.collegecoedsgonewildinthekitchen.com</a>). \
\
<h3>The Software</h3> \
\
<p>Webcam.mit.edu is currently running <a \
href=\"http://www.linuxmint.com/\">Linux Mint 14</a> , and the <a \
href=\"http://httpd.apache.org/\">Apache web server</a> -- assuming \
this page is kept up to date.  A modified version of <a \
href=\"http://www.github.com/pranjalv123/mjpg-streamer-yu12\">mjpg-streamer</a> \
is installed to give us an http interface to the camera, which, along \
with the Android phones, provides a live mjpg stream.  </p> \
\
<p> Basically, the system is running a Python Flask <a \
href=\"http://www.github.com/pranjalv123/vigilance\">webapp</a> that \
listens for connections and provides streams for each known webcam. It \
also loops continuously and captures a .jpg image every few seconds. \
This image is stored and then copied to an archive where it is stored \
to make a <a href=\"http://www.mitwebcam.com/archive.html\">complete \
archive of recorded images</a>. </p> \
\
"