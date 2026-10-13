---
name: md-parser
description: "PDF, 한글(HWP, HWPX), 워드(DOCX), 파워포인트(PPTX), 엑셀(XLSX, XLS), HTML, CSV, JSON, XML, EPUB, 아웃룩 메일(MSG), 주피터 노트북(IPYNB), ZIP, 이미지, 오디오 파일을 마크다운(.md)으로 변환하는 스킬. 사용자가 \"마크다운으로 변환해줘\", \"md로 바꿔줘\", \"파싱해줘\", \"텍스트 추출해줘\", \"파일 내용 뽑아줘\", \"문서 읽어줘\", \"parse\", \"convert to markdown\", \"extract text\" 등을 요청하거나 첨부 파일의 내용을 마크다운으로 꺼내야 할 때 반드시 이 스킬을 사용한다. 요약, 분석, 번역 같은 후속 작업 전에 문서를 텍스트로 바꾸는 전처리 단계로도 사용한다."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# md-parser

문서 파일을 마크다운으로 바꾼다. 변환은 `scripts/parse.py`가 맡는다. 스크립트는 포맷마다 정해진 순서로 엔진을 실행한다. 앞 엔진이 오류를 내거나 빈 결과를 내면 다음 엔진으로 넘어간다. 아래 경로는 스킬 폴더를 기준으로 한다.

## 설치

변환 전에 한 번 설치한다.

```bash
python -m pip install "markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription]" pdfplumber python-hwpx olefile
python -m pip install --use-pep517 pyhwp
```

- 시스템 파이썬이 패키지 설치를 막으면 가상환경에 설치하거나 명령 끝에 `--break-system-packages`를 붙인다.
- pyhwp는 소스 형태로만 배포된다. `--use-pep517`을 붙이면 일부 리눅스 배포판의 setuptools에서 생기는 빌드 오류를 피할 수 있다.
- mp3, m4a, mp4 오디오를 변환하려면 ffmpeg가 필요하다. 이미지 메타데이터를 읽으려면 exiftool이 필요하다. 두 프로그램이 없어도 다른 포맷은 정상적으로 변환된다.

## 실행

사용자가 첨부했거나 경로를 알려준 파일을 입력으로 쓴다.

```bash
python scripts/parse.py <입력 파일> <출력 폴더>/<원본 파일명>_parsed.md
python scripts/parse.py <입력 파일> <출력 폴더> --chunk --chunk-size 2000
```

- 기본 출력은 파일 하나이며 이름은 `<원본 파일명>_parsed.md`로 정한다.
- `--chunk`는 사용자가 "청크", "chunk", "분할"을 요청할 때만 붙인다. 기본 크기는 2,000자이다.
- 청크는 제목(#) 경계에서 먼저 나뉜다. 기준 크기의 1.5배를 넘는 조각은 문단 경계에서 다시 나뉜다.
- 오디오 파일과 오디오가 들어 있는 ZIP은 아래 오디오 기준을 먼저 적용한다.

## 결과 파일

모든 결과 파일 맨 위에는 YAML 머리말이 붙는다. 항목은 원본 파일명(source), 확장자(format), 변환 시각(parsed_at), 사용 엔진(engine), 글자 수(char_count)이며 청크 파일에는 청크 번호(chunk)와 전체 청크 수(total_chunks)가 더해진다.

| 파일 | 생성 조건 | 내용 |
|---|---|---|
| `<원본 파일명>_parsed.md` 또는 `<원본 파일명>_chunk_001.md`부터 이어지는 파일 | 항상 | 본문 |
| `<원본 파일명>_tables.md` | PDF에서 표가 감지될 때 | pdfplumber가 추출한 표 |
| `<원본 파일명>_fulltext.md` | HWP 본문에 `<표>`나 `<그림>`이 남았을 때, HWPX에 글상자 같은 도형 안 글자가 있을 때 | 표 안 글자와 도형 안 글자를 포함한 전체 텍스트. 표 모양은 없다 |

## 포맷별 엔진

| 포맷 | 엔진 순서 | 결과 특성 |
|---|---|---|
| PDF (.pdf) | markitdown, 표 파일은 pdfplumber | 본문에서는 표 모양이 흐트러질 수 있으므로 표는 `_tables.md`에서 확인한다. pdfplumber는 선이 그어진 표를 기준으로 칸을 나누므로 선이 없는 표는 칸이 어긋날 수 있다 |
| 한글 HWPX (.hwpx) | python-hwpx export_markdown, python-hwpx TextExtractor, 섹션 XML 직접 읽기 | 표는 마크다운 표로 나온다. export_markdown은 도형 안 글자를 출력하지 않으므로 그 글자는 `_fulltext.md`에 담긴다. XML 직접 읽기까지 내려가면 표가 본문 뒤에 모인다 |
| 한글 HWP (.hwp) | pyhwp hwp5txt, olefile로 HWP 5.0 구조 직접 읽기 | hwp5txt는 표와 도형을 `<표>`, `<그림>`으로 바꾸고 내용을 출력하지 않는다. 그 내용은 `_fulltext.md`에 담긴다. 배포용 문서는 hwp5txt만 읽을 수 있다 |
| 그 밖의 문서 (.docx .pptx .xlsx .xls .csv .html .htm .epub .ipynb .msg .rss .atom .txt .md .json .jsonl .xml .zip) | markitdown | 제목, 목록, 표, 링크가 마크다운 문법으로 바뀐다. 텍스트 파일은 공백 정리 외에는 원문을 그대로 옮긴다. ZIP은 안에 든 파일을 하나씩 변환한다 |
| 이미지 (.jpg .jpeg .png) | markitdown | exiftool이 있으면 EXIF 메타데이터만 나온다. 그림 속 글자는 추출하지 않는다 |
| 오디오 (.wav .mp3 .m4a .mp4) | markitdown | 음성을 외부 서비스로 보내 받아쓴다. 아래 오디오 기준을 따른다 |

구형 워드(.doc), 구형 파워포인트(.ppt), .gif, .webp는 markitdown이 지원하지 않는다. 사용자에게 .docx, .pptx, .png로 저장한 파일을 요청한다.

## 오디오 기준

markitdown은 SpeechRecognition 라이브러리를 통해 Google 웹 음성 API로 받아쓴다. 이 과정에서 음성 데이터가 Google 서버로 전송된다. 인식 언어는 영어(en-US)로 고정되어 있어서 한국어 음성은 제대로 받아쓰지 못한다.

- 스크립트는 `--allow-audio-upload` 없이 오디오를 받으면 변환을 멈추고 종료 코드 2를 반환한다.
- 사용자에게 외부 전송과 영어 인식 한계를 알린다. 사용자가 동의하면 같은 명령에 `--allow-audio-upload`를 붙여 다시 실행한다.
- 사용자가 동의하지 않으면 오디오 변환을 진행하지 않는다. ZIP이라면 오디오를 뺀 압축 파일을 요청한다.

## 결과 점검

실행 로그의 `[INFO] 엔진: ... | 글자 수: ...` 줄에서 사용한 엔진과 글자 수를 확인한 뒤 사용자에게 결과를 전달한다.

| 상황 | 대응 |
|---|---|
| 글자 수가 0 | 스캔 PDF나 이미지일 가능성이 높다. 글자 인식(OCR) 도구가 따로 필요하다고 알린다 |
| `파싱 실패`와 함께 지원하지 않는다는 메시지 | 위 포맷 표를 근거로 변환 가능한 형식으로 저장한 파일을 요청한다 |
| 암호가 걸린 파일 | 스크립트에는 암호 입력 기능이 없다. 암호를 해제한 사본을 요청한다 |
| HWP 표의 행과 열 모양이 필요할 때 | `_fulltext.md`에는 표 안 글자만 있다. 한글 프로그램에서 HWPX로 저장한 파일을 요청한다 |
| 엔진 전환 로그(`다음 엔진으로 전환`)가 보일 때 | 결과 파일의 engine 항목과 위 포맷 표의 결과 특성을 대조하여 품질 차이를 알린다 |

결과 파일은 사용자가 내려받을 수 있는 위치에 저장한다. `_tables.md`나 `_fulltext.md`가 생기면 본문 파일과 함께 전달하고 각 파일의 용도를 한 줄로 설명한다.

## 한컴 공개 문서 고지

HWP 직접 읽기 기능은 한컴이 공개한 HWP 5.0 문서 형식을 따른다.

본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.
