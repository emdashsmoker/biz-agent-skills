# 근거 문헌

## 설계

| 문헌 | 요지 | 사용 위치 |
|------|-----------|-----------|
| Baker, R. 외(2013), Summary Report of the AAPOR Task Force on Non-probability Sampling, Journal of Survey Statistics and Methodology 1(2)(https://doi.org/10.1093/jssam/smt008) | 비확률표본은 대상별 선정 확률을 알 수 없어 확률표본 방식의 오차범위를 산출할 근거가 없다. 결과 해석에는 모집 방식과 가정의 명시가 필요하다 | design.md 표본 유형, reporting.md 수치 문장 |
| Cochran, W. G.(1977), Sampling Techniques 3rd ed., Wiley | 비율 추정을 위한 표본 크기 식과 유한 모집단 보정 식을 제시한다 | design.md 정밀도 기준 표본 크기 |
| Cohen, J.(1992), A Power Primer, Psychological Bulletin 112(1)(https://doi.org/10.1037/0033-2909.112.1.155) | 효과크기를 작음, 중간, 큼(d = 0.2, 0.5, 0.8)으로 구분하고 검정력 80% 기준의 필요 표본을 제시한다 | design.md 비교 기준 표본 크기 |
| Hesterberg, T.(2008), It's Time to Retire the "n >= 30" Rule, Proceedings of the Joint Statistical Meetings(https://research.google/pubs/pub34906/) | n ≥ 30 경험칙은 치우친 자료에서 정규 근사의 정확도를 보장하지 못한다. 부트스트랩 기반 점검을 권고한다 | design.md 30명 표본의 충분성, analysis.md 비교 방법 |
| Groves, R. M.(2006), Nonresponse Rates and Nonresponse Bias in Household Surveys, Public Opinion Quarterly 70(5)(https://doi.org/10.1093/poq/nfl033) | 무응답은 편향을 유발할 수 있으나 항상 유발하지는 않는다. 편향의 크기는 무응답 비율과 응답자 및 무응답자 간 차이의 곱으로 표현된다 | design.md 무응답 |
| Groves, R. M. & Peytcheva, E.(2008), The Impact of Nonresponse Rates on Nonresponse Bias: A Meta-Analysis, Public Opinion Quarterly 72(2)(https://doi.org/10.1093/poq/nfn011) | 무응답 편향을 직접 추정한 59개 방법론 연구를 종합한 결과 응답률과 편향의 관계는 약하게 나타났다 | design.md 무응답 |
| Guest, G., Bunce, A. & Johnson, L.(2006), How Many Interviews Are Enough? An Experiment with Data Saturation and Variability, Field Methods 18(1)(https://doi.org/10.1177/1525822X05279903) | 심층 인터뷰 60건을 분석한 결과 새로운 주제는 첫 12건 이내에서 포화되었고 주요 주제는 6건 시점에 이미 확인되었다 | design.md 인터뷰 수 |
| Norman, G.(2010), Likert Scales, Levels of Measurement and the "Laws" of Statistics, Advances in Health Sciences Education 15(5)(https://doi.org/10.1007/s10459-010-9222-y) | 1930년대 이후 연구를 검토하여 리커트 자료, 소표본, 비정규 분포에서도 모수 통계가 강건함을 제시한다 | design.md 문항 설계, analysis.md 비교 방법 |
| Krosnick, J. A.(1991), Response Strategies for Coping with the Cognitive Demands of Attitude Measures in Surveys, Applied Cognitive Psychology 5(3)(https://doi.org/10.1002/acp.2350050305) | 응답 부담이 증가하면 응답자는 충분한 숙고 없이 무난한 응답이나 동일한 응답을 선택하는 전략을 사용한다 | design.md 문항 설계 |
| Podsakoff, P. M. 외(2003), Common Method Biases in Behavioral Research: A Critical Review of the Literature and Recommended Remedies, Journal of Applied Psychology 88(5)(https://doi.org/10.1037/0021-9010.88.5.879) | 같은 응답자와 같은 방법으로 원인과 결과를 측정하면 관계가 과대 추정될 수 있다. 출처 분리, 배치 분리, 익명 보장 등 설계 단계의 대응 방안을 제시한다 | design.md 문항 설계 |

## 조사 유형

| 문헌 | 요지 | 사용 위치 |
|------|-----------|-----------|
| Martilla, J. A. & James, J. C.(1977), Importance-Performance Analysis, Journal of Marketing 41(1)(https://doi.org/10.1177/002224297704100112) | 속성별 중요도와 성과를 기준선으로 구분한 4분면에 배치하여 개선 우선순위를 결정한다 | survey-types.md 우선순위 도출 |
| Borich, G. D.(1980), A Needs Assessment Model for Conducting Follow-Up Studies, Journal of Teacher Education 31(3)(https://doi.org/10.1177/002248718003100310) | 역량별 중요도와 현재 수준의 차이에 중요도 평균을 곱한 가중 불일치 점수로 교육 요구의 순위를 산출한다 | survey-types.md 우선순위 도출 |
| DARPA, The Heilmeier Catechism(8문항 정리 참고 https://techtransferfordefense.stanford.edu/creating-impactful-one-pagers-using-heilmeier-catechism) | 연구 제안 평가를 위한 8개 질문으로 목표, 현행 방식의 한계, 새로운 점, 수요자와 기대 변화, 위험, 비용, 기간, 중간 및 최종 점검을 질문한다 | survey-types.md 하일마이어 문답 |
| Pier, E. L. 외(2018), Low Agreement among Reviewers Evaluating the Same NIH Grant Applications, PNAS 115(12)(https://doi.org/10.1073/pnas.1714379115) | 이미 연구비를 지원받은 제안서 25건을 심사위원 43명이 재평가한 결과 점수와 강약점 판단 모두에서 평가자 간 일치가 나타나지 않았다 | survey-types.md 평가 |
| Saaty, T. L.(1980), The Analytic Hierarchy Process, McGraw-Hill | 계층분석법의 일관성 지수와 행렬 크기별 무작위 지수를 제시한다 | analysis.md 측정 품질 |
| Saaty, T. L.(1990), How to Make a Decision: The Analytic Hierarchy Process, European Journal of Operational Research 48(1)(https://doi.org/10.1016/0377-2217(90)90057-I) | 쌍대비교로 가중치를 구하는 절차와 일관성 비율 10% 이하 기준을 제시한다 | survey-types.md 기준 가중치 |
| Saaty, T. L. & Ozdemir, M. S.(2003), Why the Magic Number Seven Plus or Minus Two, Mathematical and Computer Modelling 38(3-4)(https://doi.org/10.1016/S0895-7177(03)90083-5) | 한 묶음의 비교 항목이 7개를 초과하면 불일치 원인의 식별이 어려워지므로 7개 이하를 권고한다 | survey-types.md 기준 가중치 |
| Aczél, J. & Saaty, T. L.(1983), Procedures for Synthesizing Ratio Judgements, Journal of Mathematical Psychology 27(1)(https://doi.org/10.1016/0022-2496(83)90028-7) | 복수 판단자의 비율 판단을 통합하는 방법으로 기하평균을 도출한다 | survey-types.md 기준 가중치 |
| Pöppelbuß, J. & Röglinger, M.(2011), What Makes a Useful Maturity Model? A Framework of General Design Principles for Maturity Models and Its Demonstration in Business Process Management, ECIS 2011 Proceedings(https://aisel.aisnet.org/ecis2011/28) | 성숙도 모델이 갖추어야 할 일반 설계 원칙을 기본 요소, 현재 수준 진단, 개선 처방의 용도별로 정리한다 | survey-types.md 진단형 설문 |
| Cronbach, L. J.(1951), Coefficient Alpha and the Internal Structure of Tests, Psychometrika 16(3)(https://doi.org/10.1007/BF02310555) | 복수 문항이 동일한 대상을 측정하는 정도를 나타내는 내적 일관성 계수를 제시한다 | survey-types.md 점수 계산, analysis.md 측정 품질 |

## 분석

| 문헌 | 요지 | 사용 위치 |
|------|-----------|-----------|
| Delacre, M., Lakens, D. & Leys, C.(2017), Why Psychologists Should by Default Use Welch's t-test Instead of Student's t-test, International Review of Social Psychology 30(1)(https://doi.org/10.5334/irsp.82) | 등분산 가정이 성립하지 않으면 스튜던트 t검정의 오류가 증가한다. 웰치 t검정은 가정이 성립할 때도 손실이 작아 기본 방법으로 적합하다 | analysis.md 비교 방법 |
| Delacre, M. 외(2019), Taking Parametric Assumptions Seriously: Arguments for the Use of Welch's F-test instead of the Classical F-test in One-Way ANOVA, International Review of Social Psychology 32(1)(https://doi.org/10.5334/irsp.198) | 세 집단 이상의 평균 비교에서 웰치 분산분석을 기본 방법으로 권고한다 | analysis.md 비교 방법 |
| Benjamini, Y. & Hochberg, Y.(1995), Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing, Journal of the Royal Statistical Society Series B 57(1)(https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) | 여러 검정을 할 때 유의 판정 중 거짓 발견의 비율을 통제하는 보정 방법을 제시한다 | analysis.md 다중비교 |
| Wasserstein, R. L. & Lazar, N. A.(2016), The ASA Statement on p-Values: Context, Process, and Purpose, The American Statistician 70(2)(https://doi.org/10.1080/00031305.2016.1154108) | 미국통계학회가 발표한 p값 6원칙이다. p값은 자료와 특정 모형의 불일치 정도를 나타내며 가설이 참일 확률이나 효과의 크기를 나타내지 않는다. 의사결정은 기준선 통과 여부만으로 내리지 않으며 분석 전체를 투명하게 보고해야 한다 | analysis.md 해석 기준 |
| Barnett, A. G., van der Pols, J. C. & Dobson, A. J.(2005), Regression to the Mean: What It Is and How to Deal with It, International Journal of Epidemiology 34(1)(https://doi.org/10.1093/ije/dyh299) | 극단적 측정치로 선정된 대상을 재측정하면 평균 방향으로 회귀하여 실제 변화처럼 보일 수 있다. 설계와 분석 단계의 대응 방안을 제시한다 | analysis.md 해석 기준 |
| Shrout, P. E. & Fleiss, J. L.(1979), Intraclass Correlations: Uses in Assessing Rater Reliability, Psychological Bulletin 86(2)(https://doi.org/10.1037/0033-2909.86.2.420) | 평가자 신뢰도를 측정하는 급내상관계수의 유형과 계산식을 제시한다 | analysis.md 측정 품질 |

## 보고

| 문헌 | 요지 | 사용 위치 |
|------|-----------|-----------|
| Huff, D.(1954), How to Lie with Statistics, W. W. Norton. 국역본 『새빨간 거짓말, 통계』(https://dl.nanet.go.kr/detail/MONO12022000010027) | 편향된 표본, 선별된 평균, 누락된 수치, 무의미한 차이, 과장된 그래프, 면적 그림, 대상이 바뀐 수치, 선후 관계의 인과 해석, 기준 변경을 사례로 설명한다. 통계 해석 시 확인할 다섯 질문을 제시한다 | reporting.md 왜곡 점검 |
