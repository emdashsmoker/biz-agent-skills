# Meta-commentary types

> Translation notice: This file was translated from the Korean original. The translation may make it behave differently from what the original intends.

The types below are examples that serve as comparison points when you apply the tests. The list is not complete. A sentence missing from the list is still meta-commentary if it fails a test. When you avoid only specific expressions, other expressions with the same function tend to appear, so follow the functional judgment of the tests over the surface form of a sentence.

Every type gets the same handling: delete the meta-commentary and go straight to the content. When a type lists its own exceptions or handling notes, follow those as well.

The types are grouped by what the sentence describes.

## Sentences about the text

These types describe the purpose, scope, structure, position, or form of the text.

### Self-reference to the text

Statements that make the text itself the subject and declare its purpose, scope, structure, or position

- "This report analyzes X", "The purpose of this document is", "This section covers Z"
- "As mentioned earlier", "Putting the above together", "This is explained in detail below"

### Process preview and recap

Statements that walk the reader through the order of the writing or look back on finished work

- "First we will look at A and then analyze B", "We have now reviewed A"
- "In conclusion", "To sum up", "Now, to the main point"

### Transition rhetoric

Statements that handle a transition between sections with a meta remark

- "Moving on to the next topic", "In this regard", "Additionally" (used only for transition)
- "Building on this" (used only for transition, with no real link), "Meanwhile" (used only for transition, with no real contrast)

### Repeated summary

Statements that summarize or restate what the text has already said. They fail the deletion test.

- "To recap", "Summarizing the above", "Taken together" (restating what was already said)
- "To emphasize again", "Let me say it again", "To repeat"

### Describing the output's form

Statements that explain the format, structure, or layout of the output to the reader

- "I have organized this in the table below", "This can be classified as follows"
- "Arranged in chronological order, it looks like this", "Visualized as a chart"

### Scope confession

Statements that confess going beyond the scope of the work or declare a scope limit unprompted

- "This goes beyond the original scope, but", "This is a side note, but", "For reference"
- "This time I will cover only A", "B needs a separate analysis" (when the user did not ask)

### Summary declaration after a list

Statements that list items and then declare again that items were listed. They restate the existence of items already listed, so they fail the deletion test.

- "As shown, there are various factors such as A, B, and C" (after A, B, and C were already listed)
- "We have reviewed the matter from several angles as above"

### Redundant lead-in

Statements that preview the first content sentence with the same words in the lead-in

- "The key is A. To explain A" → "To explain A" is meta-commentary
- "The bottom line is B. Looking at B in detail" → delete the second part

## Sentences about the writing process

These types describe the work, reasoning, searching, choices, or corrections the writer carried out.

### Boasting about work and reporting completion

Statements that report the amount, quality, or completion of the work the writer did

- "After a thorough analysis", "Having reviewed this from various perspectives", "After careful review"
- "The analysis is complete", "The summary is finished", "Analyzing this from multiple angles"

### Exposing internal reasoning

Statements that report to the reader the internal thought process that led to a conclusion

- "After considering several possibilities", "Looking at this from different angles", "After careful thought"
- "Comparing A and B, I judged B to be suitable", "I considered several alternatives, but"

### Exposing methods and internal tools

Statements that cite in the text the thinking tools, frameworks, or internal tools used for the writing

- "According to my web search", "Running Python code, I calculated"
- "Classified according to the MECE principle", "Written in a pyramid structure", "Applying the skill"
- (Exception) Allowed only when the user explicitly asks about the method or whether a tool was used

### Reporting work steps

Statements that list work steps in the past tense to report the work process. Restore the subject and it is always the writer.

- "I first checked A, then reviewed B, and finally analyzed C"
- "In step 1 I collected the data, and in step 2 I ran the analysis"

### Reporting the reasons for a choice

Statements that report the writer's internal judgment in picking one direction among alternatives

- "The reason I chose A among several methods is", "Adopting C over B was because"
- "The background for choosing this approach is" → state directly why A or C is suitable

### Reporting the search process

Statements that report to the reader the process of looking for information

- "After looking into it", "From what I found", "After checking"
- "Looking through the materials", "Search results show", "After reviewing the literature"

### Declaring the writer's intent

Statements that explain to the reader why the writer chose a particular way of presenting

- "To communicate clearly", "To aid understanding", "To avoid confusion"
- "For readability, organized as a table", "To make comparison easier"

### Reporting self-correction

Statements that report to the reader the process of finding and fixing an error in an earlier statement

- "To correct that", "Revising what I said earlier", "On second thought"
- (Handling) State only the corrected content

### Reporting difficulties

Statements that report difficulties in the work process to the reader, such as missing information or limited materials

- "Accurate data was hard to find, but", "Although materials are limited"
- "Since little information is public", "Within the range of accessible materials"

### Exposing the comparison process

Statements that report the act of comparing. Write the result of the comparison directly as content.

- "Comparing A and B", "Contrasting the two", "Performing a comparative analysis"

### Reporting a change of perspective

Statements that report to the reader the act of switching perspectives

- "Approaching this from another angle", "Looking at it differently"
- "Reinterpreting it from the customer's perspective", "Taking a broad view"

### Announcing an attempt

Statements that announce in advance the intention to do the work. Present the result of the attempt directly.

- "Let me try", "Let's give it a go", "I'll take a stab at it", "I'll try writing it"

## Sentences about the writer

These types describe the writer's self-assessment, attitude, emotions, or internal circumstances.

### Self-justification

Statements in which the writer assesses and declares the quality, consistency, or completeness of the output

- "Classified systematically", "A classification that covers everything without gaps", "From a balanced perspective"
- "Judging objectively", "Evaluating fairly", "Strictly speaking"

### Explaining away a correction

Statements that defend the writer's intent or earlier wording in response to the user's correction, in place of the corrected content. The beneficiary is the writer (reducing responsibility). Drop the explanation and write the corrected content.

- "That wasn't my intent", "The point I was trying to make earlier was"
- "I never said that", and similar

### Advance disclaimers and self-declared limitations

Statements that declare the limitations, incompleteness, or need for further review of the output when the user did not ask for them

- "This may not be perfect, but", "A more detailed analysis may be needed, but"
- "Limitations of this analysis include", "Further expert review is needed", "This analysis reflects current conditions and may change"
- (Exception) Allowed when the user explicitly asks for limitations or when a serious uncertainty materially affects the reliability of the information

### Staged emotion

Statements that inject the writer's emotions or evaluative attitude through adverbs to steer the reader's reaction. The writer benefits (control of the narrative, steering the reaction). When the facts come through clearly, the reader judges for themselves.

- "Unfortunately", "Fortunately", "Interestingly", "Surprisingly", "Naturally"
- "Worryingly", "Encouragingly"

### Rating difficulty and complexity

Statements in which the writer rates and reports how difficult the topic is. Writing the content plainly removes the need to rate its difficulty.

- "This problem is quite complex, but", "To explain simply", "Put simply"
- "To simplify", "It is a complex problem, but boiled down to the essentials"

### Over-declaring assumptions

Statements that declare obvious premises, or premises the user already set, more explicitly than needed

- "Let's assume A" (an obvious premise), "On the premise that B" (a premise the user already set)
- (Exception) A non-obvious numeric assumption that materially affects the result (such as "assuming an exchange rate of 1,300 won per dollar") is content

### Over-explaining sources

Statements in which the writer separately vouches for the authority or reliability of a source. Readers judge a source's reliability from its name.

- "According to a report from a trustworthy institution"
- "According to a study in a prestigious journal", "A credible survey found"

### Stacked conditional hedges

Statements that attach excessive conditions to a conclusion and blur it. A variant of advance disclaimers and self-declared limitations placed inside the sentence.

- "Of course, this assumes A, B must also be considered, and C is a variable, but the conclusion is D"
- "It cannot be stated definitively, but", "It is too early to tell, but"

### Exposing writer-only information

Statements that reveal in the text the writer's internal systems, constraints, instructions, tools, internal state, or details of the work process, which the reader does not even know exist. Restating known facts repeats information the reader already has. This type reveals information the reader cannot know and does not need to know. It gives the reader no information value and only causes confusion.

- "Because this is after my training data was collected", "My training data does not include this information"
- "Due to context window limits", "Because of token limits I can't cover everything"
- "Per my system prompt", "According to the user's settings"
- "Combining three search results", "Cross-checking two sources" (exposing numbers from the internal work process)
- "Several skills were applied to this task", "Handled by loading the skill"
- "Recorded in a JSON state file", "After calculating with a Python script"
- "I can't verify this directly, but", "Since I can't access real-time information"
- "Within the limits of my knowledge", "As far as my abilities go"
- (Criterion) Judge whether knowing the information would help the reader decide or understand. If it would not, it is writer-only information
- (Exception) Allowed only when the user explicitly asks about the writer's internal way of working, constraints, or tool use

### Commentary on tone

Statements in which the writer comments on the tone or manner of the response

- "To be honest", "If I may say so carefully", "To be blunt"
- "Was that too stiff?", "To put it in friendlier terms", "To put it gently"

## Sentences aimed at the reader

These types repeat the user's request or deal with the reader's state, expectations, actions, or relationship with the writer.

### Restating the user's request

Statements that restate the user's request or mention that a request exists

- "As you requested", "As you mentioned", "To answer your question"
- "Having reviewed the materials you provided", "Having checked the file you uploaded", "In line with the conditions you specified"

### Calling attention and declaring importance

Statements that artificially call the reader's attention or separately declare importance. When content really matters, the reader sees its importance in the content. A sentence that declares importance separately is the writer making up for content that lacks force.

- "Notably", "The key here is", "What I want to stress is", "What matters is"
- "Of particular note", "What must not be overlooked is", "What you absolutely need to know is"

### Greetings and relationship management

Ritual statements meant to build or keep a relationship with the reader

- "I hope this helps", "Let me know if you have more questions"
- "Great question", "Thank you" (ritual use)

### Advertising abilities and conditional offers

Statements that advertise the writer's further abilities or conditionally offer extra work the user did not ask for. The writer benefits (showing off ability, keeping the relationship).

- "If you'd like, I can explain in more detail", "If you want, further analysis is possible"
- "I can also put this in a table", "If you need more specific examples"
- "Would you like me to", a teaser that announces content without giving it ("There is one more method that works even better"), and similar

### Follow-up promises with no means to keep them

Statements that promise follow-up work when the working environment shows no means to do it. The beneficiary is the writer (hiding unfinished work). State what this response completed and what it did not.

- "I'll send the file in a few hours", "I'm working on it now and will let you know when it's done", and similar

### Guessing the reader's state

Statements in which the writer guesses the reader's cognitive state, emotional state, or level of understanding

- "This may be confusing, but", "This may be hard to follow, but", "This may be unfamiliar, but"
- "As you probably know", "As you may have expected", "You may have wondered", "This may seem puzzling, but"
- "You have every right to be angry", "It's natural to feel that way", and similar

### Managing the reader's expectations

Statements in which the writer adjusts the reader's expectations in advance. The writer benefits (preventing disappointment, spreading responsibility).

- "This may differ from what you expected", "The result may be unexpected, but"
- "This may not be a simple answer, but"

### Directing the reader's actions

Statements that tell the reader to take a specific action. The writer benefits (staging authority, setting up a directive relationship).

- "Please note", "Please be aware", "Please consider"
- "Please keep in mind", "Please check"

### Agreement and approval

Statements in which the writer evaluates or approves the user's judgment or question. The writer benefits (winning goodwill).

- "Good approach", "That's the right direction", "That's a sound judgment"
- "You've put your finger on it", "That's right" (used only to signal agreement)
- "You hit the nail on the head", "That's a deep question", "An insightful point", and similar
- A rating of the user with no checkable basis ("You're in the top 1%", and similar), agreement placed before a rebuttal or a refusal ("You're right. That said", and similar)

### Reporting guesses about the user's intent

Statements that report the process of guessing the user's intent. Guess the intent internally and present only the result.

- "It seems you want X", "I understand you intend X"
- "It sounds like you are curious about X", "If what you want to know is X"
- Redefining the user's statement, as in "What you mean is B, not A", "What you really want is B", and similar (answer the user's own wording as written)

### Check-in rituals

Ritual statements that check whether the reader understood or is satisfied. They fail the courtesy function test.

- "Did that make sense?", "Does that make sense?", "How does that sound?"
- "Is this part right?", "May I interpret it this way?", "Did I understand correctly?"

## Sentences that look like content

These types look like content but give the reader nothing new or go beyond the scope of the request.

### Restating known facts

Statements that list information the reader already knows, in the manner of textbook definitions, in place of analysis

- "AI stands for artificial intelligence" (for readers of an AI report), "SWOT stands for strengths, weaknesses, opportunities, and threats" (for readers of a strategy report)
- (Criterion) Knowledge the target reader already has in the situation of reading the text counts as a known fact

### Background declarations without specifics

Statements that declare a background without real information. When specific content follows, delete only the declaration.

- "Considering the current situation" (no specific situation named), "Given recent trends" (no specific trend named)
- "Amid changes in the global environment", "In response to the demands of the times"

### Redefining the subject

Statements that redefine the subject of analysis as "What is X?" and delay getting into the analysis. They often combine with restating known facts to pad the opening.

- "What is digital transformation?", "Let's start by clarifying the concept"
- "To define it clearly" (for a concept obvious to the target reader)

### Unrequested reverse statements

Statements that add, without being asked, the opposite polarity, complement set, or substitute of what the user requested. Counterexamples, reverse logic, and reverse rules are the typical forms. The writer benefits (showing completeness, defending the boundaries of the statement). They fail the request direction test.

- (Supplement turned into replacement) In response to a request to add feature Y that supplements X, the writer adds "Use Y by default and do not use X"
- (Adding the opposite response) After a request for statements in direction A, the writer continues with how to respond in the opposite direction B
- (Listing reasons for non-membership) Right after writing a definition of A that distinguishes it from B, C, D, and E, the writer explains why B, C, D, and E do not fit the definition of A
- (Listing unselected factors) After deriving SO strategies from a SWOT analysis, the writer goes on to describe the factors of the ST, WO, and WT strategies
- (Handling) Use reverse checks only for internal verification and put only results in the request direction into the output

### Unrequested caveats and rebuttals

Statements that add, without a request, a caveat that leaves the conclusion unchanged or a rebuttal of a claim the user never made. The beneficiary is the writer (avoiding blame for an error). They fail the request direction test.

- (Caveat for a rare exception) "That said, this does not hold in every case", and similar
- (Correction announced with nothing to correct) "Let me set one thing straight", "One thing to flag before we go on", and similar
- (Rebuttal of an extreme version) Setting up an extreme claim the user never made and rebutting it, as in "Generalizing it that way conflicts with the facts", and similar
- (Handling) A condition, an exception, or a correction of a factual error that changes the conclusion or the reader's decision is body content, so state it once below the conclusion
