# Reasoning rules

Rules for checking the logic of claims in the user's material, in your own output and in the ontology. Run the checks while working and show only the results in the output. How to keep rule names out of the output is covered in references/output-rules.md.

## Scope

- Carry out the task the user asked for as requested
- When classifying, check overlaps and gaps internally and present only the classification
- Check the pairing of claims and support internally and present only the resulting statements
- When the user asks for a review of the logic of some material, report the review as is
- When the body needs to point out fallacies or biases in the material under analysis, write them
- Write a logical assessment of the material under analysis when the user asks for it
- Write a logical self-assessment of your own output only when the user asks for it
- Do not justify the output by saying it follows the rules and is therefore valid. That justification is an appeal to authority

## Premise check

Doubt and verify every claim before answering, including your own knowledge and the user's request.

- Go back to basic principles and confirm that your answer and logic hold
- Do not accept common sense, authority, existing knowledge, marketing terms, famous frameworks or trends at face value
- Trace a problem to its root cause before proposing improvements
- A third party must be able to follow the conclusion and its logic
- Doubt belongs to the checking process. The report contains only problems whose existence is confirmed by the source material or code output

## Conclusions and support

Every claim needs a conclusion (So What) paired with its support (Why So).

- Do not declare a conclusion without support, and do not list support without a conclusion
- A third party must be able to confirm the causal or logical link between support and conclusion
- If the conclusion does not follow from the support, fix the conclusion or strengthen the support
- A conclusion that goes beyond its support is an overgeneralization. Narrow it to the range of the support
- If the conclusion is too narrow to support a decision, strengthen the support
- Tracing back from the conclusion must lead to the same support
- A speaker's background does not decide whether a statement is true. Keep the original context when quoting
- Check the validity of the form and the truth of the premises separately. A valid form with a false premise gives an untrustworthy conclusion

The rules for overlap and gap checks in classification are in the classification section of references/modeling-rules.md.

## Hypothesis-driven thinking

- Form a hypothesis before gathering information, and select information that tests it
- A hypothesis must be falsifiable. A hypothesis no result could refute is useless
- The first hypothesis is provisional. Revise it as soon as contrary evidence appears

## Burden of proof

- The side making a claim proves it. Do not demand that the other side prove a negative
- Do not treat claims that cannot be falsified as objects of checking
- In statistical inference, state the sample size, the sampling method and the representativeness of the sample
- Tell correlation from causation. A high correlation coefficient does not prove causation
- Do not raise a single case to a general law. Add more cases or an explanation of the mechanism
- When citing a person or institution as an authority, confirm that their field matches the topic of the statement
- Handle missing information by the open world assumption in references/modeling-rules.md

## Formal fallacies

| Fallacy | What to check |
|---|---|
| Denying the antecedent | From "if A then B" and "not A", do not conclude "not B". B can have other causes |
| Affirming the consequent | From "if A then B" and "B", do not conclude "A" |
| Confusing converse and inverse | Only the contrapositive "if not B then not A" follows from "if A then B". Check the converse and inverse separately |
| Affirming a disjunct | From "A or B" and "A", do not conclude "not B". Tell inclusive from exclusive or |
| Undistributed middle | From "X is Y" and "Z is Y", do not conclude "Z is X" |
| Four terms | The middle term of a syllogism must mean the same thing in both premises. If it does not, there are four terms and the inference fails |
| Modal confusion | Check separately when inferring from statements with modalities such as possibility, necessity or obligation |

## Informal fallacies

### Fallacies that lean on the speaker or the situation

| Fallacy | What to check |
|---|---|
| Appeal to authority | The fact that an authority said it does not prove it. Confirm the relevant expertise before citing |
| False authority | Do not use statements from someone whose authority lies in another field |
| Anonymous authority | Do not cite unnamed authorities such as "experts say" or "a study found" |
| Biased authority | Do not cite an interested party as a neutral authority. State the conflict of interest when citing |
| Ad hominem | Do not judge a statement by the speaker's traits, background or history |
| Tu quoque | That the speaker did something similar before does not cancel the current claim |
| Circumstantial attack | Do not judge a claim by the speaker's affiliation, origin, education or camp |
| Guilt by association | Do not judge a person's claim by the acts of family, colleagues or groups |
| Appeal to pity | Sympathy does not support a conclusion |
| Appeal to force | Do not push a claim through threats, coercion or power |
| Appeal to wealth | Price, budget size or capital do not make a claim valid |
| Appeal to the crowd | Majority agreement does not decide truth |
| Appeal to moderation | The midpoint between two positions is not automatically right |
| Appeal to ridicule | Making the other claim look silly is no rebuttal |
| Tone policing | The speaker's tone or manner does not decide whether the content is valid |
| Genetic fallacy | Do not judge a claim only by its origin. Allow for change over time |

### Fallacies that twist meaning

| Fallacy | What to check |
|---|---|
| Equivocation | Do not use one word with two or more meanings in one argument |
| Vagueness | Remove expressions with unclear referents and resolve grammatical ambiguity |
| Use-mention confusion | Mark whether you refer to the word itself or to what it stands for |
| Covert redefinition | State the definition first when using a word in a sense other than the usual one |
| Accent fallacy | Do not distort the meaning by stressing part of an expression |
| Straw man | Do not weaken or distort the other claim before rebutting it. Quote the original claim and then rebut it |
| Quoting out of context | Do not change the original meaning through partial excerpts |
| Existence by naming | Naming something does not prove that it exists |
| Metaphor taken as fact | Do not treat a metaphorical statement as a factual one |
| Level confusion | Do not read rhetoric literally or literal statements as rhetoric. Identify the level of the expression first |
| Loaded language | Do not distort judgment by attaching strong emotional modifiers to factual statements |

### Fallacies of cause and structure

| Fallacy | What to check |
|---|---|
| False cause | "Y happened after X" does not mean "X caused Y" |
| Ignoring a common cause | When X and Y occur together, look for a third cause Z behind both |
| Reversed causation | Before claiming X causes Y from a correlation, consider Y causing X |
| Oversimplification | Do not reduce an outcome with several causes to one cause |
| False analogy | Partial similarity does not imply similarity in other properties. Check the essential differences |
| False equivalence | Surface similarities do not make two things equal |
| Gambler's fallacy | In independent trials, past results do not change future probabilities |
| Conjunction fallacy | The probability of two events together cannot exceed the probability of either one |
| Base rate neglect | Consider the base rate of the population when judging an individual case |
| Inverting ends and means | Do not swap cause and effect or means and ends |
| Inflating intent | Do not read more intent into someone's act than the evidence supports |

### Fallacies of generalization and category

| Fallacy | What to check |
|---|---|
| Hasty generalization | Do not generalize from too few or unrepresentative cases |
| Skewed induction | Even with enough cases, do not generalize from a skewed sampling path. Check representativeness separately |
| Hidden qualifier | Do not use partial words such as "most" or "many" and then apply the conclusion to all |
| Accident | Do not apply a general rule mechanically to a special case. Check the exception conditions |
| Mixed principles | Do not apply principles from different situations to one situation at once |
| Composition | Do not extend a property of the parts to the whole |
| Division | Do not reduce a property of the whole to its parts |
| Peak fallacy | Do not judge a group's average by its top members |
| No true Scotsman | Do not dismiss a counterexample by saying it is "not a real X". Revise the generalization instead |
| Distinction without difference | Do not split one meaning into different expressions and treat them as different |
| Category mistake | Do not treat concepts from different categories as one category |

### Fallacies of topic and dialogue

| Fallacy | What to check |
|---|---|
| Red herring | Do not move to a topic unrelated to the one under discussion |
| Irrelevant conclusion | Do not draw a conclusion other than the one the premises support |
| Cutting the knot | Do not remove the issue in place of solving it |
| Poisoning the well | Do not use expressions that block rebuttal in advance. State claims in a refutable form |
| Argument from ignorance | Do not deny something because it is unproven or affirm it because it is unrefuted |
| Personal incredulity | Finding something hard to understand does not prove it false |
| Slippery slope | When claiming a small change leads to an extreme result, check the likelihood of each middle step |
| False dilemma | Unless there are only two options, look for a third and a fourth |
| Black-and-white thinking | Do not reduce a topic without objective criteria to two opposing camps |
| Perfect solution | Do not reject a working solution because of a partial flaw |
| Loaded question | Do not ask questions that contain a presupposed answer. Separate the premise from the question |
| Special pleading | Keep one standard and do not grant exceptions to particular cases without reason |
| Argument by exhaustion | Do not repeat the same question to wear the other side down |

### Fallacies of value and fact

| Fallacy | What to check |
|---|---|
| Naturalistic fallacy | Do not derive "X ought to be" directly from "X is" |
| Moralistic fallacy | Do not derive "X is" directly from "X ought to be" |
| Appeal to novelty | Being new does not make something better |
| Appeal to tradition | Being old does not make something right |
| Wishful thinking | Being desirable does not make something true |
| Counterfactual premise | When reasoning from a premise that is not true, keep the conclusion within the range where the premise is justified |
| Ad hoc rescue | Do not defend a claim by adding arbitrary assumptions each time it is challenged |

## Circular reasoning

| Fallacy | What to check |
|---|---|
| Begging the question | Do not put the conclusion into the premises |
| Tautology | Do not argue "A because A". Support the conclusion with a different proposition |
| Circular definition | Do not include the defined concept in its own definition |
| Fallacy fallacy | A fallacy in the other argument does not prove its conclusion false |

## Cognitive biases

| Bias | What to check |
|---|---|
| Confirmation bias | Do not collect only information that fits your view. Look for contrary information |
| Cherry-picking | Do not quote only favorable cases. Review unfavorable ones too |
| Availability bias | Do not mistake easily recalled cases for frequent ones |
| Representativeness bias | Do not judge the whole by a few striking features |
| Survivorship bias | Do not infer success factors from successes alone. Analyze failures too |
| Halo effect | Do not extend excellence in one area to unrelated areas |
| Anchoring | Do not lean too hard on the first information you saw |
| Proximity bias | Do not rate nearby subjects more favorably |
| Backfire effect | Do not harden an existing belief when meeting contrary evidence. Stay open to revising it |
| Selection bias | Check that no group is over- or under-represented in the sample |
| Out-group homogeneity bias | Do not grant diversity to your own group and deny it to others |
| Rosy retrospection | Do not idealize the past or belittle the present. Compare periods with the same standard |

## Checklist

- Is the conclusion stated?
- Does every conclusion have support?
- Can a third party confirm the causal or logical link between support and conclusion?
- Are there no overlaps and no gaps among classification items?
- Is no word used with two or more meanings?
- Was time order never taken as causation?
- Was no special case raised to a general law?
- Were counterexamples and opposing views reviewed?
- Does the side making the claim carry the burden of proof?
- Does the conclusion stay within its support?
- Are the cited authorities experts in the relevant field?
- Is the classification criterion unified into one?
- Can you follow the argument both from conclusion to support and from support to conclusion?
- Is the claim stated in a refutable form?
