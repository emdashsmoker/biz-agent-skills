## [1] Open the attached file on document work by department

The file is open. It has 10 departments and 6 columns, with no blank cells or duplicate departments.

| Department | Headcount | Monthly document search hours per person | Search hours band | Monthly report writing hours per person | Document storage |
|---|---:|---:|---|---:|---|
| Quality | 12 | 18.5 | 15 hours or more | 22.0 | Electronic |
| Design | 15 | 21.0 | 15 hours or more | 16.5 | Mixed |
| Production Control | 9 | 9.5 | 5-15 hours | 12.0 | Electronic |
| Purchasing | 7 | 6.0 | 5-15 hours | 8.5 | Electronic |
| Sales | 11 | 4.5 | Under 5 hours | 14.0 | Electronic |
| HR | 5 | 3.0 | Under 5 hours | 10.5 | Electronic |
| Finance | 6 | 7.5 | 5-15 hours | 18.0 | Electronic |
| IT | 5 | 5.5 | 5-15 hours | 6.0 | Electronic |
| R&D Center | 14 | 16.0 | 15 hours or more | 25.5 | Mixed |
| Safety and Environment | 4 | 12.0 | 5-15 hours | 9.0 | Paper |

**At a glance**
- Total headcount: 88
- Monthly document search hours per person: from 3.0 hours (HR) to 21.0 hours (Design). The company-wide average weighted by headcount is 12.2 hours.
- Monthly report writing hours per person: from 6.0 hours (IT) to 25.5 hours (R&D Center).
- Document storage: 7 departments use electronic documents, 2 use a mix (Design, R&D Center) and 1 uses paper (Safety and Environment).
- The "Search hours band" column matches the actual search hours in every row.

The hour columns carry no unit, but the band column is in hours, so I read them as hours.

## [2] Pick out only the departments that spend a lot of time finding documents

I took "a lot" to mean departments whose **search hours band, already in the file, is "15 hours or more."** Three departments qualify.

| Department | Headcount | Monthly document search hours per person | Department monthly search hours (headcount × per person) | Document storage |
|---|---:|---:|---:|---|
| Design | 15 | 21.0 | 315.0 | Mixed |
| Quality | 12 | 18.5 | 222.0 | Electronic |
| R&D Center | 14 | 16.0 | 224.0 | Mixed |

- The three departments have 41 people, 47% of the 88 in total. Yet they account for 71% (761 hours) of the company's document search time (1,073.5 hours a month).
- Ranking by department total (headcount × hours per person) puts the same three departments in places 1 to 3. The gap to fourth place, Production Control (85.5 hours), is large, so the result is the same whether you rank per person or per department.
- The next department down is Safety and Environment (12.0 hours per person). Lowering the cutoff to "10 hours or more" would add it for 4 departments.

The original data is unchanged. I only showed the filtered result.

## [3] The Design headcount was entered wrong. Change it to 14

I changed the Design headcount **from 15 to 14**. No other values were touched.

The original `input.csv` is unchanged, and the corrected version is saved separately.
`document_work_by_department_corrected.csv`

This change moves the following numbers:
- Total headcount: 88 → 87
- Design's department monthly search hours: 315 → 294 (21.0 hours × 14 people)
- The "high search time" departments picked earlier are based on hours per person, so they are still Design, Quality and R&D Center. Only their combined headcount drops from 41 to 40.

## [4] Never mind, undo the change you just made

Undone. The Design headcount is back to **15**, and the data is exactly as it was when first opened.

- Total headcount is back to 88, and Design's department monthly search hours are back to 315.
- I deleted the corrected file made earlier (`document_work_by_department_corrected.csv`). The original `input.csv` was never modified, so it is as it was.

## [5] Total the headcount by document storage

I counted all 10 departments. Design has 15 people, as just restored.

| Document storage | Departments | Total headcount | Share | Departments included |
|---|---:|---:|---:|---|
| Electronic | 7 | 55 | 62.5% | Quality, Production Control, Purchasing, Sales, HR, Finance, IT |
| Mixed | 2 | 29 | 33.0% | Design (15), R&D Center (14) |
| Paper | 1 | 4 | 4.5% | Safety and Environment |
| **Total** | **10** | **88** | **100%** | |

- Among the three "15 hours or more" departments picked earlier, 12 people use electronic documents (Quality) and 29 use a mix (Design, R&D Center).
- Both mixed-storage departments are in the top three for search time. With only two mixed-storage departments, though, it is hard to conclude that storage is what drives the longer search time.
