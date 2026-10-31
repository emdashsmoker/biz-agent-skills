---
name: digest
description: Converts web addresses, documents (PDF, HWP, HWPX, DOCX, PPTX, XLSX and more), audio and video files, caption files (SRT, VTT), and pasted text into text, then organizes them into meeting minutes, briefings, reports, translations, or markdown conversions. Audio is transcribed locally with faster-whisper, web pages are extracted with trafilatura, and documents are converted with markitdown, pdfplumber, python-hwpx, and pyhwp. Use this skill whenever the user asks to write up meeting minutes, clean up a transcript, organize a recording, convert speech to text, clean up captions, summarize a video, summarize or translate a news article, translate a column, extract the body of a web page, convert a document to markdown, extract file contents, or write a report or briefing that combines several sources. Also use it whenever the user hands over a file or link and asks for a summary, write-up, or translation, even without naming a format.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# digest

This English version was translated from the Korean original. It may behave differently from what the original intends.

The skill turns many kinds of input into text and then into writing a reader can use right away. `scripts/extract.py` handles conversion and the model handles the writing. Save the conversion result to a file first, then read that file and write. Reading the raw input directly lets timing lines, markup tags, and repeated lines leak noise into the result.

## Terms

| Term | Meaning |
|---|---|
| Input | A file the user submitted, a web address, or text pasted into the chat |
| Conversion | A file that carries the input's content unchanged as markdown text |
| Translation | The whole input rendered in another language |
| Write-up | A restructured text built from the input. Meeting minutes, briefings, and reports are write-ups |
| User language | The language the user writes in during the conversation |

## Workflow

1. Check the input. If a request arrives without input, briefly list the input types and output types available and ask for the input. For a meeting-minutes request, also list the grouping options (speaker, topic, time). Ask for the meeting name, date and time, and attendees at the same time.
2. Choose the output type using the "Output types" section.
3. Install the required packages. Do this before any other work.
4. Convert every input except pasted text with the script.
5. Read the conversion result files. Do not read the original document, caption, or audio files.
6. Write in the format for the chosen output type.
7. Go through the "Pre-delivery check" section, then deliver. Output write-ups and translations as a chat reply, and save them as a markdown file when the user wants a file. Deliver conversions as files.

When input arrives with the request, skip the guidance and start from step 2. After the first use, keep handling new input in the same conversation this way until the user asks you to stop.

## Output types

If the user specifies a type, format, or length, follow it. Otherwise check the table from the top and pick the first matching type.

| Order | Condition | Output |
|---|---|---|
| 1 | The user only asks for a format change, such as convert, extract, or turn into markdown | Conversion |
| 2 | The user asks for a translation | Translation |
| 3 | The user says the input is from a meeting, or the input records several participants discussing agenda items | Meeting minutes |
| 4 | There is one input | Briefing |
| 5 | There are two or more inputs | Report |

Handle a summary request as a write-up following rows 3 to 5. When the request sets a length, such as "summarize in three lines", the user's length takes priority over the default format of the chosen type.

## Installation

Install only the packages for the input types at hand.

| Input type | Packages |
|---|---|
| Web address | httpx, trafilatura |
| PDF, DOCX, PPTX, XLSX and other documents | markitdown[pdf,docx,pptx,xlsx,xls], pdfplumber |
| HWPX | python-hwpx, beautifulsoup4, lxml |
| HWP | pyhwp, olefile |
| Audio, video | faster-whisper |
| Captions | none |

```bash
pip install httpx trafilatura "markitdown[pdf,docx,pptx,xlsx,xls]" pdfplumber python-hwpx beautifulsoup4 lxml olefile faster-whisper
pip install pyhwp
```

- On a personal computer, create a project virtual environment (venv, conda, or similar) and install there. Installing into the system Python can conflict with packages other programs use.
- In a disposable isolated environment such as a cloud sandbox, rerun the install with `--break-system-packages` if you see an `externally-managed-environment` error.
- If pyhwp fails with a build error mentioning `install_layout`, retry with `SETUPTOOLS_USE_DISTUTILS=stdlib pip install pyhwp`. If it still fails, continue without pyhwp. HWP files then go through the olefile fallback.
- ffmpeg is optional. The script uses it for audio decoding when present and uses the decoder bundled with faster-whisper otherwise.
- Whisper models download from Hugging Face on the first transcription. Transcription cannot run where the network is blocked, so tell the user.
- If the script returns a `missing_dependency` error, run the `install` command in the result and try again.

## Input conversion

### Processing by input type

| Input | Extensions | Method | Result file |
|---|---|---|---|
| Web page | http, https address | trafilatura extracts body and metadata, simple HTML extraction on failure | `web_(address hash).md` |
| File at a web address | Extensions below | Downloaded, then processed like a local file | Result for that file type |
| PDF | .pdf | markitdown for body text, pdfplumber for tables | `(name)_parsed.md`, plus `(name)_tables.md` when tables exist |
| HWPX | .hwpx | python-hwpx export_markdown, then TextExtractor, then direct XML parsing | `(name)_parsed.md` |
| HWP | .hwp | pyhwp (hwp5txt), then olefile record parsing | `(name)_parsed.md` |
| Other documents | .docx .pptx .xlsx .xls .csv .json .xml .html .htm .txt .md .epub .zip | markitdown | `(name)_parsed.md` |
| Images | .jpg .jpeg .png | markitdown (EXIF metadata only) | `(name)_parsed.md` |
| Captions | .srt .vtt | Removes timing lines, markup tags, and consecutive duplicate lines | `(name)_captions.md` |
| Audio, video | .ogg .opus .m4a .aac .mp3 .wav .flac .wma .webm .amr .mp4 .mkv .avi .mov | Local transcription with faster-whisper | `(name)_transcript.md` |
| Legacy documents | .doc .ppt | No extraction engine | none |

PDF body extraction loses the cell layout of tables, so read table content from `_tables.md`. The script cannot extract what an image shows. If the model can view images in the current environment, read the image directly. Notice for the HWP fallback parser: "본 제품은 한컴의 HWP 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다." (This product was developed with reference to the HWP document file (.hwp) specification published by Hancom.)

### Script usage

`scripts/extract.py` in the examples is a path relative to this skill's folder. Results are saved to the folder in the `DIGEST_WORK_DIR` environment variable, which defaults to `digest_work` under the current folder. Run the script once per input.

```bash
python scripts/extract.py report.pdf
python scripts/extract.py "https://example.com/news/123" --max-chars 50000
python scripts/extract.py meeting.m4a --model small --language en
python scripts/extract.py lecture.vtt --start 00:10:00 --end 00:25:00
python scripts/extract.py report.pdf --chunk --chunk-size 2000
python scripts/extract.py "https://example.com/files/plan.hwpx" --download
python scripts/extract.py --bundle
python scripts/extract.py --clean
```

| Option | Default | Purpose |
|---|---|---|
| `--out-dir` | `digest_work` | Output folder |
| `--max-chars` | 0 (no limit) | Maximum characters of result text. Anything beyond is cut and marked as truncated |
| `--timeout` | 15 | Web request timeout in seconds |
| `--download` | off | Keep the original file of a web address in the `downloads` folder |
| `--chunk`, `--chunk-size` | off, 2000 | Split a document into heading-based chunk files |
| `--start`, `--end` | whole file | Range for captions and audio (for example 00:10:00) |
| `--timestamps` | off | Prefix each caption or transcript line with a time |
| `--model` | tiny | Whisper model size |
| `--language` | auto-detect | Audio language code (for example ko, en) |
| `--beam-size` | 5 | Beam search size for transcription |
| `--bundle` | off | Bundle files in the `downloads` folder into one ZIP |
| `--clean` | off | Delete files in the `downloads` folder |
| `DIGEST_ACCEPT_LANGUAGE` environment variable | English first | Preferred language sent with web requests |

### Reading the result

The script prints a JSON summary. Read the file in `output_path` (or `chunk_paths`, `tables_path`). If `truncated` is true, tell the user the rest of the input was not reflected. Handle `warnings` and `error` values as follows.

| Value | Meaning | Action |
|---|---|---|
| `missing_dependency` | Package not installed | Run the `install` command, then retry |
| `encrypted` | Password-protected file | Ask for an unlocked copy |
| `text_empty` | Almost no text (a scanned document, for example) | Tell the user optical character recognition (OCR) is needed |
| `hwp_table_placeholder` | pyhwp replaces table content with placeholders | If table content matters, ask for the file saved as HWPX |
| `hwp_olefile_fallback` | Fallback parser used, garbled characters possible | If garbled characters appear, ask for the file saved as HWPX |
| `unsupported_extract` | Format cannot be extracted | List supported formats and ask for the file saved as docx, pptx, or similar |
| `unsupported_content_type` | The address is neither a web page nor a supported file | Tell the user it cannot be accessed |
| `failed` | Request or conversion failed (see `status_code`, `detail`) | Try another address or ask for the file |

### Web addresses

- Fetch with the script first. If network limits in the environment keep the script from reaching the address, use the web reading tool the environment provides. If there is none, ask the user for the file or the text.
- The skill has no search function. Addresses come from the user or from separate web search results.
- Pages behind a login or subscription yield only their public part. If the body is missing, ask the user to supply it.
- For document addresses, extract the text and do not keep the original. Use `--download` only when the user asks to keep files or when the task collects documents found through web search.
- Bundle three or more downloaded files with `--bundle` before delivery, and deliver two or fewer one by one. Before starting a second download task in the same conversation, clear earlier files with `--clean`.

### Audio and video

- The script decodes the input to 16 kHz mono and transcribes on the CPU with int8 precision. It saves one line per segment without times. Add `--timestamps` for time-based minutes or when the user asks for times.
- When the user wants only part of a recording, process that range with `--start` and `--end`. Pass `--language` when the language is known.
- Use tiny by default. Use small or larger when the user asks for better quality. Use tiny or base when memory is short or the recording runs 60 minutes or longer.

| Model | Parameters | Relative speed (vs large) |
|---|---|---|
| tiny | about 39M | about 10x |
| base | about 74M | about 7x |
| small | about 244M | about 4x |
| medium | about 769M | about 2x |
| large-v3 | about 1,550M | 1x |

Larger models are more accurate, slower, and use more memory. Recognition quality varies widely by language. tiny makes many recognition errors, so it needs more correction.

> OpenAI(2022), Whisper model sizes, parameters, and relative speed(https://github.com/openai/whisper)

### Caption files

- Clean the caption file with the script and read only the cleaned `_captions.md`. Auto-generated captions sometimes repeat one sentence across several cues, so the script drops a line identical to the line before it.
- When the user wants only a certain time span, extract that span with `--start` and `--end`.

### Video platform addresses

When the user gives only the address of a video page on a video sharing service, do not download the video or its captions with automated tools without the user's consent. Platform terms sometimes restrict automated collection and downloading. Ask the user for one of the following.

- A caption file (.srt, .vtt) the user obtained in a way the platform's terms allow
- Text copied from the platform's own transcript view
- An audio or video file the user holds

Explain how to obtain captions only when the user asks. When the user asks, answer in this order.

1. Identify the platform from the address the user gave.
2. Lay out the ways to get captions on that platform from the model's own knowledge. Consider both the platform's built-in features and outside methods.
3. If the environment provides a web search tool, check step 2 against current information. Platform features, terms, and whether outside methods still work change often. Without a search tool, tell the user the guidance may be out of date.
4. Guide the user through the most useful method in steps they can follow themselves. When choosing, put official and lawful routes first. Judge usefulness by whether it runs in the user's environment, whether it yields captions in the needed language, and how few steps it takes.
5. Explain the risks that come with the method thoroughly.
6. Ask the user whether to carry out the method. If the user wants it, carry it out in the current environment. If the environment cannot run it, guide the user to run it themselves. Either way, get caption files as .srt or .vtt.
7. Once the captions are in hand, continue from step 2 of the workflow. If the user already asked for an output, follow that request.

### Reading limits

Set a per-input character limit with `--max-chars` so the conversion results read in one task stay within the model's context window. The input count is the number of inputs read in one task. If the user sets a limit, use it.

| Inputs | Limit per input (for a 1M-token context window) |
|---|---|
| 1-2 | no limit |
| 3-5 | 100,000 characters |
| 6-10 | 50,000 characters |
| 11-20 | 25,000 characters |
| 21 or more | 15,000 characters |

- The table assumes a total reading budget of 500,000 characters.
- If the context window is smaller than 1M tokens, multiply the table's limits by (context window tokens ÷ 1,000,000). Replace "no limit" with (context window tokens × 0.5 ÷ input count).
- If the context window size is unknown, calculate with 200,000 tokens.
- Do the limit arithmetic in code.
- Conversions are delivered only as files, so the limit does not apply to them.

## Write-up principles

These principles apply to meeting minutes, briefings, and reports.

- Use only what the input contains. Do not add claims, judgments, figures, or plans that are not in the input.
- Correct recognition errors in transcripts, auto-generated captions, and auto-generated meeting transcripts. Targets are words misheard as similar-sounding words, wrong word spacing, repeated segments, and sentences that do not connect to their surroundings.
- Correct only when surrounding sentences or other mentions in the input narrow the right spelling down to one option. If they do not, keep the original spelling. Apply the same test to proper nouns and technical terms.
- Write write-ups in the user language, including when the input is in another language.
- Do arithmetic on figures in code.

## Meeting minutes

Group by speaker, topic, or time. If the user names no grouping, group by topic. For a recording, finish transcription, correct the transcript, and treat it as the meeting transcript.

Before you start writing, check whether the meeting name, date and time, and attendees appear in the transcript or the user's description. Ask the user about the unconfirmed fields in a single question. When asking for the meeting name, also suggest a name based on the main agenda. Leave out the line for any field the user asks to omit or does not know. When grouping by speaker or naming owners in the next steps, if the transcript labels speakers without names (for example "Speaker 1"), ask in the same question who each speaker is. If the user prefers not to say, keep the transcript labels.

```markdown
# Meeting overview
- (Meeting name) Name of the meeting
- (Purpose) Purpose the meeting addressed
- (Date and time) YYYY-MM-DD HH:MM-HH:MM
- (Attendees) Name, Name, Name

# Discussion
- **(Level-1 label) Claim**
    + (Level-2 label) Evidence for the claim

# Next steps
- **(Owner) Recipient, deliverable, deadline**
```

| Grouping | Level-1 label | Level-2 label | How to group |
|---|---|---|---|
| Speaker | Speaker name | Topic | Group by speaker, using the names the user gave or the transcript labels. Write each speaker's claims as one block, never split across places |
| Topic | Topic | Keyword | Group similar claims under one topic. Topics must not overlap, and no discussion may be left out |
| Time | Topic | Keyword | Follow the order in which the discussion happened. Without time data, follow the order of remarks. Do not group by speaker, so the flow stays intact |

- Write the purpose from the transcript as one concise, clear simple sentence with a single subject and predicate.
- The default format for the date and time is `YYYY-MM-DD HH:MM-HH:MM` on a 24-hour clock (for example 2026-03-05 14:00-15:30). If the user's region writes dates and times differently, follow that convention (for example 03/05/2026 2:00-3:30 PM for a user in the United States). Use the user's local time zone for the times.
- Separate attendees with commas.
- Write three to five lines for the next steps. If the transcript has fewer items, write only those.
- Bold level-1 lines and do not indent them. Indent level-2 lines.
- Attach evidence from the transcript as level 2 under every level-1 claim.

## Briefing

Keep the flow of a single input. Videos, audio, articles, and documents all use this format.

```markdown
# Overview
- (Title) Title of the input
- (Field name) Confirmed basic information

# Summary
Three to five lines

# Content
## Subtopic following the input's flow
- Content

# Takeaways
Three to five lines
```

| Input | Overview fields |
|---|---|
| Video captions, video file | Title, publisher, publication date, length, view count, source address |
| Audio file | File name, length, detected language |
| Web article | Title, outlet, author, publication date, source address |
| Document | Title, issuer, issue date, source |

- Fill the overview only with fields confirmed by the conversion metadata or the user's description. Leave out unconfirmed fields entirely.
- Write the content in the order it appears in the input. Videos and audio follow time order. Cover every topic without omission, with no length limit.
- In takeaways, write what the content means and what needs further checking. Do not write forecasts or judgments the input does not support.

## Report

Combine two or more inputs around topics.

- Structure a report that shares a status or trend as why, what, how. Structure a report that asks for a solution or decision as situation, complication, question, answer.
- Name each heading so its title alone tells the reader what follows.
- When inputs disagree, write each input's position side by side with its source.
- Keep the figures that drive the conclusion to three or fewer. More figures blur what the reader should judge by.
- Use at most three tables, only where a summary helps, placed right after the claim they support. Do not place tables back to back.
- Cite sources so each sentence can be traced to its input.

## Translation

Translate into the language the user names. Without one, translate into the user language. If the source is already in the user language and no target is named, ask for the target language. Pick one of the following modes by the nature of the text.

| Mode | For | Rules |
|---|---|---|
| General translation | Texts centered on conveying facts, such as news reports, official letters, manuals, papers, and meeting minutes | Render the whole source without distortion or omission. Use markdown and bullets only where the source uses them |
| Essay translation | Texts centered on the author's argument, such as essays, columns, editorials, and op-eds | Translate everything without summarizing. Write the body in the target language's polite register (for Korean, 존댓말). Use bullets only where the author intended structure. Put an overview and a summary of up to ten lines at the top, written without the polite register |

- Intended structure often appears where items are listed after a colon (:). Do not turn paragraphs that flow as sentences into bullets.
- A translation follows the source's style, so the "Writing style" section does not apply. It does apply to the overview and summary of an essay translation.

## Conversion

- Run the script without `--max-chars` and deliver the result files through the environment's file delivery method. In the chat reply, list only the files and their character counts.
- For PDFs, include `_tables.md` only when tables exist.
- When the user asks for chunks or splitting, use `--chunk`. The target size is 2,000 characters unless the user sets one.

## Writing style

These rules apply to all write-ups and to the overview and summary of an essay translation. The rules were written for Korean. In other languages, apply the same principles as terse bullet phrasing in that language.

- Write in bullet style and end lines with noun phrases (for example "Budget cut agreed", "Further review needed", "Recovery expected in H2"). Do not use a polite or honorific register.
- Put one message in each sentence. If an actor, an object, or a method appears twice in one sentence, split the sentence.
- Do not join sentences with connectors such as "and", "but", or "while". Use commas only to list three or more items of the same kind.
- Put a label in parentheses before a sentence when needed (for example "(Budget adjustment) Q2 budget cut agreed"). Do not attach labels with a colon or hyphen. Name labels after their content, and do not use empty names such as "Explanation" or "Evidence".
- Give each heading one topic. Do not combine two topics as in "A and B". Within one text, keep headings either all keyword style or all sentence style.
- Use sub-bullets (+) only when there are two or more items at the same level. Merge a single item into the line above.
- Do not use contrasts such as "not A but B", the em dash character, the tilde (write ranges with "-"), or expressions that announce a count in advance such as "three key tasks".
- Do not use intensifying adverbs such as "very" or "highly", or inflated judgments such as "groundbreaking" or "innovative".
- Do not write sentences about the text itself or the writing process, such as "This report...", "As you requested", or "In summary".
- Avoid stiff, translated-sounding phrasing such as "in the case of" or "it is necessary to".
- Attach a source to every figure. Write sources in a `>` block as "Organization or author(year), title(link)", and use a separate block for each source.

## Pre-delivery check

- Does the output type match the request and the "Output types" section?
- Was the writing based on the conversion result files?
- Is every topic in the input reflected?
- Are there no claims, judgments, figures, or plans that the input lacks?
- Does every correction meet the correction test?
- Does the overview contain only confirmed fields?
- If any input was truncated, was the user told?
- Before writing minutes, were the unconfirmed meeting name, date and time, and attendees asked about?
- Does every claim in the minutes carry evidence?
- Is no paragraph missing from the translation?
- Were the writing style rules followed?
