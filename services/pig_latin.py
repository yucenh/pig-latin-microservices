from services import nice_json
from flask import Flask
from flask import request
from flask import render_template
import json
import requests
import string 

app = Flask(__name__)


def isvowel(c):
    return c in "aeiouAEIOU"


def isSlientPrefix(string):
    slientList = ["ps", "kn", "wh", "gn", "pn"]
    for slient in slientList:
        if string.startswith(slient):
            return True

    return False
    

def getPrefix(string):
    for i in range(0, len(string)):
        if isvowel(string[i]):
            return i
    return -1



def convert_sentence(sentence):
    list_of_words = sentence.split(' ')
    new_sentence = ""  

    for word in list_of_words:
        isFirstCharUpper = ('A' <= word[0] <= 'Z')
        isLastCharPunctuation = word[-1] in string.punctuation
        punctuation = word[-1] if isLastCharPunctuation else None
        prefixId = getPrefix(word)

        if prefixId == -1:
            new_sentence += word
            continue

        appendStr = word[:prefixId].lower() 
        newWord = word[prefixId:] if not isLastCharPunctuation else word[prefixId:-1]
        
        if newWord is None:
            newWord = ""

        if isFirstCharUpper:
            s = list(newWord)
            s[0] = s[0].upper()
            newWord = "".join(s)

        if len(appendStr) == 0 or isSlientPrefix(word): 
            # print word, (word if not isLastCharPunctuation else word[:-1])
            newWord = (word if not isLastCharPunctuation else word[:-1]) + "yay"
        else:
            newWord = newWord + appendStr + "ay"

        if punctuation: 
            newWord = newWord + punctuation

        new_sentence = new_sentence + newWord + " "  

    return new_sentence.strip()


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
            "result": convert_sentence(data)
        })


if __name__ == "__main__":
    app.run(port=80, debug=True)
