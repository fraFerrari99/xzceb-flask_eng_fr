"""
Translator file with the functions defined
"""
import os
import json
from ibm_watson import LanguageTranslatorV3,ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')




def englishToFrench(english_text):
    """
    Translating from english to french
    """
    if english_text=="":
        raise ApiException(0)
    french_text = language_translator.translate(
                                 text = english_text,
                                 model_id = "en-fr",
                                 source = "en",
                                 target = "fr").get_result()
    french_text = json.loads(
                 json.dumps(french_text, indent=2, ensure_ascii=False))['translations'][0]['translation']
    return french_text



def frenchToEnglish(french_text):
    """
    Translating from french to english
    """
    if french_text=="":
        raise ApiException(0)
    english_text = language_translator.translate(
                                 text = french_text,
                                 model_id = "fr-en",
                                 source = "fr",
                                 target = "en").get_result()
    english_text = json.loads(
                  json.dumps(english_text, indent=2, ensure_ascii=False))['translations'][0]['translation']
    return english_text