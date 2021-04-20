import os
import openai
import click
import os
from dotenv import load_dotenv

from translator import googletrans_to_en, googletrans_to_ko, papago_to_ko

load_dotenv()

openai.api_key = os.environ["OPENAI_API_SECRET"]


def format_prompt(string):
    return f'The most fundamental, and modern version among various answers to the question "{string}" is the following.'


@click.command()
@click.option("--question")
def main(question):
    question_en = googletrans_to_en(question)

    response = openai.Completion.create(
        engine="davinci",
        prompt=format_prompt(question_en),
        max_tokens=40,
        temperature=0.8,
    )

    generated = question_en + response["choices"][0]["text"]

    print("In English: \n")
    print(generated)
    print(generated + "\t (...omitted)")

    try:
        generated_ko = papago_to_ko(generated)
        print("\nIn Korean (Papago Translated): \n")
    except ValueError:
        generated_ko = googletrans_to_ko(generated)
        print("\nIn Korean (Google Translated): \n")

    print(generated_ko + "\t (...후략)")


if __name__ == "__main__":
    main()
