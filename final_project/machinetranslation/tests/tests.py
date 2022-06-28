import unittest
from ibm_watson import ApiException
from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    
    def test_english_to_french(self):

        self.assertRaises(ApiException,englishToFrench,"")
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

    def test_french_to_english(self):

        self.assertRaises(ApiException,frenchToEnglish,"")
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")


unittest.main()
