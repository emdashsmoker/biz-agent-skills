# Examples of removing meta-commentary

> Translation notice: This file was translated from the Korean original. The translation may make it behave differently from what the original intends.

Each example places text that contains meta-commentary (before) next to the same text with the meta-commentary removed (after). The after version keeps the content of the before version unchanged and removes only the meta-commentary. When removing meta-commentary leaves an awkward ending or heading, smooth it while keeping the original writing style.

The facts in the examples are fictional and only show the format, so do not use them as real evidence. The names listed under removed types are either type names from references/types.md or bypass form names from SKILL.md.

## Report opening

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

## Analysis body

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

## Implications

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

## Conversational reply

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

## Adding a supplementary rule

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

## Concept definition

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
