## Pilot answering questions from internal documents on company-owned servers

- (Model) Publicly downloadable large language model run on company-owned servers
    + Servers equipped with chips used for artificial intelligence (AI) computation
    + Model size of 70 billion internal numerical values set during training
    + Up to about 128,000 tokens of text handled in a single request
    + Model fitted to the company's line of business through additional training that adjusts only a small set of added numerical values

> (large language model) An AI program that writes answers in ordinary sentences based on patterns learned from very large amounts of text

> (token) A word or part of a word as the unit in which a large language model reads and writes text

- (Answer reliability) Answers based on internal documents to make their accuracy verifiable
    + Internal documents stored in a search database that finds passages by meaning regardless of wording
    + Passages related to each question retrieved from that database as the basis for the answer
    + Citation of source documents required in every answer
    + Review of answers by a second large language model to track false information presented as fact
- (Operating efficiency) Reduction in the wait before an answer starts and in computing cost per token
    + Internal numerical values stored in a shortened 4-bit format to reduce the model's memory needs
    + More efficient storage of intermediate calculations the model reuses for each new token
- (Safety controls) Automatic protection of personal information and of the model's operating rules
    + Hiding of information that can identify a specific person
    + Filtering of inputs containing instructions meant to override those rules
