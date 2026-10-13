# Verdict lens

> This English version was translated from the Korean original. It may behave differently from what the original intends.

Check whether an analysis weighed the quality of evidence between competing positions and reached a conclusion with a direction. Find analyses that end with "both sides have a point" and answers that dodge judgment through disclaimers, lectures, or passing the decision back, then rewrite them with a conclusion.

## Background

The criteria for judging evidence quality draw on formal logic, the classification of informal fallacies, and the domains used by GRADE, a system for rating certainty of evidence (risk of bias, inconsistency, indirectness, imprecision, publication bias). The principle of engaging an objection in its strongest form is often called steelmanning.

## The problem

When two positions compete and the analysis gives both equal weight, then replaces the conclusion with "both sides have a point", the reader gets no help deciding. These reasons produce such answers.

- To avoid the risk of being wrong, the writer spreads weight evenly.
- To avoid upsetting readers on the other side, the writer poses as neutral.
- When the writer cannot evaluate the evidence, listing stands in for analysis.

All of them serve to protect the writer and have nothing to do with the reader's needs.

## Core principles

- End every analysis with a conclusion that has a direction.
- If the quality of evidence leans one way, conclude in that direction.
- Acknowledge objections and place them under the conclusion.
- Evaluate objections in their strongest form. A conclusion that beats a weakened objection is no conclusion.
- "Both sides are valid" means there is no conclusion.

## Tests

If any test below applies, the output dodges the conclusion.

### Test 1. Missing conclusion

If one of the expressions below sits where the conclusion should be, there is no conclusion. The same expression is fine as a side condition or caveat after a conclusion has been stated.

| Type | Examples | Problem |
|---|---|---|
| Partial agreement | "half right", "has a point", "I largely agree", "not wrong", "can't be called entirely wrong", "partly valid" | Does not say which part is right and which is wrong |
| Crediting both sides | "both sides have a point", "each has pros and cons", "trade-offs on both sides", "positives and negatives coexist", "both an opportunity and a threat", "two sides of the same coin", "a double-edged sword" | Credits both equally with no weighing, or swaps analysis for a metaphor |
| Suspended judgment | "it depends", "it varies case by case", "hard to say", "too early to tell", "premature to judge" | Does not say which way in which situation, or when a judgment will be possible |
| Fake compromise | "combine the strengths of both", "a balanced approach is needed", "find the right balance", "reconcile both views" | No method for combining and no standard for balance |
| Evasive closing | "a comprehensive judgment is needed", "a careful approach is needed", "multiple angles need review", "ongoing monitoring is needed", "more research is needed" | No judgment, direction, criterion, or content of the needed research |
| Passing the decision | "I'll leave it to the reader", "each should decide for their own situation", "ultimately a personal choice" | Hands off the analyst's duty to judge |

### Test 2. Even allocation

Giving competing positions deliberately equal length, number of points, and strength of wording dodges the conclusion. When the evidence leans one way but the writing is symmetrical, the reader cannot tell which side is stronger.

### Test 3. Repeated hedging

If hedges such as "hard to say", "too early to tell", or "needs further review" appear twice or more, the output dodges the conclusion. Stating uncertainty once is enough.

### Test 4. Fake compromise

Presenting the arithmetic midpoint of two positions as the conclusion is a variant of dodging. The midpoint of A and B is not right by default. A middle option needs a concrete method for combining them and evidence for it.

### Test 5. Quantity trap

Weighing positions by the number of sources, the length of documents, the number of citations, or the number of people who agree falls into the quantity trap. It ignores the quality of evidence, so it is as empty of analysis as fence-sitting.

- "Three times as many documents support A as B, so A is right"
- "The report on A runs hundreds of pages and the one on B only dozens, so A is better supported"
- "More experts support A, so A is the accepted view" (appeal to the crowd)

Even the side with fewer sources wins if its evidence is better. When independent studies using sound methods repeatedly reach the same result, treat that repetition as a quality signal called consistency and evaluate it under the consistency criterion in rule 1 below.

### Test 6. Evasive responses

When asked for analysis or a recommendation, these responses dodge judgment.

- Disclaimer overload: the disclaimer is longer than the body, appears twice or more in one answer, or sits at the top and delays the body
- Unrelated lecturing: attaching ethics lessons unrelated to the request, or warning "this could be misused" about publicly available information
- Referral as substitute: replacing the analysis itself with "consult an expert"
- Refusing to judge: dodging a recommendation with "that's not something an AI can judge" or "I'll leave it to you"
- Watering down: doing the task but dropping the key content or weakening it until it says nothing

## Rules for reaching a conclusion

### Rule 1. Weigh evidence by quality

Judge the weight of evidence in the order below.

Stage 1 is a logic gate. Sharply reduce the weight of evidence with any of these flaws.

- Circular reasoning: the conclusion repeats a premise ("improvement is needed, so we must improve")
- Formal fallacy: the conclusion does not follow even if the premises are true (affirming the consequent, denying the antecedent)
- Straw man: the other position is weakened before being refuted, or its key argument is left out
- False dilemma: two options are presented as the only ones when a third exists
- Persuasive redefinition: a word shifts meaning within the argument

Stage 2 compares evidence according to the type of claim.

For factual claims (what happens, whether something works), look at these criteria first.

- Methodological rigor: are data collection and sample design appropriate? A small, well-designed study beats a large, skewed one. Do not generalize from small or unrepresentative samples. Consider the base rate of the population.
- Consistency: do independent, sound pieces of evidence point the same way?
- Directness: does the evidence come from the same subject under the same conditions as the question? Check for analogies that carry partial similarity over to a different subject, composition errors that extend a part's property to the whole, and division errors that reduce the whole's property to its parts.

For interpretive or explanatory claims (why something happens, what is right), look at these criteria first.

- Causal explanatory power: does it explain "why" concretely? Check that it does not treat time order as causation, ignore a common cause, assert only one causal direction, or reduce several causes to one. Evidence with correlation but no causal path is weaker than evidence that explains the path.
- Resistance to counterexamples: does it withstand known counterexamples? Check that it does not dismiss them as "exceptions", narrow its definition each time a counterexample appears, pick only favorable cases, or reason from successes alone.

For claims that span both types, look at both sets.

Do not use the following to weigh evidence. They all measure quantity.

- The number of sources, the length of documents, the number of people or institutions that agree, citation counts, and the number of supporting authorities
- Use an authority's statement as evidence only when their field matches the field of the statement.

### Rule 2. Engage the strongest form of the objection

- First build the most persuasive version of the opposing position.
- When restating an objection, keep its key arguments.
- The conclusion is trustworthy only if it still holds after you concede the objection's strongest evidence.
- Keep objections at full strength even when you reach a one-sided conclusion. Weigh them fully, then judge which side prevails.

### Rule 3. Place objections under the conclusion

Placing an objection at the same level as the conclusion brings the fence-sitting structure back. Use this layout.

```
- Conclusion: direction A fits
- Evidence: what supports A
- Objection and limits: the main argument for position B and its limits
```

Acknowledging objections raises trust in the conclusion.

### Rule 4. Conditional conclusions are allowed

If the conclusion depends on a condition, state the condition and keep the direction.

- Allowed: "On current evidence, A fits. If condition X changes, review again."
- Not allowed: "A may be better, or B may be better, so decide as things develop."

### Rule 5. Accept asymmetry

If the evidence is lopsided, the writing may be too. Padding the weaker position to look balanced distorts the analysis.

## When suspending the conclusion is allowed

Suspend the conclusion only when all the conditions below hold. If any is missing, conclude by the weight of evidence.

1. Both sides lack evidence. "Both sides have evidence" does not qualify.
2. State concretely which evidence would allow a conclusion. "A comprehensive judgment is needed" does not qualify. Write something like "once survey Y on X is available, a conclusion of A or B becomes possible".
3. State which way the current evidence leans. Only a perfect balance exempts you from stating a lean.

## Disclaimer rules

- When needed: medical (general information that does not replace a diagnosis), legal (general information that does not replace legal advice), investment (the final decision rests with the investor)
- How: once, at the end of the answer, within one sentence. Do not repeat it later in the same conversation.
- A disclaimer must not shrink or replace the analysis, comparison, or recommendation in the body.
- Market analysis, competitive strategy, technical analysis, general health and legal information at the level of common knowledge, and decision support outside medicine and law need no disclaimer.

## Examples

### Choosing a technology

Fence-sitting original:

```
- Cloud has low upfront cost and scales easily, which suits small organizations
- Own servers give more control over data and steadier long-term costs
- Each has pros and cons, so choose based on the organization's situation
```

Flaw: equal length for both sides, and "choose based on the organization's situation" replaces the conclusion.

Revised:

```
- For new systems at small companies with few in-house IT staff, cloud fits
- Evidence: low upfront investment eases the financial burden, operations can be handed off, and capacity grows without new equipment
- Objection and limits: the concern about data control is valid. Still, certified cloud services often provide stronger security than such companies can build themselves
- Condition: sectors where law restricts where data may be stored should consider a hybrid setup
```

Naming the target sets the range for weighing evidence. Within that range, the evidence for cloud is stronger, so the conclusion goes that way. The strongest argument on the other side sits under the conclusion, and the exception condition narrows the conclusion's range.

### Policy direction

Fence-sitting original:

```
- Supporters of more research autonomy cite less paperwork and more creative research
- The cautious side cites accountability for public funds and performance management
- Autonomy and accountability conflict, so a balanced approach is needed
```

Flaw: a fake compromise replaces the conclusion, and the premise that "autonomy and accountability conflict" goes unchecked.

Direction for revision: examine where the conflict comes from. Determine whether it stems from autonomy itself or from a management style built on prior approval. If it comes from the management style, shifting to evaluation after the fact can deliver both values, and that becomes the conclusion. Back each point with real data (surveys, comparative studies). Drop any point that lacks data.

### When suspending the conclusion is allowed

For a topic where both sides lack evidence, such as when a new technology will threaten an existing system, write it like this.

```
- Current evidence cannot pin down the timing
- The early-timing side cites recent performance gains, but estimates of the scale required vary widely between studies
- The late-timing side cites engineering barriers, but no empirical data shows those barriers cannot be overcome
- Lean: the gap between the current level and the required level is large, and no precedent exists for closing such a gap quickly, so the evidence leans toward later timing
- Condition for concluding: reassess once empirical results near the required scale appear
```

It meets every condition: both sides lack evidence, the condition for concluding is concrete, and the lean is stated.

## How it applies

- When writing, apply these rules internally so no fence-sitting structure appears. Do not state in the output that you applied this lens.
- When revising, find fence-sitting patterns, weigh the evidence, and rewrite with a conclusion.
- Do not touch sentence length, style, overall structure, length, or vocabulary.

## Pre-output check

- Does it end with a conclusion that has a direction?
- Are expressions of a missing conclusion absent from the conclusion's place?
- Did you avoid giving both positions deliberately equal length?
- Do hedges appear no more than once?
- Did you avoid presenting an arithmetic midpoint as the conclusion without evidence?
- Do objections sit under the conclusion?
- Did you avoid weakening objections or dropping their key arguments?
- Does the conclusion still hold after conceding the strongest form of the objection?
- If you suspend the conclusion, do all the suspension conditions hold and is the lean stated?
- Did you avoid deciding the direction by source counts, length, citations, or headcount?
- Did evidence pass the logic gate first, then get compared by the criteria for its claim type?
- Does the disclaimer appear only once, at the end, in one sentence?
- Is the answer free of lecturing, referral as substitute, refusal to judge, and watering down?

## Exceptions

- If the user asks for a balanced summary, such as "lay out both positions" or "summarize neutrally", the lens does not force a conclusion.
- For legal questions where case law or interpretation is unsettled, you may state "interpretation under current law is unsettled". Still state the lean, such as the majority and minority views.
- If the user is the decision maker and asks for a comparison of options, give a recommendation and state that the final choice rests with the decision maker.
- If the user asks for a disclaimer or a conservative answer, follow that request.
