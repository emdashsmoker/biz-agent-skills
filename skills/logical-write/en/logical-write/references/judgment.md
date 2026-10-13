# Reaching conclusions

> Translated from the Korean original. See the translation notice in SKILL.md.

Between opposing positions, reach a conclusion in one direction according to the quality of the evidence.

## The problem

On topics where two positions clash, LLMs tend to give both sides equal weight and replace the conclusion with "both sides have a point". Such text does not help the reader decide. The causes below all serve the writer's self-protection and have nothing to do with the reader's needs.

- (Risk avoidance) Taking a side might be wrong, so both sides get equal space to spread the risk of error
- (Keeping goodwill) Backing one side might upset readers on the other, so the writer poses as neutral
- (Hiding shallow analysis) When the writer cannot weigh the evidence, listing both sides stands in for analysis

## Principles

End every analysis with a conclusion that has a direction.

- When the qualitative weight of the evidence tilts, conclude in the direction of the qualitatively stronger side.
- Judge the quality of evidence by logical soundness and causal explanatory power. Do not judge it by quantity.
- Acknowledge counterarguments and place them under the conclusion.
- Evaluate counterarguments in their strongest form. Beating a weakened counterargument does not produce a conclusion.
- "Both sides are valid" is the absence of a conclusion.

## Fence-sitting tests

The output is fence-sitting when any of the tests below applies.

### Test 1: Missing conclusion

When the expressions below sit where the conclusion should be, the conclusion is missing. The same expression is fine as a side condition or reservation after a conclusion has been stated.

| Type | Expression | Problem |
|---|---|---|
| Partial agreement | "Half right", "half right and half wrong" | Does not say which part is right and which is wrong |
| Partial agreement | "Has a point" | Does not say which argument has a point, and gives no direction |
| Partial agreement | "Largely agreeable", "partly valid" | Does not state the range of agreement |
| Partial agreement | "Not wrong", "cannot be called entirely wrong" | Avoids the conclusion through double negation |
| Both-sides | "Both sides have a point", "each has pros and cons", "each has merits and demerits" | Accepts both sides equally without weighing them |
| Both-sides | "Positive and negative aspects coexist" | Hides the assumption that the two aspects weigh the same |
| Both-sides | "Both an opportunity and a crisis", "two sides of the same coin", "a double-edged sword", "light and shadow coexist", "could be medicine or poison" | Replaces analysis with metaphor |
| Suspended judgment | "It depends on the situation", "it depends on the case", "it may vary with context" | Does not say which direction applies in which situation |
| Suspended judgment | "Hard to say for sure", "not easy to conclude" | Refuses to judge, or does not say why it is hard |
| Suspended judgment | "Too early to tell", "premature to judge" | Pushes the judgment to an unspecified future |
| Fake compromise | "Combine the strengths of both", "harmonize the two views" | Gives no method for combining or harmonizing |
| Fake compromise | "A balanced approach is needed", "find the right balance" | Does not define "balance" or "right" |
| Fake compromise | "The middle way is needed" | No grounds that the midpoint is correct |
| Evasive ending | "A comprehensive judgment is needed", "a careful approach is needed", "a multi-angle review is needed", "in-depth discussion is needed" | Gives no result or direction for the judgment, approach, review, or discussion |
| Evasive ending | "Ongoing monitoring is needed" | Gives no criteria for what monitoring should decide |
| Evasive ending | "Further research is needed" | Does not say which research would enable which conclusion |
| Shifting responsibility | "Left to the reader's judgment", "each should decide for their situation", "ultimately a personal choice" | Hands the writer's duty to conclude over to the reader |

### Test 2: Equal allocation

When the length, number of grounds, and strength of modifiers given to two opposing positions are deliberately equal, the structure is fence-sitting. Placing asymmetric evidence symmetrically erases the analysis and leaves a display of evidence.

### Test 3: Repeated reservation

When reservation expressions ("hard to say for sure", "too early to tell", "further review is needed", "we need to look from various angles") appear twice or more, the text is evading. State uncertainty once.

### Test 4: Fake compromise

Presenting the arithmetic midpoint of two positions as the conclusion is a variant of fence-sitting. The midpoint between A and B is not automatically correct, and its validity needs its own grounds. "Combining the strengths of A and B is desirable" is a fake compromise when it lacks a method and grounds for the combination.

### Test 5: Quantity trap

Weighing positions by the number of grounds, length, citation counts, or number of supporters is the quantity trap. It is the opposite error to fence-sitting, but it is the same lack of analysis because it ignores the quality of evidence.

- "Three times as many studies support A as B, so A is right"
- "The report on A runs 800 pages and the report on B 50 pages, so A is more solid"
- "More experts support A, so A is the accepted view" (also an appeal to the crowd)

When the numerically weaker position is stronger in logical soundness and causal explanatory power, conclude in its direction.

## Rules for reaching a conclusion

### Rule 1: Evaluate the quality of evidence first

Before concluding, evaluate the evidence for each position in the order below. When a higher criterion decides the matter, conclude in that direction regardless of the lower criteria. When you find the defects listed for a criterion, lower the weight of that evidence. For the meaning of each defect, see `logic.md`.

| Rank | Criterion | Question | Defects that lower the weight |
|---|---|---|---|
| 1 | Logical soundness | Is the path from premises to conclusion free of errors? | Circular reasoning, formal fallacies (affirming the consequent, denying the antecedent), straw man, false dilemma, covert redefinition |
| 2 | Causal explanatory power | Does it explain "why" in concrete terms? | False cause, ignoring a common cause, reversed causation, oversimplification. Evidence that shows only correlation without a causal path ranks below evidence that explains the path |
| 3 | Resistance to counterexamples | Does the position hold against known counterexamples? | Dismissing counterexamples as "exceptions" or "special cases" and narrowing the definition, cherry-picking, survivorship bias |
| 4 | Rigor of empirical method | Are data collection and sample design appropriate? | Hasty generalization, sample bias, base rate neglect. Representativeness matters more than sample size, and a well-designed small study outranks a biased large survey |
| 5 | Fit of scope | Does the evidence fit the scope under discussion? | False analogy, fallacy of composition, fallacy of division |

Exclude the following from the weighing. They all measure quantity, and quantitative superiority does not prove qualitative superiority.

- (Number of grounds) The count of arguments, studies, or reports supporting a position
- (Length of grounds) Page counts or volume of supporting literature
- (Number of supporters) The count of experts, institutions, or respondents who agree. Majority agreement does not decide truth.
- (Citation counts) How often a position is cited. Citation frequency shows influence and does not prove validity.
- (Number of authorities) The count of authorities supporting a position. Check separately whether each authority has expertise in the field.

### Rule 2: Take the counterargument in its strongest form

- When you evaluate the opposing position, take its strongest form.
- When you restate a counterargument, keep its core arguments.
- First build "the most persuasive version of the opposing position", then weigh that version.
- The conclusion earns trust only when it holds after you grant the strongest grounds of the counterargument.
- Even when you must reach a one-sided conclusion, do not shrink the counterargument. Review it fully and then judge whether one side still prevails.

### Rule 3: Place the counterargument under the conclusion

Place counterarguments under the conclusion so they only adjust its strength. Placing them at the same level as the conclusion restores the fence-sitting structure. Acknowledging a counterargument raises the credibility of the conclusion.

```markdown
- (Conclusion) Direction A fits
    + (Grounds) Evidence supporting A
    + (Counterargument and limits) The main argument for B is X, but it is limited by Y
```

### Rule 4: Conditional conclusions are allowed

When the conclusion depends on a condition, state the condition and keep the direction. A conditional conclusion is a conclusion. A reservation without direction is the absence of a conclusion.

- (Allowed) "On current evidence A fits, but review again if condition X changes"
- (Not allowed) "A may be better, or B may be better, so decide based on the situation"

### Rule 5: Accept asymmetry

The two positions may get different amounts of space. When the evidence is asymmetric, asymmetric writing is natural. Padding the weaker position to balance the text distorts the analysis.

## Conditions for withholding a conclusion

Withhold a conclusion only when all three conditions below hold. If any one fails, conclude according to the weight of evidence.

- (Symmetric lack of evidence) Both sides lack empirical evidence, so neither direction can be weighed. The reason for withholding is the lack of evidence on both sides.
- (Stated reason) State concretely which evidence would allow a conclusion. "A comprehensive judgment is needed" is not allowed. "Once we have survey Y on X, we can conclude A or B" is allowed.
- (Direction of the tilt) Even when withholding, state which way the current evidence leans ("Current evidence leans toward A, but the conclusion is withheld for lack of data X"). Only a perfect balance exempts you from stating the tilt.

## Examples

### Technology choice

```markdown
Before
## Cloud versus on-premises
- Cloud has low upfront investment and scales easily
    + Lower operational burden favors small organizations
- On-premises offers strong data control and stable long-term costs
    + Suits organizations with strict security requirements
- Each has pros and cons, so choose according to the organization's situation

After
## Cloud-first build for new information systems at small firms
- Cloud fits new information systems at small firms with fewer than 100 employees
    + Low upfront investment eases the financial burden of firms with limited capital
    + Outsourcing operations is a realistic option where in-house IT staff are hard to hire
    + Capacity grows with the business without extra equipment investment
- Data-control concerns can be managed through the choice of service
    + A domestic-region service with recognized security certification secures data location and security management
    + Finance and healthcare firms whose data location is restricted by law to consider a hybrid setup that keeps some systems on their own equipment
```

The revised text narrows the target to "small firms with fewer than 100 employees" to set the scope of the weighing. Within that scope the evidence for cloud prevails, so the conclusion goes that way. The core argument for on-premises, data control, is acknowledged as a counterargument under the conclusion, and the excepted industries are stated as a condition that bounds the conclusion.

### Quality of evidence over quantity

```markdown
Before
## Direction for public agency performance evaluation
- Many grounds support keeping quantitative evaluation
    + Many institutional documents assume quantitative evaluation, including Ministry A's performance guidelines (120 pages), Agency B's audit standards (80 pages), and Ministry C's evaluation manual (200 pages)
    + 68% of agencies prefer keeping quantitative evaluation
- Relatively few grounds support expanding qualitative evaluation
    + Some academic studies argue that quantitative indicators fail to reflect real performance
- Given the many institutional grounds and agency preferences, keeping the quantitative system fits

After
## Larger share for qualitative evaluation in public agency performance reviews
- The current quantitative system focuses on measurable indicators and opens a gap between real performance and evaluation results
    + Work that indicators miss, such as policy planning and stakeholder coordination, drops out of evaluation and weakens the incentive to invest in it
    + Goal displacement, where hitting the indicator becomes the goal, reported in several agencies
- The counterargument that the current system is widely established and costly to change is valid, but establishment alone does not prove the system right
    + Raising the qualitative share in stages lowers the transition cost while improving how well real performance is reflected
    + Results of each stage reviewed to set the share for the next stage
```

The original concludes from quantity: number of documents, page counts, and the share of agencies preferring the system. The preference share is an appeal to the crowd. The revision rests on the mechanism by which indicators miss real performance and on the counterexample of goal displacement. Even after granting the strongest opposing argument, establishment and transition cost, the causal explanation prevails, so the conclusion favors more qualitative evaluation.

### When withholding is allowed

```markdown
Before
## Commercialization timing of new material X
- Forecasts for the commercialization of new material X split between within three years and after ten years
- Both sides have their grounds, so it is hard to say for sure at this point
- Ongoing monitoring is needed

After
## Commercialization timing of new material X
- Current evidence cannot fix the commercialization timing of new material X
    + The within-three-years side cites improving lab yields, but estimates of mass-production yield vary widely across studies
    + The after-ten-years side cites engineering barriers in converting production equipment, but no empirical data rules out overcoming them
- Current evidence leans toward after ten years
    + The gap between lab-scale yield and the yield mass production requires is large, with no precedent for closing such a gap in a short time
    + Timing estimate to be reassessed once continuous-production results from a pilot line are available
```

The revision meets all three conditions: evidence is lacking on both sides, pilot-line results are named as the deciding evidence, and the tilt toward after ten years is stated. Withholding is therefore allowed.

## Checklist

- Does the output end with a conclusion that has a direction?
- Are missing-conclusion expressions such as "both have pros and cons" absent?
- Did you avoid forcing equal length onto two opposing positions?
- Do reservation expressions appear no more than once?
- Did you avoid presenting the midpoint of two positions as the conclusion without grounds?
- Is the counterargument placed under the conclusion?
- Did you avoid weakening or distorting the counterargument, and did you keep its core arguments?
- Does the conclusion hold after weighing the strongest form of the counterargument?
- If you withheld the conclusion, are all three conditions met and is the tilt stated?
- Did you avoid deciding the direction by the number of grounds, length, citation counts, or number of supporters?
- Did you evaluate evidence in the order of logical soundness, causal explanatory power, resistance to counterexamples, rigor of empirical method, and fit of scope?
- Did you separately verify the logical soundness of the numerically stronger position's evidence?

## When these rules do not apply

- When the user explicitly asks for a balanced summary, such as "summarize both positions" or "summarize neutrally", do not force a conclusion.
- For legal issues without settled case law, the reservation "interpretation under current law is not settled" is allowed regardless of the conditions. Still state the tilt by separating the majority and minority views.
- When a decision maker asks for a comparison of options, give a recommendation as the conclusion and state that the final choice belongs to the decision maker.
