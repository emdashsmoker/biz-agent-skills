## Factory AI with results traceable to linked equipment, process, and quality records

### Factory data from separate systems linked through one ontology
- Equipment, process, and quality areas of the factory described in one ontology
    + Ontology structure following the levels of an international manufacturing standard from company and plant down to production line and machine
    + Reasoning software to apply the category levels and chained relations of the ontology to work out links that no one entered

> (ontology) A formal set of definitions that states the kinds of things in a field and their relations in a form computers can process

- Data from the MES (Manufacturing Execution System) and the ERP (Enterprise Resource Planning) system loaded into a knowledge graph through preset conversion rules

> (knowledge graph) A database that stores each record together with its links to related records

- Equipment data described in international standard formats to let the system read data from machines of different makers with the same meaning

### Anomalies detected by AI traced to possible root causes through the knowledge graph
- AI model to detect anomalies by learning from each record together with its linked records
- Links in the knowledge graph followed back from each detected anomaly to a list of possible root causes

### Operators' questions answered by AI with supporting records from the knowledge graph
- Questions asked and answered in everyday language
- Related records and links looked up in the knowledge graph ahead of each answer
- Supporting records and links shown with each answer to let operators check the basis

### Accuracy of data and ontology maintained through checks and version records
- Each record checked against preset rules for missing or inconsistent values
- Each change to the ontology saved as a separate version
- Retest after each change using a fixed list of questions the ontology must be able to answer
