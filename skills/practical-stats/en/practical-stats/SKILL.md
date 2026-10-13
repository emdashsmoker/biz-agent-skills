---
name: practical-stats
description: Statistical design and analysis for planning and consulting work with surveys, demand surveys, diagnostic surveys, or secondary data. Starts from the decision the results must inform, designs the sample, questions, and analysis at minimum cost, computes every number with code, and reports without distortion. Use when the user mentions survey or questionnaire design, demand surveys, technology, project, or RFP-format demand surveys, maturity assessments, sample size, margin of error, whether 30 respondents are enough, group comparisons, significance tests, importance-performance analysis, needs assessment, priorities, AHP, or statistical review of a report, or provides survey data, summary tables, or submitted proposals for analysis. Apply it even without statistical terms. Read references/design.md (design), references/survey-types.md (survey types), references/analysis.md (processing and analysis), references/reporting.md (reporting and distortion checks), and references/sources.md (literature).
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# Practical Statistics

> This skill is an English translation of the Korean original. The translation may cause the skill to behave differently from the original intent.

## Terms

| Term | Definition |
|------|------------|
| Decision question | A sentence stating who decides what, and by when, based on the survey results |
| Stakeholder | A client, contracting organization, or internal decision maker who receives or uses the survey results |
| Analysis plan | A list of empty result tables and empty charts prepared before data collection |
| Probability sample | A sample drawn at random from a population list, so each unit's selection probability is known |
| Non-probability sample | A sample where respondents select themselves or the researcher picks them for convenience, such as open calls, online panels, or referrals |
| Margin of error | The spread of an estimate caused by chance alone in a probability sample, at a 95% confidence level by default |
| Effect size | A number that expresses the size of a difference or relationship independently of sample size |
| Comparison group | A subgroup reported separately (region, company size, industry, and so on) |
| Top-two-box share | The share of responses that chose 4 or 5 on a 5-point scale |
| Processing log | A document that records each judgment and rule applied while turning raw data into analysis data |

Use these terms with the same definitions in all outputs, and keep the same names throughout.

## Operating Principles

- (Start from the decision) Link every question and every analysis to a decision question. Delete questions that link to no decision question. The decision question sets the sample size and the scope of analysis.
- (Reproducible computation) Compute every number, including shares, means, sample sizes, and test results, with code. The model and the user make the judgments needed to read and tidy irregular tables. Write each judgment as a rule in the processing log and apply it with code. Anyone with the same raw data and the same processing log must be able to reproduce the same results.
- (Simplest design) When several methods answer a decision question, choose the one with the fewest questions, the smallest sample, and the fewest analysis steps. Prefer question formats whose results move directly into one table or one bar chart.
- (Conclusions within the evidence) Keep conclusions within the population the sample represents. Describe results from non-probability samples as results for the respondents.

## Workflow

| Stage | Task | Output | Reference |
|-------|------|--------|-----------|
| Questions | Write decision questions and build the analysis plan | Decision questions, analysis plan | references/design.md |
| Design | Identify the survey type and set the sample and questions | Sampling plan, draft questionnaire | references/design.md, references/survey-types.md |
| Processing | Turn raw data into analysis data | Analysis data, processing log | references/analysis.md |
| Analysis | Compute in the row order of the analysis plan | Result tables, computation code | references/analysis.md |
| Reporting | Turn results into sentences and charts and check for distortion | Report sentences, charts | references/reporting.md |

The user can start at any stage. When the user provides already collected data, set the decision question first. If the request and the data structure let you infer the question, state the inferred question in one line and proceed.

## Survey Types

| Type | Input | Unit of analysis |
|------|-------|------------------|
| Respondent demand survey | Survey responses about needs, intentions, and preferences | Respondent |
| Project-type demand survey | Project candidate proposals submitted in a set format, such as technology demand surveys, project demand surveys, or RFP-format demand surveys | Proposal |
| Diagnostic survey | Responses to the items of a fixed diagnostic model, such as a maturity model | Assessed organization |
| Secondary data | Official statistics, administrative data, existing survey results | Unit of the original data |

When one assignment mixes several types, design and analyze each type separately. The criteria for each type are in references/survey-types.md.

## Cost Reduction

Survey cost grows with the number of questions, the sample size, the number of comparison groups, and processing time. Reduce cost in this order.

- Remove from scope any question that official statistics or administrative data can answer.
- Delete questions that do not link to the analysis plan.
- Set the sample size by the required precision and the number of comparison groups. Halving the margin of error requires four times the sample.
- Keep only the comparison groups used in the decision. Each comparison group needs its own minimum sample.
- Keep only the open-ended questions that have a coding scheme in the analysis plan.

Criteria for judging whether 30 respondents are enough, with an example explanation for stakeholders, are in references/design.md.

## User Confirmation

Ask the user only in the cases below. For every other choice, apply this skill's default criteria and state the applied criterion in one line with the results.

- The request and the data do not allow you to infer the decision question
- A single processing judgment changes a conclusion to be reported
- A choice between budget and precision is required

## Computation Tools

- The default tools are Python with pandas, NumPy, SciPy, statsmodels, and matplotlib. These tools cover every computation this skill requires.
- Use separately installed statistical software such as SPSS, Stata, SAS, or R, and libraries outside the default tools, only when the user has installed them in their own environment. Record the tool name, version, and settings in the processing log.
- In an environment that cannot run code, present the formula and the input numbers along with a spreadsheet formula. Do not report numbers estimated by the model as results.

## Pre-Delivery Check

- Does every question and every result table link to a decision question?
- Is every number the output of executed code, with the formula and inputs kept?
- Can the processing log alone rebuild the same analysis data?
- Does every number carry its population, sample size, and time point?
- Are non-probability sample results described as results for the respondents?
- Are items whose difference has a confidence interval that includes 0 grouped as similar?
- Is the distortion check in references/reporting.md complete?
