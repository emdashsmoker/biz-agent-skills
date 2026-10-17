# biz-agent-skills

Agent Skills for the report writing and analysis work of planners, consultants and analysts. Every skill ships as a Korean original and an English translation. The Korean originals follow the document conventions of Korean public agencies and companies.

기획자, 컨설턴트, 분석가의 보고서 작성과 분석 업무를 위한 에이전트 스킬 모음입니다. 모든 스킬은 한국어 원본과 영어 번역본을 함께 제공합니다. 한국어 원본은 한국 공공기관과 기업의 문서 관행을 기준으로 작성했습니다.

<details>
<summary><b>English</b></summary>

## Skills

A skill whose name ends in `-lite` is a lite edition: the same function with shorter instructions and lower token use.

### Research

- [`environment-analysis`](skills/environment-analysis/): Researches the macro environment, industry, internal capability and benchmarks, then turns them into sourced facts and implications.
- [`environment-analysis-lite`](skills/environment-analysis-lite/): Lite edition of `environment-analysis`.
- [`five-forces`](skills/five-forces/): Analyzes the competition in an industry with Michael Porter's Five Forces framework.
- [`source-check`](skills/source-check/): Answers only from the files you provide and from searched sources that pass a quality filter.
- [`digest`](skills/digest/): Turns web pages, documents, audio and video into minutes, briefings, reports or translations. [Samples](skills/digest/demo/en/)
- [`md-parser`](skills/md-parser/): Converts PDF, HWP, HWPX, Office files and more into Markdown.

### Analysis

- [`practical-calc`](skills/practical-calc/): Runs practical calculations such as CAGR, NPV, B/C, IRR, AHP and financial ratios as reproducible Python scripts.
- [`practical-calc-lite`](skills/practical-calc-lite/): Lite edition of `practical-calc`.
- [`cagr`](skills/cagr/): Calculates a compound annual growth rate from two points in time.
- [`practical-stats`](skills/practical-stats/): Designs and runs practical statistical analysis of surveys and secondary data around the decision it must inform.
- [`network-analysis`](skills/network-analysis/): Runs social network analysis with NetworkX code and charts. [Samples](skills/network-analysis/demo/en/)
- [`network-analysis-lite`](skills/network-analysis-lite/): Lite edition of `network-analysis`.
- [`ontology-modeling`](skills/ontology-modeling/): Designs definitions, classes and relations without overlaps or gaps, and builds an OWL ontology when needed. [Samples](skills/ontology-modeling/demo/en/)
- [`dataframe-ops`](skills/dataframe-ops/): Turns plain-language or cell-reference requests about tables into pandas code and runs it. [Samples](skills/dataframe-ops/demo/en/)
- [`chart`](skills/chart/): Settles the message first, then builds static report charts with matplotlib. [Samples](skills/chart/demo/en/)
- [`biz-code-style`](skills/biz-code-style/): Sets how coding, analysis and chart work runs and how the outputs look. [Samples](skills/biz-code-style/demo/en/)
- [`biz-code-style-lite`](skills/biz-code-style-lite/): Lite edition of `biz-code-style`.

### Planning

- [`strategy-builder`](skills/strategy-builder/): Builds an organization's strategy framework step by step, from environment analysis to performance indicators. [Samples](skills/strategy-builder/demo/en/)
- [`rfp-strategy`](skills/rfp-strategy/): Analyzes a request for proposal and builds a bid strategy.
- [`project-plan`](skills/project-plan/): Writes a project overview and a WBS for a project under contract. [Samples](skills/project-plan/demo/en/)
- [`think-review`](skills/think-review/): Checks plans, arguments and documents from first principles. [Samples](skills/think-review/demo/en/)
- [`think-review-lite`](skills/think-review-lite/): Lite edition of `think-review`.

### Writing

- [`logical-write`](skills/logical-write/): Writes and revises Korean outline-style (gaejosik) reports in a Markdown hierarchy. [Samples](skills/logical-write/demo/en/)
- [`logical-write-lite`](skills/logical-write-lite/): Lite edition of `logical-write`.
- [`clear-comm`](skills/clear-comm/): Writes emails, replies, feedback and announcements that put the point first. [Samples](skills/clear-comm/demo/en/)
- [`anti-slop`](skills/anti-slop/): Finds and fixes the stock phrasing of language models. [Samples](skills/anti-slop/demo/en/)
- [`no-jargon`](skills/no-jargon/): Rewrites jargon so that readers outside the field can follow. [Samples](skills/no-jargon/demo/en/)
- [`onto-mece`](skills/onto-mece/): Checks classifications, hierarchies and definitions in a text for overlaps and gaps. [Samples](skills/onto-mece/demo/en/)
- [`fx-krw`](skills/fx-krw/): Adds a Korean won equivalent next to each foreign currency amount. [Samples](skills/fx-krw/demo/en/)

### Working setup

- [`lean-work`](skills/lean-work/): Fixes the purpose, reader and scope first, then keeps only what the work needs.
- [`long-task-ledger`](skills/long-task-ledger/): Records long multi-step agent work so it can resume after a truncated conversation or a new session.
- [`pref-architect`](skills/pref-architect/): Designs short always-on instructions and on-demand modular skills through an interview.
- [`skill-forge`](skills/skill-forge/): Builds, combines and manages skills and agent instructions.
- [`offline-deps-builder`](skills/offline-deps-builder/): Builds dependency skills that carry the libraries, fonts and models another skill would download at run time.

## Installation

Each skill folder holds the install packages and the source folders.

```
skills/think-review/
├── think-review-ko.skill    Korean install package
├── think-review-en.skill    English install package
├── ko/think-review/         Korean source
└── en/think-review/         English source
```

- A `.skill` file is a zip archive of the skill folder. Where only `.zip` uploads are accepted, rename the extension to `.zip`.
- To install from source, copy the folder named after the skill (for example `ko/think-review/`) into your agent's skills folder.
- The Korean and English editions share one skill name, so only one of them can be installed at a time.

## Limitations

- Testing used Claude Opus 5.5 and Claude Fable 5.1. Results may differ with other models and environments.
- Testing did not cover every edge case, and some skills have had limited testing.
- Some skills may duplicate functions of other skills.
- Skills that run code need a code execution environment and network access.
- Laws, public programs and methods in the skills reflect the time of writing.
- The English editions are translations. Rules about Korean grammar and Korean document conventions may behave differently from the original.

## Disclaimer

The skills come as they are, without any warranty. Correct operation in every environment is not guaranteed. The end user bears responsibility for using the skills and their output.

본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다. (This product was developed with reference to the HWP document file (.hwp) specification published by Hancom.) Hangul, Hancom Office and HWPX are trademarks of Hancom Inc. The skills in this repository are not affiliated with Hancom Inc.

## License

[GPL-3.0-or-later](LICENSE). Copyright (C) 2026 Em Dash Smoker.

Each skill carries its own `LICENSE` and `NOTICE.md`. Under the output exception in `NOTICE.md`, the documents, charts and other files you make with a skill are free of GPL terms. The sample files in the `demo/` folders are licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Packages, fonts and models that a skill installs at run time keep their own licenses. When a skill uses such items, the "Third-party software" section of its `NOTICE.md` lists them with their licenses.

</details>

<details>
<summary><b>한국어</b></summary>

## 스킬 목록

이름 끝에 `-lite`가 붙은 스킬은 같은 기능을 유지하면서 지침 분량을 줄여 토큰 사용량을 낮춘 경량판입니다.

### 조사

- [`environment-analysis`](skills/environment-analysis/): 거시환경, 산업, 내부 역량, 벤치마킹 사례를 조사해 출처가 있는 팩트와 시사점으로 정리합니다.
- [`environment-analysis-lite`](skills/environment-analysis-lite/): `environment-analysis`의 경량판입니다.
- [`five-forces`](skills/five-forces/): 마이클 포터의 5-Forces 프레임워크로 산업의 경쟁환경을 분석합니다.
- [`source-check`](skills/source-check/): 사용자가 제공한 파일과 품질 기준을 통과한 검색 출처만으로 답합니다.
- [`digest`](skills/digest/): 웹 페이지, 문서, 음성, 영상을 회의록, 브리핑, 보고서, 번역문으로 정리합니다. [예시](skills/digest/demo/ko/)
- [`md-parser`](skills/md-parser/): PDF, HWP, HWPX, 오피스 파일 등을 마크다운으로 변환합니다.

### 분석

- [`practical-calc`](skills/practical-calc/): CAGR, NPV, B/C, IRR, AHP, 재무비율 같은 실무 계산을 재현 가능한 파이썬 스크립트로 수행합니다.
- [`practical-calc-lite`](skills/practical-calc-lite/): `practical-calc`의 경량판입니다.
- [`cagr`](skills/cagr/): 두 시점의 값으로 연평균 성장률을 계산합니다.
- [`practical-stats`](skills/practical-stats/): 설문조사와 2차 자료를 다루는 실무 통계 분석을 의사결정 목적에 맞춰 설계하고 수행합니다.
- [`network-analysis`](skills/network-analysis/): NetworkX 코드와 그림으로 소셜 네트워크 분석을 수행합니다. [예시](skills/network-analysis/demo/ko/)
- [`network-analysis-lite`](skills/network-analysis-lite/): `network-analysis`의 경량판입니다.
- [`ontology-modeling`](skills/ontology-modeling/): 개념 정의, 분류, 관계를 중복과 누락 없이 설계하고 필요한 경우 OWL 온톨로지를 구축합니다. [예시](skills/ontology-modeling/demo/ko/)
- [`dataframe-ops`](skills/dataframe-ops/): 자연어나 엑셀식 좌표로 받은 표 데이터 요청을 pandas 코드로 변환해 실행합니다. [예시](skills/dataframe-ops/demo/ko/)
- [`chart`](skills/chart/): 전달할 메시지를 먼저 확정한 뒤 matplotlib으로 보고서용 정적 차트를 작성합니다. [예시](skills/chart/demo/ko/)
- [`biz-code-style`](skills/biz-code-style/): 코딩, 데이터 분석, 차트 작업의 진행 방식과 산출물 스타일을 정합니다. [예시](skills/biz-code-style/demo/ko/)
- [`biz-code-style-lite`](skills/biz-code-style-lite/): `biz-code-style`의 경량판입니다.

### 기획

- [`strategy-builder`](skills/strategy-builder/): 환경분석부터 성과지표까지 조직의 전략체계를 단계별로 수립합니다. [예시](skills/strategy-builder/demo/ko/)
- [`rfp-strategy`](skills/rfp-strategy/): 제안요청서(RFP)를 분석해 입찰 전략을 수립합니다.
- [`project-plan`](skills/project-plan/): 계약을 마친 과업의 사업 개요와 WBS를 작성합니다. [예시](skills/project-plan/demo/ko/)
- [`think-review`](skills/think-review/): 기획, 주장, 문서를 제1원칙으로 점검합니다. [예시](skills/think-review/demo/ko/)
- [`think-review-lite`](skills/think-review-lite/): `think-review`의 경량판입니다.

### 글쓰기

- [`logical-write`](skills/logical-write/): 마크다운 계위 구조의 논리적 개조식 문장으로 보고서를 작성하고 수정합니다. [예시](skills/logical-write/demo/ko/)
- [`logical-write-lite`](skills/logical-write-lite/): `logical-write`의 경량판입니다.
- [`clear-comm`](skills/clear-comm/): 이메일, 답장, 피드백, 공지를 요점부터 전달하는 존댓말 산문으로 작성합니다. [예시](skills/clear-comm/demo/ko/)
- [`anti-slop`](skills/anti-slop/): 언어 모델이 자주 만드는 상투 표현을 찾아 수정합니다. [예시](skills/anti-slop/demo/ko/)
- [`no-jargon`](skills/no-jargon/): 분야 밖의 독자도 읽을 수 있도록 전문용어를 쉬운 표현으로 바꾸어 작성합니다. [예시](skills/no-jargon/demo/ko/)
- [`onto-mece`](skills/onto-mece/): 글 속 분류, 상하 구조, 정의에 중복이나 누락이 있는지 점검합니다. [예시](skills/onto-mece/demo/ko/)
- [`fx-krw`](skills/fx-krw/): 외화 금액 옆에 원화 환산액을 함께 표기합니다. [예시](skills/fx-krw/demo/ko/)

### 작업 환경

- [`lean-work`](skills/lean-work/): 목적, 독자, 범위를 먼저 정하고 작업에 필요한 요소만 남깁니다.
- [`long-task-ledger`](skills/long-task-ledger/): 대화가 잘리거나 세션이 바뀌어도 긴 다단계 작업을 이어 갈 수 있도록 기록합니다.
- [`pref-architect`](skills/pref-architect/): 인터뷰로 짧은 상시 지침과 필요할 때만 불러오는 모듈 스킬을 설계합니다.
- [`skill-forge`](skills/skill-forge/): 스킬과 에이전트 지침을 생성하고 조합하고 관리합니다.
- [`offline-deps-builder`](skills/offline-deps-builder/): 다른 스킬이 실행 중에 내려받는 라이브러리, 글꼴, 모델을 미리 포함한 의존성 스킬을 생성합니다.

## 설치

스킬 폴더마다 설치용 패키지와 소스 폴더가 포함되어 있습니다.

```
skills/think-review/
├── think-review-ko.skill    한국어판 설치용 패키지
├── think-review-en.skill    영어판 설치용 패키지
├── ko/think-review/         한국어판 소스
└── en/think-review/         영어판 소스
```

- `.skill` 파일은 스킬 폴더를 묶은 zip 파일입니다. `.zip` 파일만 올릴 수 있는 환경에서는 확장자를 `.zip`으로 변경해 업로드합니다.
- 소스로 설치할 때는 스킬 이름과 같은 폴더(예를 들어 `ko/think-review/`)를 에이전트의 스킬 폴더에 복사합니다.
- 한국어판과 영어판은 스킬 이름이 같아서 둘 중 하나만 설치할 수 있습니다.

## 한계

- 테스트는 Claude Opus 5.5와 Claude Fable 5.1에서 진행했습니다. 다른 모델과 실행 환경에서는 결과가 달라질 수 있습니다.
- 모든 예외 상황에 대한 테스트는 완료되지 않았습니다. 일부 스킬은 테스트 범위가 제한적입니다.
- 일부 스킬은 기능이 중복될 수 있습니다.
- 코드를 실행하는 스킬은 코드 실행 환경과 네트워크 연결이 필요합니다.
- 스킬에 수록한 법령, 제도, 방법론은 작성 시점을 기준으로 합니다.
- 영어판은 번역본이므로 한국어 문법과 한국 문서 관행에 관한 규칙이 원본과 다르게 작동할 수 있습니다.

## 면책 고지

이 저장소의 스킬은 어떠한 보증 없이 있는 그대로 제공합니다. 모든 환경에서 정상 작동을 보장하지 않습니다. 스킬 사용과 결과물에 대한 책임은 최종 사용자에게 있습니다.

본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다. 한/글, 한컴오피스, HWPX는 한글과컴퓨터의 상표입니다. 이 저장소의 스킬은 한글과컴퓨터와 제휴 관계가 없습니다.

## 라이선스

[GPL-3.0-or-later](LICENSE)를 따릅니다. Copyright (C) 2026 Em Dash Smoker.

스킬마다 `LICENSE`와 `NOTICE.md`가 들어 있습니다. `NOTICE.md`의 출력물 예외 조항에 따라 스킬로 만든 문서, 차트, 파일은 GPL 조건 없이 사용할 수 있습니다. `demo/` 폴더의 예시 파일은 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)을 따릅니다. 스킬이 실행 중에 설치하는 패키지, 글꼴, 모델은 각자의 라이선스를 따릅니다. 해당 항목을 사용하는 스킬은 `NOTICE.md`의 "Third-party software" 절에 항목과 라이선스를 명시합니다.

</details>

## References

Thanks to the developers and contributors of these projects.

이 프로젝트들의 개발자와 기여자분들께 감사드립니다.

- [python-hwpx](https://github.com/airmang/python-hwpx)
- [pyhwp](https://github.com/mete0r/pyhwp)
- [Owlready2](https://bitbucket.org/jibalamy/owlready2)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
