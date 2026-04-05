# Side-by-Side Comparison: EAGCF vs. NIST AI 600-1
## *AI Risk Management Framework: Generative AI Profile*

**NIST Document:** NIST AI 600-1 (July 2024)
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** NIST AI 600-1 is the authoritative GenAI-specific profile of the AI RMF 1.0, and is explicitly referenced in EAGCF as one of the execution-layer backbone documents (Part IX, NIST AI RMF Playbook + GenAI Profile). This comparison therefore tests *coverage depth* rather than simple presence/absence — EAGCF is expected to cover most 600-1 items but may have gaps in specificity for certain GenAI-native risk types. The 12 GAI risk categories and ~120+ suggested actions are mapped systematically.

---

## 1. Document Scope Alignment

| Dimension | NIST AI 600-1 | EAGCF |
|---|---|---|
| **Framework base** | AI RMF 1.0 (Govern, Map, Measure, Manage) | NIST AI RMF + ISO 42001 + COBIT + COSO + TOGAF |
| **Coverage scope** | 12 GenAI-specific risk categories; ~120 suggested actions across GV/MP/MS/MG | Full AI governance; GenAI addressed in Part V §5.15 (GEN domain) and Part IX |
| **Action specificity** | Specific suggested actions per AI RMF subcategory | Control objectives, owners, evidence requirements, monitoring signals |
| **Certification path** | No | ISO 42001 via EAGCF shell |
| **Audience** | AI developers, deployers, governance teams | Board, CRO, governance office, internal audit, compliance |
| **Content provenance** | Dedicated Appendix A.3 (major GAI governance theme) | Partially covered via MSC-08 (watermarking) and OUT domain |
| **Incident disclosure** | Dedicated Appendix A.4 with minimum criteria | Part VII §7.3 (incident taxonomy and severity) |

---

## 2. 12 GenAI Risk Categories vs. EAGCF Control Domains

| NIST AI 600-1 Risk Category | EAGCF Control Mapping | Coverage Status | Notes |
|---|---|---|---|
| **1. CBRN Information or Capabilities** | Tier 0 (Prohibited) — no CBRN facilitation; GEN-07 (jailbreak library); EP-5 (output classifier) | ✅ Covered | Tier 0 explicitly prohibits CBRN-enabling outputs |
| **2. Confabulation (hallucination)** | OUT-03 (output factuality controls); GEN-01 (confabulation detection); Part VII §7.1 (MON-10: output quality signal) | ✅ Covered | |
| **3. Dangerous, Violent, or Hateful Content** | GEN-02 through GEN-04 (content safety controls); EP-5 (output classifier); Part IV §4.1 (Tier 0: harmful content) | ✅ Covered | |
| **4. Data Privacy (memorization, PII leakage, de-anonymization)** | Part V §5.2 (DAT-01 through DAT-08); OUT-03 (output PII screening); N1002-01 (membership inference — gap item) | ✅ Covered | Membership inference as a named attack vector is a gap (N1002-01); general data privacy well covered |
| **5. Environmental Impacts** | Not addressed | ❌ Gap | EAGCF does not address compute energy consumption, carbon footprint, or water use for AI training/inference. This was also gap N-06 in the NIST AI 100-1 comparison |
| **6. Harmful Bias and Homogenization** | Part V §5.2 (DAT-05: bias testing); GEN-05 (fairness testing); Part VIII §8.8 (sector overlays) | ✅ Covered | Model collapse / algorithmic monoculture not explicitly named |
| **7. Human-AI Configuration (over-reliance, automation bias, anthropomorphization)** | Part V §5.7 (OUT-06: human override; OUT-07: recourse mechanism); Part VI §6.3 (HITL thresholds); Part VIII §8.9 (workforce enablement: automation bias training) | ⚠️ Partial | HITL and override mechanisms present; emotional entanglement and anthropomorphization as specific named risk categories not controlled |
| **8. Information Integrity (deepfakes, disinformation, synthetic media)** | Part V §5.7 (OUT-04: output labeling); MSC-08 (watermarking); OUT-08 (deepfake detection — gap N8596-01) | ⚠️ Partial | Watermarking and output labeling present; deepfake detection and disinformation monitoring not yet addressed (aligns with N8596-01 gap) |
| **9. Information Security (prompt injection, data poisoning, model extraction)** | Part V §5.4 (PRM-05: injection), §5.11 (MSC domain: supply chain), §5.8 (IAM domain) | ✅ Covered | Comprehensively addressed across multiple domains |
| **10. Intellectual Property (copyright, training data memorization, plagiarism)** | Part V §5.11 (MSC-01/02: training data lineage and provenance); Part V §5.2 (DAT-04) | ⚠️ Partial | Training data lineage and provenance present; specific IP infringement monitoring, copyright claims response process, and legal status of AI-generated content not detailed |
| **11. Obscene, Degrading, and/or Abusive Content (CSAM, NCII)** | Tier 0 (Prohibited — CSAM/NCII); GEN-02 (content safety); EP-5 (output classifier with CSAM/NCII category) | ✅ Covered | Tier 0 explicitly prohibits CSAM/NCII |
| **12. Value Chain and Component Integration** | Part V §5.11 (MSC-01 through MSC-08: full supply chain domain); Part V §5.9 (VND domain: 8 controls) | ✅ Covered | |

**Risk Category Coverage:** 8 covered (67%), 3 partial (25%), 1 gap (8%)

---

## 3. GOVERN Function: Suggested Actions vs. EAGCF

| NIST AI 600-1 Suggested Action | EAGCF Coverage | Status |
|---|---|---|
| **GV-1.1-001** — Align with data privacy, copyright, IP laws | Part VIII §8.8 (sector regulatory overlays); Part IV §4.4 (regulatory requirements integration) | ✅ |
| **GV-1.2-001** — Transparency policies for training/generated data origin | Part V §5.11 (MSC-01/02); Part IV §4.3 (transparency requirements) | ✅ |
| **GV-1.2-002** — Policies for evaluating risk-relevant capabilities and safety robustness, pre-deployment and ongoing | Part IV §4.1 (Deliverable B: pre-deployment gates); Part XII §12.2 (ongoing control validation) | ✅ |
| **GV-1.3-001 through 007** — Risk tier definition, minimum thresholds, CBRN test plan, halt-development plan | Part IV §4.1 (Deliverable B: 5-tier risk model with Tier 0 Prohibited and Tier 1 senior approval gate); Part IV §4.7 (exception and waiver model) | ✅ |
| **GV-1.4-001/002** — Policies to prevent CSAM/NCII; acceptable use policies | Part IV §4.1 (Tier 0 Prohibited classification); Part IV §4.3 (transparency/acceptable use) | ✅ |
| **GV-1.5-001 through 003** — Periodic review; after-action review policy; document retention for TEVV | Part VII §7.4 (post-incident corrective action); Part IV §4.4 (governance enforcement model) | ⚠️ Partial — TEVV history retention policy not explicitly required |
| **GV-1.6-001 through 003** — AI system inventory; exemptions; inventory fields including provenance and known issues from AVID/CVE | Part IV §4.3 (AI use case registration); Deliverable G §G.5 (AI Use Case Registration template) | ⚠️ Partial — AVID/CVE/OECD AI incident monitor as inventory data sources not specified |
| **GV-1.7-001/002** — Decommissioning protocols; emotional entanglement considerations | Part VII §7.1 (lifecycle: Decommission stage; Deliverable D); Part IV §4.2 (governance lifecycle) | ⚠️ Partial — emotional entanglement not addressed in decommission protocol |
| **GV-2.1-001 through 005** — Roles for incident communication; diverse incident response teams; national security inclusion; whistleblower protections | Part VI §6.4 (AI governance office); Part VII §7.3 (incident taxonomy); N801-06 (whistleblower policy — gap item from NIST 800-1) | ⚠️ Partial — whistleblower protection gap confirmed (aligns with N801-06) |
| **GV-3.2-001 through 005** — Independent evaluations; human-AI configuration policies; user feedback and recourse; threat modeling | Part VI §6.7 (external assurance); Part V §5.7 (OUT-07: recourse mechanism — gap N-08 from NIST 100-1); Part XII §12.1 (red-team pipeline) | ⚠️ Partial — user feedback/recourse mechanism gap confirmed (aligns with N-08) |
| **GV-4.1-001 through 003** — Safety culture: explainability; structured public feedback; senior oversight across lifecycle | Part IV §4.5 (design principles); Part VI §6.1 (board oversight) | ⚠️ Partial — structured public feedback exercises (red-teaming, participatory engagement) not required by policy |
| **GV-4.2-001 through 003** — Terms of use/service; inclusive risk ID process; downstream impact documentation | Part IV §4.3 (acceptable use); Part VII §7.3 (incident scope) | ⚠️ Partial |
| **GV-4.3-001 through 003** — Content provenance effectiveness measurement; minimum incident reporting criteria; information sharing | Part VII §7.3 (incident taxonomy); Part IV §4.3 | ⚠️ Partial — minimum incident reporting field standard (System ID, Reporter, etc.) not specified as required format |
| **GV-5.1-001/002** — Outreach and feedback resources; disclosure to users prior to interaction in high-risk contexts | Not explicitly required | ⚠️ Partial — OUT-04 (output labeling) partially covers disclosure |
| **GV-6.1-001 through 010** — Third-party IP/rights management; educational activities; SLAs with content ownership clauses; supplier risk framework; third-party access inventory | Part V §5.9 (VND domain: 8 controls); Deliverable G §G.13 (vendor due diligence) | ✅ |
| **GV-6.2-001 through 007** — Third-party contingency; incident plans for third-party systems; data redundancy; fallback testing; vendor contract requirements (SLA, incident response, critical support) | Part XIV §14.4 (vendor governance: multi-model fallback architecture); Part V §5.9 (VND controls) | ✅ |

---

## 4. MAP Function: Suggested Actions vs. EAGCF

| NIST AI 600-1 Suggested Action | EAGCF Coverage | Status |
|---|---|---|
| **MP-1.1-001 through 004** — Document intended purposes, context, risk measurement plans, foreseeable illegal uses | Part IV §4.1 (Deliverable B: intake and tiering); Deliverable G §G.4 (AI Use Case Registration) | ✅ |
| **MP-1.2-001/002** — Interdisciplinary teams with diverse demographics, domain expertise, lived experience; representative evaluation participants | Not explicitly required | ❌ Gap — also gap N-01 from NIST AI 100-1 comparison; confirmed critical gap |
| **MP-2.1-001/002** — Data origin practices; TEVV for data/content flows including transformations | Part V §5.11 (MSC-01/02) | ✅ |
| **MP-2.2-001/002** — Upstream dependency documentation; external network interaction analysis | Part V §5.11 (MSC-07) | ⚠️ Partial |
| **MP-2.3-001 through 005** — Accuracy/quality/authenticity testing; fact-checking; adversarial testing plans | Part XII §12.1 (red-team pipeline); Part XII §12.2 (control validation matrix) | ✅ |
| **MP-3.4-001 through 006** — Human-AI configuration proficiency; content lineage literacy; certification programs; monitoring of human-GAI outcomes; end-user prototyping participation | Part VIII §8.9 (workforce enablement) | ⚠️ Partial — content lineage literacy certification and end-user prototyping participation not required |
| **MP-4.1-001 through 010** — Privacy monitoring; IP infringement response; training data curation policies; PII detection in output; training data legal diligence | Part V §5.2 (DAT), §5.11 (MSC), §5.7 (OUT-03: PII screening) | ⚠️ Partial — IP infringement response process and training data legal compliance audit not specified |
| **MP-5.1-001 through 006** — Provenance testing; provenance harm enumeration; disclosure decisions; adversarial role-playing; threat profiling | Part XII §12.1; Part VII §7.3; Part V §5.11 | ⚠️ Partial — provenance-specific threat profiling and disclosure decision framework not formalized |
| **MP-5.2-001/002** — Downstream impact context identification; AI Actor engagement for unanticipated impacts | Not addressed | ❌ Gap — also gaps N-02/N-03 from NIST AI 100-1 comparison; external stakeholder feedback loop |

---

## 5. MEASURE Function: Suggested Actions vs. EAGCF

| NIST AI 600-1 Suggested Action | EAGCF Coverage | Status |
|---|---|---|
| **MS-1.1-001 through 009** — Content provenance tracing tools; anomaly detection; disaggregated metrics by demographic; novel GAI risk measurement; equity monitoring; training data quality metrics; structured public feedback metrics; tracking unmeasurable risks | Part VII §7.1 (Deliverable E: monitoring signal catalog); Part VII §7.2 (KPI/KRI/KCI framework) | ⚠️ Partial — demographic disaggregation of monitoring metrics not required; tracking unmeasured/unmeasurable risks as a distinct category not formalized |
| **MS-1.3-001 through 003** — Define relevant groups; external evaluations; independence of evaluators from developers | Part VI §6.7 (external assurance); Part XII §12.1 (external red team) | ✅ |
| **MS-2.2-001 through 004** — Bias assessment and re-sampling; content provenance data privacy; consent withdrawal; DP/PETs for human subjects | Part V §5.2 (DAT-06: privacy controls); N1002-02 (DP training — gap item) | ⚠️ Partial — consent withdrawal / right-to-revoke for training data participation not addressed |
| **MS-2.3-001 through 004** — Baseline model performance; empirical capability validation; share pre-deployment testing with release authority; NIST Dioptra testing | Part VII §7.5 (assurance evidence pack); Part XII §12.2 | ⚠️ Partial — NIST Dioptra not referenced as a testing tool; pre-deployment testing sharing with release authority not formalized |
| **MS-2.5-001 through 006** — No anecdotal testing; RLHF/fine-tuning/RAG documentation; citation verification; anthropomorphization tracking; data provenance verification; safety guardrail review | Part V §5.11 (MSC); Part V §5.3 (MDL-05: model card) | ⚠️ Partial — citation verification and anthropomorphization tracking not specified |
| **MS-2.6-001 through 007** — Adverse human impacts on content moderators; training data safety assessment; fine-tuned model re-evaluation; GAI output review; error handling; safety circumvention evaluation | Part XII §12.2 (control validation); Part VIII §8.9 (workforce: content moderator welfare) | ⚠️ Partial — content moderator health/welfare assessment (MS-2.6-001) not addressed |
| **MS-2.7-001 through 009** — Security assessment against standard vectors; benchmark against industry standards; authentication metrics (watermark FP/FN rates); red-team against all adversarial ML categories; fine-tuning safety verification | Part XII §12.1–12.4; Part XIV §14.5 (behavioral fingerprinting) | ✅ |
| **MS-2.8-001 through 004** — IP violation/take-down statistics; annotator instruction documentation; tamper-proof content history; user testing of instructions | Part V §5.14 (LOG domain) | ⚠️ Partial — IP violation statistics and take-down request tracking not required |
| **MS-2.9-001/002** — XAI techniques (embedding analysis, counterfactual prompts); model card documentation | Part V §5.3 (MDL-05: model card) | ✅ |
| **MS-2.10-001 through 003** — Red-team for privacy attacks; stakeholder engagement on provenance; training data deduplication | Part XII §12.1; Part V §5.11 | ⚠️ Partial — training data deduplication as a specific required practice not addressed |
| **MS-2.11-001 through 005** — Bias benchmarks; fairness assessments by demographic; community engagement; data source bias documentation; synthetic data proportion assessment (model collapse prevention) | Part V §5.2 (DAT-05: bias testing); GEN-05 (fairness testing) | ⚠️ Partial — model collapse / synthetic data proportion monitoring not addressed |
| **MS-2.12-001 through 004** — Environmental safety to physical environments; design impact documentation; energy/water consumption measurement; carbon offset verification | Not addressed | ❌ Gap — environmental impact assessment not in EAGCF |
| **MS-2.13-001** — Measurement error models for pre-deployment metrics | Part XII §12.2 | ⚠️ Partial |
| **MS-3.2-001** — Emergent risk identification including external consultation | Part VII §7.3 (incident taxonomy); Part VI §6.7 (external assurance) | ✅ |
| **MS-3.3-001 through 005** — Demographic impact assessments; user studies on AI content perception; bias testing in generated content; training materials; structured community feedback | Part VIII §8.9 (workforce enablement); Part VII §7.1 (user feedback signals) | ⚠️ Partial — community impact assessments and cultural group studies not required |
| **MS-4.2-001 through 005** — Adversarial testing cadence; real-world validation; interpretability for deployed decisions; override documentation; public feedback integration into design | Part XII §12.1; Part VII §7.4 | ⚠️ Partial — documentation of human override instances not specifically required |

---

## 6. MANAGE Function: Suggested Actions vs. EAGCF

| NIST AI 600-1 Suggested Action | EAGCF Coverage | Status |
|---|---|---|
| **MG-1.3-001/002** — Document trade-offs; staged release; monitor risk controls | Part IV §4.6 (exception model); Part VII §7.4 (corrective action) | ✅ |
| **MG-2.2-001 through 009** — Risk tolerance guideline comparison; training data provenance tracking; feedback loop monitoring; bias remediation; harmful content due diligence; real-time auditing; structured feedback; synthetic data PETs | Part VII §7.1; Part V §5.2 | ⚠️ Partial — synthetic data PETs and real-time audit tools for content lineage not specified |
| **MG-2.3-001** — GAI incident response and recovery plans including value chain; stakeholder communication details | Part VII §7.3; Part VII §7.4 | ✅ |
| **MG-2.4-001 through 004** — Deactivation communication plans; escalation for deactivation; remediation timelines; deactivation criteria review | Part IV §4.7 (exception/waiver); Part VII §7.3 (incident escalation) | ✅ |
| **MG-3.1-001 through 005** — Third-party risk tolerance application; value chain testing (poisoning, malware, labor, data privacy, geopolitical); fine-tuned model reassessment; IP/CBRN review of training data; review of model cards/system cards | Part V §5.9 (VND domain); Part V §5.11 (MSC domain); Deliverable G §G.13 | ✅ |
| **MG-3.2-001 through 009** — XAI for monitoring; fine-tuning documentation with baseline access; training data documentation; user-reported content feedback; content filters; real-time monitoring alerts; governance board recommendations; human moderation; decommission/retrain triggers | Part VII §7.1 (monitoring); Part V §5.3 (MDL); GEN-08 | ⚠️ Partial — access to un-tuned baseline models for debugging not required; governance board input for third-party models not required |
| **MG-4.1-001 through 007** — External awareness of emerging practices; post-deployment monitoring for confabulation/CBRN/cyber; sentiment analysis; active learning for failure identification; transparency reports; dataset modification tracking; escalation capability | Part VII §7.1 (monitoring signals); Part IV §4.3 (transparency) | ⚠️ Partial — transparency reports to external stakeholders; dataset modification tracking (provenance for deletions/rectification) not specified |
| **MG-4.2-001 through 003** — Regular monitoring reports; incident post-mortems; visualizations for non-technical stakeholders | Part VII §7.4 (post-incident); Part VI §6.1 (board reporting) | ✅ |
| **MG-4.3-001 through 003** — After-action assessments; error/near-miss tracking; legal/regulatory reporting (HIPAA, etc.) | Part VII §7.4 (corrective action); Part VIII §8.8 (sector overlays: HIPAA, SR 11-7) | ✅ |

---

## 7. Content Provenance vs. EAGCF

NIST AI 600-1 Appendix A.3 makes content provenance a major governance theme, with four provenance techniques. Mapping to EAGCF:

| Content Provenance Element | EAGCF Coverage | Status |
|---|---|---|
| **Digital watermarking** | Part V §5.11 (MSC-08: watermarking) | ✅ |
| **Metadata recording** (origin, creator, date, modifications) | Part V §5.14 (LOG domain: LOG-02/03 metadata); Part V §5.11 (MSC-01/02: provenance attestation) | ✅ |
| **Digital fingerprinting** | Part XIV §14.5 (behavioral fingerprinting) | ⚠️ Partial — behavioral fingerprinting for model integrity; content fingerprinting for output provenance not addressed |
| **Human authentication** (human-generated vs. AI-generated labeling) | Part V §5.7 (OUT-04: output labeling) | ✅ |
| **Provenance for training data** (tracking all training data transformations) | Part V §5.11 (MSC-01/02) | ✅ |
| **Watermarking robustness-complexity trade-off acknowledgment** | Not acknowledged | ❌ Gap — theoretical limits of watermarking (from NIST AI 100-2 comparison also) |
| **Provenance measurement effectiveness evaluation** | Part XII §12.2 (control validation matrix) | ⚠️ Partial |

---

## 8. Incident Disclosure vs. EAGCF

NIST AI 600-1 Appendix A.4 establishes minimum incident reporting criteria and calls for AI incident database reporting.

| Incident Disclosure Element | EAGCF Coverage | Status |
|---|---|---|
| **Minimum incident fields** (System ID, Title, Reporter, Date, Description, Impact, Stakeholders) | Part VII §7.3 (incident taxonomy — 4 severity levels, 7 categories) | ⚠️ Partial — severity and category fields present; standardized minimum field set for incident record not formalized |
| **Reporting to AI incident databases** (AVID, OECD AI incident monitor) | Not addressed | ❌ Gap — also gap from NIST 800-1 comparison (N801-07 variant) |
| **After-action communication to legal/regulatory bodies** | Part VIII §8.8 (sector overlays: HIPAA, SR 11-7) | ⚠️ Partial |

---

## 9. Scoring Summary

| NIST AI 600-1 Section | Items | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| 12 GenAI Risk Categories | 12 | 8 | 0 | 3 | 1 |
| GOVERN Function (~40 actions) | 40 | 13 | 0 | 24 | 3 |
| MAP Function (~20 actions) | 20 | 5 | 0 | 10 | 5 |
| MEASURE Function (~35 actions) | 35 | 7 | 0 | 25 | 3 |
| MANAGE Function (~30 actions) | 30 | 13 | 0 | 17 | 0 |
| Content Provenance | 7 | 4 | 0 | 2 | 1 |
| Incident Disclosure | 3 | 0 | 0 | 2 | 1 |
| **TOTALS** | **147 items** | **50 (34%)** | **0 (0%)** | **83 (56%)** | **14 (10%)** |

**Coverage interpretation:** 90% total coverage (34% direct + 56% partial). The very high partial rate reflects that NIST AI 600-1 goes deeper into GenAI-specific *implementation detail* (content provenance, specific metrics, structured public feedback design) than EAGCF's governance-level controls. EAGCF covers the *what* and *who* of these requirements; NIST AI 600-1 provides the *how* and *measure* specifics. This is the expected relationship for a backbone document.

The 10% gap rate (14 items) includes:
- Environmental impact (confirmed critical gap N-06)
- Interdisciplinary team diversity (confirmed critical gap N-01)
- External stakeholder feedback loops (confirmed gaps N-02/N-03)
- Content fingerprinting (distinct from behavioral fingerprinting)
- AI incident database reporting (confirmed gap from 800-1)
- Watermarking theoretical limits acknowledgment
- Training data consent withdrawal / machine unlearning (confirmed gap N1002-04)

---

## 10. Where EAGCF Materially Exceeds NIST AI 600-1

| Dimension | EAGCF Capability | NIST AI 600-1 |
|---|---|---|
| **Enforcement architecture** | 9 enforcement points (EP-1 through EP-9) — production-grade control implementation | Suggested actions (no implementation architecture) |
| **Agentic governance** | AGT-01 through AGT-10 (10 specific controls for single-agent and multi-agent) | Not addressed |
| **Risk tiering with lifecycle gates** | 5-tier model wired to 11-stage lifecycle with explicit gate intensity | GV-1.3 risk tiers defined but not lifecycle-wired |
| **Control taxonomy structure** | 15 domains, 97+ controls, preventive/detective/corrective | Suggested actions (not structured as control taxonomy) |
| **Governance operating model** | 9 bodies, RACI, decision rights, review cadences | GV function describes roles; no operating model |
| **Vendor scoring model** | 6-dimension scoring, behavioral fingerprinting, multi-model fallback | GV-6 third-party actions; no scoring model |
| **CI/CD governance integration** | 5-gate pipeline, 6 pre-commit hooks | Not addressed |
| **Sector overlays** | Financial services (SR 11-7), healthcare (HIPAA), safety-critical | Not addressed |
| **Cost governance** | SLA model, ROI metrics, misallocation diagnostic | Not addressed |
| **Adoption acceleration** | Fast-lane approval, 7 anti-patterns, governance theater warning | Not addressed |
| **Model supply chain provenance** | MSC-01 through MSC-08 (training data → quantization → watermarking) | Value chain and data provenance addressed; no supply chain control architecture |

---

## 11. Gap Items: Recommended EAGCF Additions from NIST AI 600-1

| Gap ID | NIST AI 600-1 Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N600-01** | Risk category 5 | **Environmental impact assessment**: Require energy/water consumption estimation and carbon impact documentation for AI model training, fine-tuning, and high-volume deployment (especially LLMs). Aligns with N-06 from NIST 100-1 comparison | High | Part V §5.15 GEN domain — add GEN-09: Environmental Impact Reporting; or Part IV §4.1 (Tier 1+ gate: require environmental assessment) |
| **N600-02** | MP-1.2 | **Interdisciplinary team diversity requirement**: Require that AI use case review teams include diverse demographics, domain expertise, and lived experience representations, not just technical staff. Aligns with N-01 from NIST 100-1 comparison | High | Part VI §6.3 (AI governance office) — add diversity requirement to team composition |
| **N600-03** | MP-5.2 / GV-5.1 | **External stakeholder feedback loop**: Require structured external feedback mechanisms (participatory engagement, community forums) for Tier 1 (High) AI systems affecting external populations. Aligns with N-02/N-03 from NIST 100-1 comparison | High | Part IV §4.3 (transparency) — add stakeholder feedback requirement for Tier 1/2 systems |
| **N600-04** | Appendix A.4 | **Standardized incident reporting fields**: Define minimum required fields for all AI incident records (System ID, Title, Reporter, Source, Date Reported, Date of Incident, Description, Impact(s), Stakeholders Impacted) | Medium | Part VII §7.3 (incident taxonomy) — add minimum field standard to incident record template |
| **N600-05** | Appendix A.4 / GV-4.3 | **AI incident database reporting**: Require reporting of verified AI incidents to external AI incident databases (AVID, OECD AI incident monitor, CVE/NVD for AI security issues) for Tier 0/1 systems | Medium | Part VII §7.4 (corrective action) — add external reporting requirement for Tier 0/1 incidents |
| **N600-06** | GV-2.1-005 / GV-4.1 | **AI safety whistleblower protection**: Formal policy protecting internal reporters of AI safety violations or well-substantiated public safety risks. Aligns with N801-06 from NIST 800-1 comparison | Medium | Part VI §6.3 or Part IV §4.4 — add whistleblower protection policy requirement |
| **N600-07** | MS-2.11-005 | **Model collapse / synthetic data proportion monitoring**: Require assessment of synthetic data proportion in training data and monitoring for model collapse indicators (distribution collapse, output homogenization) | Medium | Part V §5.11 (MSC-01) — add model collapse risk as a data provenance concern; Part VII §7.1 (MON) — add MON-23: synthetic data proportion signal |
| **N600-08** | GV-1.6-003 | **AI inventory: known issues from AVID/CVE/OECD**: Require AI system inventory to include known vulnerabilities and incidents from external AI incident databases (AVID, CVE, OECD AI incident monitor, NVD) | Low | Deliverable G §G.5 (AI Use Case Registration) — add known vulnerability fields |
| **N600-09** | MS-2.12 | **Content moderator welfare assessment**: For AI systems requiring human content moderation at scale (GenAI output review, harmful content labeling), require health and wellbeing impact assessment for content moderation personnel exposed to harmful content | Low | Part VIII §8.9 (workforce enablement) — add content moderator welfare requirement |
| **N600-10** | A.3 (Content Provenance) | **Content digital fingerprinting**: Distinct from behavioral fingerprinting (model integrity), add content fingerprinting for tracking AI-generated output provenance through distribution chains | Low | Part V §5.11 (MSC-08) — extend watermarking control to include digital fingerprinting as a content provenance technique |

---

## 12. Synthesis

NIST AI 600-1 is the **most directly relevant** comparison document for EAGCF because it is explicitly referenced as a backbone document in EAGCF's execution layer and shares the same AI RMF 1.0 structure. The 90% coverage rate (highest across all comparisons so far) reflects this close architectural alignment.

**Highest-value additions:**
1. **Environmental impact** (N600-01) — a regulatory and reputational risk increasingly material in EU AI Act context
2. **Interdisciplinary team diversity** (N600-02) — confirmed critical gap across both NIST 100-1 and 600-1
3. **External stakeholder feedback loops** (N600-03) — confirmed gap across NIST 100-1 and 600-1
4. **Model collapse monitoring** (N600-07) — novel risk not in EAGCF; important for LLM-heavy deployments
5. **AI incident database reporting** (N600-05) — important for ecosystem-level accountability

**Integration posture:** EAGCF should formally reference NIST AI 600-1 in the executive summary and in GEN domain (Part V §5.15) as the primary technical implementation guide for GenAI-specific controls. The alignment is already strong; the gaps are at the measurement, transparency, and social/environmental dimensions that EAGCF's governance-first design underweights.

**Coverage summary:**
- NIST AI 600-1 items with direct EAGCF coverage: **50 (34%)**
- NIST AI 600-1 items partially covered: **83 (56%)**
- NIST AI 600-1 items not addressed: **14 (10%)**
- Items where EAGCF materially exceeds NIST AI 600-1: **11 dimensions**

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Next comparison in sequence: NIST AI 100-5 (AI Use in Cybersecurity) or NIST AI 700-1/700-2 (AI Standards)*
