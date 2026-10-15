The project describes the equipment, production process, and quality areas in an ontology, with reference to the levels that ISA-95, a standard of the International Society of Automation, sets out for a manufacturing company's systems, from shop floor equipment up to company-wide business planning.

> (ontology) A structured description of the categories of items in a field and the relations among them, written in a form a computer can process

The project builds a knowledge graph by converting production data from the MES (Manufacturing Execution System) and business data from the ERP (Enterprise Resource Planning) system with preset conversion rules.

> (knowledge graph) A body of data that records actual items and the relations among them, organized by the categories defined in the ontology

At the equipment level, each machine and its data are described in the data structures and record formats of international standards for industrial equipment, so that systems from different makers can exchange data and interpret it with the same meaning.

Reasoning software works out relations that are not recorded directly, based on how categories sit within broader categories and on rules that join a series of linked relations into a single relation, and checks against preset conditions confirm that the data is accurate and consistent.

The AI (artificial intelligence) part of the system follows a neuro-symbolic design with two combined parts: a method that turns each item and relation in the knowledge graph into a set of numbers reflecting its relations to other items, so that an AI model can learn from it, and an anomaly detection model based on a GNN (graph neural network). For each anomaly detected, searches along the links in the knowledge graph trace the anomaly back to its possible root causes.

> (neuro-symbolic design) An AI design that reaches its results by combining patterns learned from data with knowledge and rules written down explicitly

> (GNN) A type of AI model that learns patterns from data made up of items and the relations among them

When equipment operators ask questions, an LLM (large language model) works through the knowledge graph using GraphRAG (Graph Retrieval-Augmented Generation) and produces answers that show which facts and relations in the knowledge graph support them.

> (LLM) An AI model trained on very large amounts of text to understand and write everyday language

> (GraphRAG) A method in which an AI model looks up relevant facts in a knowledge graph before writing its answer

Changes to the categories and relations defined in the ontology are controlled by saving each change as a separate version and by tests, rerun after every change, that confirm the ontology still answers its competency questions (CQs) correctly.

> (competency questions) A set of questions, agreed at the design stage, that the ontology must be able to answer to serve its purpose
