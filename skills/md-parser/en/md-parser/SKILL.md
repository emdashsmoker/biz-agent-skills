---
name: md-parser
description: "Converts PDF, Hangul word processor (HWP, HWPX), Word (DOCX), PowerPoint (PPTX), Excel (XLSX, XLS), HTML, CSV, JSON, XML, EPUB, Outlook mail (MSG), Jupyter notebook (IPYNB), ZIP, image, and audio files to Markdown (.md). Always use this skill when the user asks to \"convert to markdown\", \"turn this into md\", \"parse this file\", \"extract the text\", \"pull the content out of this file\", or \"read this document\", or whenever the content of an attached file needs to come out as Markdown. Also use it as a preprocessing step that turns documents into text before summarizing, analyzing, or translating them."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# md-parser

> This skill was translated from the Korean original. It may behave differently from what the original intends.

This skill converts document files to Markdown. `scripts/parse.py` does the conversion. The script runs a fixed sequence of engines for each format. If an engine fails or returns an empty result, the script moves on to the next engine. All paths below are relative to the skill folder.

## Installation

Install once before converting.

```bash
python -m pip install "markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription]" pdfplumber python-hwpx olefile
python -m pip install --use-pep517 pyhwp
```

- If the system Python blocks package installation, install into a virtual environment or add `--break-system-packages` to the command.
- pyhwp is published as source only. `--use-pep517` avoids a build error that occurs with the setuptools shipped by some Linux distributions.
- mp3, m4a, and mp4 audio need ffmpeg. Image metadata needs exiftool. Other formats convert normally without these two programs.

## Running

Use the file the user attached or pointed to as input.

```bash
python scripts/parse.py <input file> <output folder>/<original file name>_parsed.md
python scripts/parse.py <input file> <output folder> --chunk --chunk-size 2000
```

- The default output is a single file named `<original file name>_parsed.md`.
- Add `--chunk` only when the user asks for "chunks", "chunking", or "splitting". The default size is 2,000 characters.
- Chunks are split at headings (#) first. Pieces larger than 1.5 times the target size are split again at paragraph boundaries.
- For audio files and ZIP files that contain audio, apply the audio rules below first.

## Output files

Every output file starts with a YAML header. The fields are the source file name (source), the extension (format), the conversion time (parsed_at), the engine used (engine), and the character count (char_count). Chunk files also get the chunk number (chunk) and the total number of chunks (total_chunks).

| File | Created when | Content |
|---|---|---|
| `<original file name>_parsed.md`, or files starting at `<original file name>_chunk_001.md` | Always | Body text |
| `<original file name>_tables.md` | A PDF contains detected tables | Tables extracted by pdfplumber |
| `<original file name>_fulltext.md` | An HWP body still contains `<표>` or `<그림>`, or an HWPX file has text inside shapes such as text boxes | Full text including text inside tables and shapes. Table layout is not kept |

## Engines by format

| Format | Engine order | Result |
|---|---|---|
| PDF (.pdf) | markitdown, pdfplumber for the table file | Table layout can break in the body text, so check tables in `_tables.md`. pdfplumber splits cells along ruled lines, so tables without lines can come out with misaligned cells |
| Hangul HWPX (.hwpx) | python-hwpx export_markdown, python-hwpx TextExtractor, direct reading of section XML | Tables come out as Markdown tables. export_markdown does not output text inside shapes, so that text goes to `_fulltext.md`. If the chain falls back to direct XML reading, tables are collected after the body text |
| Hangul HWP (.hwp) | pyhwp hwp5txt, direct reading of the HWP 5.0 structure with olefile | hwp5txt replaces tables and shapes with `<표>` (table) and `<그림>` (picture) and omits their content. That content goes to `_fulltext.md`. Only hwp5txt can read distribution documents |
| Other documents (.docx .pptx .xlsx .xls .csv .html .htm .epub .ipynb .msg .rss .atom .txt .md .json .jsonl .xml .zip) | markitdown | Headings, lists, tables, and links become Markdown syntax. Text files are copied as-is apart from whitespace cleanup. ZIP files have each contained file converted one by one |
| Images (.jpg .jpeg .png) | markitdown | With exiftool installed, only EXIF metadata comes out. Text inside the image is not extracted |
| Audio (.wav .mp3 .m4a .mp4) | markitdown | The audio is sent to an external service for transcription. Follow the audio rules below |

markitdown does not support legacy Word (.doc), legacy PowerPoint (.ppt), .gif, or .webp. Ask the user for a copy saved as .docx, .pptx, or .png.

## Audio rules

markitdown transcribes audio through the Google Web Speech API via the SpeechRecognition library. The audio data is sent to Google servers in the process. The recognition language is fixed to English (en-US), so speech in other languages is not transcribed correctly.

- Without `--allow-audio-upload`, the script stops on audio input and returns exit code 2.
- Tell the user about the external transfer and the English-only recognition. If the user agrees, run the same command again with `--allow-audio-upload`.
- If the user does not agree, do not convert the audio. For a ZIP file, ask for an archive without the audio files.

## Checking results

Check the engine and character count in the `[INFO] engine: ... | characters: ...` line of the log, then report the result to the user.

| Situation | Response |
|---|---|
| Character count is 0 | The file is likely a scanned PDF or an image. Tell the user that a text recognition (OCR) tool is needed |
| `parsing failed` with a message that the format is unsupported | Use the format table above to ask for a copy saved in a convertible format |
| Password-protected file | The script has no password option. Ask for a copy with the password removed |
| Rows and columns of HWP tables are needed | `_fulltext.md` only holds the text inside tables. Ask for a copy saved as HWPX in the Hangul word processor |
| The log shows an engine switch (`switching to next engine`) | Compare the engine field of the output file with the result column of the format table and tell the user about any quality difference |

Save the output files where the user can download them. If `_tables.md` or `_fulltext.md` is created, deliver it together with the body file and explain the purpose of each file in one line.

## Hancom specification notice

Direct HWP reading follows the HWP 5.0 document format published by Hancom.

본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.
(This product was developed with reference to the HWP document file (.hwp) specification published by Hancom.)
