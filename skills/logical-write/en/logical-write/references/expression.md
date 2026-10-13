# Formulaic phrasing and meta commentary

> Translated from the Korean original. See the translation notice in SKILL.md. The example phrases are English renderings of Korean patterns.

Both are judged by the same question. When deleting an expression costs the reader no information, delete it. The rules in this file do not touch style choices such as sentence length, linking expressions, ending style, macro structure, or length.

## Empty expressions

### Filler connectors

Expressions that are empty but pad the text or pretend to connect it. Delete them and go straight to the content.

| Type | Example | Handling |
|---|---|---|
| Context labels | "In this context", "considering the context", "from this perspective" | Delete and go straight to the content |
| Evasive implication | "This has significant implications", "this offers implications", "this is meaningful" | State the specific implication or delete |
| Declared importance | "What matters is", "the notable point is", "the key here is", "what I want to stress is" | Delete and let the content carry it |
| Announced steps | "First we look at A", "next, analyzing B", "finally, to sum up" | Delete and go straight to the content |
| Declared scope | "This text covers X", "the scope of this analysis is" | Delete and go straight to the content |

Use "context" and "implication" only where they carry a precise meaning.

### Excess modifiers and evaluative words

| Type | Example | Handling |
|---|---|---|
| Empty intensifiers | very, quite, extremely, really, like crazy, particularly (when overused), true, virtually, substantially | Delete or state the specific degree |
| Exclamatory evaluation | excellent, outstanding, groundbreaking, innovative, historic, astonishing, insightful | Replace with specific grounds |
| Exaggerated qualifiers | enormous, explosive, dramatic, unprecedented, first-ever, radical | Replace with specific figures or a comparison point |
| Undeniability claims | "It cannot be denied that", "it is clear that", "it is self-evident that" | Delete and state the fact itself |

### Stacked hedges

Uncertainty expressions piled up in one sentence or adjacent sentences, as in "a quite, somewhat, rather positive change seems to have occurred". State the uncertainty once and delete the rest.

### Abstract repackaging

Wrapping clear content in an abstract noun through "Y called X" or "X as Y". Y adds no information and only lengthens the sentence. Delete "called [abstract noun]" or "as [abstract noun]" and use X directly, or rebuild the particles.

| Before | After |
|---|---|
| a single mechanism called token prediction | token prediction |
| under the goal called cost reduction | to reduce costs |
| amid the great tide called digital transformation | as digital transformation proceeds |
| carrying the task called AI adoption | during AI adoption |
| the essential value called productivity gains | productivity gains |
| the language model as a single prediction task | the language model predicts the next token |
| AI as a means of organizational innovation | organizational innovation using AI |

### Declarative definition lists

Lining up facts the reader already knows as "X is Y" in place of analysis and judgment. Sometimes it detours through noun phrases without predicates.

| Before | Problem |
|---|---|
| The essence is next-token probability prediction | Wraps a known fact in "essence" to pass it off as new |
| The structure is transformers and attention | Repeats a textbook definition without analysis |
| Training consists of pretraining and alignment stages | Mechanically repeats the same "X is Y" frame |
| Capabilities and limits arise together from the principle | Ends with a declaration and no concrete explanation |
| Use of attention and input context | Presents a noun phrase without a predicate as if it were analysis |
| Capabilities and limits stemming from the principle | Lists a symmetric pair such as "capabilities and limits" to avoid specifics |

- (Test) When deleting the sentence costs the reader no understanding, it applies.
- (Paragraph test) Even when each sentence seems informative, it applies at paragraph level when the whole paragraph only restates textbook-level known facts.
- (Handling) Delete definitions the reader knows and fill the space with analysis or judgment the reader lacks.
- (Detour detection) Block "Y called X" and it moves to "X as Y". Block that and it moves to an "X's Y" noun phrase or an "X is Y" declaration. Judge by whether information is added, not by the surface form.

## Formulaic LLM rhetoric

| Pattern | Example | Handling |
|---|---|---|
| Contrast emphasis | "not merely A but B", "not A but true B", "not A but B", "beyond A to B", "not stopping at A but B" | Drop the negate-then-assert frame and state B directly |
| Repeated frames | "X is ... Y is also ... Z too is ..." | Vary the structure |
| Dramatic fragments | "Innovation. That is it." | Rebuild as a complete sentence |
| Staccato rhythm | "Fast. Accurate. Efficient." | Merge into content-centered sentences |
| Self-posed questions | "Why did this happen? Because" | Delete the question and state the answer |
| Overgeneralized implications | "This signals a paradigm shift for the entire industry" | Narrow the conclusion to the scope of the evidence |
| Vague partial assessments | "Half right", "largely agreeable" | State the range of agreement and disagreement specifically |
| Meta-emphasis clichés | "To put it strongly", "the point is", "one thing to note", "to draw a line here" | Delete |

### Symbol overuse

The habit of handing the decision about sentence structure to a symbol.

| Symbol | Overuse | Allowed when | Handling |
|---|---|---|---|
| Em dash | Inserting a phrase without settling the sentence structure | Never | Rebuild with sentence splits, parentheses, or commas |
| Colon | Replacing a clause with a label such as "Conclusion:" or "Key point:" | Introducing a real list or a formal quotation. The user's notation guidelines take priority when they differ | Delete a colon that opens a single clause and write a sentence |
| Semicolon | Joining sentences instead of splitting them, avoiding a structural decision | Joining closely related independent clauses reads naturally. The user's notation guidelines take priority when they differ | Split or rebuild the sentence |
| Ellipsis | Staging a dramatic pause or a pensive mood | Marking omissions in a quotation | Delete and complete the sentence |
| Bold inside sentences | Bolding keywords everywhere for emphasis | Terms being defined, technical identifiers, and other targets the reader scans for | Delete emphasis bold |
| Decoration | Emoji, decorative symbols, decorative dividers | Never | Delete |
| Three-item comma lists | Forcing items into threes out of habit regardless of content | The real number of items is three | Match the count to the content. Two items stay two, four stay four |

When colons, semicolons, and ellipses average more than one per 150 words, the density is too high and needs cutting. Punctuation limits also follow the common notation in `sentence.md`.

## Tautology and circularity

Drawing a conclusion from itself without grounds.

| Type | Example | Handling |
|---|---|---|
| A because A | "Improvement is needed, so improvement is required" | Add specific grounds or delete |
| Restated purpose | "The system exists to be used", "the budget is allocated to be spent" | State the specific use or delete |
| Empty obligation | "It is judged that we should", "it is judged that review in this direction is needed" | State a concrete action or condition |
| Circular definition | Reusing the defined concept in its definition | Rebuild the definition from outside grounds |

## Count announcements and tier modifiers

- Do not announce a count before the content. This covers "three major strategies", "four measures", "five key tasks", "seven directions", "three promises", and "two axes". List the content directly without announcing the count.
- A count that emerges naturally from the listed items is fine ("split into short, medium, and long term").
- Rewrite needless tier modifiers such as "triple structure", "four-tier architecture", or "six-layer module stack" as concrete content.

## Structural monotony

| Type | Description | Handling |
|---|---|---|
| Repeated heading labels | Generic labels such as "Overview", "Background", "Current status", "Conclusion" repeated | Rename with keywords reflecting the content |
| Repeated subheading labels | Empty labels such as "(Explanation)", "(Reason)", "(Claim)", "(Evidence)" repeated | Rename with keywords carrying real content |
| Fixed syntax | The same subject-predicate pattern three or more times in adjacent sentences | Vary the structure |
| Listing compulsion | Plain lists repeated with no relation between adjacent items | Give items relations such as cause, elaboration, or contrast |
| Bold subheading overuse | Bold subheadings attached mechanically to every item | Attach them selectively where needed |

## Missing grounds

| Type | Example | Handling |
|---|---|---|
| Conclusion without grounds | "AI adoption will revolutionize productivity" | Add specific grounds or a source |
| Figures without sources | "The market is expected to grow 30%" | State the source or delete |
| Authority in place of argument | Concluding from the name of a famous institution alone | Present real grounds in addition to the authority |
| Generalization without cases | "Global companies have all adopted AI recently" | Name specific cases or narrow the scope |

## Meta commentary

### Definition

Meta commentary is a sentence about something outside the body: the text itself, the writing process, the writer's inner state, the interaction with the user, or the tools used. The writer reports, justifies, previews, or looks back on their own actions. Reverse statements the user did not request (counterexamples, reverse logic, reverse rules, explanations of what falls outside) are also meta commentary, because they move the counterexample checks and boundary checks the writer did while reasoning into the output and expose that internal verification. A response should read as the information itself. Write so the reader does not see the text as a text, the writer as a writer, or the writing process.

### Tests

Every sentence must pass the tests below before output. When any test flags a sentence, delete it or replace it with content. Apply the subject test first because it is the most mechanical, then the other four.

- (Subject test) The sentence is meta commentary when its real subject, stated or implied, is the text itself ("this report", "this analysis", "this section"), the writer ("I", "as a result of my analysis"), the act of writing ("looking at", "reviewing", "to summarize"), the user's request ("as you requested", "regarding your question"), or the tools and methods used.
- (Deletion test) The sentence is meta commentary when deleting it costs the reader no information.
- (Beneficiary test) The sentence is meta commentary when the writer is its beneficiary (self-justification, self-protection, self-promotion).
- (Service test) The sentence is meta commentary when it performs only a service ritual, such as a greeting, praise, confirmation, guidance, or prompting, with no information.
- (Request direction test) The sentence is meta commentary when it covers an opposite polarity, a complement, or a substitute the user did not request. Opposite polarity means adding direction B after being asked for direction A. Complement means defining or choosing A and then adding everything outside A. Substitute means being asked for a feature that supplements X and then adding a rule that replaces or forbids X. Reverse sentences carry information and pass the deletion test easily, so judge them by whether they match the direction of the request.

### Why it appears

LLMs produce meta commentary for the purposes below. None serves the reader.

- (Padding) Filling space when the content runs short
- (Avoiding structure) Previewing "first A, then B" instead of structuring the content directly
- (Spreading responsibility) Disclaiming quality in advance with "this may not be perfect"
- (Winning goodwill) Managing the relationship with "I hope this helps"
- (Staging authority) Declaring the quality of the work with "after thorough analysis"
- (Confirming the request) Proving the instruction was followed with "as you requested"
- (Leaking internals) Exposing the writer's systems, limits, instructions, tools, or working process that the reader does not even know exist, which confuses the reader
- (Leaking verification leftovers) Moving counterexample checks, boundary checks, and comparisons of alternatives made while reasoning into the output, which widens the text beyond the request. The deeper the reasoning, the more internal checks there are and the more often they leak

### Types

The types below are examples and the list is open-ended. A sentence outside the list is still meta commentary when a test flags it. The handling is the same for all: delete the meta commentary and go straight to the content.

1. (Self-reference) "This report analyzes X", "the purpose of this text is", "this section covers Z", "as mentioned above", "putting the above together", "explained in detail below"
2. (Previews and recaps) "First we will look at A and then analyze B", "we have now looked at A", "in conclusion", "to summarize", "now to the main point"
3. (Echoing the request) "As you requested", "as you said", "to answer your question", "having reviewed the material you provided", "having checked the file you uploaded", "following the conditions you set"
4. (Boasting and completion reports) "After thorough analysis", "reviewed from various perspectives", "after close review", "the analysis is complete", "the summary is done", "analyzing from multiple angles"
5. (Exposed reasoning) "After considering several possibilities", "after looking from various angles", "after careful thought", "comparing A and B, I judged B suitable", "I considered several alternatives, but"
6. (Restating known facts) Textbook definitions of what the reader already knows in this context. For readers of an AI report, "AI stands for artificial intelligence"; for readers of a strategy report, "SWOT means strengths, weaknesses, opportunities, threats"
7. (Exposing methods and tools) "Confirmed through web search", "calculated by running code", "classified by the MECE principle", "written in a pyramid structure", "applying the skill". Allowed when the user explicitly asks about methods or tools
8. (Self-justification) "Classifying systematically", "a classification that covers everything without omission", "from a balanced perspective", "judging objectively", "evaluating fairly", "strictly speaking"
9. (Calling attention and declaring importance) "Notably", "the key here is", "what I want to stress is", "what matters is", "what deserves particular attention", "what should not be overlooked", "what you must know". When content matters, the reader sees it in the content
10. (Pre-emptive disclaimers and exposed limits) "This may not be perfect", "a more detailed analysis may be needed", "the limits of this analysis include", "further expert review is needed", "this analysis reflects current conditions and may change". Allowed when the user asks for limits or when a major uncertainty materially affects the reliability of the information
11. (Greetings and relationship management) "I hope this helps", "let me know if you have more questions", "great question", ritual "thank you"
12. (Transitional rhetoric) "Now moving to the next topic", "in this regard", "additionally" used only to transition, "based on this" without a real link, "meanwhile" without a real contrast
13. (Advertising ability and conditional offers) "I can explain in more detail if needed", "further analysis is possible if you wish", "I could also put this in a table", "if you need more specific examples"
14. (Guessing the reader's state) "This may be confusing", "this may be hard to understand", "this may be unfamiliar", "as you may already know", "as you may have expected", "you may have wondered", "this may seem odd"
15. (Staged emotion) "Unfortunately", "fortunately", "interestingly", "surprisingly", "naturally", "worryingly", "encouragingly"
16. (Repeated summaries) Re-summarizing what was already written: "to recap", "summing up the above", "all in all", "to stress once more", "to repeat", "as I said"
17. (Rating difficulty) "This problem is quite complex", "simply put", "in plain terms", "to simplify", "it is complex, but the gist is". Writing the content plainly is enough
18. (Reporting work order) "I first checked A, then reviewed B, and finally analyzed C", "step one collected data and step two ran the analysis"
19. (Reporting choice reasons) "The reason I chose A among several methods", "adopting C instead of B", "the background for choosing this approach". State why A or C fits directly
20. (Reporting search steps) "Having looked into it", "according to what I found", "having checked", "looking at the material", "search results show", "having reviewed the literature"
21. (Managing expectations) "This may differ from what you expected", "the result may be unexpected", "this may not be a simple answer"
22. (Declaring intent) "To communicate clearly", "to aid understanding", "to avoid confusion", "organized in a table for readability", "to make comparison easier"
23. (Explaining the output form) "Summarized in the table below", "can be classified as follows", "arranged chronologically as follows", "visualized as a chart"
24. (Confessing scope) "This goes beyond the original scope, but", "this is incidental, but", "for reference", and, without a user request, "this time I will only cover A" or "B needs a separate analysis"
25. (Directing the reader) "Please note", "please be careful", "please consider", "please keep in mind", "please check"
26. (Agreement and approval) "Good approach", "right direction", "sound judgment", "you pinpointed it", "correct" used only to agree
27. (Reporting self-correction) "Correction", "to revise what I said earlier", "on second thought". Write only the corrected content
28. (Reporting obstacles) "Accurate data was hard to find, but", "material is limited, but", "little information is public", "within the accessible material"
29. (Over-declaring assumptions) "I will assume A" for a self-evident premise, "under the premise B" for a premise the user already set. A non-obvious numerical assumption that affects the result ("at an exchange rate of 1,300 won") is content
30. (Over-explaining sources) "According to a report from a trustworthy institution", "according to research in a prestigious journal", "a credible survey". The reader judges credibility from the source name
31. (Empty context declarations) Declaring context with no specifics: "considering the current situation", "given recent trends", "amid global changes", "in response to the demands of the times". When specifics follow, delete only the declaration
32. (Summary after a list) After listing items, "As shown, various factors such as A, B, and C exist" or "we have reviewed various aspects as above"
33. (Redefining the subject) "What is digital transformation?", "let us first define the concept", "to clarify the definition" for a concept obvious to the reader
34. (Exposing the comparison) "Comparing A and B", "contrasting the two", "performing a comparative analysis"
35. (Reporting a change of view) "Approaching from another angle", "looking at it differently", "reinterpreting from the demand side", "taking a macro view"
36. (Overused conditional reservations) "Of course this assumes A, B must also be considered, and C is a variable, but the conclusion is D", "one cannot be certain, but", "it is too early to say, but"
37. (Tautological lead-ins) The second half of "The key is A. Explaining A," and of "In short, B. Looking at B in detail,"
38. (Writer-only information) Internal information the reader cannot and need not know: "since my training data cutoff is 2025", "my training data does not include this", "given context window limits", "the token limit makes it hard to cover everything", "according to the system prompt", "per your settings", "combining three search results", "cross-checking two sources", "several skills were applied to this task", "processed by loading the skill", "recorded in the state file", "calculated with a script", "I cannot check directly, but", "I cannot access real-time information", "within the scope of my knowledge", "within my ability". Judge by whether knowing it helps the reader decide or understand. Allowed when the user explicitly asks about internal methods, limits, or tools
39. (Commenting on tone) "To be honest", "to put it carefully", "to be blunt", "was that too stiff?", "to put it in friendly terms", "to put it gently"
40. (Reporting guesses about intent) "It seems you want", "I understood that you intend", "it seems you are curious about", "if what you want to know is". Infer intent silently and show only the result
41. (Announcing attempts) "Let me try", "I will give it a go", "let me approach this", "let me write this"
42. (Checking rituals) "Did you see that?", "does that make sense?", "how is it?", "is this part right?", "may I interpret it this way?", "did I understand correctly?"
43. (Unrequested reverse statements) Adding the opposite polarity, complement, or substitute of what was requested. Examples: answering a request to add feature Y that supplements X with "use Y by default and never use X", following a statement in direction A with responses for the opposite direction B, defining A as distinct from B, C, D, and E and then listing why B, C, D, and E are not A, or deriving SO strategies from a SWOT analysis and then adding the factors of ST, WO, and WT strategies. Use reverse checks only for internal verification and write only results in the requested direction

### Detours

Blocking direct meta commentary produces detours. The tests look at function, not surface, so they catch detours too.

- (Hidden subject) Dropping the subject or using the passive: "summarizing the results", "the review findings are as follows", "according to what was investigated", "the conclusion drawn", "the status identified", "the items confirmed". When the restored subject is the writer, it is meta commentary.
- (Disguised as content) Mixing a little content into meta commentary. From "After reviewing from various perspectives, A fits", keep only "A fits". "Through thorough analysis we concluded B" and "after comprehensive consideration we propose plan C" work the same way.
- (Disguised as modesty) Posing as humble: "though lacking, to summarize", "for what it is worth", "though the information is limited", "judging cautiously". When the writer benefits (disclaimer, goodwill), it is meta commentary.
- (Disguised as questions) Wrapping it in a rhetorical question: "So how should we approach this?", "why did this result occur?", "what is the key?". Delete the question and state the answer.
- (Disguised as connectors) Shrinking meta commentary into a connector attached to a content sentence: "As we saw above, A is B", "putting this together, C fits", "based on the above analysis, we propose D". Delete only the connector part.

### First and last sentences

- Start with content. Do not start with a greeting, an echo of the request, or a preview.
- End with content. Do not end with a greeting, an invitation to ask more, or a disclaimer.

### When it is allowed

- The user explicitly asks for it (for example, "state the purpose of this report at the start")
- Genre conventions require it, as in the purpose and method sections of an academic paper
- The user explicitly asks for limits, cautions, or an explanation of methods

## Examples

### Formulaic rhetoric and count announcements

```markdown
Before
## Three core strategic directions
- Not mere technology adoption but digital transformation in the true sense is needed
    + Why is this transformation needed? Because the limits of the old way are obvious
- This signals a paradigm shift for the entire industry and will truly be a game changer
    + Innovation. That is the key.
- The three core strategies are as follows
    + First, strengthen digital capabilities
    + Second, build a data-driven decision system
    + Third, innovate the organizational culture

After
## Direction for digital transformation
- (Digital capability) Staff technical skills built in stages through training that reflects field needs
    + Larger scale of transition support programs considered to cut initial adoption costs
    + On-the-job application tasks after training to connect learning to work
- (Data-based decisions) Data collection and analysis introduced per work process to move from experience-based to data-based decisions
    + Linked analysis of data from existing production management and enterprise resource systems prepared first
    + Data analysis results scheduled as a regular agenda item in decision meetings
- (Culture shift) Cross-department collaboration set up during the transition to raise acceptance of change
    + Pilot tasks make success cases visible and raise acceptance in stages
    + Evaluation bonus points for joint cross-department tasks
```

Removed from the original: the count announcement ("three core strategic directions"), contrast emphasis ("not mere A but true B"), the self-posed question, exaggerated change phrases ("paradigm shift", "game changer"), the dramatic fragment ("Innovation. That is the key."), and the empty intensifier ("truly").

### Meta commentary in a conclusion

```markdown
Before
## Implications
- Based on the above analysis, we derived the following implications
- In conclusion, the late-stage funding gap in the domestic startup ecosystem is structural
    + As we saw above, investment is increasingly concentrated in early stages, and in this way various factors interact
    + Of course one cannot be certain, but if the trend continues more companies will drop out at the growth stage
- We reviewed various aspects as above, and the limits of this analysis include restricted access to data on unlisted companies
    + Further expert review is needed, so please note this
    + I hope this helps

After
## Closing the late-stage funding gap for startups
- The late-stage funding gap in the domestic startup ecosystem is structural
    + Concentration of investment in early stages cuts off funding paths for later stages
    + More companies expected to drop out at the growth stage if the trend continues
- New tax incentives for private investors joining late-stage rounds need review
    + A dedicated growth-stage investment track after early rounds would clarify funding paths by stage
    + Growth-stage investment records to be considered in public fund-of-funds allocation reviews
```

Removed from the original: self-justification, explanation of the output form, recaps, connector disguises, the summary after a list, overused conditional reservations, pre-emptive disclaimers, directions to the reader, and the greeting.

## Checklist

- Are filler connectors, empty intensifiers, and exclamatory evaluations absent?
- Are uncertainty expressions not stacked in one sentence?
- Is there no abstract repackaging where Y in "Y called X" adds nothing?
- Did you avoid lining up known facts as "X is Y"?
- Is formulaic rhetoric such as contrast emphasis, self-posed questions, and dramatic fragments absent?
- Are em dashes, dramatic ellipses, emphasis bold, and overused colons and semicolons absent?
- Are "A because A" tautologies and empty obligations absent?
- Are count announcements absent?
- Does no syntactic pattern repeat three or more times in a row?
- Are headings and subheadings free of repeated empty labels?
- Do conclusions and claims have grounds, and do figures have sources?
- Are sentences whose subject is the text, the writer, the writing, the request, or the tools absent?
- Are sentences that benefit the writer, or that only perform service rituals, absent?
- Are sentences on opposite directions, complements, or replacement rules the user did not request absent?
- Are detours such as hidden subjects, disguised content, modesty, questions, and connectors absent?
- Do the first and last sentences carry content?
- Does the text read without awkward rhythm when read aloud?
