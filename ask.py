import os
import openai
import click
from googletrans import Translator
import os
import sys
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_SECRET"]


def papago(source: str):
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


def prompt(string):
    return f'The most fundamental, and modern version among various answers to the question "{string}" is the following.'


@click.command()
@click.option("--question")
def main(question):
    translator = Translator()
    source = translator.translate(question, dest="en")

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt(source.text),
        max_tokens=300,
        temperature=0.8,
    )

    print("In English: \n")
    print(source.text + response["choices"][0]["text"])

    try:
        x = papago(source.text + response["choices"][0]["text"])
        print("\nIn Korean (Papago Translated): \n")
        print(x + "\t (...omitted)")
    except ValueError:
        x = translator.translate(
            source.text + response["choices"][0]["text"], dest="ko"
        ).text
        print("\nIn Korean (Google Translated): \n")
        print(x + "\t (...후략)")


if __name__ == "__main__":
    main()
