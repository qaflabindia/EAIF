# Side-by-Side Comparison: EAGCF vs. NIST AI 100-5e2025
## *A Plan for Global Engagement on AI Standards*

**NIST Document:** NIST AI 100-5e2025 (April 2025)
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** NIST AI 100-5 is the U.S. Government's strategic plan for international AI standards engagement — it is a standards *diplomacy* and *prioritization* document, not a technical governance standard. Its primary value to EAGCF is: (1) confirming which NIST topics are considered urgent for standardization (informing EAGCF's normative reference stack), (2) identifying emerging ISO/IEC standards on AI cybersecurity (27090, 27091.2) not yet in EAGCF, and (3) providing the government's view of AI standards maturity levels. This is the lowest-governance-relevance document in the comparison series.

---

## 1. Document Scope Alignment

| Dimension | NIST AI 100-5e2025 | EAGCF |
|---|---|---|
| **Document type** | Standards strategy / diplomacy plan | Enterprise governance and control framework |
| **Primary purpose** | Drive development and adoption of AI standards globally | Enable enterprises to govern, control, and assure AI use |
| **Governance content** | Identifies priority standardization topics; no controls or requirements | 15 control domains, 9 enforcement points, 10 archetypes |
| **Audience** | U.S. Government agencies, SDO participants, international partners | Board, CRO, governance office, internal audit, compliance |
| **Binding nature** | Not binding — strategic intent only | Voluntary enterprise standard, wired to ISO 42001 |

---

## 2. Tier 1 Priority Standardization Topics vs. EAGCF Coverage

Topics classified as "urgently needed and ready for standardization" — the most mature and important.

| NIST AI 100-5 Tier 1 Topic | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Terminology and taxonomy** (AI red-teaming, generative AI, model fine-tuning, model openness) | Part II §2.2 (definitions); Part III (comparative analysis); Glossary | ✅ Covered | EAGCF defines key terms; aligned with ISO/IEC 22989:2022 vocabulary |
| **Measurement methods and metrics (TEVV)** (shared testing, evaluation, verification, validation) | Part XII (control validation); Part VII §7.2 (KPI/KRI/KCI); Deliverable E (monitoring signals) | ✅ Covered | |
| **Digital content transparency / content provenance** (watermarking, metadata recording, synthetic content detection) | Part V §5.11 (MSC-08: watermarking); OUT-04 (output labeling) | ⚠️ Partial | Surface coverage; deep synthetic content gaps identified in NIST AI 100-4 comparison |
| **Risk-based management of AI systems** (AI RMF, ISO 23894, ISO 42001 for GenAI) | Part IV (governance framework); Deliverable B (risk tiering); full ISO 42001 management system shell | ✅ Covered | EAGCF is itself a realization of this standardization priority |
| **Security and privacy** (adversarial ML mitigations, PETs; foundation: NIST AI 100-2) | Part XII (control validation); Part V domains 2, 4, 8, 11; Part XI (enforcement architecture) | ✅ Covered | Comprehensive — EAGCF extensively references and implements AI 100-2 recommendations |
| **Transparency among AI actors** (training data characteristics, performance results, model cards, data cards, SBOMs) | Part V §5.3 (MDL-05: model card); Part V §5.11 (MSC-01/02); Deliverable G §G.5 (AI Use Case Registration) | ✅ Covered | SBOM (Software/AI Bill of Materials) not explicitly required |
| **Training data practices** (quality, preprocessing, change management, filtering) | Part V §5.2 (DAT domain, 8 controls); Part V §5.11 (MSC-01/02) | ✅ Covered | |
| **Incident response and recovery plans** (drawing on cybersecurity analogues; proactive baseline + responsive controls) | Part VII §7.3 (incident taxonomy); Part VII §7.4 (corrective action); Part XIII §13.1 (CI/CD governance) | ✅ Covered | |

---

## 3. Tier 2 Topics vs. EAGCF

Topics requiring more scientific work before standardization.

| NIST AI 100-5 Tier 2 Topic | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Measuring resource consumption** (energy, compute, carbon — no agreed standard yet) | Not addressed | ❌ Gap | Environmental impact gap confirmed (N600-01, N-06) |
| **Conformity assessment** (depends on base standards; ISO 42001 conformity assessment in development) | Part IV §4.8 (assurance model); Part VI §6.7 (external assurance) | ⚠️ Partial | EAGCF is wired to ISO 42001 for certification; formal conformity assessment methodology not detailed |
| **Testing and evaluation datasets** (standard practices for data integrity, quality, change management) | Part V §5.2 (DAT domain); Part XII §12.2 (control validation matrix) | ✅ Covered | |

---

## 4. Tier 3 Topics vs. EAGCF

Topics requiring significant foundational work.

| NIST AI 100-5 Tier 3 Topic | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Interpretability and explainability techniques** | Part V §5.3 (MDL-05: model card — includes explainability requirements); Part XII §12.2 | ⚠️ Partial | Explainability in model card present; formal explainability measurement technique requirement not specified; gap N-09 from NIST 100-1 comparison confirmed |
| **Human-AI configuration** (metrics for human-AI teaming performance, bias, trust) | Part V §5.7 (OUT-06: human override; AGT-06: HITL thresholds); Part VI §6.3 | ⚠️ Partial | HITL and override mechanisms present; human-AI configuration performance metrics not specified |
| **AI hardware performance measurement** (NPUs, TPUs, cross-platform comparison) | Not addressed | ❌ Gap | AI hardware performance benchmarking not in EAGCF scope |

---

## 5. Emerging ISO/IEC Standards Referenced vs. EAGCF

NIST AI 100-5 references several key standards under development that EAGCF should track.

| Emerging Standard | Description | EAGCF Coverage | Priority |
|---|---|---|---|
| **ISO/IEC CD 27090** | Cybersecurity — AI — Guidance for addressing security threats and failures in AI systems | Not referenced | High — this will be the primary ISO AI cybersecurity standard; EAGCF should monitor and align when finalized |
| **ISO/IEC WD 27091** | Cybersecurity and Privacy — AI — Privacy protection | Not referenced | High — AI-specific privacy protection standard; complements DAT domain |
| **CTA-5203** | Cybersecurity Threats and Security Controls for Machine Learning Based Systems | Not referenced | Medium — add as informative reference in Part XII |
| **ISO/IEC 22989:2022** | AI concepts and terminology (basis for NIST AI 100-5 terminology alignment) | Referenced implicitly via definitions | Low |
| **ISO/IEC 42001 conformity assessment** | Certification assessment methodology for ISO 42001 (in development) | Part IV §4.8 (assurance model) — partial | Medium — when finalized, EAGCF should update its ISO 42001 integration guidance |

---

## 6. Scoring Summary

| NIST AI 100-5 Area | Items | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| Tier 1 standardization priorities | 8 | 6 | 0 | 2 | 0 |
| Tier 2 standardization topics | 3 | 1 | 0 | 1 | 1 |
| Tier 3 standardization topics | 3 | 0 | 0 | 2 | 1 |
| Emerging ISO/IEC standards | 5 | 0 | 0 | 1 | 4 |
| **TOTALS** | **19 items** | **7 (37%)** | **0** | **6 (32%)** | **6 (32%)** |

**Coverage interpretation:** 69% total (37% + 32%). The gap rate primarily reflects emerging ISO standards (27090, 27091) not yet finalized when EAGCF was written, and the structural topics (resource measurement, hardware benchmarking) outside EAGCF's enterprise governance scope.

---

## 7. Gap Items: Recommended EAGCF Additions

| Gap ID | Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N1005-01** | §4.1 Security | **ISO/IEC 27090 tracking**: When ISO/IEC 27090 (AI Cybersecurity) is finalized, incorporate as a normative reference in EAGCF Part XI (enforcement architecture) and Part XII (control validation) alongside NIST AI 100-2 | High | Note in Part XI §11.1 and Part XII §12.3 as "watch standard" |
| **N1005-02** | §4.1 Security | **AI Software Bill of Materials (SBOM)**: Require AI SBOM as part of vendor due diligence (VND domain) and model supply chain documentation (MSC domain) — specifically for training data, model weights, third-party components | Medium | Part V §5.11 (MSC-07) — add SBOM requirement; Deliverable G §G.13 (Vendor Due Diligence) |
| **N1005-03** | §4.2 Conformity | **ISO 42001 conformity assessment pathway**: When ISO 42001 conformity assessment standard is finalized, update EAGCF assurance model with audit and certification process guidance | Low | Part IV §4.8 (assurance model) — update when standard available |

---

## 8. Key NIST AI Standards Confirmation

NIST AI 100-5 confirms the following priority rankings useful for EAGCF's normative reference stack:

| NIST Standard | Role in EAGCF | NIST AI 100-5 Confirmation |
|---|---|---|
| **NIST AI RMF (100-1)** | EAGCF governance backbone | Tier 1 — "ready for standardization" (revision for GenAI ongoing) |
| **NIST AI 100-2e2025** | EAGCF adversarial ML reference | Tier 1 — "urgently needed"; primary security/privacy foundation |
| **ISO/IEC 42001** | EAGCF management system shell | Tier 1 — "ready"; conformity assessment standards in development |
| **ISO/IEC 23894** | EAGCF risk methodology | Tier 1 — "ready"; AI-specific risk management process |
| **Watermarking / provenance** | EAGCF MSC-08, OUT-04 | Tier 1 — "needs accelerated study"; standards work accelerating |
| **Explainability methods** | EAGCF MDL-05 (partial) | Tier 3 — "significant foundational work needed" (confirms why EAGCF gap N-09 is hard to fill) |

---

*Comparison prepared as part of EAGCF continuous improvement program.*
