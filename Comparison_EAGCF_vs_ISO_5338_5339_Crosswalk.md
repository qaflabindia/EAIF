# Side-by-Side Comparison: EAGCF vs. ISO/IEC 5338 and ISO/IEC 5339 Crosswalk
## *NIST AI RMF ↔ ISO/IEC 5338 (AI System Life Cycle Processes) and ISO/IEC 5339 (AI Applications Guidance)*

**Source Document:** `Crosswalk_NIST_AI_RMF_and_ISO_5338_5339.pdf` (NIST, 2024)
**Standards Covered:**
- **ISO/IEC 5338:2023** — Information technology — AI system life cycle processes
- **ISO/IEC 5339:2024** — Information technology — Guidance for AI applications
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** ISO/IEC 5338 defines the engineering and process framework for AI system lifecycle management; ISO/IEC 5339 provides governance guidance on AI applications from three stakeholder perspectives: Make (developer/builder), Use (operator/deployer), and Impact (affected individuals and society). Together they form the ISO lifecycle and application governance complement to ISO 42001 (management systems) and ISO 23894 (risk method). This crosswalk's value to EAGCF is in confirming lifecycle coverage and identifying three ISO 5339 trustworthiness characteristics (Controllability, Predictability, Dependability) not present in the NIST AI RMF.

---

## 1. Document Scope Alignment

| Dimension | ISO/IEC 5338 | ISO/IEC 5339 | EAGCF |
|---|---|---|---|
| **Primary purpose** | AI system lifecycle process engineering | AI application governance from stakeholder perspectives (Make/Use/Impact) | Enterprise governance and control operating model |
| **Lifecycle coverage** | Full lifecycle: plan, design, data, build, deploy, operate, monitor | Deployment context and stakeholder impacts | 11-stage lifecycle with tiered gate intensity |
| **Stakeholder model** | Developer, operator, deployer, end-user | Make/Use/Impact (3 perspectives) | Board, CRO, governance office, business owner, internal audit + affected populations |
| **Trustworthiness model** | Inherits from ISO/IEC 24028 | 10 non-functional characteristics (7 overlap with NIST RMF + 3 unique) | NIST AI RMF 7 characteristics implemented via 15 control domains |
| **Binding nature** | International standard | International standard | Voluntary enterprise standard |

---

## 2. ISO/IEC 5338 Lifecycle Stages vs. EAGCF

ISO/IEC 5338 defines AI system lifecycle process categories aligned with the AI RMF lifecycle. EAGCF's 11-stage lifecycle (Deliverable D) maps cleanly:

| ISO/IEC 5338 Lifecycle Stage | EAGCF Lifecycle Equivalent | Coverage | Notes |
|---|---|---|---|
| **Plan and Design** | Stage 1: AI Strategy Intake; Stage 2: Use Case Registration; Stage 3: Impact Assessment | ✅ Covered | Deliverable G §G.5 (registration) + §G.3 (impact assessment) |
| **Data and Data Collection** | Stage 4: Data Governance Gate | ✅ Covered | Part V §5.2 (DAT domain: 8 controls); MSC-01/02 (training data lineage) |
| **Build** | Stage 5: Model Development Gate; Stage 6: Prompt/Instruction Development | ✅ Covered | Part V §5.3 (MDL domain); Part V §5.4 (PRM domain) |
| **Deploy** | Stage 7: Deployment Gate; Stage 8: Vendor/Supply Chain Gate | ✅ Covered | Part XIII §13.1 (CI/CD lifecycle governance); Part XI (enforcement architecture) |
| **Operation and Monitoring** | Stage 9: Runtime Monitoring; Stage 10: Incident Response; Stage 11: Decommission | ✅ Covered | Deliverable E (monitoring signals); Part VII (monitoring, incidents, assurance) |

**Lifecycle coverage: 5/5 stages — 100%**

---

## 3. ISO/IEC 5339 Stakeholder Perspectives vs. EAGCF

ISO/IEC 5339 organizes AI governance around three perspectives:

### Make Perspective (Developer/Builder)

| ISO/IEC 5339 Make Requirement | EAGCF Coverage | Status |
|---|---|---|
| Design and develop AI systems with trustworthiness characteristics built-in | Part V §5.3 (MDL domain: model controls); Part XII §12.1 (red-team at build stage) | ✅ Covered |
| Document AI system capabilities and limitations | MDL-05 (model card); Deliverable G §G.6 (model card template) | ✅ Covered |
| Implement non-functional characteristics per ISO 22989 taxonomy | Part XII §12.2 (control validation: maps to 7 AI RMF trustworthiness characteristics) | ✅ Covered |
| Provide adequate documentation for operators | MDL-05 model card; OUT-03 output factuality requirements; API documentation requirements (VND domain) | ✅ Covered |

### Use Perspective (Operator/Deployer)

| ISO/IEC 5339 Use Requirement | EAGCF Coverage | Status |
|---|---|---|
| Configure AI systems within deployment context | Part V §5.4 (PRM domain: system prompt as versioned governed artifact); Part V §5.5 (RAG domain) | ✅ Covered |
| Monitor AI system performance in operational context | Deliverable E (runtime monitoring signal catalog); Part VII §7.1 | ✅ Covered |
| Maintain human oversight and override capability | Part VI §6.3 (HITL governance); AGT-06 (agentic HITL thresholds); OUT-06 (human override) | ✅ Covered |
| Manage vendor relationships and supply chain | Part V §5.9 (VND domain: 6-dimension vendor scoring); Part V §5.11 (MSC domain) | ✅ Covered |
| Ensure appropriate access and identity controls | Part V §5.9.3 [IAM domain]; Part IX (identity/access controls) | ✅ Covered |

### Impact Perspective (Affected Individuals and Society)

| ISO/IEC 5339 Impact Requirement | EAGCF Coverage | Status |
|---|---|---|
| Assess impacts on individuals, groups, and society before deployment | Deliverable G §G.3 (AI Impact Assessment: mandatory Tier 1/2 gate) | ✅ Covered |
| Manage societal and environmental impacts | Part V §5.8 (FAI domain: societal impact); Deliverable G §G.3 (impact assessment) | ⚠️ Partial — N-06: environmental/compute impact not addressed |
| Provide affected individuals with notice and explanation | Part V §5.7 (OUT-03: output factuality; OUT-04: output labeling; OUT-05: human override notification) | ✅ Covered |
| Preserve fundamental rights and non-discrimination | Part V §5.8 (FAI domain: FAI-01 through FAI-06) | ✅ Covered |

---

## 4. ISO/IEC 5339 Trustworthiness Characteristics vs. EAGCF

ISO/IEC 5339 defines 10 non-functional trustworthiness characteristics. Seven overlap with NIST AI RMF; three are unique to ISO/IEC 5339:

### Shared Characteristics (7)

| ISO/IEC 5339 Characteristic | NIST AI RMF Equivalent | EAGCF Coverage | Status |
|---|---|---|---|
| **5.5.2.9 Performance** (Valid and Reliable) | Valid and Reliable | Part V §5.3 (MDL domain); Part XII §12.2 | ✅ Covered |
| **5.5.2.4 Security** (Secure and Resilient) | Secure and Resilient | Part XI (enforcement); Part XII §12.1 (red-team) | ✅ Covered |
| **5.5.2.8 Transparency** (Accountable and Transparent) | Accountable and Transparent | Part IV §4.3; Part V §5.7 (OUT domain) | ✅ Covered |
| **5.5.2.6 Explainability** (Explainable and Interpretable) | Explainable and Interpretable | Part V §5.3 (MDL-05) | ⚠️ Partial — N-09 confirmed |
| **5.5.2.10 Fairness** (Fair — Bias Managed) | Fair — Bias Managed | Part V §5.8 (FAI domain) | ✅ Covered |

*Note: ISO/IEC 5339 does not explicitly include Safety or Privacy-Enhanced as separate characteristics, treating them implicitly within other categories. EAGCF explicitly covers both.*

### Unique ISO/IEC 5339 Characteristics (3) — Not in NIST AI RMF

| ISO/IEC 5339 Unique Characteristic | Description | EAGCF Coverage | Status |
|---|---|---|---|
| **Controllability (5.5.2.7)** | Degree to which an AI system can be steered, corrected, or shut down by authorized parties; includes kill switches and override mechanisms | Part VI §6.3 (HITL governance); AGT-06 (agentic HITL thresholds); Part XI EP-9 (circuit breaker/kill switch); Part V §5.7 (OUT-06: human override) | ✅ Covered — EAGCF's enforcement architecture directly addresses controllability |
| **Predictability (5.5.2.7)** | Degree to which AI system behavior is consistent and predictable across similar inputs and contexts | Part V §5.3 (MDL-03: benchmark; MDL-04: drift detection — unexpected behavior as a drift signal); Part XIV §14.2 (SLA thresholds for consistent performance) | ⚠️ Partial — behavioral consistency monitoring present; formal predictability requirement (same input → same output within tolerance) not explicitly specified |
| **Dependability (5.5.2.1)** | Composite attribute covering reliability, availability, safety, security, maintainability; AI system availability for its intended function | Part XIV §14.2 (SLA table: uptime/availability); Part XIII §13.1 (CI/CD: maintainability); Part V §5.3 (MDL domain: reliability) | ✅ Covered |

---

## 5. AI RMF Core Function ↔ ISO 5339 Perspective Mapping vs. EAGCF

The crosswalk document provides a key structural alignment:

| AI RMF Core Function | ISO/IEC 5339 Perspective | EAGCF Implementation |
|---|---|---|
| **GOVERN** (cross-cutting) | Infuses all three perspectives | Part IV (governance framework); Part VI (governance operating model) — cross-cutting across all lifecycle stages |
| **MAP** | Make perspective (design/development decisions) | Part V §5.3 (MDL domain); Part V §5.2 (DAT domain); Deliverable G §G.5 (use case registration) |
| **MEASURE** | Use perspective (operational evaluation) | Part XII (control validation); Deliverable E (monitoring signals); Part VII §7.2 (KPI/KRI/KCI) |
| **MANAGE** | Impact perspective (consequence management) | Part VII §7.3–7.5 (incident taxonomy, corrective action, escalation); Part VIII (adoption acceleration) |

---

## 6. Notable EAGCF Strengths vs. ISO 5338/5339

| Area | EAGCF Capability | ISO 5338/5339 |
|---|---|---|
| **Safety as explicit characteristic** | Tier 0 Prohibited + Tier 1 High risk gates; EP-1 through EP-9 | Not an explicit trustworthiness characteristic in ISO 5339 |
| **Privacy-Enhanced as explicit characteristic** | Part V §5.2 (DAT domain: 8 controls); Deliverable G §G.8 (DPIA) | Not explicit in ISO 5339 trustworthiness model |
| **Agentic governance** | AGT-01 through AGT-10 (full agentic control domain) | Not addressed in either standard |
| **GenAI-specific controls** | Part V §5.15 (GEN domain: full GenAI control set) | Process framework only; no GenAI-specific provisions |
| **Vendor and supply chain governance** | Part V §5.9 (VND domain) + Part V §5.11 (MSC domain) | ISO 5338 lifecycle includes data/build; no vendor scoring framework |

---

## 7. Scoring Summary

| Coverage Area | Items | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| ISO 5338 lifecycle stages | 5 | 5 | 0 | 0 | 0 |
| ISO 5339 Make perspective | 4 | 4 | 0 | 0 | 0 |
| ISO 5339 Use perspective | 5 | 5 | 0 | 0 | 0 |
| ISO 5339 Impact perspective | 4 | 3 | 0 | 1 | 0 |
| Shared trustworthiness characteristics | 5 | 4 | 0 | 1 | 0 |
| Unique ISO 5339 characteristics | 3 | 2 | 1 | 1 | 0 |
| **TOTALS** | **26 items** | **23 (88%)** | **1** | **3 (12%)** | **0 (0%)** |

**Coverage interpretation:** 100% of items are at least partially covered; 88% fully addressed. The three partial items are N-06 (environmental impact), N-09 (explainability measurement), and predictability specification. Zero gaps.

---

## 8. Recommended EAGCF Enhancements

| Enhancement ID | Source | Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N-5339-01** | ISO 5339 §5.5.2.7 | **Behavioral predictability requirement**: For Tier 1/2 AI systems, add an explicit predictability requirement — AI system outputs must remain within defined tolerance bounds across repeated equivalent inputs and contexts. Define acceptable variation thresholds and monitoring criteria | Low | Part V §5.3 (MDL-04: drift detection) — extend to include behavioral predictability bounds |
| **N-5339-02** | ISO 5338/5339 | **ISO 5338/5339 normative reference**: Add ISO/IEC 5338 and ISO/IEC 5339 to EAGCF's normative reference stack, positioning them as the lifecycle process and application governance complements to ISO 42001 (management systems) and ISO 23894 (risk method) | Low | Part IV §4.2 (normative references section) |

---

## 9. Synthesis

The ISO 5338/5339 crosswalk confirms that EAGCF's architecture is comprehensively aligned with the ISO AI standards family:
- **ISO 42001** (management systems) → EAGCF governance shell
- **ISO 23894** (risk method) → EAGCF risk tiering methodology
- **ISO 42005** (impact assessment) → EAGCF AI Impact Assessment template
- **ISO 5338** (lifecycle) → EAGCF 11-stage lifecycle (Deliverable D)
- **ISO 5339** (application governance) → EAGCF's Make/Use/Impact coverage via MDL, DAT, VND, OUT domains

The three unique ISO 5339 characteristics (Controllability, Predictability, Dependability) are all materially addressed in EAGCF. Controllability — the most important of the three for enterprise governance — is particularly well-covered via EAGCF's enforcement architecture (EP-9 circuit breaker, AGT-06 HITL thresholds, OUT-06 human override).

**Coverage summary:**
- Items fully covered: **23 (88%)**
- Items partially covered: **3 (12%)**
- Items not addressed: **0 (0%)**

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Comparisons completed (17 sources): NIST AI 100-1, 100-2, 100-4, 100-5, 600-1, 700-1, 700-2, 800-1, 800-2, IR 8596; ISO crosswalks (42001/23894, 42005, 5338/5339); OECD/EU AI Act crosswalk; Google DeepMind Gap Analysis; AI Verify crosswalks*
