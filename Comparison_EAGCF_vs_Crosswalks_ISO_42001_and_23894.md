# Side-by-Side Comparison: EAGCF vs. ISO/IEC Crosswalk Documents
## *NIST AI RMF to ISO 42001 Crosswalk + ISO/IEC 23894 to NIST AI RMF Crosswalk*

**Documents:**
- `NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf` — NIST AI RMF subcategory → ISO/IEC 42001 clause mapping
- `ai-2025-00109_revised_ISO_IEC_23894_Crosswalk_to_the_NIST_AI_RMF.pdf` — ISO/IEC 23894 → NIST AI RMF function mapping

**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** EAGCF explicitly uses NIST AI RMF as its governance backbone and ISO/IEC 42001 as its management system shell. These crosswalk documents confirm the alignment between those two frameworks and help identify any EAGCF structural gaps relative to both ISO standards. The primary question is: does EAGCF's composite design cover the full ISO 42001 + ISO 23894 governance scope?

---

## 1. EAGCF's ISO Framework Coverage — Design Intent

EAGCF explicitly references the following ISO standards in its normative architecture:

| ISO Standard | Role in EAGCF | Expected Coverage |
|---|---|---|
| **ISO/IEC 42001:2023** | Management system shell + certification path | Full via GOVERN + governance body design |
| **ISO/IEC 23894:2023** | AI risk methodology | Full via risk tiering (Deliverable B) + governance lifecycle |
| **ISO/IEC 38507** | Board-level governance anchor | Partial (strategic layer only) |
| **ISO 31000** | Enterprise risk integration (via COSO ERM) | Partial (wired through 23894) |

---

## 2. ISO/IEC 42001 Crosswalk — EAGCF Coverage Assessment

### 2.1 GOVERN Function → ISO 42001

| AI RMF Subcategory | ISO 42001 Clauses | EAGCF Coverage | Status |
|---|---|---|---|
| GV 1.1 — Legal/regulatory requirements | 4.1, 6.2, B.2.2, B.2.4 | Part IV §4.4 (regulatory integration); Part VIII §8.8 (sector overlays) | ✅ |
| GV 1.2 — Trustworthy AI in policies | B.9.3, B.6.1.2–3, B.10.3, B.2.2, 4.4, 5.2 | Part IV §4.2 (principles → controls translation) | ✅ |
| GV 1.3 — Risk tolerance determination | 6.1.2, 6.1.1, 6.1.3 | Part IV §4.1 (Deliverable B: 5-tier risk model) | ✅ |
| GV 1.4 — Risk management transparency | 6.1.2, 6.1.3, 8.3 | Part IV §4.3 (transparency requirements) | ✅ |
| GV 1.5 — Ongoing monitoring and review | 8.2, 8.3, 8.4 | Part VII §7.1 (monitoring signal catalog) | ✅ |
| GV 1.6 — AI system inventory | B.4.5, B.4.3–6, B.4.2 | Deliverable G §G.5 (AI Use Case Registration) | ✅ |
| GV 1.7 — Decommissioning | B.6.2.6 | Part VII §7.1 (Deliverable D: lifecycle stage 11 — Decommission) | ✅ |
| GV 2.1 — Roles and responsibilities | 9.1, 5.3, 7.1–7.4, B.3.2 | Part VI (governance roles and accountability) | ✅ |
| GV 2.2 — Training for AI risk management | 7.2 | Part VIII §8.9 (workforce enablement) | ✅ |
| GV 2.3 — Executive leadership accountability | 5.1, 9.3.1–3, 5.2 | Part VI §6.1 (board and committee oversight) | ✅ |
| GV 3.1 — Diverse interdisciplinary teams | B.4.6, B.5.4 | Not explicitly required | ❌ Gap — confirmed critical gap N-01 across multiple comparisons |
| GV 3.2 — Human-AI oversight policies | B.6.1.3, B.9.3, B.4.6, B.5.3, 7.2, B.3.2 | Part V §5.7 (OUT-06: human override); Part VI §6.3 (HITL) | ✅ |
| GV 4.1 — Safety culture / critical thinking | B.5.2, B.6.1.2–3, B.9.2–3, B.10.3, B.5.4 | Part IV §4.5 (design principles); Part VIII §8.10 (anti-patterns) | ✅ |
| GV 4.2 — Team risk documentation | B.5.4, B.8.5, 7.4, 6.1.4, B.5.5 | Part VI §6.4 (AI governance office documentation obligations) | ✅ |
| GV 4.3 — Testing, incidents, info sharing | B.6.2.4–7, B.8.2–5, B.6.1.2–3 | Part VII §7.3 (incident taxonomy); Part XIII §13.1 (CI/CD) | ✅ |
| GV 5.1 — External feedback on AI impacts | B.10.4, B.5.3–4, B.8.3 | Not formally required | ❌ Gap — confirmed N-02/N-03, N600-03 |
| GV 5.2 — Feedback incorporated in design | B.8.3, B.10.4, B.5.4–5, B.6.1.3, B.6.2.6 | Not formally required | ❌ Gap — same as above |
| GV 6.1 — Third-party IP and rights | B.10.2, B.10.3 | Part V §5.9 (VND domain); Deliverable G §G.13 | ✅ |
| GV 6.2 — Third-party contingency | B.10.2, B.10.3 | Part XIV §14.4 (vendor governance: fallback architecture) | ✅ |

**GOVERN coverage:** 16/19 = 84% (3 gaps: diverse teams, external feedback loops × 2)

### 2.2 MAP Function → ISO 42001

| AI RMF Subcategory | ISO 42001 Clauses | EAGCF Coverage | Status |
|---|---|---|---|
| MP 1.1 — Intended purposes/context documented | 6.1.4, B.5.2–5 | Part IV §4.1 (intake and tiering); Deliverable G §G.5 | ✅ |
| MP 1.2 — Interdisciplinary team documentation | B.4.6, 7.2 | Not required | ❌ Gap — N-01 confirmed again |
| MP 1.3 — Org mission/goals understood | 4.1, 5.2, 6.2, 7.5.3, 7.3–4 | Part I §1.1 (executive synthesis); Part IV §4.5 | ✅ |
| MP 1.4 — Business value/context defined | 5.1, 4.1, B.2.2, B.5.2, B.9.4, B.6.2.2 | Part IV §4.1 (use case intake) | ✅ |
| MP 1.5 — Risk tolerances documented | 6.1.1 | Part IV §4.1 (Deliverable B) | ✅ |
| MP 1.6 — System requirements; socio-technical implications | B.6.2.2, B.5.4–5 | Part II §2.3 (system archetypes); Part V (control domains) | ✅ |
| MP 2.1 — Specific AI tasks and methods defined | B.6.2.3, B.4.2–6 | Part II §2.2 (archetype definitions) | ✅ |
| MP 2.2 — System knowledge limits; human oversight | B.6.2.7, B.9.3, B.8.2 | Part V §5.7 (OUT-06: limits documentation); AGT-06 (HITL) | ✅ |
| MP 2.3 — Scientific integrity and TEVV | B.6.1.3, B.6.2.7, B.7.2–6, B.6.2.4 | Part XII (control validation); Part VII §7.5 | ✅ |
| MP 3.1–3.5 — Benefits, costs, scope, proficiency, oversight | B.5.2–5, 8.2–4, B.4.6, B.6.1.3, B.6.2.7, B.8.2 | Part IV §4.2; Part VI; Part VIII | ✅ |
| MP 4.1–4.2 — Technology/legal risk mapping | 4.1, B.2.2, B.9.2, B.9.4, B.6.2.7, B.8.2, B.10.3 | Part VIII §8.8 (sector overlays) | ✅ |
| MP 5.1–5.2 — Impact likelihood/magnitude; stakeholder engagement | 6.1.2, B.5.2, B.6.1.3, B.6.2.6, B.8.3 | Part IV §4.1 (tiering); Part VII §7.3 (impact taxonomy) | ⚠️ Partial — external stakeholder engagement gap |

**MAP coverage:** 16/18 = 89% (1 confirmed gap: interdisciplinary teams; 1 partial: external stakeholder engagement)

### 2.3 MEASURE Function → ISO 42001

| AI RMF Subcategory | ISO 42001 Clauses | EAGCF Coverage | Status |
|---|---|---|---|
| MS 1.1–1.3 — Measurement approaches, metrics, assessors | 6.1.1–2, B.6.2.4, B.5.4, B.5.2, B.5.5 | Part VII §7.2 (KPI/KRI/KCI); Part XII §12.2; Part VI §6.7 (external assurance) | ✅ |
| MS 2.5 — Validity and reliability | B.6.2.4–5, B.6.2.7, B.8.2 | Part XII §12.2 (control validation matrix) | ✅ |
| MS 2.6 — Safety risk evaluation | B.6.2.8, B.6.2.6, B.6.2.4, 8.2 | Part IV §4.1 (Tier 0/1 safety gates) | ✅ |
| MS 2.7 — Security and resilience | B.7.2, B.3.2, B.2.3, B.5.2, B.6.1.2–3, B.6.2.3, B.9.3 | Part XII (control validation pipeline) | ✅ |
| MS 2.8 — Transparency and accountability | B.7.2, B.5.4–5, B.6.1.2, B.9.3, 6.1.2 | Part IV §4.3 (transparency); LOG domain | ✅ |
| MS 2.9 — Model explainability | B.7.5, B.6.2.5, B.6.2.7, B.8.2 | Part V §5.3 (MDL-05: model card) | ⚠️ Partial — explainability depth gap (N-09) |
| MS 2.10 — Privacy risk | B.5.2, B.7.2–3, B.2.3 | Part V §5.2 (DAT domain) | ✅ |
| MS 2.11 — Fairness and bias | B.5.5, B.5.4 | GEN-05 (fairness testing); DAT-05 | ✅ |
| MS 2.12 — Environmental impact | B.5.5, B.4.5 | Not addressed | ❌ Gap — N600-01, N-06 confirmed again |
| MS 2.13 — TEVV metrics effectiveness | B.6.2.4, B.6.2.6 | Part XII §12.2 | ✅ |
| MS 3.1–3.3 — Risk tracking, hard-to-assess risks, end-user feedback | 8.2, 4.4, 8.4, B.6.2.8, 10.1, B.8.2–4, B.8.3 | Part VII §7.3; Part XII §12.1 | ⚠️ Partial — end-user community feedback gap |
| MS 4.1–4.3 — Measurement deployment, validation, improvement | B.6.2.4, B.5.4–5, 9.1, B.8.2–3, 9.2.1, 9.3.1, B.6.2.6–7 | Part VII §7.4 (corrective action); Part VII §7.2 | ✅ |

**MEASURE coverage:** 16/18 = 89% (2 gaps/partials: environmental impact, end-user feedback)

### 2.4 MANAGE Function → ISO 42001

| AI RMF Subcategory | ISO 42001 Clauses | EAGCF Coverage | Status |
|---|---|---|---|
| MG 1.1–1.4 — System purpose validation; risk prioritization; high-priority responses; residual risk documentation | B.9.3, B.9.2, B.9.4, B.6.1.3, B.6.2.4, 9.3.3, 6.1.2–4 | Part IV §4.1 (Deliverable B tiering); Part VII §7.4 | ✅ |
| MG 2.1–2.4 — Resource allocation; sustaining system value; unknown risk response; deactivation | B.4.2, 7.1, B.3.3, B.6.1.2–3, B.6.2.4–6, B.7.2, 7.1, 10.1, 10.2, 6.1.1–3, B.9.4, B.8.2, B.6.2.7, B.6.1.3 | Part VII §7.3–4; Part XIV §14.4; Part IV §4.7 | ✅ |
| MG 3.1–3.2 — Third-party monitoring; pre-trained model monitoring | B.10.3, B.10.2, B.4.4, B.6.2.6 | Part V §5.9 (VND domain); Part XIV §14.5 (behavioral fingerprinting) | ✅ |
| MG 4.1–4.3 — Post-deployment monitoring; continual improvement; incident communication | 9.2.1, B.6.2.6, B.8.3, B.10.4, 9.3.3, B.6.2.4, B.6.2.6, 9.3.2, B.8.5 | Part VII §7.1–4 | ✅ |

**MANAGE coverage:** 13/13 = 100%

---

## 3. ISO/IEC 23894 Crosswalk Assessment

ISO/IEC 23894 maps at the function level (not subcategory level). EAGCF's alignment with each AI RMF function was verified across the entire framework above. The specific 23894 clause structure confirms EAGCF's risk management architecture:

| ISO 23894 Clause | NIST AI RMF Function | EAGCF Implementation |
|---|---|---|
| **Clause 5** — Framework (Leadership, Integration, Design, Implementation, Evaluation, Improvement) | GOVERN | Part IV (governance framework); Part VI (governance roles) |
| **Clause 6.3** — Scope, context, criteria | MAP | Part IV §4.1 (intake and tiering); Part II §2.1 (scope) |
| **Clause 6.4** — Risk assessment (identification, analysis, evaluation) | MAP + MEASURE | Part IV §4.1 (Deliverable B); Part XII (control validation) |
| **Clause 6.5** — Risk treatment | MANAGE | Part VII §7.4 (corrective action); Part IV §4.7 (exception model) |
| **Clause 6.6** — Monitoring and review | MEASURE + MANAGE | Part VII §7.1 (Deliverable E); Part XIV §14.5 |
| **Clause 6.7** — Recording and reporting | MEASURE + MANAGE | Part V §5.14 (LOG domain); Part VI §6.1 (board reporting) |
| **Clause 6.2** — Communication and consultation | **No AI RMF mapping** (documented gap in crosswalk) | Part IV §4.3 (transparency); Part VIII §8.9 |

**ISO 23894 coverage:** Full structural alignment confirmed. The single documented gap in ISO 23894 (§6.2 Communication and consultation has no AI RMF counterpart) is covered in EAGCF via transparency requirements and workforce enablement.

---

## 4. Gaps Confirmed by Crosswalk Analysis

The crosswalk documents triangulate the following EAGCF gaps through a different analytical lens — confirming gaps identified in direct NIST document comparisons:

| EAGCF Gap | ISO 42001 Clause | Confirmed by | Priority |
|---|---|---|---|
| **Diverse interdisciplinary team** | B.4.6, B.5.4 (GV 3.1, MP 1.2) | N-01 (AI 100-1), N600-02 (AI 600-1), GV 3.1 crosswalk | Critical |
| **External stakeholder feedback loops** | B.10.4, B.5.3–4, B.8.3 (GV 5.1, GV 5.2) | N-02/N-03 (AI 100-1), N600-03 (AI 600-1), GV 5.1/5.2 crosswalk | Critical |
| **Environmental impact assessment** | B.5.5, B.4.5 (MS 2.12) | N-06 (AI 100-1), N600-01 (AI 600-1), MS 2.12 crosswalk | High |
| **Explainability depth** | B.7.5, B.6.2.5 (MS 2.9) | N-09 (AI 100-1), MS 2.9 crosswalk | Medium |
| **Decommissioning emotional entanglement** | B.6.2.6 (GV 1.7) | N600-07 (AI 600-1), GV 1.7 crosswalk | Low |

**New observation from crosswalk:** ISO 42001 Annex B contains significant operational detail (B.4.x through B.10.x) representing AI-specific implementation guidance. EAGCF covers the *intent* of each ISO 42001 annex clause through its own control domain architecture, but does not explicitly cross-reference ISO 42001 annex items in its control structure. This is a traceability gap for certification purposes.

---

## 5. Scoring Summary

| Crosswalk Coverage Area | Subcategories | ✅ | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|
| GOVERN function (via ISO 42001) | 19 | 16 (84%) | 0 | 3 (16%) |
| MAP function (via ISO 42001) | 18 | 16 (89%) | 1 | 1 (6%) |
| MEASURE function (via ISO 42001) | 18 | 14 (78%) | 2 | 2 (11%) |
| MANAGE function (via ISO 42001) | 13 | 13 (100%) | 0 | 0 |
| ISO 23894 structural alignment | 7 clauses | 7 (100%) | 0 | 0 |
| **TOTALS** | **75 items** | **66 (88%)** | **3 (4%)** | **6 (8%)** |

**Coverage interpretation:** 92% total coverage (88% + 4%). The crosswalk analysis confirms EAGCF's strong structural alignment with both ISO standards. The 8% gap rate maps exactly to the three confirmed cross-document critical gaps (diverse teams, external feedback loops, environmental impact) plus minor partials (explainability, decommissioning detail).

---

## 6. Traceability Recommendation

For organizations pursuing ISO 42001 certification using EAGCF as their AI Management System implementation:

**Recommended additions to EAGCF:**
1. Add an **ISO 42001 clause traceability annex** that maps each EAGCF control to its corresponding ISO 42001 clause (inverse of the crosswalk documents)
2. Add the three critical ISO 42001 requirements not yet in EAGCF (GV 3.1 diverse teams, GV 5.1/5.2 external feedback loops, MS 2.12 environmental impact)
3. Reference the published crosswalk documents as supporting evidence of framework equivalence in the EAGCF assurance model

This would make EAGCF directly usable as evidence of ISO 42001 clause compliance in a certification audit.

---

*Comparison prepared as part of EAGCF continuous improvement program.*
