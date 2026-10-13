# Design

## Decision Question

Write the decision question in the form "[Who] decides [what] by [when]. To decide, they need to know [what]." The [what] in the second sentence is the survey target.

- (Respondent demand survey example) The program office decides whether to open a training course before next year's budget is set. To decide, it needs to know the share of target companies that intend to participate and their preferred timing.
- (Project-type demand survey example) The planning committee decides the set of candidate projects within one month after the call closes. To decide, it needs to know the distribution of submitted proposals by field and their evaluation tiers.
- (Diagnostic survey example) The agency decides its priority improvement areas by year end. To decide, it needs to know the score of each diagnostic area and the change from the previous year.

When there are several decision questions, mark the one that requires the largest sample. That question sets the total sample size.

## Analysis Plan

Before collecting data, draw the tables and charts of the final report in empty form. The columns of the plan and an example row are below.

| No. | Question to answer | Survey items | Analysis method | Comparison group | Chart type | Linked decision |
|-----|--------------------|--------------|-----------------|------------------|------------|-----------------|
| 1 | How many companies intend to participate? | Item 3 | Share | Company size | Horizontal bar | Whether to open the course |

- One row of the plan answers one question.
- Items not linked to the plan are candidates for deletion. If there is a reason to keep an item, write the reason below the plan.
- Build items that share a chart on the same scale and in the same direction, so one chart can compare their results.
- The comparisons written in the plan are the confirmatory comparisons. Mark comparisons added after data collection as exploratory results during analysis.

## Sample Type

- Use a probability sample when a population list exists and random selection and follow-up contact are possible.
- Respondents gathered through open calls, online panels, or referrals form a non-probability sample. A non-probability sample has no theoretical basis for a probability-style margin of error (Baker et al. 2013). Report its results as results for the respondents.
- For a non-probability sample, set target response counts for each main comparison group so responses do not pile up in one group.
- When the population is small enough to send the questionnaire to everyone, consider a census first. A census needs no selection design and lets you focus effort on managing nonresponse.

## Sample Size for Precision

When estimating a share, set the sample size by the target margin of error (Cochran 1977).

- Margin of error e = 1.96 × √(p(1 − p) ÷ n)
- Required sample n₀ = 1.96² × p(1 − p) ÷ e²
- Adjusted sample for a small population of size N: n = n₀ ÷ (1 + (n₀ − 1) ÷ N)
- Use p = 0.5 when p is unknown. The margin of error is largest at p = 0.5.

| Responses | Margin of error (p = 0.5, 95% confidence) |
|-----------|--------------------------------------------|
| 30 | ±17.9 pp |
| 50 | ±13.9 pp |
| 100 | ±9.8 pp |
| 200 | ±6.9 pp |
| 400 | ±4.9 pp |
| 1,000 | ±3.1 pp |

- Halving the margin of error requires four times the sample.
- A target margin of ±10 pp requires 97 responses. With a population of 200 units, the adjusted requirement is 66.
- A target margin of ±5 pp requires 385 responses. With a population of 200 units, the adjusted requirement is 132.
- Spreadsheet formulas: margin of error `=1.96*SQRT(0.25/n)`, required sample `=ROUNDUP(1.96^2*0.25/e^2,0)`. Replace n and e with the relevant cell addresses.

## Sample Size for Comparison

To test differences between comparison groups, each group needs the sample below. The basis is a 5% significance level, 80% power, and a two-sided test, and the size categories follow Cohen (1992).

| Compared quantity | Difference to detect | Required sample per group |
|-------------------|----------------------|---------------------------|
| Mean | Small (d = 0.2) | 394 |
| Mean | Medium (d = 0.5) | 64 |
| Mean | Large (d = 0.8) | 26 |
| Share | 50% vs 60% | 388 |
| Share | 50% vs 70% | 93 |

- d is the difference between two means divided by the standard deviation.
- With k comparison groups, the required sample grows roughly k times.
- Remove from the design any comparison that the decision does not use.
- You can recompute these numbers with `statsmodels.stats.power`.

## Are 30 Respondents Enough?

When sizing a demand survey, someone may ask to cut the sample on the claim that "30 respondents produce a normal distribution." The basis and the proper use of this claim are below.

- The n ≥ 30 rule is a rule of thumb from the central limit theorem. The theorem concerns the distribution of the sample mean, which approaches a normal distribution as the sample grows. The distribution of individual responses keeps its original shape regardless of sample size.
- How fast the sample mean approaches normality depends on the skew of the data. Data with a long tail on one side, such as amounts, revenue, or time spent, need samples larger than 30 (Hesterberg 2008).
- Sample size sets precision separately from the normal approximation. The margin of error for a share with 30 responses is about ±17.9 pp.
- Thirty responses can confirm a broad direction. If 24 of 30 responses (80%) give the same answer, the 95% Wilson confidence interval runs from 62.7% to 90.5%, above a majority.
- Differences between comparison groups, fine rankings among items, and means of skewed amount data require larger samples.
- Samples of around 30 remain useful for pretesting questions and for supplementing interview findings.

Use the text below as a starting point when explaining this to stakeholders.

> With 30 responses, the margin of error for a share is about ±18 percentage points. That is enough to confirm a broad direction such as whether a majority agrees. Comparing differences of about 20 percentage points across regions or company sizes requires about 93 responses per comparison group. Once we agree on the level of conclusion you need, we will set the sample to match.

## Nonresponse

Nonresponse bias can be written as follows (Groves 2006).

- Bias = (1 − response rate) × (respondent mean − nonrespondent mean)
- A low response rate produces little bias when respondents and nonrespondents answer alike. A synthesis of 59 methodological studies also found a weak relationship between response rates and bias (Groves & Peytcheva 2008).
- When people interested in the topic respond more often, demand is overestimated. As a hypothetical example, with a 30% response rate, 60% participation intent among respondents, and 30% among nonrespondents, the true intent is 39% while the survey shows 60%.

Pushing the response rate up gives no guarantee that this bias shrinks. The checks below reveal the direction of bias at low cost.

- Compare the respondent profile (company size, region, industry) with the profile of the population list.
- Compare the answers of respondents near the deadline with those of early respondents. Late respondents' answers offer clues about nonrespondents' answers.
- Focus reminder contacts on comparison groups with too few responses.

## Number of Interviews

- In a study that interviewed people with similar backgrounds, new themes almost all appeared within the first 12 interviews, and the main themes were already visible after 6 (Guest, Bunce, Johnson 2006).
- When several groups with different backgrounds exist, set the number of interviews for each group separately.

## Question Design

- Ask one thing per question. Split "Are the cost and the timeline appropriate?" into two questions.
- Use one scale across the whole assignment. The default is a 5-point scale with a text label on every point.
- Offer "not applicable" and "don't know" as separate options outside the scale. Count these two options separately from scale scores in the analysis.
- Using means and mean-comparison tests on Likert scale scores does not change practical conclusions much (Norman 2010). Reporting the top-two-box share alongside the mean also reveals items where responses split to both ends.
- Build priority questions as "choose your top 3." Ranking every item burdens respondents more as the number of items grows. The results of a top-3 choice fit into one bar chart of selection shares.
- As response burden grows, more respondents stop thinking carefully and pick the same number repeatedly (Krosnick 1991). Split grid questions into short blocks.
- Asking the same respondent about both cause and outcome can make the two answers look more strongly related than they are (Podsakoff et al. 2003). Obtain outcome measures from objective data or from other respondents. If the same respondent must answer both, place the two items in different sections and guarantee anonymity.
- Keep only the open-ended questions that have a coding scheme in the analysis plan.
- Pretest by having 3-5 people similar to the target read the items aloud and answer them, and look for items they interpret differently. This number is a default of this skill, and the purpose of the pretest is to check comprehension.

## Design Check

- Does every item link to a row of the analysis plan?
- Was the sample size set by the decision question that requires the largest sample?
- Are target response counts set for each comparison group?
- Do items that share a chart use the same scale and direction?
- Are "not applicable" and "don't know" separated from the scale?
