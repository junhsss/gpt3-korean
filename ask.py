import os
import openai
import click
import os
from dotenv import load_dotenv

from translator import translate_papago, translate_google

load_dotenv()

openai.api_key = os.environ["OPENAI_API_SECRET"]


def format_prompt(string):
    return f'The most fundamental, and modern version among various answers to the question "{string}" is the following.'


@click.command()
@click.option("--question")
def main(question):
    question_en = translate_google(question, "en")

    response = openai.Completion.create(
        engine="davinci",
        prompt=format_prompt(question_en),
        max_tokens=100,
        top_p=0.98,
    )

    generated = question_en + response["choices"][0]["text"]

    print("In English: \n")
    print(generated)
    print(generated + "\t (...omitted)")

    try:
        generated_ko = translate_papago(generated, "ko")
        print("\nIn Korean (Papago Translated): \n")
    except ValueError:
        generated_ko = translate_google(generated, "ko")
        print("\nIn Korean (Google Translated): \n")

    print(generated_ko + "\t (...후략)")


if __name__ == "__main__":
    main()
