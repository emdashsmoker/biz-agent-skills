# biz-agent-skills

[한국어](README.ko.md)

Agent Skills for the report writing and analysis work of planners, consultants and analysts. Every skill ships as a Korean original and an English translation. The Korean originals follow the document conventions of Korean public agencies and companies.

## Skills

A skill whose name ends in `-lite` is a lite edition: the same function with shorter instructions and lower token use.

### Research

- `environment-analysis`: Researches the macro environment, industry, internal capability and benchmarks, then turns them into sourced facts and implications.
- `environment-analysis-lite`: Lite edition of `environment-analysis`.
- `five-forces`: Analyzes the competition in an industry with Michael Porter's Five Forces framework.
- `source-check`: Answers only from the files you provide and from searched sources that pass a quality filter.
- `digest`: Turns web pages, documents, audio and video into minutes, briefings, reports or translations.
- `md-parser`: Converts PDF, HWP, HWPX, Office files and more into Markdown.

### Analysis

- `practical-calc`: Runs practical calculations such as CAGR, NPV, B/C, IRR, AHP and financial ratios as reproducible Python scripts.
- `practical-calc-lite`: Lite edition of `practical-calc`.
- `cagr`: Calculates a compound annual growth rate from two points in time.
- `practical-stats`: Designs and runs practical statistical analysis of surveys and secondary data around the decision it must inform.
- `network-analysis`: Runs social network analysis with NetworkX code and charts.
- `network-analysis-lite`: Lite edition of `network-analysis`.
- `ontology-modeling`: Designs definitions, classes and relations without overlaps or gaps, and builds an OWL ontology when needed.
- `dataframe-ops`: Turns plain-language or cell-reference requests about tables into pandas code and runs it.
- `chart`: Settles the message first, then builds static report charts with matplotlib.
- `biz-code-style`: Sets how coding, analysis and chart work runs and how the outputs look.
- `biz-code-style-lite`: Lite edition of `biz-code-style`.

### Planning

- `strategy-builder`: Builds an organization's strategy framework step by step, from environment analysis to performance indicators.
- `rfp-strategy`: Analyzes a request for proposal and builds a bid strategy.
- `project-plan`: Writes a project overview and a WBS for a project under contract.
- `think-review`: Checks plans, arguments and documents from first principles.
- `think-review-lite`: Lite edition of `think-review`.

### Writing

- `logical-write`: Writes and revises Korean outline-style (gaejosik) reports in a Markdown hierarchy.
- `logical-write-lite`: Lite edition of `logical-write`.
- `clear-comm`: Writes emails, replies, feedback and announcements that put the point first.
- `anti-slop`: Finds and fixes the stock phrasing of language models.
- `no-jargon`: Rewrites jargon so that readers outside the field can follow.
- `onto-mece`: Checks classifications, hierarchies and definitions in a text for overlaps and gaps.
- `fx-krw`: Adds a Korean won equivalent next to each foreign currency amount.

### Working setup

- `lean-work`: Fixes the purpose, reader and scope first, then keeps only what the work needs.
- `long-task-ledger`: Records long multi-step agent work so it can resume after a truncated conversation or a new session.
- `pref-architect`: Designs short always-on instructions and on-demand modular skills through an interview.
- `skill-forge`: Builds, combines and manages skills and agent instructions.
- `offline-deps-builder`: Builds dependency skills that carry the libraries, fonts and models another skill would download at run time.

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

## License

[GPL-3.0-or-later](LICENSE). Copyright (C) 2026 Em Dash Smoker.

Each skill carries its own `LICENSE` and `NOTICE.md`. Under the output exception in `NOTICE.md`, the documents, charts and other files you make with a skill are free of GPL terms. Packages, fonts and models that a skill installs at run time keep their own licenses.
