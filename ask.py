import os
import openai
import click
from googletrans import Translator
import os
from dotenv import load_dotenv

from utils import papago

load_dotenv()

openai.api_key = os.environ["OPENAI_API_SECRET"]


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
        max_tokens=40,
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
