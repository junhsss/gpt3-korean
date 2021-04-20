import os
import urllib
import json
from googletrans import Translator


def papago_to_ko(source: str):
    try:
        client_id = os.environ["NAVER_API_CLIENT"]
        client_secret = os.environ["NAVER_API_SECRET"]
        encText = urllib.parse.quote(source)
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            return json.loads(response_body.decode("utf-8"))["message"]["result"][
                "translatedText"
            ]
        else:
            raise ValueError
    except:
        raise ValueError


def googletrans_to_en(question: str):
    translator = Translator()
    return translator.translate(question, dest="en").text


def googletrans_to_ko(generated: str):
    translator = Translator()
    return translator.translate(generated, dest="ko").text
