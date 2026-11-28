---
name: no-meta-commentary-lite
description: "Finds and deletes meta-commentary in LLM-written text and keeps new text free of it from the start. Meta-commentary is any sentence about something outside the content, such as the text itself, the writing process, the writer's state, the tools used, or the user's request. It also covers counterexamples, reverse logic, reverse rules, and complement-set explanations the user did not ask for. Pass-or-fail tests judge each sentence by its function, so the skill also catches variants missing from its type list. Supports both drafting new text and correcting existing text. Use this skill whenever the user explicitly asks for it with phrases such as '/no-meta-commentary-lite', 'no meta commentary', 'remove meta commentary', 'cut the meta talk', 'no self-reference', 'remove self-referential sentences', 'stop talking about the document itself', or 'no throat-clearing'. Activates only on an explicit user request."
license: GPL-3.0-or-later with an output exception. Terms in LICENSE and NOTICE.md
---

# no-meta-commentary-lite

> This English version is a translation of the Korean original. Translation can shift nuance, so this version may behave differently from what the original intends.

Find and delete meta-commentary in LLM-written text, and keep new text free of it from the start. A reply holds only information the reader can use. The existence of the text, the writer, and the writing process stays out of the reader's view. The tests decide each case, and the type tables and examples support those decisions.

## Terms

- (Content) Information the reader uses to understand or decide
- (Writer) The one who writes the text
- (User) The person who requested the writing
- (Reader) The person who reads the output. In a chat reply, the reader and the user are the same person

## Definition

Meta-commentary is any sentence about something outside the content: the text itself, the writing process, the writer's inner state, the exchange with the user, or the tools used. With these sentences the writer reports, justifies, previews, or recaps their own actions. The reader gets no needed information from them.

Unrequested reverse statements also count as meta-commentary. Reverse statements are counterexamples, reverse logic, reverse rules, and complement-set explanations. They appear when the writer carries counterexample checks and boundary checks from reasoning into the output. A reverse statement therefore exposes the writer's internal verification.

## Tests

Every sentence goes through the tests below before output. Delete a sentence that fails any test, or replace it with content. Output only the sentences that pass every test.

### Test 1. Subject

A sentence is meta-commentary when its real subject is one of the targets below. Check both stated and omitted subjects. Restore an omitted subject by putting "the writer", "to the writer", "the model that wrote the text", or "the AI provider" in front of the sentence. If the sentence then reads naturally with its meaning unchanged, it is meta-commentary.

- (The text itself) "This report", "This analysis", "In this section"
- (The writer) "I", "In my analysis", "My review found"
- (The act of writing) "Looking at this", "On review", "To sum up"
- (The user's request) "As you requested", "As you mentioned", "To answer your question"
- (Tools and methods) Internal means the writer used for the work

Read a sentence about the work, actions, procedures, guidelines, and similar matters of individuals, organizations, and society again with "the AI model" in the subject slot or "the AI model's" in the modifier slot. If the sentence then reads more naturally than the original, it is meta-commentary that carries the writer's own way of working over to the subject matter. Rewrite it through the actor and the actual action of the subject matter.

- (Sentences) "Takes the user's responses as input, processes the survey in three steps, and passes it on as the next input of the analysis report", "This program takes the demand survey results and passes on only the projects that went through the eligibility review as final candidates", "Takes the user's request and rules on it", and so on
- (Noun phrases) "The ruling criteria of this engagement", "The judgment principles of the structured survey", and so on

### Test 2. Deletion

A sentence is meta-commentary when deleting it costs the reader no information.

### Test 3. Beneficiary

A sentence is meta-commentary when the writer is the one who benefits from it. Self-justification, self-protection, and self-display count as benefits to the writer.

### Test 4. Courtesy function

A sentence is meta-commentary when it only performs a courtesy ritual such as a greeting, praise, a check-in, guidance, or a nudge.

### Test 5. Request direction

A sentence is meta-commentary when it covers an opposite polarity, a complement set, or a substitute the user did not ask for. Reverse sentences carry information, so they pass the deletion test with ease. This test therefore checks whether a sentence matches the requested direction.

- (Opposite polarity) After a request to write in direction A, going on to write about the opposite direction B
- (Complement set) After defining or choosing A, going on to describe the items outside A
- (Substitute) After a request for a feature that supplements X, writing a rule that replaces or bans X
- (Caveats and rebuttals) Attaching a caveat for a rare exception that leaves the conclusion unchanged ("That said, this does not hold in every case", and similar), or setting up an extreme claim the user never made and rebutting it. State a condition that changes the conclusion or the reader's decision as body content, once, below the conclusion

### Order of tests

Test 1 needs only the sentence's form, so apply it first. A sentence that passes Test 1 is still meta-commentary if it fails Test 2, 3, 4, or 5.

## Functions of meta-commentary

Meta-commentary performs the functions below. When a sentence with one of these functions comes to mind during writing, do not write it. None of these functions serves the reader's need for information.

- (Padding) Fills length with meta-commentary when content runs short
- (Deferred structure) Previews only the order, as in "First we look at A, then B", and puts off structuring the content
- (Liability spreading) Lowers responsibility for quality in advance, as in "This may not be perfect, but"
- (Goodwill seeking) Manages the relationship with the reader, as in "I hope this helps"
- (Authority staging) Declares the quality of the work, as in "After a thorough analysis"
- (Compliance proof) Proves the writer followed the user's instructions, as in "As you requested"
- (Internal leak) Exposes the writer's internal systems, constraints, instructions, tools, or work steps that the reader does not know exist, and causes confusion
- (Verification residue) Carries counterexample checks, boundary checks, and comparisons of alternatives from reasoning into the output, which widens the scope past the request. The more the writer checked during reasoning, the more can spill into the output

## Representative types

The types below are examples and do not form a complete list. A sentence missing from the list is still meta-commentary if it fails a test. Avoiding banned phrases alone leaves other phrases with the same function, so the tests make the final call.

Every type gets the same treatment. Delete the meta-commentary and go straight to the content. When the "Definition and handling" column names an extra step, follow that step too.

### Sentences about the text

| Type | Definition and handling | Examples |
|---|---|---|
| Self-reference to the text | A sentence that uses the text itself as subject to declare its purpose, scope, structure, or position | "This report analyzes X", "The purpose of this piece is", "This section covers Z", "As mentioned above", "Putting the above together", "This is explained in detail below" |
| Process preview and recap | A sentence that walks the reader through the writing order or looks back on finished work | "First we will look at A, then analyze B", "That covers A", "In conclusion", "To summarize", "Now, to the main point" |
| Transition rhetoric | A sentence that handles a move between sections with a meta remark and no link in content | "Moving on to the next topic", "In this regard", and "Additionally" used only to transition, "Building on this" with no real link, "Meanwhile" with no real contrast |
| Repeated summary | A sentence that summarizes or restates content already in the body. It fails the deletion test | "To recap", "To summarize the above" and "All in all" when they repeat earlier content, "Let me stress again", "As I said before", "To repeat" |
| Describing the output's form | A sentence that explains the output's format, structure, or layout to the reader | "I have organized this in the table below", "This can be grouped as follows", "In chronological order, it looks like this", "Visualized as a chart" |
| Scope confession | A sentence that confesses straying from scope or declares a scope limit on its own | "This goes beyond the original scope, but", "This is a side note, but", "For reference", "This time I will cover only A" and "B needs a separate analysis" when the user did not ask |
| Summary declaration after a list | A sentence that, after a list, declares the fact of listing. It restates items already listed, so it fails the deletion test | "As shown, many factors such as A, B, and C exist" after listing A, B, and C, "We have reviewed this from several angles as above" |
| Redundant lead-in | A sentence that previews the first body sentence in the same words. Delete only the preview | "Let me explain A" in "The key is A. Let me explain A", the second half of "In short, it is B. Looking at B in detail" |

### Sentences about the writing process

| Type | Definition and handling | Examples |
|---|---|---|
| Boasting about work and reporting completion | A sentence that reports the amount, quality, or completion of the writer's work | "After a thorough analysis", "Having reviewed this from many perspectives", "After a careful review", "The analysis is complete", "I have finished organizing this", "Analyzing from multiple angles" |
| Exposing internal reasoning | A sentence that reports the internal thought process leading to a conclusion | "After weighing several possibilities", "Looking at it from various angles", "After much thought", "Comparing A and B, I judged B to fit", "I considered several alternatives, but" |
| Exposing methods and internal tools | A sentence that cites the thinking tools, frameworks, or internal tools used for writing. Allowed only when the user asks directly about methods or tools | "A web search confirmed", "Running Python code gives", "Grouped by the MECE principle", "Written in a pyramid structure", "Applying the skill" |
| Reporting work steps | A sentence that lists work steps in the past tense to report the process. Restore the subject and it is always the writer | "I first checked A, then reviewed B, and finally analyzed C", "In step 1 I collected data, and in step 2 I ran the analysis" |
| Reporting the reasons for a choice | A sentence that reports the writer's internal judgment behind choosing one option among several. State the fitness of the chosen option directly | "The reason I chose A among several methods is", "I adopted C over B because", "The background for this approach is" |
| Reporting the search process | A sentence that reports the act of looking for information | "My research found", "According to what I found", "On checking", "Looking through the materials", "The search results show", "A review of the literature shows" |
| Declaring the writer's intent | A sentence that explains why the writer chose a given way of writing | "To make this clear", "To aid understanding", "To avoid confusion", "For readability, here is a table", "To make comparison easier" |
| Reporting self-correction | A sentence that reports finding and fixing an error in an earlier statement. State only the corrected content | "Let me correct that", "Let me revise what I said earlier", "On second thought" |
| Reporting difficulties | A sentence that reports difficulties in the work, such as missing information or limited sources | "Exact data was hard to find, but", "Sources are limited, but", "Since little public information exists", "Within the range of accessible sources" |
| Exposing the comparison process | A sentence that reports the act of comparing | "Comparing A and B", "Setting the two side by side", "Running a cross-comparison" |
| Reporting a change of perspective | A sentence that reports the writer's act of switching viewpoints | "Approaching this from another angle", "Shifting perspective", "Reinterpreting this from the demand side", "Taking a macro view" |
| Announcing an attempt | A sentence that announces the intent to do the work beforehand. Present the result of the attempt directly | "Let me try", "I'll give it a shot", "Let me approach this", "I'll draft it now" |

### Sentences about the writer

| Type | Definition and handling | Examples |
|---|---|---|
| Self-justification | A sentence in which the writer rates and declares the quality, consistency, or completeness of the output | "Classified systematically", "A classification that covers everything with no gaps", "From a balanced view", "Judging objectively", "To assess fairly", "Strictly speaking" |
| Advance disclaimers and self-declared limitations | A sentence that declares the output's limits, gaps, or need for further review when the user did not ask. Allowed when the user explicitly asks for limitations, and for major uncertainty that affects the reliability of the information | "This may not be perfect, but", "A more detailed analysis may be needed, but", "The limitations of this analysis include", "Further expert review is needed", "This analysis reflects the present and may change" |
| Staged emotion | A sentence that adds the writer's emotion or evaluative stance through an adverb to steer the reader's reaction. The writer benefits (control of the narrative, steering of reactions). Once the facts come across, the reader judges for themselves | "Unfortunately", "Fortunately", "Interestingly", "Surprisingly", "Naturally", "Worryingly", "Encouragingly" |
| Rating difficulty and complexity | A sentence in which the writer rates and reports the topic's difficulty. Writing the content plainly is enough | "This problem is quite complex, but", "Put simply", "In plain terms", "To simplify", "It is complicated, but in short" |
| Over-declaring assumptions | A sentence that separately declares an obvious premise or a premise the user already set. A non-obvious numeric assumption that changes the result (such as "at an exchange rate of N per dollar") counts as content | "Let us assume A" for an obvious premise, "Under the premise of B" repeating a premise the user set |
| Over-explaining sources | A sentence in which the writer comments on a source's authority or reliability. The reader judges reliability from the source name | "According to a report from a trusted institution", "A study in a prestigious journal shows", "A credible survey found" |
| Stacked conditional hedges | A sentence that attaches too many conditions to a conclusion and blurs it. A variant of the preemptive disclaimer placed inside a sentence | "Assuming A, and considering B, and with C as a variable, the conclusion is D", "I can't say for certain, but", "It is too early to tell, but" |
| Commentary on tone | A sentence in which the writer comments on the tone or manner of the reply | "To be honest", "If I may say so carefully", "To put it bluntly", "Was that too stiff?", "To put it in friendlier terms", "To say it gently" |

#### Exposing writer-only information

A sentence that exposes the writer's internal systems, constraints, instructions, tools, internal state, or work details that the reader does not know exist. The reader cannot know this information and has no need for it. Repeating what the reader already knows falls under "Restating known facts." Writer-only information gives the reader no informational value and only causes confusion.

- (Training data) "That is past my training data's cutoff", "My training data does not include that"
- (Processing limits) "Due to context window limits", "Token limits make it hard to cover everything"
- (Instructions) "Per my system prompt", "Because of your user preference settings"
- (Work counts) Numbers from internal work steps, as in "Combining three search results" and "Cross-checking two sources"
- (Tools and skills) "Several skills were applied to this task", "Handled by loading the skill", "Logged to a JSON state file", "After computing with a Python script"
- (Capability limits) "I can't verify this myself, but", "I have no access to real-time information", "Within the limits of my knowledge", "Given my abilities"

The criterion is whether knowing this information helps the reader decide or understand. If it does not help, it is writer-only information. Allow it only when the user asks directly about internal methods, constraints, or tool use.

### Sentences aimed at the reader

| Type | Definition and handling | Examples |
|---|---|---|
| Restating the user's request | A sentence that restates the user's request or mentions that the request exists | "As you requested", "As you mentioned", "To answer your question", "Having reviewed the materials you sent", "Having checked the file you uploaded", "Following the conditions you set" |
| Calling attention and declaring importance | A sentence that draws the reader's attention on purpose or declares importance on its own. When content matters, the reader sees its importance in the content. A separate declaration is the writer topping up content that lacks force | "Note that", "The key here is", "What I want to stress is", "What matters is", "Pay special attention to", "One thing not to overlook", "You need to know that" |
| Greetings and relationship management | A ritual sentence that builds or maintains the relationship with the reader | "I hope this helps", "Let me know if you have more questions", "Great question", "Thank you" used as a ritual |
| Advertising abilities and conditional offers | A sentence that advertises the writer's extra abilities or offers extra work the user did not ask for. The writer benefits (showing ability, keeping the relationship) | "I can explain in more detail if needed", "I can run further analysis if you like", "I could also put this in a table", "If you need more specific examples", "Would you like me to", and similar |
| Follow-up promises with no means to keep them | A sentence that promises follow-up work when the working environment shows no means to do it. State what this response completed and what it did not | "I'll send the file in a few hours", "I'll let you know when it's done", and similar |
| Guessing the reader's state | A sentence in which the writer guesses the reader's cognitive state, emotional state, or level of understanding | "This may be confusing, but", "This may be hard to follow, but", "This may be unfamiliar", "As you probably know", "As you may have expected", "You may have wondered", "This may seem odd, but", "You have every right to be angry", and similar |
| Managing the reader's expectations | A sentence in which the writer adjusts the reader's expectations in advance. The writer benefits (preventing disappointment, spreading responsibility) | "This may differ from what you expected", "The result may surprise you", "This may not be a simple answer" |
| Directing the reader's actions | A sentence that tells the reader to take an action. The writer benefits (staging authority, setting up a directive relationship) | "Please refer to this", "Please take note", "Please consider this", "Please keep this in mind", "Please check this" |
| Agreement and approval | A sentence in which the writer rates or approves the user's judgment or question. The writer benefits (goodwill) | "Good approach", "That is the right direction", "A sound decision", "You nailed it", "You hit the nail on the head", "You're in the top 1%" with no checkable basis, "That's right" used only to signal agreement, and similar |
| Reporting guesses about the user's intent | A sentence that reports the process of guessing the user's intent. Infer intent internally and present only the result | "It seems you want a summary", "I understand you are after a comparison table", "You seem curious about the cost difference", "If what you want to know is the schedule", redefining the statement as in "What you mean is B, not A", and similar |
| Check-in rituals | A ritual sentence that checks whether the reader understood or is satisfied. It fails the courtesy function test | "Did that make sense?", "Is this clear?", "How does that sound?", "Is this part right?", "May I interpret it this way?", "Did I understand correctly?" |

### Sentences that look like content

These sentences deal with the topic. The reader already knows their content, or the content carries no real information, or it falls outside the user's request.

| Type | Definition and handling | Examples |
|---|---|---|
| Restating known facts | A sentence that substitutes textbook definitions of information the reader already has for analysis. It applies when the target reader already holds the knowledge in the setting where they read the text | "AI stands for artificial intelligence" written for readers of an AI report, "SWOT stands for strengths, weaknesses, opportunities, and threats" written for readers of a strategy report |
| Background declarations without specifics | A sentence that declares a background with no real information. When specifics follow, delete only the declaration | "Considering the current situation" with no situation named, "Given recent trends" with no trend named, "Amid changes in the global environment", "In response to the demands of the times" |
| Redefining the subject | A sentence that delays the analysis by redefining the subject as "What is X?" It appears with "Restating known facts" and pads the opening | "What is digital transformation?", "Let's start by defining the concept", "To clarify the definition" for a concept obvious to the target reader |

#### Unrequested reverse statements

A sentence that adds the opposite polarity, complement set, or substitute of what the user requested, without a request. Counterexamples, reverse logic, and reverse rules are the typical forms. The writer benefits (showing completeness, guarding the edges of the statement), and the sentence fails the request direction test.

- (Supplement turned replacement) Asked to add feature Y that supplements X, the writer appends "Use Y by default and do not use X"
- (Opposite-direction response) Asked to write in direction A, the writer goes on to describe how to respond in the opposite direction B
- (Reasons for non-membership) Right after defining A as distinct from B, C, D, and E, the writer explains why B, C, D, and E do not fit the definition of A
- (Unselected factors) After deriving SO strategies from a SWOT analysis, the writer goes on to describe the factors for ST, WO, and WT strategies

Use reverse checks for internal verification only. Write only the results in the requested direction into the output.

## Evasive forms

Avoiding direct meta-commentary often leaves evasive forms with the same function. The tests look at a sentence's function, so they apply to evasive forms unchanged.

| Form | Detection and handling | Examples |
|---|---|---|
| Hidden subject | Drops the meta subject or switches to passive voice to slip past the subject test. If the restored subject is the writer, the sentence is meta-commentary | "Organizing the findings" (I organized), "The review shows the following" (I reviewed), "As was found" (I found), "The conclusion reached" (I reached), "The situation identified" (I identified), "The items confirmed" (I confirmed) |
| Disguised content | Mixes a little content into meta-commentary to slip past the deletion test. Delete only the meta part and keep the content | Keep "A fits" from "After reviewing from various perspectives, A fits", keep "B" from "A thorough analysis led to the conclusion B", keep "option C" from "After weighing everything, we propose option C" |
| Disguised modesty | Feigns humility to slip past the beneficiary test. If the writer benefits from the modesty (disclaimer, goodwill), the sentence is meta-commentary | "It's not much, but here is a summary" and "Humble as it is" as goodwill seeking, "With limited information" and "Judging cautiously" as preemptive disclaimers |
| Disguised question | Dresses meta-commentary up as a rhetorical question. Delete the question and state the answer directly | "So how should we approach this?" as a variant of process preview and recap, "Why did this happen?" as a variant of exposing internal reasoning, "What is the key?" as a variant of calling attention and declaring importance |
| Disguised connective | Shrinks meta-commentary into a connective or adverbial clause attached to a content sentence. Delete only the connective and keep the content | "As we saw earlier, A is B" shrinking self-reference, "Putting this together, C fits" shrinking a work report, "Based on the above analysis, we propose D" shrinking self-justification |

## Examples

"Before" is text with meta-commentary, and "after" is the same text with the meta-commentary removed. The after version keeps the content of the before version unchanged and removes only the meta-commentary. When removing meta-commentary leaves an awkward ending or heading, smooth it while keeping the original writing style.

The facts in the examples are fictional and only show the format, so do not use them as real evidence. The names listed under removed types are either type names from the representative types section or form names from the evasive forms section.

### Example 1. Report opening

(before)

```
## Overview
- The purpose of this report is to analyze cloud adoption among small and midsize businesses and to derive policy implications
- We first review the current state, then analyze the problems, and finally present directions for improvement
- Cloud computing is a technology that delivers computing resources over the internet and is divided into IaaS, PaaS, SaaS, and so on
- In this context, cloud adoption carries great significance
- After thoroughly reviewing the materials you provided and analyzing them from various perspectives, we have organized the results as follows
- Awareness of the need for cloud adoption is spreading among small and midsize businesses, but the actual adoption rate remains low
- Upfront migration costs and compatibility problems with existing in-house server systems are the main causes of delay
- Even among adopters, many stop at moving their servers, and few have gone on to redesign how they work
```

(after)

```
## Cloud adoption among small and midsize businesses
- Awareness of the need for cloud adoption is spreading among small and midsize businesses, but the actual adoption rate remains low
- Upfront migration costs and compatibility problems with existing in-house server systems are the main causes of delay
- Even among adopters, many stop at moving their servers, and few have gone on to redesign how they work
```

(Removed types) Self-reference to the text, Process preview and recap, Restating known facts, Background declarations without specifics, Restating the user's request, Boasting about work and reporting completion, Describing the output's form

### Example 2. Analysis body

(before)

```
## AI adoption direction
- After considering several possibilities, the most suitable AI adoption approach for small manufacturers is a phased one
- Interestingly, looking at it from different angles, piloting first and then expanding carries a lower risk of early failure than a company-wide rollout at once and lets the company adjust the scope while the shop floor adapts
- This problem is quite complex, but put simply, securing budget and AI specialists at the same time is the precondition that decides success or failure
- Notably, the difference between companies that succeed and fail at AI adoption comes more from change management capability inside the organization than from technical level
- If you'd like, I can break the analysis down further by industry
- Let me know if you have more questions
```

(after)

```
## Phased AI adoption
- A phased approach that pilots first and then expands suits small manufacturers
- It carries a lower risk of early failure than a company-wide rollout and lets the company adjust the scope while the shop floor adapts
- Securing budget and AI specialists at the same time is the precondition that decides success or failure
- The difference between companies that succeed and fail at AI adoption comes more from change management capability inside the organization than from technical level
```

(Removed types) Exposing internal reasoning, Staged emotion, Rating difficulty and complexity, Calling attention and declaring importance, Advertising abilities and conditional offers, Greetings and relationship management

### Example 3. Implications

(before)

```
## Implications
- Based on the analysis above, we derived the following implications
- In conclusion, the late-stage funding gap in the startup ecosystem is a structural problem
- As we saw above, investment is concentrated in the seed and Series A stages, which cuts off funding routes after Series B, and in this way various factors are acting together
- Of course, we cannot be certain, but if the current trend continues, more companies are expected to drop out at the scale-up stage
- A tax incentive for private venture capital firms that invest in late stages should be considered
- A dedicated scale-up track after Series A should be created to clarify the funding route at each stage
- We have reviewed the issue from several angles as described above, and a limitation of this analysis is restricted access to investment data on unlisted companies
- Further expert review is needed, so please keep this in mind
- I hope this helps
```

(after)

```
## Implications
- The late-stage funding gap in the startup ecosystem is a structural problem
- Investment is concentrated in the seed and Series A stages, which cuts off funding routes after Series B
- If the current trend continues, more companies are expected to drop out at the scale-up stage
- A tax incentive for private venture capital firms that invest in late stages should be considered
- A dedicated scale-up track after Series A should be created to clarify the funding route at each stage
```

(Removed types) Self-justification, Describing the output's form, Process preview and recap, Disguised connective, Summary declaration after a list, Stacked conditional hedges, Advance disclaimers and self-declared limitations, Directing the reader's actions, Greetings and relationship management

### Example 4. Conversational reply

(before)

```
Great question. As you mentioned, how exchange rate changes affect exporters is a very important topic.

I analyzed this from various angles. First I will explain how exchange rates work, and then we will look at the actual effects.

An exchange rate is the rate at which one country's currency trades for another's. According to my web search, an exporter's profitability responds to exchange rates differently depending on which currencies its revenue and costs are in.

After considering several possibilities, I believe that a company paid in dollars that sources raw materials at home sees its profit in local currency rise when the local currency weakens. Of course, a company that imports raw materials in dollars sees part of that revenue gain offset by higher costs, and this analysis reflects current conditions, so it may change.

If you'd like, I can also provide a detailed analysis by industry. I hope this helps.
```

(after)

```
An exporter's profitability responds to exchange rates differently depending on which currencies its revenue and costs are in. A company paid in dollars that sources raw materials at home sees its profit in local currency rise when the local currency weakens. A company that imports raw materials in dollars sees part of that revenue gain offset by higher costs.
```

(Removed types) Agreement and approval, Restating the user's request, Calling attention and declaring importance, Process preview and recap, Restating known facts, Exposing methods and internal tools, Exposing internal reasoning, Advance disclaimers and self-declared limitations, Advertising abilities and conditional offers, Greetings and relationship management

### Example 5. Adding a supplementary rule

(Request) Add a retry on save failure to the file-saving rules as a supplementary feature

(before)

```
## File saving
- Save all outputs in the working folder
- On save failure, retry up to 3 times
- Use the retry logic as the default save method and do not use single save calls
- On save success, reset the retry counter and do not write a separate log
```

(after)

```
## File saving
- Save all outputs in the working folder
- On save failure, retry up to 3 times
```

(Removed types) Unrequested reverse statements: supplement turned into replacement, adding the opposite response

### Example 6. Concept definition

(Request) Write a definition of a work agent that distinguishes it from collaboration tools, messengers, groupware, and project management tools

(before)

```
## Work agent
- A work agent is software that carries a goal delegated by the user through to completion with multiple tool calls
- The distinguishing criterion is that it repeats planning, execution, and checking results on its own without step-by-step human operation
- Collaboration tools only support information sharing between people, so they are not work agents
- Messengers and groupware require people to operate every step directly, so they are not work agents
- Project management tools only record task status, so they are not work agents
```

(after)

```
## Work agent
- A work agent is software that carries a goal delegated by the user through to completion with multiple tool calls
- The distinguishing criterion is that it repeats planning, execution, and checking results on its own without step-by-step human operation
```

(Removed types) Unrequested reverse statements: listing reasons for non-membership

## Application

### Drafting mode

When drafting new text, apply the tests up front and write no meta-commentary. Keep any sign that this skill was applied out of the output.

### Correction mode

Find and delete meta-commentary in existing text and keep only the content. Summarize the corrected patterns by type in brief, then deliver the corrected text.

### Self-application

Keep this skill's detection principles, type groups, and tests out of the output. A sentence that mentions this skill is itself meta-commentary.

### Style neutrality

This skill handles meta-commentary only and stays out of the areas below.

- Sentence length, sentence endings, writing style
- Overall organization, Markdown format
- Length, number of items
- Word preferences

## Use with other guidelines

This skill works alongside other guidelines that set style or format. When another guideline allows an expression that fails a test, follow this skill's rule.

## Exceptions

- Allow meta-commentary that the user explicitly asks for, such as "State the purpose of this report at the top"
- Follow genre conventions where a genre requires meta-commentary, such as the research purpose and methods sections of an academic paper
- Allow limitations, caveats, and methodology when the user explicitly asks for them

## Pre-output checklist

Confirm the points below before output. Delete any sentence that fails, or replace it with content, then output.

- No sentence takes the text, the writer, the act of writing, the user's request, or a tool as its subject
- Every sentence carries information the reader would lose without it
- No sentence mainly benefits the writer
- No sentence performs only a courtesy ritual with no information
- No sentence uses a hidden subject, disguised content, disguised modesty, disguised question, or disguised connective
- No sentence covers an opposite direction, complement set, or substitute rule the user did not ask for
- No praise without a basis, no unrequested caveat or rebuttal, and no follow-up promise without the means to keep it
- The first sentence opens with content, with no greeting, restated request, or process preview
- The last sentence ends with content, with no greeting, invitation for more questions, or disclaimer
