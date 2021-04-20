# gpt3-korean

gpt3 with papago

## Installation (macOS)

```shell
git clone https://github.com/junhsss/gpt3-korean.git
cd gpt3-korean
virtualenv venv
. venv/bin/activate
pip install -e .
```

## Usage

- 한국어 : 파파고 -> gpt3 -> 파파고

```shell
ask --question "기계와 두뇌는 무엇이 다른가?"
```

- 영어 : gpt3 -> 파파고

```shell
ask --question "What is the mind? what's its relationship with the machine and brain"
```

## Environmental Variables

.env 파일 명세
OpenAI API키 (필수)
네이버 API 키 (선택, 미입력시 구글 번역)
