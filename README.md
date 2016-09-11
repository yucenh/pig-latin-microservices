# Pig Latin microservices

Overview
========
The Pig Latin Translater is powered by microservice, which happen to be written in Python using Flask.


The Pig Latin rules: 

1. For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added. 
2. For words that begin with vowel sounds or a silent letter, one just adds "yay" to the end.

Assupmtion made: to infer silent words in the rule, popular silent prefixs ("ps", "kn", "wh", "gn", "pn") are selected.
Refer to: http://www.academia.edu/5595383/MAKE_YOUR_ENGLISH_SOUNDS_ENGLISH_SILENT_CONSONANT

Requirements
===========
* Python 2.7.9
* Works on Mac OSX. (Only test on Mac OSX)
* You would need to install venv <code> pip install virtualenv </code>.

Install, Starting and Stopping Services
=======
* Install: 
  1. <code> $ git clone https://github.com/yucenh/pig-latin-microservices </code>
  2. <code> $ cd pig-latin-microservices </code>
  3. <code> $ sudo make install</code>
* Launch the services: <code>$ make launch </code>
* Stop the services: <code> $ make shutdown </code>

Demo
=======
* GET: 
http://127.0.0.1/translate?data=pig
```
{
    "result": "igpay"
}
```

* POST: 
<code>curl --request POST --url http://127.0.0.1:80/translate --form 'data=Hello world!'</code>

You should see a response like
```
{
    "result": "Ellohay orldway!"
}
```

Testing
=======
To run test cases, simply do <code> $ python tests/pig_latin.py </code>

