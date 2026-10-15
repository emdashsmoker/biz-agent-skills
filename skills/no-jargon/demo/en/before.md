## Technical approach

**In short:** we will build a single connected digital map of the factory, covering its machines, processes and quality checks. AI then works on top of that map to catch problems early, point to their likely causes, and answer staff questions in plain language.

**1. A common definition of the factory.**
We will write down, in a form computers can use, what our equipment, processes and quality checks are and how they relate to one another: which machine sits on which line, which process step it performs, and which quality checks apply to its output. We follow ISA-95, the established international standard for structuring manufacturing operations, so we are not inventing this structure from scratch.

**2. One connected map, built from data we already have.**
Production records from our manufacturing execution system (MES) and business data from our ERP system (orders, materials, inventory) will be loaded into this structure and linked together. Instead of searching several systems by hand, anyone can follow a chain such as *defective part → production batch → machine → maintenance history*.

**3. Machines that describe their data the same way.**
Equipment from different vendors reports data in different formats. We will use two industry standards for machine data, OPC UA and the Asset Administration Shell, so that a reading from one supplier's machine means exactly the same thing as the equivalent reading from another supplier's machine.

**4. Filling gaps and catching bad data automatically.**
The system can work out facts that nobody entered directly. If a machine belongs to Line 3, and Line 3 is in Plant A, the system knows the machine is in Plant A without anyone recording it. It also checks incoming data against agreed rules (for example, "every finished batch must have an inspection record") and flags records that are missing or contradictory before they feed into decisions.

**5. AI that spots problems and points to likely causes.**
The AI combines two approaches:
- **Learning from patterns.** It learns what "normal" looks like from the connected data and flags unusual behavior. It judges each machine in the context of everything connected to it, not in isolation, so it can catch problems that no one has written a rule for.
- **Following the known rules.** It uses the explicit rules and relationships in the factory map, which keeps its findings grounded in how the factory actually works.

When the AI flags a problem, the system follows the links in the map back to a short list of possible causes, such as a particular raw-material lot or a machine that is overdue for maintenance. Engineers then know where to look first.

**6. Plain-language answers for operators.**
Operators can ask questions in everyday language, such as "Why did defects on Line 2 rise last week?" A ChatGPT-style AI assistant looks up the answer in the factory map instead of relying on general knowledge, and shows the records it used, so every answer can be checked.

**7. Keeping the system reliable as the factory changes.**
New machines, products and processes will mean updates to the factory definition. Every change is saved as a new version, so we can see exactly what changed and return to an earlier version if needed. We also keep a fixed list of business questions the system must always answer correctly (for example, "Which machines produced this batch?"). Each change is tested against that list before it goes live, so an update cannot quietly break something that used to work.
