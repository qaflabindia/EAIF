# Side-by-Side Comparison: EAGCF vs. ISO/IEC 42005 Crosswalk
## *ISO/IEC DIS 42005 AI System Impact Assessment ↔ NIST AI RMF 1.0*

**Source Document:** `ai-2025-00108_ISO_IEC_42005_to_NIST_AI_RMF_Crosswalk.pdf` (2025)
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** ISO/IEC 42005 is a developing international standard specifically for AI System Impact Assessment (ASIA) — distinct from ISO 42001 (management systems) and ISO 23894 (risk management). It covers the process of conducting structured impact assessments for AI systems, including scope definition, data information, algorithm/model information, impacts on individuals/society, and approval processes. The crosswalk maps ISO 42005 clauses to NIST AI RMF 1.0 functions, revealing that 42005 is primarily aligned with MAP and MEASURE functions, with significant gaps in MANAGE (all 4 functions unmapped). This is an impact assessment process standard — not a risk management or control standard.

---

## 1. Document Scope Alignment

| Dimension | ISO/IEC DIS 42005 | EAGCF |
|---|---|---|
| **Primary purpose** | Structured AI system impact assessment process | Enterprise AI governance and control operating model |
| **Document type** | International standard (Draft International Standard stage) | Voluntary enterprise framework wired to ISO 42001 |
| **Coverage depth** | Impact assessment process only — scope, data, algorithm, impacts, approval | 15 control domains, 9 enforcement points, 5-tier risk model, full lifecycle |
| **MANAGE function** | No coverage (all 4 MANAGE subcategories unmapped) | Full coverage: risk treatment, fallback, incident response, review cadences |
| **Certification path** | ISO standard — certifiable when finalized | ISO 42001 certification path |

---

## 2. ISO/IEC 42005 Clause-by-Clause vs. EAGCF

### GOVERN Function Mapping

| ISO 42005 Clause | AI RMF Function Mapped | EAGCF Coverage | Status |
|---|---|---|---|
| **5.1 General** (impact assessment process requirements) | GOVERN 1 | Part IV §4.2 (governance framework includes impact assessment as a required activity); Deliverable G §G.3 | ✅ Covered |
| **5.10 Recording and reporting** | GOVERN 1 | Part V §5.14 (LOG domain: evidence and logging requirements); Deliverable G §G.7 (assurance evidence pack) | ✅ Covered |
| **5.12 Monitoring and review** | GOVERN 1, MEASURE 3, MEASURE 4 | Part VII §7.1 (continuous monitoring); Part VI §6.6 (review cadences) | ✅ Covered |
| **5.6 Allocating responsibilities** | GOVERN 2, GOVERN 4 | Part VI §6.4 (RACI matrix); Part VI §6.2 (governance office: defined roles) | ✅ Covered |
| **5.4 Timing of AI system impact assessment** | GOVERN 4 | Part XIII §13.1 (CI/CD lifecycle gates: impact assessment is a required pre-deployment gate for Tier 1/2) | ✅ Covered |
| **5.11 Approval process** | GOVERN 2 | Part IV §4.6 (policy decision and approval model); Part XIII §13.1 (gate sign-off requirements) | ✅ Covered |
| *GOVERN 3* (Workforce diversity) | **No ISO 42005 mapping** | Part V §5.8 (FAI domain) — partial coverage from fairness perspective | ⚠️ Partial — N-01 confirmed |
| *GOVERN 6* (Supply chain) | **No ISO 42005 mapping** | Part V §5.9 (VND domain); Part V §5.11 (MSC domain) | ✅ Covered (EAGCF stronger than ISO 42005 here) |

### MAP Function Mapping

| ISO 42005 Clause | AI RMF Function Mapped | EAGCF Coverage | Status |
|---|---|---|---|
| **6.2 Scope of the ASIA** (purpose, boundaries) | MAP 1, MAP 2 | Deliverable G §G.5 (AI Use Case Registration: defines scope and boundary) | ✅ Covered |
| **6.3.1 AI system description** | MAP 2, MAP 3 | Deliverable G §G.5 (system description field); MDL-05 (model card) | ✅ Covered |
| **6.3.2 AI system functionalities and capabilities** | MAP 2, MAP 3 | Deliverable G §G.5; MDL-01 (benchmark: defines capability scope) | ✅ Covered |
| **6.3.3 AI system purpose** | MAP 1, MAP 3 | Deliverable G §G.5 (use case purpose and business justification) | ✅ Covered |
| **6.3.4 Intended use** | MAP 1, MAP 3 | Deliverable G §G.5 (intended use; in-scope user roles) | ✅ Covered |
| **6.3.5 Unintended uses** | MAP 3 | Deliverable G §G.3 (AI Impact Assessment: misuse scenarios section) | ✅ Covered |
| **6.4 Data information and quality** | MAP 2 | Part V §5.2 (DAT domain: 8 controls covering quality, lineage, governance) | ✅ Covered |
| **6.5 Algorithm and model information** | MAP 2 | Part V §5.3 (MDL domain); MDL-05 (model card: algorithm details) | ✅ Covered |
| **6.6.1 Geographical area and languages** | MAP 1 | Deliverable G §G.5 (deployment geography field); Part V §5.12 (cross-border jurisdiction domain) | ✅ Covered |
| **6.6.2 Deployment environment complexity** | MAP 1 | Deliverable G §G.5 (deployment environment section) | ✅ Covered |
| **6.7 Relevant interested parties** | MAP 1, GOVERN 5 | Deliverable G §G.3 (stakeholder identification); Part IV §4.3 | ⚠️ Partial — N-03 external stakeholder feedback gap |
| **6.8.1 General / 6.8.2 Benefits and harms** | MAP 5 | Deliverable G §G.3 (benefits vs. risks section) | ✅ Covered |
| **6.8.3 AI system failures and reasonably foreseeable misuse** | MAP 5 | Deliverable G §G.3 (failure mode analysis); Part IV §4.1 (Tier 0: prohibited misuse) | ✅ Covered |
| *MAP 4* (Third-party component risk mapping) | **No ISO 42005 mapping** | Part V §5.9 (VND domain); Part V §5.11 (MSC domain) | ✅ Covered (EAGCF stronger) |

### MEASURE Function Mapping

| ISO 42005 Clause | AI RMF Function Mapped | EAGCF Coverage | Status |
|---|---|---|---|
| **5.8 Performing the ASIA** | MEASURE 2 | Part XII §12.2 (control validation matrix — structured evaluation) | ✅ Covered |
| **6.8 Actual and reasonably foreseeable impacts** | MEASURE 2 | Deliverable G §G.3 (impact characterization section) | ✅ Covered |
| **6.8.3.3 Impact of reasonably foreseeable misuse** | MEASURE 2 | Deliverable G §G.3 (misuse risk section) | ✅ Covered |
| **5.9 Analysing the results of the ASIA** | MEASURE 3, MEASURE 4 | Part XII §12.2 (validation results analysis); Part VII §7.4 (corrective action) | ✅ Covered |
| *MEASURE 1* (Methods and metrics identification) | **No ISO 42005 mapping** | Part VII §7.2 (KPI/KRI/KCI framework); Part XII §12.2 | ✅ Covered (EAGCF stronger) |

### MANAGE Function: ISO 42005 Coverage Gap

| AI RMF Function | ISO 42005 Mapping | EAGCF Coverage |
|---|---|---|
| **MANAGE 1** (Prioritize, respond, manage risks) | **No ISO 42005 clause** | ✅ Part IV §4.1 (risk treatment tiers); Part VII §7.3 |
| **MANAGE 2** (Strategies to maximize benefits) | **No ISO 42005 clause** | ✅ Part XI §11.1 (proportional enforcement); Part VIII (adoption acceleration) |
| **MANAGE 3** (Third-party risk management) | **No ISO 42005 clause** | ✅ Part V §5.9 (VND domain); Part V §5.11 (MSC domain) |
| **MANAGE 4** (Risk treatment documentation and monitoring) | **No ISO 42005 clause** | ✅ Part VII §7.4 (corrective action); Part VI §6.6 (review cadences) |

**Key insight:** ISO 42005 focuses on *performing* the impact assessment, not on *managing* the risks it identifies. EAGCF's MANAGE coverage (Parts VII, VIII, XI) is substantially stronger than ISO 42005's scope.

---

## 3. ISO 42005 vs. EAGCF's AI Impact Assessment Template

EAGCF's Deliverable G §G.3 (AI Impact Assessment template) directly addresses ISO 42005's core purpose. A clause-by-clause alignment:

| ISO 42005 Clause | Deliverable G §G.3 Equivalent | Coverage |
|---|---|---|
| 5.1 General (process requirements) | Impact Assessment methodology section | ✅ |
| 5.4 Timing | Required gate: Tier 1 pre-deployment + material change | ✅ |
| 5.5/6.2 Scope definition | Use case scope and boundary fields | ✅ |
| 5.6 Responsibility allocation | Assessor role, approver role fields | ✅ |
| 5.8 Performing the assessment | Risk rating methodology | ✅ |
| 5.9 Analysing results | Findings and recommendations section | ✅ |
| 5.10 Recording and reporting | Deliverable G §G.7 (assurance evidence pack) | ✅ |
| 5.11 Approval process | Gate sign-off: governance body approval | ✅ |
| 5.12 Monitoring and review | Deliverable E monitoring signals; §7.1 review cadences | ✅ |
| 6.3.x System description, purpose, use, misuse | AI Use Case Registration (Deliverable G §G.5) | ✅ |
| 6.4 Data information and quality | Data governance section (DAT domain fields) | ✅ |
| 6.5 Algorithm/model information | MDL-05 model card (Deliverable G §G.6) | ✅ |
| 6.6 Geographical area/deployment environment | Deployment scope fields in registration | ✅ |
| 6.7 Interested parties | Stakeholder mapping section | ⚠️ Partial |
| 6.8 Impacts (benefits, harms, misuse) | Impact characterization table | ✅ |

**Full ISO 42005 alignment**: EAGCF's AI Impact Assessment template (§G.3) and AI Use Case Registration (§G.5) together cover substantially all of ISO 42005's process requirements. No new template fields required.

---

## 4. Scoring Summary

| ISO 42005 Area | Items | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| GOVERN function clauses | 8 | 6 | 1 | 1 | 0 |
| MAP function clauses | 14 | 12 | 1 | 1 | 0 |
| MEASURE function clauses | 5 | 5 | 1 | 0 | 0 |
| MANAGE function (ISO 42005 gaps) | 4 | 4 | 4 | 0 | 0 |
| **TOTALS** | **31 items** | **27 (87%)** | **7 (noted)** | **2 (6%)** | **0 (0%)** |

**Coverage interpretation:** 94% total coverage (87% direct + 6% partial). EAGCF not only covers ISO 42005 requirements but materially exceeds them in several dimensions — particularly MANAGE function coverage, supply chain governance (GOVERN 6 / MAP 4), and measurement methods (MEASURE 1). The two partial items are confirmed cross-document gaps (N-01 workforce diversity; N-03 external stakeholder feedback).

---

## 5. Recommended EAGCF Enhancement

| Enhancement ID | Source | Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N-42005-01** | ISO 42005 §6.5 | **Algorithm and model information in impact assessment**: When ISO/IEC 42005 is finalized, cross-reference EAGCF's AI Impact Assessment template (Deliverable G §G.3) and model card (§G.6) as ISO 42005 implementation artifacts. Add ISO 42005 to EAGCF's normative reference stack alongside ISO 42001 | Medium | Part IV §4.2 (normative references); Deliverable G introductory note |
| **N-42005-02** | ISO 42005 §6.7 | **Interested parties mapping in impact assessment**: Strengthen Deliverable G §G.3 to require explicit identification and documentation of all interested parties (not just affected users) who should be informed of or consulted on the impact assessment findings | Low | Deliverable G §G.3 — add interested parties field |

---

## 6. Synthesis

ISO/IEC 42005 is the impact assessment complement to ISO 42001 (management systems) and ISO 23894 (risk management). EAGCF's AI Impact Assessment template (Deliverable G §G.3) and AI Use Case Registration (Deliverable G §G.5) together form a comprehensive implementation of ISO 42005's process requirements.

**Critical observation:** ISO 42005 has no mapping to any of the four MANAGE subcategories. This reflects the standard's scope: it provides the assessment process but does not prescribe what to do with the results. EAGCF's MANAGE-equivalent capabilities (Parts VII, VIII, XI) are substantially stronger than ISO 42005's scope, making EAGCF a significantly more complete governance instrument.

When ISO/IEC 42005 is finalized (currently at DIS stage), adding it to EAGCF's normative reference stack alongside ISO 42001 would enable enterprises to claim compliance with the full suite of ISO AI standards: 42001 (management systems) + 23894 (risk method) + 42005 (impact assessment).

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Comparisons completed (16 sources): NIST AI 100-1, 100-2, 100-4, 100-5, 600-1, 700-1, 700-2, 800-1, 800-2, IR 8596; ISO 42001/23894 crosswalks; ISO 42005 crosswalk; OECD/EU AI Act crosswalk; Google DeepMind Gap Analysis; AI Verify crosswalks*
