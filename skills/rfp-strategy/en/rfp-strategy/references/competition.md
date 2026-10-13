# Competitive Structure Analysis

> Translated from the Korean original. It may behave differently from the original's intent. Statute names are given in Korean with an English gloss so they can be looked up.

Procedure and template for section 4 (competitive structure) of 02_proposal_strategy.md. The competitor search runs only where web search is allowed. The rules follow Korean public procurement.

## Eligibility judgment

Before looking for competitors, judge which company sizes can bid on this notice. Searching without this step lets large organizations that cannot bid into the candidate list and distorts the competitive structure.

- The first basis is the eligibility wording in the tender notice and RFP. Follow that wording even if it differs from the amount thresholds below.
- If the wording is missing or unclear, estimate with the rules below and mark the result [CONFIRM].
- Regulatory figures change, so check the values in force on the notice date with a web search.

### Service contract thresholds

Article 4 of 「중소기업제품 구매촉진 및 판로지원에 관한 법률」 (Act on Facilitation of Purchase of Small and Medium Enterprise-Manufactured Products and Support for Development of Their Markets) and Article 2-2 of its Enforcement Decree set company-size limits for public-agency service contracts.

| Estimated price | Who can bid |
|---|---|
| Under KRW 100 million | Small businesses or micro-enterprises. If three or fewer eligible small businesses and micro-enterprises exist, or the tender fails, it relaxes to competition among SMEs and medium-sized firms can bid |
| KRW 100 million up to the notified amount | SMEs. Mid-sized and large companies cannot bid |
| Notified amount or above | No size limit based on amount |

- Services designated as SME competition products are competed among SMEs regardless of amount. Check the notice for this designation.
- The estimated price excludes VAT. If the base amount or budget in the notice includes VAT, divide by 1.1 to get the estimated price. Do the calculation in code.
- The notified amount is the international tender threshold announced every two years under Article 4 of 「국가를 당사자로 하는 계약에 관한 법률」 (Act on Contracts to Which the State Is a Party). For goods and services of central government agencies in 2025-2026 it is KRW 230 million. If the notice date falls outside this period, check the new amount.

### Academic research exception

Article 2-3 of the same Enforcement Decree allows agencies to skip the SME priority procurement rule for academic, research, education, inspection, and similar services where competition that includes non-profit corporations is needed. A notice that uses this exception states the reason in the notice. Large consulting firms can bid on such notices. For academic research contracts, judge by the notice's eligibility wording and whether an exception reason is stated, together with the amount.

### Software project thresholds

- Article 48 of 「소프트웨어 진흥법」 (Software Promotion Act) and the Ministry of Science and ICT notice 「중소 소프트웨어사업자의 사업 참여 지원에 관한 지침」 (Guidelines on Supporting Participation of Small and Medium Software Businesses) set minimum project sizes for large software businesses. Here "large" means every software business other than an SME, including mid-sized companies.
- Appendix 1 of the guidelines sets the minimums by revenue band. As of 2026, companies with revenue of KRW 800 billion or more may bid on projects of KRW 8 billion or more, and companies below that revenue on projects of KRW 4 billion or more.
- A company that became mid-sized from SME status less than five years ago may bid on projects of KRW 2 billion or more regardless of revenue. Projects under KRW 2 billion are therefore open only to SMEs.
- Companies in business groups subject to cross-shareholding restrictions may not bid regardless of amount, except on projects recognized as exceptions.
- The project amount for software projects includes VAT. It is calculated differently from the estimated price used for service contracts.
- The ordering agency must state in the notice or RFP whether large-company participation is restricted. Check that wording first. For IT planning services such as ISP and ISMP, check the notice wording to see whether they count as software projects.
- Apply announced government reforms or proposed amendments only after confirming they are reflected in the guidelines.

### Applying the judgment

- If the judgment limits bidding to SMEs or smaller, delete the large consulting firm type from the competitive structure and do not apply the default large-firm candidate rule. Keep the university industry-academic cooperation foundation type regardless of the size judgment.
- Include company-size and region conditions in the search queries for the similar-to-bidder path and the industry path (for example, "[region] [industry] small business", "[project type] research contract SME-restricted award").
- Record the judgment and its basis (notice wording, or estimated price and the applicable article) on the first line of the competitive structure section.
- If the user asks to search without eligibility filtering, skip the eligibility judgment and its application. Regulations change often in timing and application, so the judgment can be wrong; follow the user's call. In that case apply the default large-firm candidate rule regardless of amount and skip eligibility exclusions on the industry path. Write "Filtering off (user request)" in the judgment cell.

## Searching for competitor candidates

Many organizations do not publicize public service contracts they perform. Using only the self-disclosure path leaves the candidate table empty and the competitive structure impossible to judge. Use two confirmation paths and two estimation paths together.

| Path | Kind | What it finds |
|---|---|---|
| Award records | Confirmed | Awardees and preferred bidders of past same-name projects of the same client and same-type projects of other clients |
| Self-disclosure | Confirmed | Wins and deliveries announced by the performing organization itself |
| Similar to bidder | Estimated | Organizations with business areas, size, and track record similar to the bidder |
| Industry search | Estimated | Organizations in industries able to perform this type of project |

### Award records

- Check bid opening and award results from the procurement system. Use the Public Procurement Service's KONEPS award information and contract information services on the Public Data Portal (open API), detail pages of private bid information sites, and the client's website: tender notices, preferred bidder announcements, and contract disclosure boards.
- Search engines index notice titles more than bid results, so check in two steps. First, find past notice pages by title. Second, open the page and check the bid opening result, awardee, and preferred bidder. If these are missing, search again by notice number.
- Example queries: "[past project name] bid opening result", "[past project name] preferred bidder", "[notice number] awardee", "[client name] contract disclosure [project keyword]"
- Record award results the user provides through this path as well.

### Self-disclosure

- Search for wins and deliveries the performing organization announced through press releases, website track record lists, organizational blogs, and organizational social media. Cover both the same client's projects and same-type projects of other clients.
- Example queries: "[client name] research contract awarded", "[client name] kickoff meeting contractor", "[project type] plan research final report contractor"

### Similar to bidder

- Build the bidder's profile from its business areas, size, and track record areas. Search for organizations with the same profile. This path finds the organizations the bidder meets repeatedly in the same client market.
- Example queries: "[bidder's business area] specialist consulting firm", "[bidder's main project type] research contractor"
- Skip this path if there is no bidder information.

### Industry search

- Derive from the project's characteristics the industries that could perform it, and search for organizations in those industries. For example, an ISP points to IT consulting firms and system integration affiliates, R&D performance analysis to science and technology consultancies and specialist research institutes, and a regional development plan to regional research institutes and urban planning engineering firms.
- Use association member lists, mentions of major companies in industry articles, and queries combining the project field, project type, and client type (for example, "[field] master plan research contract", "[field] university cooperation foundation policy research").
- Exclude organizations that cannot bid under the RFP's eligibility (business registration, large-company limits, regional limits) and record them in the excluded-organizations note.

### Default large-firm candidates

- Apply only to notices where the eligibility judgment allows mid-sized and large companies. If the user turned filtering off, apply to every notice.
- Large consulting firms win many public contracts without advertising a public-sector practice on their websites. Do not filter them out for lacking one.
- Use three default candidate types: consulting arms of large accounting firms, large management consulting firms, and large education-association-type organizations. The last are association-form organizations that lead with management education and certification businesses. They win public consulting contracts without calling themselves consulting firms, so search for them separately.
- Obtain organization names by searching industry articles and reports of public contract work. Search for evidence that they have worked in the project field and record it in the rationale column. If no evidence turns up, write "group of organizations with many public contracts" and cite the organization's website URL with the check date.

### Search order

- Run the award records and self-disclosure paths first. Organizations confirmed there carry stronger evidence than estimated candidates.
- Run the award records and self-disclosure paths whether or not they return results.
- Move to the next path after three consecutive queries on one path return no organizations.
- Run the similar-to-bidder and industry paths until every competitor type has at least one organization. Spend remaining searches on types that are still empty.
- Delete competitor type rows that do not apply to the project. Add a row for any new type the industry search finds.
- If web search is not allowed, record only user-provided award results and mark the rest [CONFIRM]. Mark [CONFIRM] for any type that remains empty after all four paths.

## Recording rules

- Put one of the four path names in the path column.
- Do not describe estimated candidates as confirmed organizations when writing strengths and weaknesses.
- Give a source URL for every organization. Record the posting date if found; otherwise record the search date as the "checked" date. Leave organizations without a URL out of the table. For user-provided material, write "user-provided" as the source.
- If an organization excluded on eligibility was the previous contractor or a confirmed organization, competition intensity changes. Reflect this in the strengths and weaknesses by type.
- Base expected strengths and weaknesses by type on the competitor candidate table.
- For each competitor-type strength, find bidder evidence that offsets it and pass it to the differentiators in section 6 of 02_proposal_strategy.md.

## Template

Copy this template and fill it in. Keep column names, order, and count. Do not break lines or use the `|` character inside a cell. Separate multiple values in one cell with commas.

```markdown
- (Eligibility judgment) Company sizes that can bid and the basis

| Competitor type | Expected strengths | Expected weaknesses |
|---|---|---|
| University industry-academic cooperation foundation | | |
| Large consulting firm | | |
| Specialist research institute | | |
| Consulting firm of similar size | | |

| Organization | Competitor type | Path | Similar project or rationale | Source |
|---|---|---|---|---|

- (Client's previous contractor) Organization and path. "Unconfirmed" if not found
- (Excluded organizations) Organization, reason for exclusion, path. "None" if not applicable
```
