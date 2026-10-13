# Concepts and Theory

> Translated from the Korean edition. Wording may differ from the original intent.

Covers the basic concepts of network analysis, types of relations, roles in organizations, and theories that link economic action and networks.

## Social networks

A social network is a structure of people or organizations linked by relations. Decide before the analysis what counts as a relation and state it in the results. Common criteria:

- (Between people) They know each other and have met or contacted each other directly.
- (Between organizations) They have made at least one transaction or exchange.

## Types of relations

Knoke and Kuklinski (1982) sorted social relations into seven types. Mixing types in one network blurs the reading, so pick one type of relation before starting.

| Type | Content | Example |
|---|---|---|
| Transaction | Exchange of ownership of goods or symbols | Trade between firms |
| Communication | Exchange of messages | Rumors spreading in an organization |
| Boundary penetration | Members or boundaries of units overlap | Interlocking directorates |
| Instrumental | Contact to obtain information or goods | Contacts during a job search |
| Sentiment | Liking, hostility or respect | Friendship |
| Authority and power | Giving and following orders in a formal organization | Manager and subordinate |
| Kinship | Ties of blood and marriage | Family |

> Knoke, D., Kuklinski, J. H. (1982), Network Analysis, Sage Publications

## Networks by unit of analysis

- (Ego network) One person (the ego) and the contacts tied to them. Surveying N respondents gives N ego networks. `extract_ego_network` pulls one from a whole network.
- (Dyadic network) Uses pairs of people as the unit. N people give N(N-1)/2 possible pairs.
- (Whole network) Covers every actor inside the boundary and all relations among them.

## Shapes of communication networks

Leavitt (1951) reported that network shape changed performance in experiments where small groups solved problems while communicating only along fixed channels. In the star and Y shapes, ties converge on one person. In the chain and circle, ties are spread out.

| Result | Star | Y | Chain | Circle |
|---|---|---|---|---|
| Speed of solving | Fastest | Fast | Slow | Slow |
| Errors | Few | Few | Many | Many |
| Messages sent | Fewest | Middle | Middle | Most |

The more centralized the network, the more often and the more unanimously members judged that the group had a leader. In the star, members named the central member almost unanimously. In centralized networks the central member was satisfied while peripheral members were not.

> Leavitt, H. J. (1951), Some Effects of Certain Communication Patterns on Group Performance, Journal of Abnormal and Social Psychology

> Pavitt, C., Chapter 9 Imposed Group Structures(https://www.uky.edu/%7Edrlane/teams/pavitt/ch9.htm)

## Strong and weak ties

| Aspect | Strong tie | Weak tie |
|---|---|---|
| Contact frequency | High | Low |
| Ties among the contacts | Often know each other | Often do not know each other |
| Information carried | Overlaps with what one already knows | Brings new information from other groups |
| Use | Cohesion and cooperation inside a group | Searching for and spreading information outside the group |

Granovetter (1973) argued that weak ties tend to bridge separate groups and therefore spread information farther than strong ties. When the analysis looks for new information or opportunities, examine where the weak ties sit.

> Granovetter, M. S. (1973), The Strength of Weak Ties, American Journal of Sociology 78

## Structural holes and redundancy

A person who links two people who are not tied to each other hears from both sides first and can broker between them. Burt (1992) called this gap a structural hole and explained the gain of the person who bridges it as the benefit of the third party (tertius gaudens). When an ego's contacts are already tied to each other, those relations repeat the same information and are redundant. The formulas are in `references/cohesion_subgroups.md`.

## Roles in organizations

Organizational network diagnosis sorts members into the roles below. Role names are labels for interpretation. When assigning a role, cite the indicators listed. The table maps each role to the roles Cross and Prusak (2002) described for informal networks.

| Role | Description | Indicators | Cross and Prusak role |
|---|---|---|---|
| Hub | Interacts with many colleagues in the unit, gathers and spreads information | High degree centrality | central connector |
| Broker | Links different departments or groups | High betweenness and low constraint | boundary spanner, information broker |
| Specialist | Interacts little but is sought out for expertise | Low degree in the everyday interaction network and high indegree in the advice network. Confirm expertise with data from outside the network | peripheral specialist |
| Peripheral | Does assigned work at the edge of the network. May be a newcomer or future talent | Low degree and low closeness | none |

When ties concentrate on a hub or a broker, flows between departments may break if that person leaves. In that case check concentration and cut-points together with `compute_centralization` and `find_cut_points`.

> Cross, R., Prusak, L. (2002), The People Who Make Organizations Go or Stop, Harvard Business Review(https://hbr.org/2002/06/the-people-who-make-organizations-go-or-stop)

## Embeddedness

Granovetter (1985) argued that economic action is rooted in the concrete relations actors maintain, and called this embeddedness. He criticized both of the following views.

- (Undersocialized view) Like classical and neoclassical economics, it treats actors as calculating self-interest apart from their relations.
- (Oversocialized view) It treats actors as following internalized norms mechanically.

The embeddedness view focuses on how concrete relations build trust and discourage opportunistic behavior.

> Granovetter, M. (1985), Economic Action and Social Structure: The Problem of Embeddedness, American Journal of Sociology

## Market, hierarchy and network

Powell (1990) compared market, hierarchy and network as ways to organize economic activity.

| Feature | Market | Hierarchy | Network |
|---|---|---|---|
| Normative basis | Contract and property rights | Employment relationship | Complementary strengths |
| Means of communication | Prices | Routines | Relational |
| Conflict resolution | Haggling, courts for enforcement | Administrative fiat, supervision | Norm of reciprocity, reputation |
| Flexibility | High | Low | Medium |
| Commitment between parties | Low | Medium to high | Medium to high |
| Tone | Precision or suspicion | Formal, bureaucratic | Open-ended, mutual benefits |

> Powell, W. W. (1990), Neither Market nor Hierarchy: Network Forms of Organization, Research in Organizational Behavior 12

## The paradox of embeddedness

Uzzi (1997) studied relations among firms in the New York women's apparel industry and reported that embedded ties work differently from market transactions. Embedded ties have these features:

- (Trust) Gives flexibility the contract does not cover, such as adjusted payment timing or access to resources.
- (Fine-grained information transfer) Information that prices do not carry flows between firms, which eases planning and coordination.
- (Joint problem-solving) When problems arise, the parties adjust together instead of ending the deal.

The positive effects grow with embeddedness up to a threshold and then reverse. When relations become too closed, firms grow vulnerable to outside shocks and lose access to information beyond their network. `draw_uzzi_paradox(current_embeddedness=0.7)` draws this relation as a schematic inverted U. The curve and the threshold are set for illustration.

> Uzzi, B. (1997), Social Structure and Competition in Interfirm Networks: The Paradox of Embeddedness, Administrative Science Quarterly 42

## Two-mode networks

Relations between two different kinds of sets, such as people and activities (meetings, projects, boards), form a two-mode network.

- `load_from_incidence(affiliations)` builds a two-mode graph, a people-to-people projection and an activity-to-activity projection from an incidence matrix or from `{person: [activities]}` input.
- `draw_bipartite_network(result)` draws people as circles and activities as squares.
