import unittest
import requests


class TestPigLatinService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:80/translate"

    def test_piglatin_word_translate(self):
        for inputData, expected in TEST_CASES.iteritems():
            reply = requests.get("{}?data={}".format(self.url, inputData))
            actual_reply = reply.json()["result"]

            self.assertEqual(expected, actual_reply,
                "Got {} but expected {}".format(actual_reply, expected))


    def test_piglatin_paragraph_translate(self):
        for inputData, expected in TEST_PARAGRAPH_CASES.iteritems():
            reply = requests.post("{}".format(self.url), data=dict(data=inputData))
            actual_reply = reply.json()["result"]

            self.assertEqual(expected, actual_reply,
                "Got {} but expected {}".format(actual_reply, expected))

    
TEST_CASES = {
    "pig": "igpay",
    "banana": "ananabay",
    "trash": "ashtray",
    "happy": "appyhay",
    "duck": "uckday",
    "glove": "oveglay",
    "eat": "eatyay",
    "omelet": "omeletyay",
    "are": "areyay",
}

TEST_PARAGRAPH_CASES = {
    "Where is the toilet?": "Erewhay isyay ethay oilettay?",
    "Hello world!": "Ellohay orldway!",
    "The purpose of this challenge is to demonstrate how you architect, implement test and organize your software projects- as such there will be less of an emphasis on algorithms and more on the project as a whole.": "Ethay urposepay ofyay isthay allengechay isyay otay emonstrateday owhay ouyay architectyay, implementyay, esttay andyay organizeyay ouryay oftwaresay ojectspray- asyay uchsay erethay illway ebay esslay ofyay anyay emphasisyay onyay algorithmsyay andyay oremay onyay ethay ojectpray asyay ayay olewhay."
}


if __name__ == "__main__":
    unittest.main()
