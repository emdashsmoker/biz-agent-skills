# Hyperscale AI pilot TF collaboration diagnosis

**Conclusion:** The TF currently hangs on **one person, I-A**, and on **a single contact per team**. Five of the 13 people would each split the TF if absent. Adding just **2** links (P-B–I-C, Q-B–D-C) brings that number to zero and cuts the share of paths that must pass through I-A from 67% to 37%.

![Current structure vs improved](tf_network_compare.png)

The figure file is `tf_network_compare.png`. The left side is the current structure and the right side is the improvement. A red ring marks a person whose absence splits the TF, and a green dashed line marks a link to add.

---

## 1. Problems in the current structure

### ① The whole TF connects through I-A
- If I-A is absent, the TF splits into **3 pieces** (quality and planning, 6 people / design, 4 people / I-B and I-C, 2 people).
- Of the 66 pairs among the 12 people other than I-A, **44 pairs (67%) cannot reach each other without going through I-A.** This creates a work bottleneck and tends to pile the load on I-A.

### ② Each team has only one outside contact
- The **design team** connects to the rest of the TF through a single link, *D-B–I-A*. Four people, 31% of the TF, depend on that one link.
- The **quality team** has 2 outside links, but both go through Q-A.
- Inside the teams, ties are strong. The quality and design teams each consulted in 5 of their 6 possible pairs. The problem is between teams.

### ③ Two team pairs have no direct link
- Of the 6 team pairs the 4 teams can form, **quality–design** and **planning–design** never consulted directly.
- So Q-D needs 5 steps to reach D-A, D-C and D-D.

### ④ People with only one contact
- I-C consulted only with I-B, and P-B only with P-A. If that one person is absent, they are cut off.

### People whose absence splits the TF (5)

| Person | Who gets cut off if absent | Note |
|---|---|---|
| **I-A** | 4 design members, I-B and I-C (TF splits in 3) | Most serious. Center of all connections |
| **D-B** | D-A, D-C, D-D | Design team's only contact |
| **Q-A** | Q-B, Q-C, Q-D | Quality team's only contact |
| **I-B** | I-C | |
| **P-A** | P-B | |

---

## 2. Improvement: add 2 links

| | New link | Problem solved |
|---|---|---|
| New 1 | **P-B – I-C** | The TF holds even if I-B or P-A is absent. Gives planning and info staff a direct channel |
| New 2 | **Q-B – D-C** (Q-C works the same) | Creates the missing direct quality–design link. The TF holds if Q-A or D-B is absent, and even if I-A is absent |

**Why these two**
- **2 is the minimum.** If I-A is absent the TF splits into 3 pieces, so 1 link cannot fix it.
- 18 combinations of 2 links remove every person whose absence splits the TF. Of these, I picked the one that cuts the average distance and the share of paths through I-A the most.
- The new links join **people who are not the teams' contacts** (I-A, Q-A, D-B, P-A). The aim is to share the load, not to add more work to the contacts.
- Any 2 links will not do. For example, adding *P-B–Q-D* and *D-C–I-C* still leaves the TF split if I-A is absent.

### Before and after

| Indicator | Current | Improved |
|---|---|---|
| People whose absence splits the TF | 5 | **0** |
| Links with no alternative path | 4 | **0** |
| Share of shortest paths through I-A | 67% | **37%** |
| Average distance between two people | 2.68 steps | **2.35 steps** |
| If I-A is absent | Splits into 3 pieces | Stays connected (average 3.09 steps) |
| Team pairs with no direct link | Quality–design, planning–design | Planning–design |

---

## 3. Recommendations

1. **Make each new link a joint task.** An instruction to "keep in touch" alone will not last. Assigning each pair one output they must produce together works better. For example, P-B–I-C could check the requirements and data for the pilot tasks, and Q-B–D-C could review quality criteria for AI outputs. Adjust these to the actual roles.
2. **Keep watching I-A's load.** Even after the improvement, I-A is the person most paths go through (37%). If I-A and P-A are absent at the same time, P-B, I-B and I-C are cut off. It is best to coordinate schedules so their leave or travel does not overlap.
3. **(Optional) A direct planning–design link.** If the planning team needs to hear design's needs directly at this stage, consider adding *P-B–D-C* as well. The average distance drops to 2.13 steps, the share through I-A to 22%, and the longest distance from 5 steps to 4. Bear in mind that it adds work for P-B and D-C.
4. **Measure again the same way in a month** to check whether the new links actually formed.

---

## 4. Cautions when reading this

- The data has **no counts or importance of consultations**. A single consultation counts as one link, so formal and core consultations look the same.
- Communication outside the records (messenger, informal talks and so on) may be missing.
- I-C and P-B may consult only through their team seniors by design, as support roles. Even so, the TF needs at least one alternative channel to stay connected.
- The recommended partners were picked **from the structure alone**. If the roles do not fit, Q-C works the same as Q-B. Using D-A or D-D instead of D-C still removes every person whose absence splits the TF, with a slightly smaller improvement (average 2.39 steps, 38% through I-A).

**What I'd like to check:** If you have each person's role or rank, or consultation counts, please share them. I will pick partners that fit the work better and rerun the analysis with the counts.
