## Technical Approach

**Summary:** In this pilot, we will run an AI system on our own servers. It will answer employees' questions using our internal documents. Company data stays inside the company. Each answer shows which document it came from, and safeguards are in place to catch wrong answers and protect sensitive information.

### 1. The AI model and where it runs

- **We run it ourselves.** We will use a publicly released AI model that we can download and run on our own equipment, so we don't need an outside AI service. It will run on servers with specialized AI chips in our own data center, so internal data is never sent to an outside provider.
- **Model size.** The model is large (70 billion internal settings), and it is built on the same basic design as today's popular AI chat tools.
- **How much it can read at once.** It can take in close to 100,000 words of text in one go, roughly 200 pages. That means it can work with long reports or several documents at the same time.

### 2. Answers based on our own documents

When an employee asks a question, the system first searches our internal documents and finds the most relevant passages. It then gives those passages to the AI, which writes the answer from them. To make this work, we convert our documents into a searchable library that matches by meaning, not just exact keywords. As a result, answers reflect our actual policies and data rather than the AI's general knowledge.

### 3. Tailoring the AI to our business

We give the model extra training on examples from our own field so it learns our terminology and the way we work. We use an efficient method that adjusts only a small part of the model instead of retraining all of it. This cuts the time and hardware cost of the customization by a large margin.

### 4. Checking that answers are accurate

AI systems sometimes give answers that sound confident but are wrong. We use two safeguards:

- **Sources required.** Every answer must cite the internal document it is based on, so users can check it.
- **Automated review.** A second AI automatically reviews and scores answers and flags those that look unreliable.

### 5. Speed and running cost

- **Compression.** We store the model in a compressed form so it needs less memory and fewer chips. This usually costs only a small amount of accuracy.
- **Reusing work already done.** While the AI writes an answer, the system saves partial results so it does not repeat the same calculations.

Together, these steps make answers start appearing sooner and lower the cost of producing each answer.

### 6. Security protections

- **Personal information is hidden.** Names, contact details, ID numbers, and similar personal data are automatically masked.
- **Manipulation attempts are blocked.** A filter catches attempts to trick the AI with hidden instructions, for example asking it to ignore its rules or reveal confidential information.
