# Survey Types

## Respondent Demand Survey

A survey that asks a target group about its needs, intentions, and preferences. The unit of analysis is the respondent.

### Separate What You Measure

Ask about need (is there a problem?), intention (would you use it?), and willingness to pay (would you pay for it?) with separate questions. Report the three results under their own names. Converting an intention share into actual participation requires separate evidence, such as the ratio of actual participation to stated intention in past programs.

### Setting Priorities

| Method | Required items | Result form | When to use |
|--------|----------------|-------------|-------------|
| Selection share | Top-3 choice | Bar chart of selection share by item | Many items and a quick summary is needed |
| Importance-performance analysis | Importance by item, current satisfaction by item | Four-quadrant scatter plot | Choosing improvement targets visually |
| Borich needs score | Importance by item, current level by item | Ranking of needs scores by item | Ranking training or capability development needs |

- Importance-performance analysis places satisfaction on the horizontal axis and importance on the vertical axis, and divides the plot into four quadrants with two reference lines (Martilla & James 1977). The quadrant with high importance and low satisfaction holds the priority improvement targets.
- Choose the reference line, either the item mean or the scale midpoint, before looking at the data, and state it in the report. The quadrant an item falls into changes with the reference line.
- Compute the Borich needs score for each item as Σ(importance − current level) × mean importance ÷ number of respondents (Borich 1980). Take the sum over all respondents.
- Group items with small differences in needs score or selection share at the same level. Follow the similar-level rule in references/reporting.md.

## Project-Type Demand Survey

A survey that collects project candidates in a set format to discover projects, such as technology demand surveys, project demand surveys, or RFP-format demand surveys. Submitted documents (proposals, demand forms, RFP drafts, and so on) are all called proposals below. It supports R&D project planning, discovery of AI transformation (AX) projects, and similar work. The unit of analysis is the proposal.

### Reading Submission Counts

- When submitters are parties hoping to carry out the projects, submission counts reflect the extent of participation in the call more than the size of demand. Label counts by field as "number of submissions" and do not restate them as demand size.
- When one organization submits several similar proposals or a group submits in an organized way, the count for a field rises. Set a rule for merging similar proposals and record the counts both before and after merging.

### Form Design

- Match each form field to one evaluation criterion. Delete fields that the evaluation does not use.
- Collect classification fields (technology field, development stage, type of performing organization, and so on) as multiple-choice fields. Free-text answers add a classification step.
- Collect performance targets as separate numeric fields for current level, target level, and unit. An example is reducing processing time from 30 minutes to 5 minutes.
- Set a character limit on descriptive fields. With a limit, you can estimate review time in advance.

### Heilmeier Catechism

When you need a starting point for evaluation criteria, you can use the Heilmeier Catechism published by the U.S. Defense Advanced Research Projects Agency (DARPA). Variants with different numbers of questions and wording are also in use. The questions in DARPA's published version are below.

- What are you trying to do? (with no jargon)
- How is it done today, and what are the limits of current practice?
- What is new in your approach, and why do you think it will succeed?
- Who cares? If you succeed, what difference will it make?
- What are the risks?
- How much will it cost?
- How long will it take?
- What are the mid-term and final exams to check for success?

Giving each question its own form field keeps the form and the evaluation criteria in the same order. Adjust questions that do not fit the assignment together with the evaluation criteria.

### Organizing and Classifying

- Write a code, a definition, and a typical example for each entry in the classification scheme.
- A language model can classify proposals. Have a person reclassify a randomly chosen part of the results, and revise the definition of any code with repeated disagreements before classifying again.
- Keep the merging rule for similar proposals and the merge results in the processing log.

### Evaluation

- For each evaluation criterion, write in advance what a score of 1, 3, and 5 looks like.
- Have at least two reviewers evaluate each proposal.
- Agreement between reviewers on the same proposal can be low. In a study that re-reviewed 25 proposals already funded by the U.S. National Institutes of Health (NIH), reviewers showed almost no agreement (Pier et al. 2018).
- Summarize evaluation results in tiers such as selected, further review, and on hold, in preference to fine score rankings.
- Report the share of proposals that two reviewers placed in the same tier (tier agreement rate). When a formal report is needed, add the intraclass correlation coefficient. The formula is in references/analysis.md.
- Settle proposals with split tiers through discussion and record the outcome.

### Criteria Weights

When weights among evaluation criteria are needed, you can run the analytic hierarchy process (AHP) with experts.

- Keep seven or fewer items in one comparison set (Saaty & Ozdemir 2003). The number of pairwise comparisons grows as k(k − 1) ÷ 2, so 7 items need 21 comparisons and 9 items need 36.
- When a respondent's consistency ratio exceeds 0.1, ask that respondent to recheck the comparisons (Saaty 1990). If a recheck is not possible, exclude that response from the analysis and report the number excluded.
- Combine judgments from several experts with the geometric mean for each comparison (Aczél & Saaty 1983).
- The consistency ratio formula is in references/analysis.md.

## Diagnostic Survey

A survey that scores an organization's level with a fixed diagnostic model, such as a maturity assessment. The unit of analysis is the assessed organization.

### Fixing the Model

- Before collecting data, fix the diagnostic areas, items, level definitions, scoring formula, weights, and level bands in a document and give it a version number.
- Write the level criteria specifically enough that another person would assign the same level to the same responses (Pöppelbuß & Röglinger 2011).
- Compare years using only the items common to both versions. For a year in which items or formulas changed, state the changes with the results.

### Respondents

- Decide who answers on behalf of the organization. When one person answers, that person's view becomes the organization's score.
- When several people in one organization answer, check the spread of their answers first and then set the aggregation rule (mean, median, or weighting by position).
- When area scores among respondents in the same organization differ by one scale point or more, report scores by respondent group alongside the organization score. This one-point threshold is a default of this skill.
- A self-assessment score reflects the respondent's perception. Including some items that can be confirmed with evidence, such as having a document or running a system, gives the score a verifiable basis.

### Scoring

- Use the mean of the items in an area as the default area score. If you use weights, write the weights and their rationale in the model document.
- Define level bands with numbers, including whether each boundary is inclusive. An example is level 1 for an area score of at least 1.0 and below 2.0.
- Check with Cronbach's alpha whether the items in an area measure the same thing (Cronbach 1951). By convention, 0.7 serves as a reference line.
- For an area whose alpha falls below the reference line, report item-level results along with the area score. Review the item composition of that area in the next version.
- Report area scores together with the single overall level. Differences between areas show up in the area scores.

## Secondary Data

- Join only data that share the same indicator definition, base year, unit, and survey method. Mark the point where a definition changed on the chart.
- When comparing numbers from different sources, keep a table of the definition differences by source.
- Separate nominal and real amounts and state the base year.
- State the sample size and survey method of the original source for secondary data as well.
