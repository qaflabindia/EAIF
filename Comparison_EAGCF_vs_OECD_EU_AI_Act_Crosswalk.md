# Side-by-Side Comparison: EAGCF vs. OECD/EU AI Act Crosswalk
## *Mapping NIST AI RMF Trustworthiness Characteristics to International Policy Frameworks*

**Source Document:** `crosswalk_AI_RMF_1_0_OECD_EO_AIA_BoR.pdf` (NIST, 2023)
**Frameworks Mapped:** NIST AI RMF 1.0 Trustworthiness Characteristics ↔ OECD Recommendation on AI | EU AI Act (Proposed) | EO 13960 (Promoting the Use of Trustworthy AI in the Federal Government) | Blueprint for an AI Bill of Rights
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** This crosswalk document is a 2-page alignment table showing how NIST AI RMF's 7 trustworthiness characteristics map to 4 international/U.S. policy frameworks. It is a *characteristics-level* crosswalk — not a control-level or subcategory-level mapping. Its primary governance value to EAGCF is: (1) confirming that EAGCF's trustworthiness architecture aligns with the global regulatory landscape; (2) identifying where EAGCF's design-by-choice exclusions (e.g., restricting OECD to a single footnote) may need signposting for cross-border enterprises; (3) flagging where EU AI Act obligations are anchored in specific trustworthiness characteristics.

---

## 1. Document Scope and Structure

| Dimension | OECD/EU AI Act Crosswalk | EAGCF |
|---|---|---|
| **Document type** | Characteristics-level alignment crosswalk (2 pages) | Enterprise governance and control operating model |
| **Coverage granularity** | 7 trustworthiness characteristics → 4 frameworks | 15 control domains, 9 enforcement points, 5-tier risk model, 11-stage lifecycle |
| **Regulatory scope** | International policy (OECD), EU law (EU AI Act), U.S. EO, U.S. civil rights framework | Enterprise-agnostic; sector overlays for fin, health, safety-critical |
| **Binding nature** | Reference document; EU AI Act is legally binding in EU; OECD and Blueprint are non-binding | Voluntary enterprise standard; ISO 42001-certifiable |
| **Control depth** | None — maps principles/requirements, no control specifications | Full control architecture with implementation guidance |
| **Audience** | AI developers, policymakers, standards bodies | Board, CRO, governance office, internal audit, compliance |

---

## 2. The 7 NIST AI RMF Trustworthiness Characteristics vs. EAGCF Coverage

### 2.1 Valid and Reliable

| Policy Framework Requirement | EAGCF Coverage | Status |
|---|---|---|
| **OECD:** AI systems should be accurate, robust, and responsive throughout their lifecycle | Part V §5.3 (MDL domain: drift, degradation, benchmark controls); Part XII §12.2 (control validation matrix) | ✅ Covered |
| **EU AI Act:** High-risk AI accuracy, robustness, and cybersecurity requirements (Art. 15); accuracy metrics in technical documentation | Part IV §4.1 (5-tier risk model); Part V §5.3 (MDL-01 through MDL-10); Part XII §12.2 | ✅ Covered |
| **EO 13960:** Accuracy, reliability requirements for federal AI use | Part XII §12.2 (accuracy thresholds); Part VII §7.2 (KPI/KRI/KCI) | ✅ Covered |
| **Blueprint for AI Bill of Rights:** Algorithmic discrimination protections through testing and validation | Part V §5.8 (FAI domain: bias testing, fairness metrics) | ✅ Covered |

### 2.2 Safe

| Policy Framework Requirement | EAGCF Coverage | Status |
|---|---|---|
| **OECD:** AI systems should be safe throughout their lifecycle; operators should manage risks | Part IV §4.1 (Tier 0/1 risk gates — prohibited and high-risk controls); Part XI (enforcement architecture) | ✅ Covered |
| **EU AI Act:** Prohibited AI practices (Art. 5); high-risk classification with safety requirements (Art. 9–15); post-market monitoring (Art. 61) | Part IV §4.1 (Tier 0: Prohibited; Tier 1: High); Part XIII §13.1 (CI/CD lifecycle gates); Part VII §7.1 (post-deployment monitoring) | ✅ Covered |
| **EO 13960:** Safety evaluation requirements for federal AI systems | Part XII §12.1 (red-team pipeline); Part XII §12.2 (control validation) | ✅ Covered |
| **Blueprint for AI Bill of Rights:** Safe and effective systems — pre-deployment testing, ongoing monitoring | Part XII §12.1–12.2; Part VII §7.1 | ✅ Covered |

### 2.3 Secure and Resilient

| Policy Framework Requirement | EAGCF Coverage | Status |
|---|---|---|
| **OECD:** AI systems should be protected from adversarial attacks, data poisoning, and misuse | Part V §5.11 (MSC domain); Part XI (EP-1 through EP-9); Part XII §12.1 (red-team adversarial testing) | ✅ Covered |
| **EU AI Act:** Cybersecurity requirements for high-risk AI (Art. 15.5); resilience to attacks | Part XI (enforcement architecture); Part XII §12.1 | ✅ Covered |
| **EO 13960:** Secure and resilient AI design and operation | Part XI; Part V §5.4 (PRM domain) | ✅ Covered |
| **Blueprint for AI Bill of Rights:** Data privacy and security protections | Part V §5.2 (DAT domain: 8 controls); Part V §5.8 (identity/access controls) | ✅ Covered |

### 2.4 Accountable and Transparent

| Policy Framework Requirement | EAGCF Coverage | Status |
|---|---|---|
| **OECD:** Developers and deployers should be accountable; mechanisms for affected parties to seek redress | Part VI §6.1–6.7 (governance forums, RACI, decision rights); Part IV §4.8 (assurance model) | ✅ Covered |
| **EU AI Act:** Transparency obligations for high-risk AI (Art. 13); human oversight obligations (Art. 14); fundamental rights impact assessments | Part IV §4.3 (transparency and disclosure); Part V §5.7 (OUT domain: labeling, factuality) | ⚠️ Partial |
| **EO 13960:** Transparency and accountability in federal AI | Part IV §4.3; Part XIV §14.1 (governance attestation dashboard) | ✅ Covered |
| **Blueprint for AI Bill of Rights:** Notice and explanation of automated decision-making; human alternatives and fallback | Part V §5.7 (OUT-05/06: human override; explanation requirement); Part VI §6.3 | ✅ Covered |

*Partial note: EU AI Act fundamental rights impact assessment (FRIA) under Art. 27 is not explicitly required in EAGCF; the AI Impact Assessment (Deliverable G §G.3) covers similar ground but is not framed as a rights-impact assessment.*

### 2.5 Explainable and Interpretable

| Policy Framework Requirement | EAGCF Coverage | Status |
|---|---|---|
| **OECD:** AI actors should enable human understanding of AI systems and their outputs | Part V §5.3 (MDL-05: model card — includes explainability); Part V §5.7 (OUT-03: output factuality) | ⚠️ Partial |
| **EU AI Act:** Explainability requirements for high-risk AI; instructions for use must enable operators to interpret outputs (Art. 13.3.b.ii) | Part V §5.3 (MDL-05); Deliverable G §G.5 (AI Use Case Registration — use documentation) | ⚠️ Partial |
| **EO 13960:** Explainable AI principles for federal use | Part V §5.3 (MDL-05) | ⚠️ Partial |
| **Blueprint for AI Bill of Rights:** Explanation of automated decision-making at point of decision; meaningful explanation to affected individuals | Part V §5.7 (OUT-03); Part VI §6.3 (human-in-the-loop with explanation) | ⚠️ Partial |

*Consistent partial: EAGCF gap N-09 (confirmed in NIST AI 100-1 and 100-5 comparisons) — no formal explainability measurement technique requirement; model card includes explainability field but does not mandate a specific method or required reading level for end-user explanations.*

### 2.6 Privacy-Enhanced

| Policy Framework Requirement | EAGCF Coverage | Status |
|---|---|---|
| **OECD:** AI actors should respect privacy and data protection throughout lifecycle | Part V §5.2 (DAT domain: 8 data/privacy controls); Deliverable G §G.8 (Data Protection Impact Assessment) | ✅ Covered |
| **EU AI Act:** GDPR compliance presumed; additional privacy requirements for biometric and special category data (Art. 10.5) | Part V §5.2; Part VIII §8.2 (sector overlay: healthcare) | ⚠️ Partial |
| **EO 13960:** Privacy protection in federal AI; data minimization | Part V §5.2 (DAT-02: data minimization; DAT-03: retention controls) | ✅ Covered |
| **Blueprint for AI Bill of Rights:** Data privacy protections; consent for surveillance and tracking; minimization requirements | Part V §5.2 (DAT domain); Part V §5.9 (IAM domain) | ✅ Covered |

*Partial note: EU AI Act biometric and real-time remote identification prohibitions/restrictions (Art. 5.1.d/e) are beyond EAGCF's enterprise scope; addressed at Tier 0 (Prohibited) categorically but not with specific biometric identification provisions.*

### 2.7 Fair — Bias Managed

| Policy Framework Requirement | EAGCF Coverage | Status |
|---|---|---|
| **OECD:** AI actors should make reasonable efforts to minimize biases; promote fairness | Part V §5.8 (FAI domain: FAI-01 through FAI-06: bias testing, fairness metrics, disparate impact) | ✅ Covered |
| **EU AI Act:** Non-discrimination requirements (Recital 44); bias management for training data (Art. 10.2.f) | Part V §5.8 (FAI domain); Part V §5.2 (DAT-01: data governance — bias filtering) | ✅ Covered |
| **EO 13960:** Bias and fairness for federal AI; algorithmic impact assessment requirements | Part V §5.8; Deliverable G §G.3 (AI Impact Assessment includes bias assessment section) | ✅ Covered |
| **Blueprint for AI Bill of Rights:** Algorithmic discrimination protections; fairness testing before deployment and continuously | Part V §5.8 (FAI domain); Part XII §12.2 (continuous validation) | ✅ Covered |

---

## 3. Design-by-Choice Gap: OECD Deliberate Scope Restriction

EAGCF deliberately restricts OECD AI Principles to a single board-level footnote. This is a documented design decision, not a coverage gap.

| Coverage Dimension | Decision | Rationale |
|---|---|---|
| **OECD AI Principles as normative reference** | Restricted to footnote in Part IV §4.2 | OECD is an intergovernmental policy instrument; enterprise controls derive from NIST and ISO standards with legal standing or certification pathways, not from 47-country adherent political agreements |
| **OECD trustworthiness characteristics** | Indirectly covered via NIST AI RMF (which aligns to OECD) | NIST AI RMF 1.0 is itself derived partly from OECD AI Principles; covering NIST covers OECD substance |
| **Cross-border board reporting** | Single footnote footnote enables board-level cross-border policy context | Enough for enterprises to signal awareness without importing full OECD compliance language |

---

## 4. EU AI Act Fundamental Rights Impact Assessment (FRIA) Gap

The EU AI Act (Art. 27) requires deployers of high-risk AI affecting individuals in the EU to conduct a Fundamental Rights Impact Assessment. This is the one material functional gap relative to the crosswalk frameworks.

| FRIA Component | EAGCF Coverage | Gap |
|---|---|---|
| **Rights-impact framing** (Art. 27.1: identify, assess, mitigate risks to fundamental rights) | EAGCF's AI Impact Assessment (Deliverable G §G.3) covers safety, fairness, privacy — not explicitly "fundamental rights" | N-OECD-01: Add EU AI Act Art. 27 FRIA requirement as a governance gate for Tier 1 systems where EU deployment is in scope |
| **Deployment context documentation** | Deliverable G §G.3 (AI Impact Assessment) | ⚠️ Partial — present but not rights-framed |
| **Mandatory fields (Art. 27.2)**: deployer identity, use description, relevant fundamental rights, risk assessment steps, mitigation measures | Not all fields explicitly required | ⚠️ Partial |
| **FRIA submission to market surveillance authority** | Not addressed | Out of EAGCF scope (regulatory submission process, not internal governance) |

---

## 5. EO 13960 and Blueprint for AI Bill of Rights: EAGCF Position

Both are U.S. non-binding policy documents. EAGCF's coverage is functionally complete.

| Framework | EAGCF Alignment | Notable Items |
|---|---|---|
| **EO 13960** (Promoting Trustworthy AI in Federal Government) | Strong — all 9 federal trustworthy AI principles mapped via NIST AI RMF backbone | Primarily federal agency-facing; enterprise relevance as a government contractor governance signal |
| **Blueprint for AI Bill of Rights** | Strong — 5 protections (Safe/Effective Systems, Algorithmic Discrimination Protections, Data Privacy, Notice and Explanation, Human Alternatives/Override) all implemented in EAGCF output controls and FAI domain | Most directly relevant for consumer-facing AI; EAGCF covers via OUT domain + FAI domain + AGT-06 (HITL thresholds) |

---

## 6. Scoring Summary

| Trustworthiness Characteristic | Policy Items Mapped | ✅ Covered | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|
| Valid and Reliable | 4 | 4 | 0 | 0 |
| Safe | 4 | 4 | 0 | 0 |
| Secure and Resilient | 4 | 4 | 0 | 0 |
| Accountable and Transparent | 4 | 3 | 1 | 0 |
| Explainable and Interpretable | 4 | 0 | 4 | 0 |
| Privacy-Enhanced | 4 | 3 | 1 | 0 |
| Fair — Bias Managed | 4 | 4 | 0 | 0 |
| **TOTALS** | **28 items** | **22 (79%)** | **6 (21%)** | **0 (0%)** |

**Coverage interpretation:** 100% of items are at least partially covered; 79% are fully addressed. The 21% partial rate is concentrated in two areas: (1) explainability, confirmed as a cross-document gap N-09; and (2) EU AI Act-specific requirements (FRIA, biometric provisions). No items are fully unaddressed.

---

## 7. Gap Items: Recommended EAGCF Additions

| Gap ID | Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N-OECD-01** | EU AI Act Art. 27 | **Fundamental Rights Impact Assessment (FRIA)**: For enterprises deploying Tier 1 AI systems to individuals in the EU, add a FRIA requirement as a governance gate, with documentation template aligned to Art. 27.2 mandatory fields. Frame as a jurisdiction-specific delta on the standard AI Impact Assessment | High (EU-scoped) | Part IV §4.1 (Tier 1 gate) or Part VIII §8.8 (sector/jurisdiction overlays) — add EU jurisdiction delta |
| **N-OECD-02** | EU AI Act Art. 13.3.b.ii | **Operator-interpretability documentation**: Extend AI Use Case Registration (Deliverable G §G.5) and model card (MDL-05) to include a mandatory field describing how operators interpret AI outputs in the context of the specific use case — not just explainability in general, but operator-facing interpretation guidance | Medium | Deliverable G §G.5 and Part V §5.3 (MDL-05) |

---

## 8. Synthesis

The OECD/EU AI Act crosswalk confirms that EAGCF's trustworthiness architecture is well-aligned with the international AI governance landscape. The 7 NIST AI RMF trustworthiness characteristics — which form the organizing spine of this crosswalk — are all substantively implemented in EAGCF's 15 control domains.

**Key findings:**
1. EAGCF's deliberate design to anchor on NIST and ISO (with OECD as footnote only) is well-supported: NIST AI RMF carries OECD substance into EAGCF's control architecture
2. The explainability gap (N-09, confirmed across NIST AI 100-1, 100-5, and now this crosswalk) is the most persistent partial coverage
3. EU AI Act FRIA (Art. 27) is the one material jurisdiction-specific gap — relevant only for enterprises with EU deployment scope
4. Blueprint for AI Bill of Rights' 5 protections are comprehensively addressed by EAGCF's output controls (OUT domain) and human oversight architecture (AGT-06, Part VI §6.3)

**Coverage summary:**
- Items with direct EAGCF coverage: **22 (79%)**
- Items partially covered: **6 (21%)**
- Items not addressed: **0 (0%)**
- Design-by-choice restrictions (OECD footnote): **1 deliberate decision — not a gap**

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Comparisons completed: NIST AI 100-1, 100-2, 100-4, 100-5, 600-1, 700-1, 700-2, 800-1, 800-2, IR 8596 (10 documents); ISO 42001/23894 crosswalks; OECD/EU AI Act crosswalk (13 sources)*
