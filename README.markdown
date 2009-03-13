**Khufu** Search Engine.
Version 0.1

<h2>Installation</h2>

* Run this:
 
<pre>
./khufubot.sh [URL]
python htmlfilter.py [FOLDER] > log &
./runserver.sh
./runwebdb.sh
./webdb.py
</pre>

* Run Web Server
<pre>
cd khufusite
sudo ./runfcgi.sh
sudo /usr/local/etc/rc.d/nginx start
</pre>

<h2>Web</h2>

<pre>
curl http://localhost/
</pre>
