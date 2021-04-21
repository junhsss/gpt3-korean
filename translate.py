import os
import openai
import click
import os
from dotenv import load_dotenv

from utils import translate_google

load_dotenv()

openai.api_key = os.environ["OPENAI_API_SECRET"]

def format_prompt(string, dest="en"):
    txt = (
        "English: It couldn’t be better than this!\nKorean: 이보다 더 좋을 수는 없어.\n\n"
        + "English: Don’t get me wrong.\nKorean: 오해하지 마.\n\n"
        + "English: I changed my mind.\nKorean: 마음이 바뀌었다.\n\n"
        + "English: None of your business\nKorean: 신경 꺼.\n\n"
        + "English: Who are you?\nKorean: 누구냐?\n\n"
        + "English: That makes no sense at all.\nKorean: 그건 말이 안되잖아.\n\n"
        + "English: Life Has Never Been Better, Thanks To You! \nKorean: 네 덕분에 삶이 너무 즐거워.\n\n"
        + "English: You gotta do it anyway.\nKorean: 그래도 해야지 뭐 어쩌겠어.\n\n"
        + f"English: {string}\nKorean: "
    )
    return txt


@click.command()
@click.option("--source")
def main(source):

    print(f"\nSource: {source}")
    print(f"\nTranslated (Google): {translate_google(source, 'ko')}\n\n")
    print("\nTranslated (GPT): \n")
    for i in range(10):
        response = openai.Completion.create(
            engine="davinci",
            prompt=format_prompt(source),
            max_tokens=100,
            top_p=0.95,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"],
        )

        print(f'\t{response["choices"][0]["text"]}')
        



if __name__ == "__main__":
    main()
