# Pig Latin microservices

Overview
========

Requirements
===========
* Python 2.7
* Works on Mac OSX. (Only test on Mac OSX)

Install, Starting and Stopping Services
=======
* Install: <code> $ sudo make install</code>
* Launch the services: <code>$ make launch </code>
* Stop the services: <code> $ make shutdown </code>

Demo
=======
* GET: 
http://127.0.0.1/translate?data=google

* POST: 
<code>curl --request POST --url http://127.0.0.1:80/translate --form 'data=Hello world!'</code>

Other
=======