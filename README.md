# gpt3-korean

gpt3 with papago (for fun)

## Installation (macOS)

```shell
git clone https://github.com/junhsss/gpt3-korean.git
cd gpt3-korean
virtualenv venv
. venv/bin/activate
pip install -e .
```

## Usage

# Translation

```shell
translate --source "Brains, Minds and Machines. What are the differences?"
```

```
Source: Are you nuts?

Translated (Google): 너 견과류 야?

Translated (GPT):

        기침을 하는 것 같아.
        개구리다.
        개 짖음 아니?
        깨비같아.
        괜찮아?
        그래도 이해가 가는 거야?
        깜놀.
        거짓말 미칠듯이 행동한다.
        까칠한 사람이다.
        거짓말 하는 거야?
        갑자기 까놓고 싶다.
        가식새끼 아이구나.
        깜짝 소리 치는 거 아냐?
        갑자기 뭐야!
        갑작스럽게 짜증나는데?
        그럼 머리 좀 깎아라.
        그렇게 말하는 거 당연하다 믿지마.
        거짓말 치는 놈.
        개미가 돼버렸니?
        과장 아니야?
```

# Question Answering

- 한국어 : 파파고 -> gpt3 -> 파파고

```shell
ask --question "기계와 두뇌는 무엇이 다른가?"
```

- 영어 : gpt3 -> 파파고

```shell
ask --question "Brains, Minds and Machines. What are the differences?"
```

```
In English:

Brains, Minds and Machines. What are the differences? A machine can by virtue of executing a program carry out precisely defined mathematical operations. A human brain cannot do this.

To the extent that the mind can be conceptually separated from the body there is still nothing similar to a computer in its activity. This activity follows the basic laws of humanity and obeys biological needs. So there is an observer of the external and internal environment as well as of oneself, there is an internal dialogue which constantly changes the quality of emotional attitudes to certain situations, there is freedom of action and behavior governed by needs of survival.

Given this, if machines are considered to be "tools" for help with the activities of the human mind they must be treated differently than pure tools. Moreover, if one wishes to use machines to "expand the reach" of the human mind for a more efficient and general solution of problems of science, art, social and other activities it is necessary to take into account that machines differ from human minds. This difference must be reduced to the smallest possible amount and machines should help the human mind to make the creative process simpler, quicker and easier in order to realize its potential, to increase productivity and to facilitate its close interaction with a broader number of people.

Psychology and neuroscience are very close to our work. At the level of a single neuron, the mechanism of the mind and its algorithms are hidden. In the mind of a human and human mind the machine has been derived. There is no essential difference between the development of the technologies of control, automation and robotics when applied to the operations of a machine, and operations of the mind.

The evolution of technology relies on the development of precise mathematical models of various processes and phenomena of life. The human brain has acted as a model for the development of the computer. For example, the basic architecture of the operating system of the electronic "brain" of the computer — software, in fact — is modeled after the organization of the human brain.

Mathematical algorithms to solve problems of optimal design of the mechanisms and methods of controlling these mechanisms and methods using computing machines as their implementers, also has much in common with the algorithms of the human mind. Similarly, computer programming languages, which serve as a means of formulation and implementation of algorithms, also had to develop, are used by humans, are derived from the human language.

So artificial intelligence is the application of the same kind of algorithm in the implementation of the mind by machine, and the
Brains, Minds and Machines. What are the differences? A machine can by virtue of executing a program carry out precisely defined mathematical operations. A human brain cannot do this.

To the extent that the mind can be conceptually separated from the body there is still nothing similar to a computer in its activity. This activity follows the basic laws of humanity and obeys biological needs. So there is an observer of the external and internal environment as well as of oneself, there is an internal dialogue which constantly changes the quality of emotional attitudes to certain situations, there is freedom of action and behavior governed by needs of survival.

Given this, if machines are considered to be "tools" for help with the activities of the human mind they must be treated differently than pure tools. Moreover, if one wishes to use machines to "expand the reach" of the human mind for a more efficient and general solution of problems of science, art, social and other activities it is necessary to take into account that machines differ from human minds. This difference must be reduced to the smallest possible amount and machines should help the human mind to make the creative process simpler, quicker and easier in order to realize its potential, to increase productivity and to facilitate its close interaction with a broader number of people.

Psychology and neuroscience are very close to our work. At the level of a single neuron, the mechanism of the mind and its algorithms are hidden. In the mind of a human and human mind the machine has been derived. There is no essential difference between the development of the technologies of control, automation and robotics when applied to the operations of a machine, and operations of the mind.

The evolution of technology relies on the development of precise mathematical models of various processes and phenomena of life. The human brain has acted as a model for the development of the computer. For example, the basic architecture of the operating system of the electronic "brain" of the computer — software, in fact — is modeled after the organization of the human brain.

Mathematical algorithms to solve problems of optimal design of the mechanisms and methods of controlling these mechanisms and methods using computing machines as their implementers, also has much in common with the algorithms of the human mind. Similarly, computer programming languages, which serve as a means of formulation and implementation of algorithms, also had to develop, are used by humans, are derived from the human language.

So artificial intelligence is the application of the same kind of algorithm in the implementation of the mind by machine, and the (...omitted)

In Korean (Google Translated):

두뇌, 마음, 기계. 어떤 차이가 있을까? 기계는 프로그램을 실행함으로써 정밀하게 정의된 수학적 연산을 수행할 수 있다. 인간의 뇌는 이것을 할 수 없다.

정신이 개념적으로 신체로부터 분리될 수 있는 정도까지, 그것의 활동에는 여전히 컴퓨터와 비슷한 것이 없다. 이 활동은 인류의 기본 법칙을 따르고 생물학적 요구에 복종한다. 그래서 자신뿐만 아니라 외부와 내부 환경의 관찰자가 있고, 감정적 태도의 질을 특정한 상황에 끊임없이 변화시키는 내부 대화가 있고, 생존의 필요에 의해 통제되는 행동과 행동의 자유가 있습니다.

이를 감안할 때 기계가 인간 마음의 활동을 돕는 "도구"로 간주되는 경우 순수한 도구와는 다르게 취급되어야 한다. 또한, 과학, 예술, 사회 및 기타 활동의 문제에 대한 보다 효율적이고 일반적인 해결을 위해 기계를 사용하여 인간의 마음의 "접근 거리"를 넓히고자 한다면, 기계가 인간의 마음과 다르다는 것을 고려할 필요가 있다. 이 차이는 가능한 한 최소의 양으로 줄여야 하며 기계는 인간의 마음이 창의적 과정을 더 단순하고, 더 빠르고, 더 쉽게 만들고, 생산성을 높이고, 더 많은 사람들과의 긴밀한 상호작용을 촉진하도록 도와야 한다.

심리학과 신경과학은 우리의 일에 매우 가깝다. 단일 뉴런 수준에서는, 마음의 메커니즘과 그것의 알고리즘이 숨겨져 있다. 인간과 인간의 마음속에 이 기계는 뇌, 마음, 기계였다. 어떤 차이가 있을까? 기계는 프로그램을 실행함으로써 정밀하게 정의된 수학적 연산을 수행할 수 있다. 인간의 뇌는 이것을 할 수 없다.

정신이 개념적으로 신체로부터 분리될 수 있는 정도까지, 그것의 활동에는 여전히 컴퓨터와 비슷한 것이 없다. 이 활동은 인류의 기본 법칙을 따르고 생물학적 요구에 복종한다. 그래서 자신뿐만 아니라 외부와 내부 환경의 관찰자가 있고, 감정적 태도의 질을 특정한 상황에 끊임없이 변화시키는 내부 대화가 있고, 생존의 필요에 의해 통제되는 행동과 행동의 자유가 있습니다.

이를 감안할 때 기계가 인간 마음의 활동을 돕는 "도구"로 간주되는 경우 순수한 도구와는 다르게 취급되어야 한다. 또한, 과학, 예술, 사회 및 기타 활동의 문제에 대한 보다 효율적이고 일반적인 해결을 위해 기계를 사용하여 인간의 마음의 "접근 거리"를 넓히고자 한다면, 기계가 인간의 마음과 다르다는 것을 고려할 필요가 있다. 이 차이는 가능한 한 최소의 양으로 줄여야 하며 기계는 인간의 마음이 창의적 과정을 더 단순하고, 더 빠르고, 더 쉽게 만들고, 생산성을 높이고, 더 많은 사람들과의 긴밀한 상호작용을 촉진하도록 도와야 한다.

심리학과 신경과학은 우리의 일에 매우 가깝다. 단일 뉴런 수준에서는, 마음의 메커니즘과 그것의 알고리즘이 숨겨져 있다. 인간과 인간의 마음속에서 기계가 파생되었다. 기계의 조작에 적용했을 때 제어, 자동화, 로봇 공학 기술의 발달과 정신의 조작 사이에는 본질적인 차이가 없다.

기술의 진화는 삶의 다양한 과정과 현상에 대한 정확한 수학적 모델의 개발에 의존한다. 인간의 두뇌는 컴퓨터 개발의 모델 역할을 해 왔다. 예를 들어, 컴퓨터의 전자 "브레인" 운영체제의 기본 구조인 소프트웨어는 인간의 뇌 조직을 본떠서 만들어졌다.

컴퓨팅 기계를 구현자로 사용하여 이러한 메커니즘과 방법을 제어하는 최적의 설계 문제를 해결하기 위한 수학적 알고리듬도 인간 마음의 알고리듬과 많은 공통점을 가지고 있다. 마찬가지로, 알고리즘의 공식화 및 구현의 수단으로서 기능하는 컴퓨터 프로그래밍 언어는 인간 언어에서 파생된 것이다.

인공지능은 같은 종류의 알고리즘을 기계에 의한 마음의 구현과 뇌, 마음, 기계에 적용한 것입니다. 어떤 차이가 있을까? 기계는 프로그램을 실행함으로써 정밀하게 정의된 수학적 연산을 수행할 수 있다. 인간의 뇌는 이것을 할 수 없다.

정신이 개념적으로 신체로부터 분리될 수 있는 정도까지, 그것의 활동에는 여전히 컴퓨터와 비슷한 것이 없다. 이 활동은 인류의 기본 법칙을 따르고 생물학적 요구에 복종한다. 그래서 자신뿐만 아니라 외부와 내부 환경의 관찰자가 있고, 감정적 태도의 질을 특정한 상황에 끊임없이 변화시키는 내부 대화가 있고, 생존의 필요에 의해 통제되는 행동과 행동의 자유가 있습니다.

이를 감안할 때 기계가 인간 마음의 활동을 돕는 "도구"로 간주되는 경우 순수한 도구와는 다르게 취급되어야 한다. 또한, 과학, 예술, 사회 및 기타 활동의 문제에 대한 보다 효율적이고 일반적인 해결을 위해 기계를 사용하여 인간의 마음의 "접근 거리"를 넓히고자 한다면, 기계가 인간의 마음과 다르다는 것을 고려할 필요가 있다. 이 차이는 가능한 한 최소의 양으로 줄여야 하며 기계는 인간의 마음이 창의적 과정을 더 단순하고, 더 빠르고, 더 쉽게 만들고, 생산성을 높이고, 더 많은 사람들과의 긴밀한 상호작용을 촉진하도록 도와야 한다.

심리학과 신경과학은 우리의 일에 매우 가깝다. 단일 뉴런 수준에서는, 마음의 메커니즘과 그것의 알고리즘이 숨겨져 있다. 인간과 인간의 마음속에서 기계가 파생되었다. 기계의 조작에 적용했을 때 제어, 자동화, 로봇 공학 기술의 발달과 정신의 조작 사이에는 본질적인 차이가 없다.

기술의 진화는 삶의 다양한 과정과 현상에 대한 정확한 수학적 모델의 개발에 의존한다. 인간의 두뇌는 컴퓨터 개발의 모델 역할을 해 왔다. 예를 들어, 컴퓨터의 전자 "브레인" 운영체제의 기본 구조인 소프트웨어는 인간의 뇌 조직을 본떠서 만들어졌다.

컴퓨팅 기계를 구현자로 사용하여 이러한 메커니즘과 방법을 제어하는 최적의 설계 문제를 해결하기 위한 수학적 알고리듬도 인간 마음의 알고리듬과 많은 공통점을 가지고 있다. 마찬가지로, 알고리즘의 공식화 및 구현의 수단으로서 기능하는 컴퓨터 프로그래밍 언어는 인간 언어에서 파생된 것이다.

인공지능은 기계에 의한 마음의 구현에 있어서 같은 종류의 알고리즘의 적용이고, (...후략)
```

## Environmental Variables

.env 파일을 만들어

- OpenAI API키 (필수)
- 네이버 API 키 (선택)

```

```
