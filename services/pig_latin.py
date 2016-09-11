from services import nice_json
from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)

VOWELS = ('a', 'e', 'i', 'o', 'u')

def convert_word(word):
    first_letter = word[0]
    if first_letter in VOWELS:  # if word starts with a vowel...
        return word + "hay"     # then keep it as it is and add hay to the end
    else:
        return word[1:] + word[0] + "ay"    # like the lab mentions, word[1:]
                                            # returns the word except word[0]


# From this function, it's easy to take a sentence and convert it to Pig-Latin.
def convert_sentence(sentence):
    list_of_words = sentence.split(' ')
    new_sentence = ""   # we'll keep concatenating words to this...
    for word in list_of_words:
        new_sentence = new_sentence + convert_word(word)    # ...like this
        new_sentence = new_sentence + " "   # but don't forget the space!
    return new_sentence

import re
import string
from string import ascii_letters

def translate(txt):
    vowels = 'aeiouAEIOU'
    # Separates text into words and whitespace
    words = re.findall(r'(?:\S+)|(?:\s+)', txt)
    output = []
    for word in words:
        # Whitespace does not require translation
        if not word.strip():
            output.append(word)
            continue
        # Punctuation does not require translation
        if not set(ascii_letters).intersection(word):
            output.append(word)
            continue
        
        m = re.match(r'^(?P<pre>[\W]*)(?P<word>.+?)(?P<post>[\W]*)$', word)
        d = m.groupdict()
        
        i = 0
        word = d['word']
        while len(word) > i:
            if word[i] in vowels:
                break
            if i > 0 and word[i] in 'yY':
                break               
            i += 1
        d['fore'] = word[i:]
        d['aft'] = word[:i]
        new_word = '%(pre)s%(fore)s-%(aft)say%(post)s' % d
        output.append(new_word)
    return ''.join(output) 


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "translate": "/translate",
        }
    })


@app.route('/translate', methods = ['GET', 'POST'])
def pigLatinTranslate():
    if request.method == 'POST':
        data = request.form['data']
        return nice_json({
            "result": convert_sentence(data)
        })
    else:
        data = request.args.get('data')
        return nice_json({
            "result": convert_word(data)
        })


if __name__ == "__main__":
    app.run(port=80, debug=True)
