import os
import urllib
import json
from googletrans import Translator


def translate_papago(generated: str, dest: str):
    try:
        client_id = os.environ["NAVER_API_CLIENT"]
        client_secret = os.environ["NAVER_API_SECRET"]
        encText = urllib.parse.quote(generated)
        data = f"source=en&target={dest}&text=" + encText
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


def translate_google(source: str, dest: str):
    translator = Translator()
    return translator.translate(source, dest).text
