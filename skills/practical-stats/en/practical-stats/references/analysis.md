# Processing and Analysis

## Processing

Irregular data take a different shape in every assignment, so one fixed piece of code rarely handles them. Handle processing with judgment rules and apply the rules with code.

### Procedure

- Keep the raw data unchanged and work on a copy.
- The model reads the table structure (merged cells, multi-row headers, unit rows, total rows) and drafts a tidying plan.
- Apply the plan to the first few rows and check the result before applying it to the whole table.
- Compare the row count, column count, and totals before and after to check for losses and duplicates.

### Processing Log

Record every judgment in the format below.

| No. | Target | Judgment | Applied rule | Affected cases | Change in conclusion |
|-----|--------|----------|--------------|----------------|----------------------|
| 1 | Item 7 | Move "other" answers that mean the same as an existing option into that option | If the answer text contains an option name, move it to that option | 14 | None |

In the change-in-conclusion column, state whether the main results change without the rule. If they change, confirm with the user.

### Missing Data

- Code nonresponse, not applicable, and don't know differently.
- Leave missing data blank. If imputation is necessary, record the method and the number of cases, and report the results before imputation as well.
- State the number of valid responses for each item as the denominator in result tables.

### Outliers

- Separate input errors (unit mix-ups, digit errors) from genuine extreme responses. Correct input errors when there is evidence, and record the correction.
- Keep genuine extreme responses and look at median-based results as well. If including or excluding extreme responses changes the conclusion, report both results.

### Low-Quality Responses

- Set the criteria before looking at the results.
- This skill's default criteria are responses that give the same number to every item in a grid, responses completed in less than one third of the overall median time, and responses with contradictory answers.
- Only flag such responses in the raw data. Compare results with and without them, and report the number excluded.

### Coding Open-Ended Answers

- Write a code, a definition, and a typical example for each entry in the coding scheme. One answer may receive several codes.
- When a language model codes the answers, have a person recode a randomly chosen part and check agreement. Revise the definition of any code with repeated disagreements and code again.
- Report the number and share of respondents mentioning each code. The denominator is the number of respondents who wrote an open-ended answer.

### Unit Alignment

- Align currency units, currencies, base years, and aggregation periods (annual, monthly), and record the conversion formulas in the processing log.

## Analysis

Choose the analysis method by the question type in the analysis plan. When the basic method answers the question, add no more complex method.

### Choosing the Analysis

| Question type | Basic method | Reported numbers | Chart |
|---------------|--------------|------------------|-------|
| Level | Share, mean, median | Share with Wilson confidence interval, mean, median, interquartile range | Horizontal bar, histogram |
| Comparison | Comparison methods below | Difference, confidence interval, effect size | Horizontal bar |
| Change | Paired comparison for the same units, group comparison for different units | Amount of change, confidence interval | Vertical bar, line |
| Relationship | Spearman correlation, cross-tabulation | Correlation coefficient, row shares | Scatter plot, stacked bar |
| Priority | Selection share, importance-performance analysis, Borich needs score, analytic hierarchy process | See references/survey-types.md | Bar, four-quadrant scatter plot |

Report confidence intervals and margins of error as population estimates for probability samples. For non-probability samples, follow the rules in references/reporting.md.

### Comparison Methods

- (Shares of two groups) Report the difference in shares with its 95% confidence interval. Test with a chi-square test, and use Fisher's exact test when any cell has an expected count below 5.
- (Means of two groups) Use Welch's t-test (Delacre et al. 2017). Use the same method whether or not the variances are equal. Report Cohen's d as the effect size.
- (Means of three or more groups) Use Welch's ANOVA (Delacre et al. 2019). When the groups differ, run Welch's t-test for each pair and apply a multiple comparison correction.
- (Skewed numbers) Treat a variable as skewed when the absolute skewness is 1 or more. This threshold is a default of this skill. For skewed numbers, report the median difference with a bootstrap confidence interval (Hesterberg 2008). The default bootstrap uses 2,000 resamples and a fixed random seed.
- (Likert items) Mean comparisons are acceptable (Norman 2010). Report the difference in top-two-box shares as well.
- (Two items from the same respondents) Compute the confidence interval of the difference with a paired bootstrap at the respondent level.

### Multiple Comparisons

- As the number of comparisons grows, the chance of a significant result by luck grows.
- When the analysis plan specifies several comparisons in advance, correct them with the Benjamini-Hochberg method (Benjamini & Hochberg 1995).
- Mark comparisons absent from the analysis plan as exploratory results, whether or not they are corrected.

### Interpretation Criteria

- A p-value shows how far the data depart from a specified assumption. A p-value does not show the probability that a hypothesis is true or the size of an effect (Wasserstein & Lazar 2016).
- Build conclusions around effect sizes, confidence intervals, and sample sizes, and report p-values as supporting numbers.
- Set the threshold for a practically meaningful difference (for example, 5 pp or more) at the decision question stage.
- Describe relationships from a single-time-point survey as associations. A causal statement requires time order, a review of other explanations, and a mechanism.
- When a decision rests on a pooled result, check that the main comparison groups show the same direction. When group composition differs, the pooled result and the group results can point in opposite directions.
- The before-and-after change of units selected for unusually low or high scores includes movement back toward the mean even without intervention (Barnett et al. 2005). Compare it with the change in units that were not selected.

### Weighting

- When the respondent profile differs from a known population profile (company size, region, and so on), compute results both with and without post-stratification weights.
- Post-stratification weight = share of the group in the population ÷ share of the group in the sample
- If both results lead to the same conclusion, report the unweighted result and keep the weighted result in the processing log. If the conclusions differ, report both.

## Measurement Quality

- (Cronbach's alpha) α = k ÷ (k − 1) × (1 − Σ item variances ÷ variance of the total score), where k is the number of items (Cronbach 1951).
- (Tier agreement rate) Number of proposals given the same tier by two reviewers ÷ total number of proposals
- (Intraclass correlation) When every reviewer rates every proposal, compute ICC(2,1) = (BMS − EMS) ÷ (BMS + (k − 1) × EMS + k × (JMS − EMS) ÷ n) (Shrout & Fleiss 1979). BMS is the mean square between proposals, JMS the mean square between reviewers, EMS the residual mean square, k the number of reviewers, and n the number of proposals.
- (AHP consistency ratio) CR = CI ÷ RI, with CI = (λmax − n) ÷ (n − 1). λmax is the largest eigenvalue of the pairwise comparison matrix, and n is the number of compared items.
- (Random index RI) For n = 3, 4, 5, 6, 7, 8, 9, RI is 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45 respectively (Saaty 1980).

## Computation Rules

- Compute every number with code and keep the code files with the outputs.
- Print denominators and missing counts in result tables.
- Fix the seed for any computation that uses random numbers.
- Record the names and versions of the libraries used.

| Computation | Function |
|-------------|----------|
| Confidence interval for a share | `statsmodels.stats.proportion.proportion_confint(method="wilson")` |
| Confidence interval for a difference in two shares | `statsmodels.stats.proportion.confint_proportions_2indep` |
| Chi-square test, Fisher's exact test | `scipy.stats.chi2_contingency`, `scipy.stats.fisher_exact` |
| Welch's t-test | `scipy.stats.ttest_ind(equal_var=False)` |
| Welch's ANOVA | `statsmodels.stats.oneway.anova_oneway(use_var="unequal")` |
| Skewness | `scipy.stats.skew` |
| Bootstrap confidence interval | `scipy.stats.bootstrap` (`paired=True` for same-respondent comparisons) |
| Spearman correlation | `scipy.stats.spearmanr` |
| Multiple comparison correction | `statsmodels.stats.multitest.multipletests(method="fdr_bh")` |
| Power and sample size | `statsmodels.stats.power` |
