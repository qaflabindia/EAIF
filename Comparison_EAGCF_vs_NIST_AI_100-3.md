# Side-by-Side Comparison: EAGCF vs. NIST AI 100-3
## *The Language of Trustworthy AI: An In-Depth Glossary of Terms*

**Source Document:** `NIST.AI.100-3.pdf` (NIST, March 2023)
**Authors:** Daniel Atherton, Reva Schwartz, Peter C. Fontana, Patrick Hall
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** NIST AI 100-3 is the methodology guide for the NIST trustworthy and responsible AI glossary (511 terms, 379 citations, hosted online at airc.nist.gov). The PDF itself describes the glossary development process — term selection, definition sourcing, cross-domain coverage, and alignment principles. The actual glossary is an online resource. This is a vocabulary/terminology document, not a governance framework, risk management standard, or control specification. Its value to EAGCF is: (1) establishing the authoritative source for NIST AI terminology; (2) confirming design principles for cross-domain, sector-agnostic vocabulary; (3) providing a reference for EAGCF's own definitional section (Part II §2.2).

---

## 1. Document Scope Alignment

| Dimension | NIST AI 100-3 | EAGCF |
|---|---|---|
| **Document type** | Terminology methodology guide + online glossary (511 terms) | Enterprise governance and control operating model |
| **Primary purpose** | Promote shared understanding of AI/ML terms across disciplines and sectors | Enable enterprises to govern, control, and assure AI use |
| **Governance content** | None — vocabulary only | 15 control domains, 9 enforcement points, 5-tier risk model |
| **Sector specificity** | Sector-agnostic by design | Sector-agnostic with financial services, healthcare, and safety-critical overlays |
| **Alignment basis** | IEEE, ANSI, ISO/IEC standards; peer-reviewed AI, statistics, law, social sciences literature | NIST AI RMF, ISO 42001, ISO 23894, COBIT, COSO, CRISP-ML(Q) |

---

## 2. Glossary Design Principles vs. EAGCF Definitional Architecture

| NIST AI 100-3 Principle | EAGCF Implementation | Status |
|---|---|---|
| **Alignment with existing international and industry standards** (IEEE, ANSI, ISO/IEC) | Part II §2.2 (definitions): aligned with ISO/IEC 22989 (AI concepts and terminology), NIST AI RMF, and ISO 42001 vocabulary | ✅ Covered |
| **Inclusion of terms related to emerging AI technologies** (GenAI, agentic, foundation models) | Part II §2.2 (10 AI archetypes defined); Part V §5.15 (GEN domain); Part V §5.6 (AGT domain: agentic action governance) | ✅ Covered |
| **Inclusion of definitions from wide variety of domains** (ML, statistics, psychology, behavioral sciences, social sciences, law) | Part II §2.2 — primary focus on governance and control definitions; limited behavioral science and legal vocabulary | ⚠️ Partial — EAGCF's definitional scope is narrower: governance/risk/control terms, not cross-domain AI scientific vocabulary |
| **Collaborative development** via stakeholder consultation | EAGCF developed via framework synthesis (17+ frameworks); not through public comment process | ⚠️ Partial — comprehensive framework input but not public-comment governance process |
| **Regular review and feedback** mechanisms | Part VI §6.6 (annual framework review cadence) | ✅ Covered |
| **Broad dissemination** and use | EAGCF distributed as enterprise standard; ISO 42001 certification enables external recognition | ✅ Covered |

---

## 3. Key Terminology Areas vs. EAGCF Coverage

The online NIST AI glossary (accessible via the 100-3 methodology) covers terms that EAGCF uses extensively. Alignment check on critical terms:

| NIST AI Glossary Term Category | EAGCF Definitional Coverage | Status |
|---|---|---|
| **AI risk management terms** (risk, hazard, impact, consequence, exposure) | Part II §2.2 (risk defined); Deliverable B (risk tiering: probability × severity × reversibility) | ✅ Covered |
| **Governance and accountability terms** (accountability, transparency, oversight, auditability) | Part II §2.2 (governance, controls, assurance, monitoring defined); Part VI (accountability structures) | ✅ Covered |
| **Trustworthiness characteristics** (valid, reliable, safe, secure, resilient, fair, explainable, transparent) | Part II §2.2 + Part XII §12.2 (control validation: all 7 characteristics assessed) | ✅ Covered |
| **Model lifecycle terms** (training, validation, testing, deployment, monitoring, drift, degradation) | Part II §2.2; Part V §5.3 (MDL domain: versioning, benchmark, drift, degradation controls); Deliverable D (lifecycle) | ✅ Covered |
| **GenAI-specific terms** (hallucination, prompt injection, RLHF, grounding, synthetic content) | Part V §5.4 (PRM domain: prompt injection defined); Part V §5.7 (OUT-03: hallucination defined); Part V §5.15 (GEN domain) | ✅ Covered |
| **Agentic AI terms** (agent, multi-agent, tool use, action scope, HITL) | Part II §2.2 (agentic archetype defined); Part V §5.6 (AGT domain: all 10 agentic controls with defined terms) | ✅ Covered |
| **Adversarial ML terms** (poisoning, evasion, inversion, model extraction, prompt injection) | Part V §5.11 (MSC domain); Part XII §12.1 (red-team attack library: adversarial ML taxonomy) | ✅ Covered — aligned with NIST AI 100-2e2025 NISTAML taxonomy |
| **Fairness and bias terms** (disparate impact, demographic parity, calibration, protected attribute) | Part V §5.8 (FAI domain: FAI-01 through FAI-06 with defined fairness metrics) | ✅ Covered |
| **Privacy terms** (PII, differential privacy, data minimization, consent, anonymization) | Part V §5.2 (DAT domain: data governance and privacy controls); Deliverable G §G.8 (DPIA) | ✅ Covered |
| **Cross-domain behavioral/social science terms** | Not covered in EAGCF | ⚠️ Partial — out of EAGCF scope; refer users to NIST AI 100-3 online glossary |

---

## 4. Recommended EAGCF Definitional Enhancement

| Enhancement ID | Source | Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N-103-01** | NIST AI 100-3 §1 | **Reference NIST AI Glossary as definitional authority**: In EAGCF Part II §2.2, add a note directing readers to the NIST AI 100-3 online glossary (airc.nist.gov/AI_RMF_Knowledge_Base/Glossary) as the authoritative cross-domain AI terminology reference for terms not defined within EAGCF | Low | Part II §2.2 (definitions section) — add reference note |
| **N-103-02** | NIST AI 100-3 design principles | **Cross-domain vocabulary coverage**: EAGCF's definitions are governance-focused; for behavioral science, legal, and social science AI terms, EAGCF users should consult the 511-term NIST glossary. Consider adding this as a "See Also" note in EAGCF's glossary section | Low | Part II §2.2 — supplementary reference note |

---

## 5. Scoring Summary

| Area | Items | ✅ Covered | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|
| Glossary design principles | 6 | 4 | 2 | 0 |
| Key terminology categories | 10 | 9 | 1 | 0 |
| **TOTALS** | **16 items** | **13 (81%)** | **3 (19%)** | **0 (0%)** |

**Coverage interpretation:** 100% of items at least partially covered; 81% fully addressed. EAGCF's definitional scope is purposefully narrower than the 511-term NIST glossary — it covers governance, control, risk, and AI system terms needed for enterprise governance operation. The cross-domain behavioral/social science vocabulary in the NIST glossary is beyond EAGCF's scope and not required for its audience.

---

## 6. Synthesis

NIST AI 100-3 is a vocabulary methodology document, not a governance framework. The comparison is brief by design: EAGCF's definitional architecture covers the governance-relevant subset of NIST AI 100-3's scope comprehensively. The primary EAGCF action is a simple cross-reference addition (N-103-01) pointing to the online NIST AI glossary for cross-domain definitional completeness.

**Governance relevance rating:** Low — this is a terminology reference document. The governance-critical content in this comparison series comes from the NIST AI RMF, ISO standards, and evaluation programs, not from the glossary methodology.

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Comparisons completed (20 sources): NIST AI 100-1, 100-2, 100-3, 100-4, 100-5, 600-1, 700-1, 700-2 + ARIA Companion, 800-1, 800-2, IR 8596; ISO crosswalks (42001/23894, 42005, 5338/5339); OECD/EU AI Act crosswalk; Google DeepMind Gap Analysis; AI Verify crosswalks; Americas AI Action Plan*
