---
name: digest
description: Converts web addresses, documents (PDF, HWP, HWPX, DOCX, PPTX, XLSX and more), audio and video files, caption files (SRT, VTT), and pasted text into text, then organizes them into meeting minutes, briefings, reports, translations, or markdown conversions. Audio is transcribed locally with faster-whisper, web pages are extracted with trafilatura, and documents are converted with markitdown, pdfplumber, python-hwpx, and pyhwp. Use this skill whenever the user asks to write up meeting minutes, clean up a transcript, organize a recording, convert speech to text, clean up captions, summarize a video, summarize or translate a news article, translate a column, extract the body of a web page, convert a document to markdown, extract file contents, or write a report or briefing that combines several sources. Also use it whenever the user provides a file or link and asks for a summary, write-up, or translation, even without naming a format.
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# digest

This English version was translated from the Korean original. It may behave differently from what the original intends.

The skill turns many kinds of input into text and then into writing a reader can use without further editing. `scripts/extract.py` handles conversion and the model handles the writing. Save the conversion result to a file first, then read that file and write. Reading the raw input directly lets noise such as timing lines, markup tags, repeated lines, and so on leak into the result.

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
4. Convert every input except pasted text with the script. Transcribe audio and video with the model the user selects in the "Choosing the transcription model" section.
5. Read the conversion result files. Do not read the original document, caption, or audio files.
6. Write in the format for the chosen output type.
7. Go through the "Pre-delivery check" section, then deliver. Output write-ups and translations as a chat reply, and save them as a markdown file when the user wants a file. Deliver conversions as files.

When input arrives with the request, skip the guidance and start from step 2. After the first use, keep handling new input in the same conversation this way until the user asks you to stop.

## Output types

If the user specifies a type, format, or length, follow it. Otherwise check the table from the top and select the first matching type.

| Order | Condition | Output |
|---|---|---|
| 1 | The user only asks for a format change, such as convert, extract, reformat as markdown, and so on | Conversion |
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
| Audio, video | faster-whisper, `av<19` |
| Captions | none |

```bash
pip install httpx trafilatura "markitdown[pdf,docx,pptx,xlsx,xls]" pdfplumber python-hwpx beautifulsoup4 lxml olefile faster-whisper "av<19"
pip install pyhwp
```

- On a personal computer, create a project virtual environment (venv, conda, or similar) and install there. Installing into the system Python can conflict with packages other programs use.
- In a disposable isolated environment such as a cloud sandbox, rerun the install with `--break-system-packages` if an `externally-managed-environment` error occurs.
- If pyhwp fails with a build error mentioning `install_layout`, retry with `SETUPTOOLS_USE_DISTUTILS=stdlib pip install pyhwp`. If it still fails, continue without pyhwp. HWP files then go through the olefile fallback.
- ffmpeg is optional. The script uses it for audio decoding when present and uses the decoder bundled with faster-whisper otherwise.
- The decoder bundled with faster-whisper 1.2.1 does not work with PyAV 19 or later, so the install command keeps the `av<19` condition. If an error mentioning `metadata_errors` appears where ffmpeg is absent, reinstall PyAV with `pip install "av<19"` and try again.
- Whisper models download from Hugging Face on the first transcription. Transcription cannot run where network access is restricted, so tell the user.
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
python scripts/extract.py meeting.m4a --probe
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
| `--max-chars` | 0 (no limit) | Maximum characters of result text. Text beyond the limit is cut, and a truncation mark is added at the end |
| `--timeout` | 15 | Web request timeout in seconds |
| `--download` | off | Keep the original file of a web address in the `downloads` folder |
| `--chunk`, `--chunk-size` | off, 2000 | Split a document into heading-based chunk files |
| `--start`, `--end` | whole file | Range for captions and audio (for example 00:10:00) |
| `--timestamps` | off | Prefix each caption or transcript line with a time |
| `--probe` | off | Estimate transcription time per model on this machine from a sample transcription |
| `--model` | tiny | Whisper model size |
| `--language` | auto-detect | Audio language code (for example ko, en, and so on) |
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
- Pages behind a login or subscription yield only their publicly visible content. If the body is missing, ask the user to supply it.
- For document addresses, extract the text and do not keep the original. Use `--download` only when the user asks to keep files or when the task collects documents found through web search.
- Bundle three or more downloaded files with `--bundle` before delivery, and deliver two or fewer one by one. Before starting a second download task in the same conversation, clear earlier files with `--clean`.

### Audio and video

- The script decodes the input to 16 kHz mono and transcribes on the CPU with int8 precision. It saves one line per segment without times. Add `--timestamps` for time-based minutes or when the user asks for times.
- When the user wants only part of a recording, process that range with `--start` and `--end`. Pass `--language` when the language is known.
- Choose the transcription model by following the "Choosing the transcription model" section.

### Choosing the transcription model

The transcription model is a speech recognition model that turns speech into text. The skill runs the Whisper model published by OpenAI on the user's machine, so the audio never leaves the machine. Whisper comes in several sizes. Larger models recognize speech more accurately but take longer and use more memory. The same model can take very different times on different machines. So measure the processing speed on the machine that will transcribe first. The user then compares time and accuracy from the result and selects a model. If the user specified a model in the request, skip these steps and transcribe with that model.

1. Run a probe with `--probe`. Set `--start`, `--end`, `--language`, and `--beam-size` to the same values as the real transcription. The script transcribes 60 seconds from the middle of the range with tiny to measure the processing speed. The expected time range per model calculated from the result is recorded in `estimates`.
2. Determine the recommended model by the following criteria.
    - Decide first how much recognition accuracy the output needs. For example, a write-up corrects recognition errors from the surrounding sentences during writing, so it needs less accuracy than a conversion, which delivers the transcript as it is.
    - Judge how hard the recording is to recognize from confirmed facts only. Confirmed facts are the recording conditions the user described (noise, number of speakers, share of technical terms) and the language detection result of the probe (`language`, `language_probability`).
    - Recommend the model with the shortest expected time among those that meet the needed accuracy and the recognition difficulty. Move up to a larger model one step at a time, and only when a confirmed fact calls for it.
    - If the recommended model's expected time is long, also present the next smaller model as an alternative.
3. Inform the user in this order: an explanation of the transcription model, the machine specs (`cpu_count`, `memory_gb`), the length of the processing range (`target_duration`), the expected time per model, and the recommended model with the reason. The explanation covers, in two or three sentences, what the model does, how model size relates to accuracy, time, and memory, the download of a model used for the first time, and the fact that the audio never leaves the machine. Skip the explanation if the user says they already know the transcription model. Present the expected time per model in a table with model, expected time, and recognition accuracy columns. Write the expected time as the `min`-`max` range from `estimates`.
4. Ask the user to select a model. Do not start transcribing before the user selects one.
5. Transcribe with the selected model in `--model`.

| Model | Parameters | Relative speed (vs large) | Peak memory (measured) | Recognition accuracy (relative grade) |
|---|---|---|---|---|
| tiny | about 39M | about 10x | about 0.4 GB | Lowest |
| base | about 74M | about 7x | about 0.5 GB | Low |
| small | about 244M | about 4x | about 1.2 GB | Medium |
| medium | about 769M | about 2x | about 3.3 GB | High |
| large-v3 | about 1,550M | 1x | about 5.5 GB | Highest |

- The relative speed was measured on a GPU. Judge CPU transcription time by the `--probe` result.
- The accuracy grade is the relative order among models. Actual recognition quality varies widely with the language and the recording conditions.
- The expected time does not include model download time or load time. A model used for the first time adds its download time.
- Exclude models whose peak memory exceeds `memory_gb` from the options. For a model whose peak memory is close to `memory_gb`, inform the user that it may fail for lack of memory. If `memory_gb` is null, inform the user that memory could not be checked.
- With several audio files, run a probe for each file. Calculate the total expected time per model with code and present it at once.
- If the environment limits how long a command may run, compare that limit with the upper bound of the selected model's expected time. If the upper bound is longer, transcribe with the environment's background execution feature. If there is no such feature, split the processing range with `--start` and `--end` into parts shorter than the limit and transcribe them in turn.

> OpenAI(2022), Whisper model sizes, parameters, and relative speed(https://github.com/openai/whisper)

> (Peak memory test setup) faster-whisper 1.2.1, CPU int8, beam size 5, 250 seconds of Zeroth Korean test audio(https://huggingface.co/datasets/Bingsu/zeroth-korean)

### Caption files

- Clean the caption file with the script and read only the cleaned `_captions.md`. Auto-generated captions sometimes repeat one sentence across several cues, so the script drops a line identical to the line before it.
- When the user wants only a certain time span, extract that span with `--start` and `--end`.

### Video platform addresses

When the user provides only the address of a video page on a video sharing service, do not download the video or its captions with automated tools without the user's consent. Platform terms sometimes restrict automated collection and downloading. Ask the user for one of the following.

- A caption file (.srt, .vtt) the user obtained in a way the platform's terms allow
- Text copied from the platform's own transcript view
- An audio or video file the user holds

Explain how to obtain captions only when the user asks. Follow this order when explaining.

1. Identify the platform from the address the user provided.
2. Summarize the ways to obtain captions on that platform from the model's own knowledge. Consider both the platform's built-in features and outside methods.
3. If the environment provides a web search tool, check step 2 against current information. Platform features, terms, and whether outside methods still work change often. Without a search tool, tell the user the guidance may be out of date.
4. Guide the user through the most useful method in steps they can follow themselves. When choosing, put official and lawful routes first. Judge usefulness by whether it runs in the user's environment, whether it yields captions in the needed language, and how few steps it takes.
5. Explain the risks that come with the method thoroughly.
6. Ask the user whether to carry out the method. If the user wants it, carry it out in the current environment. If the environment cannot run it, guide the user to run it themselves. Either way, obtain caption files as .srt or .vtt.
7. Once the captions are obtained, continue from step 2 of the workflow. If the user already asked for an output, follow that request.

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

Before you start writing, check whether the meeting name, date and time, and attendees appear in the transcript or the user's description. Ask the user about the unconfirmed fields in a single question. When asking for the meeting name, also suggest a name based on the main agenda. Leave out the line for any field the user asks to omit or does not know. When grouping by speaker or naming owners in the next steps, if the transcript labels speakers without names (for example "Speaker 1"), ask in the same question for each speaker's name. If the user prefers not to say, keep the transcript labels.

```markdown
# Meeting overview
- (Meeting name) Name of the meeting
- (Purpose) Purpose the meeting addressed
- (Date and time) YYYY-MM-DD HH:MM-HH:MM
- (Attendees) Name, Name, Name

# Discussion
## Header (speaker name for speaker grouping, used for other groupings when a breakdown helps)
- (Level-1 label) Claim
    + Evidence for the claim
    + (Level-2 label, when the evidence needs structuring) Evidence for the claim

# Next steps
- (Owner) Action item
```

| Grouping | Header (##) | Level-1 label | Level-2 label | How to group |
|---|---|---|---|---|
| Speaker | Speaker name | Topic | Keyword | Write one `##` header per speaker. Put all of that speaker's claims under that header. Use the name the user gave or the transcript label in the header. When the topics need a breakdown, add `###` headers under the speaker header |
| Topic | As needed | Topic | Keyword | Group similar claims under one topic. Topics must not overlap, and no discussion may be left out |
| Time | As needed | Topic | Keyword | Follow the order in which the discussion happened. Without time data, follow the order of remarks. Do not group by speaker, so the order of discussion stays intact |

- Write the purpose from the transcript as one concise, clear simple sentence with a single subject and predicate.
- The default format for the date and time is `YYYY-MM-DD HH:MM-HH:MM` on a 24-hour clock (for example 2026-03-05 14:00-15:30). If the user's region writes dates and times differently, follow that convention (for example 03/05/2026 2:00-3:30 PM for a user in the United States). Use the user's local time zone for the times.
- Separate attendees with commas.
- Write three to five lines for the next steps. If the transcript has fewer than three items, write only those.
- Write each next-step line as one sentence that states the owner's action item. Include the deadline, the deliverable's recipient, and the deliverable mentioned in the transcript (for example "(Minsu Kim) Pilot rollout plan draft to be reported to the executives by November 20", "(Jiyoung Park) Vendor data check results to be shared with the security team by next Friday", and similar lines).
- Do not indent level-1 lines. Indent level-2 lines.
- Do not duplicate the information in a header (for example a speaker name, an agenda item, and so on) in the labels or sentences under it.
- Use a level-2 label in cases where the evidence needs structuring (for example, when the evidence falls into several categories, expresses a complex concept, and so on).
- Attach evidence from the transcript as level 2 under every level-1 claim.

## Briefing

Preserve the order in which a single input presents its content. Videos, audio, articles, and documents all use this format.

```markdown
# Overview
- (Title) Title of the input
- (Field name) Confirmed basic information

# Summary
Three to five lines

# Content
## Subtopic following the input's order
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
- In takeaways, write the implications of the content and the items that need further checking. Do not write forecasts or judgments the input does not support.

## Report

Combine two or more inputs around topics.

- Structure a report that shares a status or trend as why, what, how. Structure a report that asks for a solution or decision as situation, complication, question, answer.
- Name each heading so its title alone tells the reader what follows.
- When inputs disagree, write each input's position side by side with its source.
- Keep the figures that drive the conclusion to three or fewer. More figures make the reader's basis for judgment unclear.
- Use at most three tables, only where a summary helps, placed right after the claim they support. Do not place tables back to back.
- Cite sources so each sentence can be traced to its input.

## Translation

Translate into the language the user names. Without one, translate into the user language. If the source is already in the user language and no target is named, ask for the target language. Choose one of the following modes by the nature of the text.

| Mode | For | Rules |
|---|---|---|
| General translation | Texts centered on conveying facts, such as news reports, official letters, manuals, papers, meeting minutes, and so on | Render the whole source without distortion or omission. Use markdown and bullets only where the source uses them |
| Essay translation | Texts centered on the author's argument, such as essays, columns, editorials, op-eds, and so on | Translate everything without summarizing. Write the body in the target language's polite register (for Korean, 존댓말). Use bullets only where the author intended structure. Put an overview and a summary of up to ten lines at the top, written without the polite register |

- Intended structure often appears where items are listed after a colon (:). Do not convert narrative paragraphs into bullets.
- A translation follows the source's style, so the "Writing style" section does not apply. It does apply to the overview and summary of an essay translation.

## Conversion

- Run the script without `--max-chars` and deliver the result files through the environment's file delivery method. In the chat reply, list only the files and their character counts.
- For PDFs, include `_tables.md` only when tables exist.
- When the user asks for chunks or splitting, use `--chunk`. The target size is 2,000 characters unless the user sets one.

## Writing style

These rules apply to all write-ups and to the overview and summary of an essay translation. The rules were written for Korean. In other languages, apply the same principles as terse bullet phrasing in that language.

- Write in bullet style and end lines with noun phrases (for example "Budget cut agreed", "Further review needed", "Recovery expected in H2", and so on). Keep a formal written register, and do not use a polite or honorific register. Do not use colloquial words or slang (for example "kinda", "pretty much", "a bunch of", and so on).
- Put one message in each sentence. If an actor, an object, or a method appears twice in one sentence, split the sentence.
- Do not join sentences with connectors such as "and", "but", "while", and so on. Use commas only to list three or more items of the same kind.
- Put a label in parentheses before a sentence when needed (for example "(Sales division) Q2 marketing budget cut agreed"). Do not attach labels with a colon or hyphen. Name labels after their content, and do not use empty names such as "Explanation", "Evidence", and so on.
- A label is a marker that lets the reader find and compare items before reading the sentences. When the items under one parent divide by one criterion (for example actor, period, option, and so on), label every item with its category name. On other items, attach a label only when it carries information that the heading and the sentence do not.
- Do not repeat the information in a label in its heading or its sentence. When the same label appears in several places, check whether the classification overlaps. Merge overlapping content into one place.
- Give each heading one topic. Do not combine two topics as in "A and B". Within one text, keep headings either all keyword style or all sentence style.
- Use sub-bullets (+) only when there are two or more items at the same level. Merge a single item into the line above.
- Classify headings, labels, and bullets by one criterion. Write items at the same level so that they do not overlap. Lower-level items must collectively cover the full scope of their higher-level item without omission.
- Do not use contrasts such as "not A but B", the em dash character, the tilde (write ranges with "-"), or expressions that announce a count in advance such as "three key tasks".
- Do not use intensifying adverbs such as "very", "highly", and so on, or inflated judgments such as "groundbreaking", "innovative", and so on.
- Do not write sentences about the text itself or the writing process, such as "This report...", "As you requested", "In summary", and so on.
- Avoid stiff, translated-sounding phrasing such as "in the case of", "it is necessary to", and so on.
- Do not use placeholder nouns such as "thing", "stuff", "part", "aspect", and so on. Name what they refer to with a specific noun (for example "the agenda item for further discussion" for "the part to discuss").
- Attach a source to every figure. Write sources in a `>` block as "Organization or author(year), title(link)", and use a separate block for each source.

## Pre-delivery check

- Does the output type match the request and the "Output types" section?
- Was the writing based on the conversion result files?
- Was audio transcribed with the model the user selected or specified?
- Did the model guidance include the explanation of the model and the reason for the recommendation?
- Is every topic in the input reflected?
- Are there no claims, judgments, figures, or plans that the input lacks?
- Does every correction meet the correction test?
- Does the overview contain only confirmed fields?
- If any input was truncated, was the user told?
- Before writing minutes, were the unconfirmed meeting name, date and time, and attendees asked about?
- Does every claim in the minutes carry evidence?
- Is each header in the minutes used as its grouping specifies, with its information not duplicated in the labels or sentences under it?
- Is each next-step line a sentence with the deadline, the deliverable's recipient, and the deliverable mentioned in the transcript?
- Is no paragraph missing from the translation?
- Are headings, labels, and bullets classified by one criterion without overlap or omission?
- Reading only the labels, is there no label whose content duplicates another and no label that repeats its heading or sentence?
- Were the writing style rules followed?
