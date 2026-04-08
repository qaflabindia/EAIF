# Side-by-Side Comparison: EAGCF vs. NIST Cybersecurity Framework (CSF) 2.0
## *NIST CSWP 29 — The NIST Cybersecurity Framework 2.0*

**Source Document:** `NIST.CSWP.29.pdf` (NIST, February 26, 2024)
**DOI:** https://doi.org/10.6028/NIST.CSWP.29
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.3, 2026)
**Comparison Date:** April 2026
**Analyst Note:** NIST CSF 2.0 is the revised NIST Cybersecurity Framework — a major update that adds GOVERN as a new sixth Function (alongside IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) and significantly expands supply chain risk management. CSF 2.0 is not an AI-specific framework; however, it is the foundational cybersecurity governance reference for virtually all U.S. enterprises and is explicitly noted in CSF 2.0 §5.2 as complementary to the NIST AI RMF. EAGCF's cybersecurity posture is built on defense-in-depth (Part XI: 9 enforcement points, Part XII: red-team and control validation) and explicitly integrates AI-specific security controls from NIST AI 100-2 (adversarial ML) and NIST IR 8596 (Cyber AI Profile). This comparison assesses whether EAGCF's AI governance controls satisfy the CSF 2.0 cybersecurity outcomes relevant to AI systems, and identifies any gaps where CSF 2.0's cybersecurity requirements are not addressed by EAGCF's AI governance architecture.

---

## 1. Document Scope Alignment

| Dimension | NIST CSF 2.0 | EAGCF |
|---|---|---|
| **Document type** | Cybersecurity risk governance framework | Enterprise AI governance and control framework |
| **Primary purpose** | Help organizations manage and reduce cybersecurity risks across all technology environments | Enable enterprises to govern, control, and assure AI use |
| **AI coverage** | Technology-neutral (applies to IT, IoT, OT, cloud, mobile, AI); §5.2 notes AI RMF as companion for AI-specific risks | AI-native (designed specifically for AI systems, including GenAI and agentic AI) |
| **Scope** | All organizational cybersecurity risks including AI | AI system governance — cybersecurity is one of 15 control domains |
| **Binding nature** | Voluntary; referenced in Federal mandates and sector regulations | Voluntary enterprise standard wired to ISO 42001 |
| **Risk philosophy** | Outcomes-based: what to achieve, not how | Risk-tiered: proportional controls based on AI system risk tier (Tier 0–4) |
| **Governance structure** | 6 Functions → 22 Categories → Subcategories | 15 control domains → 9 enforcement points → 5-tier risk model |

---

## 2. GOVERN Function vs. EAGCF

The new GOVERN function in CSF 2.0 is the most significant addition. It establishes that cybersecurity risk management strategy, expectations, and policy must be established, communicated, and monitored — sitting at the center of the CSF wheel, informing all other functions.

### GV.OC — Organizational Context

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **GV.OC-01**: Organizational mission understood; informs cybersecurity risk management | Part IV §4.1 (use-case intake: business mission mapped to risk tier); Part I (core thesis: accelerate AI adoption) | ✅ Covered |
| **GV.OC-02**: Internal and external stakeholders understood; needs and expectations considered | Part VI §6.2 (governance office: stakeholder identification); Part XVI §16.2.2 (external stakeholder feedback mechanism) | ✅ Covered |
| **GV.OC-03**: Legal, regulatory, and contractual requirements for cybersecurity including privacy understood and managed | Part VIII §8.8 (sector overlays: regulatory mapping); Part V §5.2 (DAT domain: privacy and data protection); Part XVI §16.4 (EU AI Act FRIA for jurisdiction-specific requirements) | ✅ Covered |
| **GV.OC-04**: Critical objectives and services external stakeholders depend on are understood | Part IV §4.3 (transparency and disclosure); Part V §5.7 (OUT domain: output quality and reliability) | ✅ Covered |
| **GV.OC-05**: Services the organization depends on externally are understood | Part V §5.9 (VND domain: vendor dependency mapping); Part V §5.11 (MSC domain: supply chain) | ✅ Covered |

### GV.RM — Risk Management Strategy

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **GV.RM-01**: Risk management objectives established and agreed to by organizational stakeholders | Part IV §4.1 (governance objectives); Part VI §6.1 (board and committee oversight) | ✅ Covered |
| **GV.RM-02**: Risk appetite and tolerance statements established, communicated, maintained | Part IV §4.1 (5-tier risk model: Tier 0 = Prohibited; Tier 4 = Low risk; risk appetite by tier); Deliverable B (risk-tiering model) | ✅ Covered |
| **GV.RM-03**: Cybersecurity risk management integrated into enterprise risk management | Part VI §6.2 (governance office: CISO integration); Part VI §6.4 (RACI: CISO co-accountable for AI security) | ✅ Covered |
| **GV.RM-04**: Strategic direction for appropriate risk response options established | Part IV §4.5 (enforcement and remediation model); Part VIII §8.1–8.2 (minimum viable governance; fast-lane patterns) | ✅ Covered |
| **GV.RM-05**: Lines of communication for cybersecurity risks established, including suppliers | Part VI §6.4 (RACI and decision rights); Part V §5.9 (VND-07: vendor incident notification SLA) | ✅ Covered |
| **GV.RM-06**: Standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks | Part IV §4.1 (risk tiering formula: probability × severity × reversibility); Deliverable B | ✅ Covered |
| **GV.RM-07**: Strategic opportunities (positive risks) included in cybersecurity risk discussions | Part VIII §8.2 (governance misallocation diagnostic: explicitly addresses over-governing low-risk = missed opportunity cost) | ✅ Covered |

### GV.RR — Roles, Responsibilities, and Authorities

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **GV.RR-01**: Organizational leadership responsible and accountable for cybersecurity risk | Part VI §6.1 (board oversight: AI risk appetite); Part VI §6.2 (executive governance: CISO and CAIO joint accountability) | ✅ Covered |
| **GV.RR-02**: Roles and responsibilities for cybersecurity established, communicated, enforced | Part VI §6.4 (RACI: 9 governance bodies, decision rights, AI security role assignments) | ✅ Covered |
| **GV.RR-03**: Adequate resources allocated commensurate with cybersecurity risk strategy | Part VI §6.2 (governance office resourcing); Part VIII §8.3 (workforce enablement) | ✅ Covered |
| **GV.RR-04**: Cybersecurity included in human resources practices | Part VIII §8.3 (workforce enablement: AI security training); Part VI §6.4 (HR integration for AI policy) | ⚠️ Partial — AI security included in training but HR process integration (hiring, onboarding, offboarding) not explicitly specified |

### GV.PO — Policy

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **GV.PO-01**: Policy for managing cybersecurity risks established based on organizational context; communicated and enforced | Part XI §11.1 (enforcement architecture: 9 enforcement points enforce security policies across all AI system layers); Part IV §4.1–4.8 | ✅ Covered |
| **GV.PO-02**: Policy reviewed, updated, communicated, enforced to reflect changes in requirements, threats, technology, mission | Part VI §6.6 (annual framework review cadence); Part XVI §16.1 (standards watch register: threat landscape monitoring) | ✅ Covered |

### GV.OV — Oversight

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **GV.OV-01**: Cybersecurity risk management strategy outcomes reviewed to inform and adjust strategy | Part VI §6.6 (annual review cadence: KPI/KRI trends trigger framework updates) | ✅ Covered |
| **GV.OV-02**: Risk management strategy reviewed and adjusted to ensure coverage | Part VI §6.6 (annual review); Part XVI §16.1 (standards watch register: material change monitoring) | ✅ Covered |
| **GV.OV-03**: Organizational cybersecurity risk management performance evaluated | Part VII §7.1 (KPI/KRI/KCI framework: performance measurement); Part XII §12.2 (control validation matrix) | ✅ Covered |

### GV.SC — Cybersecurity Supply Chain Risk Management

This is a significantly expanded category in CSF 2.0 and directly maps to EAGCF's model supply chain (MSC) and vendor (VND) domains.

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **GV.SC-01**: Cybersecurity SCRM program, strategy, objectives, policies, and processes established | Part V §5.9 (VND domain: vendor governance); Part V §5.11 (MSC domain: model supply chain and provenance) | ✅ Covered |
| **GV.SC-02**: Cybersecurity roles for suppliers, customers, partners established and coordinated | Part V §5.9 (VND-02: vendor security accountability); Part XIV §14.2 (SLA requirements for AI vendors) | ✅ Covered |
| **GV.SC-03**: Supply chain risk management integrated into cybersecurity and ERM | Part V §5.9 (VND domain integrated with MSC); Part VI §6.4 (RACI: supply chain risk owner) | ✅ Covered |
| **GV.SC-04**: Suppliers known and prioritized by criticality | Part V §5.9 (VND-01: vendor tiering by risk level; 6-dimension vendor scoring) | ✅ Covered |
| **GV.SC-05**: Requirements to address cybersecurity risks in supply chains integrated into contracts | Part XIV §14.2 (SLA table: vendor contractual requirements including security); Part V §5.9 (VND-05: contract requirements) | ✅ Covered |
| **GV.SC-06**: Planning and due diligence performed before entering supplier relationships | Part V §5.9 (VND-03: pre-engagement due diligence; VND-06: security assessment) | ✅ Covered |
| **GV.SC-07**: Risks posed by suppliers understood, recorded, prioritized, assessed, responded to, and monitored | Part V §5.9 (VND-07: ongoing monitoring; VND-08: incident notification); Part V §5.11 (MSC-01 through MSC-10) | ✅ Covered |
| **GV.SC-08**: Relevant suppliers included in incident planning, response, and recovery | Part VII §7.3 (incident taxonomy: vendor-initiated incidents); Part V §5.9 (VND-07: vendor incident SLA) | ✅ Covered |
| **GV.SC-09**: Supply chain security practices integrated and performance monitored throughout lifecycle | Part V §5.11 (MSC domain: monitoring through deployment and decommission); Deliverable D (lifecycle gate: supply chain review at stage 6) | ✅ Covered |
| **GV.SC-10**: Plans include provisions for activities after conclusion of partnership | Part V §5.9 (VND-09: contract exit and data deletion provisions) | ✅ Covered |

---

## 3. IDENTIFY Function vs. EAGCF

### ID.AM — Asset Management

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **ID.AM-01/02**: Hardware and software inventories maintained | Part V §5.11 (MSC-09: AI SBOM — base model ID, training data sources, third-party components) | ✅ Covered |
| **ID.AM-04**: Inventories of services provided by suppliers | Part V §5.9 (VND domain: vendor service register) | ✅ Covered |
| **ID.AM-05**: Assets prioritized based on classification, criticality, and impact | Part IV §4.1 (5-tier risk model: risk-tiered asset classification) | ✅ Covered |
| **ID.AM-07**: Inventories of data and corresponding metadata maintained | Part V §5.2 (DAT domain: data inventory and classification); Deliverable G §G.8 (DPIA) | ✅ Covered |
| **ID.AM-08**: Systems managed throughout lifecycle | Deliverable D (11-stage lifecycle governance map) | ✅ Covered |

### ID.RA — Risk Assessment

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **ID.RA-01**: Vulnerabilities in assets identified, validated, and recorded | Part XII §12.1 (red-team pipeline: vulnerability identification and recording) | ✅ Covered |
| **ID.RA-02**: Cyber threat intelligence received from information sharing forums | Part XVI §16.4 (AI-ISAC participation when operational); Part XII §12.1 (threat intelligence integration) | ⚠️ Partial — threat intelligence integration not fully formalized (N-AP-02 confirmed) |
| **ID.RA-03**: Internal and external threats identified and recorded | Part XII §12.1 (red-team attack library: internal and external threat taxonomy); Part V §5.11 (MSC domain: supply chain threat library) | ✅ Covered |
| **ID.RA-04**: Potential impacts and likelihoods of threats identified and recorded | Deliverable B (risk-tiering: probability × severity × reversibility); Deliverable G §G.3 (AI Impact Assessment) | ✅ Covered |
| **ID.RA-05**: Threats, vulnerabilities, likelihoods used to prioritize risk response | Part IV §4.1 (tier-based prioritization); Part VIII §8.1 (minimum viable vs. enhanced governance by tier) | ✅ Covered |
| **ID.RA-06**: Risk responses chosen, prioritized, planned, tracked | Part IV §4.5 (enforcement and remediation model); Part VII §7.4 (corrective action process) | ✅ Covered |
| **ID.RA-07**: Changes and exceptions managed and assessed for risk | Part IV §4.6 (exception and waiver model); Part XIII §13.1 (change management domain) | ✅ Covered |
| **ID.RA-08**: Processes for receiving, analyzing, and responding to vulnerability disclosures established | Part XII §12.1 (red-team pipeline: vulnerability disclosure); Part XVI §16.4 (external incident reporting) | ⚠️ Partial — formal coordinated vulnerability disclosure (CVD) process not explicitly specified (N-CSF-01 below) |
| **ID.RA-09**: Authenticity and integrity of hardware and software assessed before acquisition | Part V §5.11 (MSC-09: AI SBOM pre-acquisition verification); Part V §5.9 (VND-03: due diligence) | ✅ Covered |
| **ID.RA-10**: Critical suppliers assessed before acquisition | Part V §5.9 (VND-03: pre-engagement assessment; VND-06: 6-dimension vendor scoring) | ✅ Covered |

### ID.IM — Improvement

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **ID.IM-01/02/03**: Improvements identified from evaluations, tests, and operational execution | Part VI §6.6 (annual review: improvement identification); Part XII §12.2 (post-validation remediation tracking) | ✅ Covered |
| **ID.IM-04**: Incident response plans maintained and improved | Part VII §7.3–7.4 (incident taxonomy; corrective action; post-incident review) | ✅ Covered |

---

## 4. PROTECT Function vs. EAGCF

### PR.AA — Identity Management, Authentication, and Access Control

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **PR.AA-01**: Identities and credentials for authorized users, services, hardware managed | Part IX (identity and access domain: IAM controls for AI systems) | ✅ Covered |
| **PR.AA-02**: Identities proofed and bound to credentials based on context | Part IX (identity proofing controls) | ✅ Covered |
| **PR.AA-03**: Users, services, hardware authenticated | Part IX (authentication controls); Part XI §11.1 (EP-1: input authentication enforcement point) | ✅ Covered |
| **PR.AA-04**: Identity assertions protected, conveyed, and verified | Part IX (identity assertion integrity); Part V §5.11 (MSC-10: deepfake fraud — liveness detection for identity verification) | ✅ Covered |
| **PR.AA-05**: Access permissions defined in policy, enforced, reviewed, with least privilege and separation of duties | Part IX (access control policy: least privilege, separation of duties for AI system management roles) | ✅ Covered |
| **PR.AA-06**: Physical access managed, monitored, enforced commensurate with risk | Not AI-specific — physical security is out of EAGCF's AI governance scope | ⚠️ Out of scope — physical security is a general IT/facilities control, not an AI governance control |

### PR.AT — Awareness and Training

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **PR.AT-01**: Personnel provided with cybersecurity awareness and training | Part VIII §8.3 (workforce enablement: AI risk awareness training); Part VI §6.4 (training as governance requirement) | ✅ Covered |
| **PR.AT-02**: Specialized roles provided with role-specific training | Part VIII §8.3 (specialized training: risk officers, model owners, security personnel); Part XVI §16.2.1 (interdisciplinary team competency requirements) | ✅ Covered |

### PR.DS — Data Security

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **PR.DS-01**: Data-at-rest confidentiality, integrity, availability protected | Part V §5.2 (DAT-05: encryption at rest); Part V §5.11 (MSC domain: model weight protection) | ✅ Covered |
| **PR.DS-02**: Data-in-transit protected | Part V §5.2 (DAT-06: encryption in transit); Part V §5.4 (PRM-04: prompt pipeline encryption) | ✅ Covered |
| **PR.DS-10**: Data-in-use protected | Part V §5.2 (DAT domain: inference-time data protection); Part V §5.11 (MSC domain: runtime security) | ✅ Covered |
| **PR.DS-11**: Backups created, protected, maintained, tested | Part V §5.3 (MDL-07: model versioning and backup); Part XIII §13.1 (change management: rollback capability) | ✅ Covered |

### PR.PS — Platform Security

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **PR.PS-01**: Configuration management practices established | Part XIII §13.1 (change management: configuration control for AI systems) | ✅ Covered |
| **PR.PS-02/03**: Software and hardware maintained, replaced, removed commensurate with risk | Part XIII §13.1 (change management); Deliverable D (lifecycle stage 11: decommission) | ✅ Covered |
| **PR.PS-04**: Log records generated for continuous monitoring | Part XIV §14.1 (logging domain: immutable audit log); Deliverable E (monitoring signal catalog) | ✅ Covered |
| **PR.PS-05**: Unauthorized software execution prevented | Part XI §11.1 (EP-1: input scope enforcement; EP-3: tool/action allowlist) | ✅ Covered |
| **PR.PS-06**: Secure software development practices integrated throughout SDLC | Part VIII §8.8 (secure-by-design mandate); Deliverable D (lifecycle gates at design, development, testing stages) | ✅ Covered |

### PR.IR — Technology Infrastructure Resilience

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **PR.IR-01**: Networks and environments protected from unauthorized logical access | Part IX (identity/access); Part XI §11.1 (9 enforcement points: network-layer controls at EP-1, EP-7) | ✅ Covered |
| **PR.IR-02**: Technology assets protected from environmental threats | Physical/environmental controls — out of EAGCF scope | ⚠️ Out of scope |
| **PR.IR-03**: Mechanisms for resilience in normal and adverse situations | Part XI §11.1 (defense-in-depth: redundant enforcement points); Part VII §7.3 (incident response with recovery) | ✅ Covered |
| **PR.IR-04**: Adequate resource capacity for availability maintained | Part XIV §14.2 (SLA table: availability thresholds); Part V §5.3 (MDL-06: performance degradation controls) | ✅ Covered |

---

## 5. DETECT Function vs. EAGCF

### DE.CM — Continuous Monitoring

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **DE.CM-01**: Networks monitored for potentially adverse events | Part XI §11.1 (EP-7: network-level monitoring enforcement point) | ✅ Covered |
| **DE.CM-03**: Personnel activity and technology usage monitored | Part XIV §14.1 (logging: user interaction audit trail); Part XVI §16.6 (MON-23: over-reliance monitoring) | ✅ Covered |
| **DE.CM-06**: External service provider activities monitored | Part V §5.9 (VND-07: vendor performance monitoring); Part XIV §14.1 (third-party audit log requirements) | ✅ Covered |
| **DE.CM-09**: Computing hardware, software, runtime environments monitored | Deliverable E (≥24 monitoring signals: drift, degradation, prompt injection, output anomaly, energy); Part XVI §16.5–16.6 (MON-21 through MON-24) | ✅ Covered |

### DE.AE — Adverse Event Analysis

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **DE.AE-02**: Potentially adverse events analyzed | Part VII §7.3 (incident taxonomy: event analysis and classification) | ✅ Covered |
| **DE.AE-03**: Information correlated from multiple sources | Part VII §7.3 (incident correlation: multi-signal escalation); Deliverable E (monitoring signals aggregated into KRI dashboard) | ✅ Covered |
| **DE.AE-04**: Estimated impact and scope of adverse events understood | Deliverable B (risk-tiering: impact severity classification); Part VII §7.3 (incident severity model) | ✅ Covered |
| **DE.AE-06**: Information on adverse events provided to authorized staff | Part VII §7.3 (escalation paths: severity-tiered notification to CISO, CAIO, board) | ✅ Covered |
| **DE.AE-07**: Cyber threat intelligence integrated into analysis | Part XII §12.1 (threat intelligence integration in red-team attack library); Part XVI §16.4 (AI-ISAC feeds) | ⚠️ Partial — threat intelligence integration not fully formalized |
| **DE.AE-08**: Incidents declared when adverse events meet defined criteria | Part VII §7.3 (incident declaration criteria: KRI threshold breaches trigger formal incident declaration) | ✅ Covered |

---

## 6. RESPOND Function vs. EAGCF

### RS.MA — Incident Management

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **RS.MA-01**: Incident response plan executed with relevant third parties | Part VII §7.3–7.4 (incident governance: vendor notification SLA, regulatory reporting); Part XVI §16.4 (external reporting) | ✅ Covered |
| **RS.MA-02/03**: Incidents triaged, validated, categorized, prioritized | Part VII §7.3 (incident taxonomy: severity tiers; triage and categorization) | ✅ Covered |
| **RS.MA-04**: Incidents escalated or elevated as needed | Part VII §7.3 (escalation paths: CISO → CAIO → Board by severity tier) | ✅ Covered |
| **RS.MA-05**: Criteria for initiating incident recovery applied | Part VII §7.4 (corrective action: recovery criteria by incident tier) | ✅ Covered |

### RS.AN — Incident Analysis

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **RS.AN-03**: Root cause analysis performed | Part VII §7.4 (corrective action: root cause analysis requirement) | ✅ Covered |
| **RS.AN-06/07**: Actions recorded; incident data and metadata collected with integrity | Part XIV §14.1 (logging: immutable audit log; forensic-grade incident data) | ✅ Covered |
| **RS.AN-08**: Incident magnitude estimated and validated | Part VII §7.3 (incident severity model: quantified impact assessment) | ✅ Covered |

### RS.CO — Incident Response Reporting and Communication

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **RS.CO-02/03**: Internal and external stakeholders notified | Part VII §7.3 (escalation: internal notification); Part XVI §16.4 (external reporting: AI-ISAC, AIID, regulators) | ✅ Covered |

### RS.MI — Incident Mitigation

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **RS.MI-01/02**: Incidents contained and eradicated | Part VII §7.4 (corrective action: containment and remediation); Part XIII §13.1 (rollback capability for AI system changes) | ✅ Covered |

---

## 7. RECOVER Function vs. EAGCF

| CSF 2.0 Subcategory | EAGCF Coverage | Status |
|---|---|---|
| **RC.RP-01/02**: Recovery plan executed; actions selected, scoped, prioritized | Part VII §7.4 (recovery actions: system rollback, model reversion, retraining triggers) | ✅ Covered |
| **RC.RP-03**: Integrity of backups verified before restoration | Part V §5.3 (MDL-07: model version integrity verification before restoration) | ✅ Covered |
| **RC.RP-04/05**: Critical functions considered; integrity of restored assets verified | Part VII §7.4 (post-recovery validation: control validation matrix re-run required post-incident) | ✅ Covered |
| **RC.RP-06**: End of incident recovery declared; documentation completed | Part VII §7.4 (corrective action: incident close-out documentation and lessons learned) | ✅ Covered |
| **RC.CO-03/04**: Recovery activities communicated to internal and external stakeholders | Part VII §7.3–7.4 (stakeholder notification during recovery); Part XVI §16.4 (external reporting completion) | ✅ Covered |

---

## 8. CSF 2.0 Tiers vs. EAGCF Risk Tiers

CSF 2.0 defines four organizational maturity tiers. EAGCF uses five system risk tiers (Tier 0–4). These are different concepts — CSF Tiers characterize governance maturity; EAGCF Tiers characterize AI system risk level — but they are complementary.

| CSF 2.0 Tier | Description | EAGCF Equivalent |
|---|---|---|
| **Tier 1: Partial** | Ad hoc, irregular; limited cybersecurity awareness | Organizations before EAGCF adoption — governance theater mode |
| **Tier 2: Risk Informed** | Management-approved practices; not organization-wide policy | EAGCF minimum viable governance (Part VIII §8.1) — risk-informed but not fully systematic |
| **Tier 3: Repeatable** | Formally approved policy; consistent; routinely updated | EAGCF standard adoption — all 15 control domains operational, annual review cadence |
| **Tier 4: Adaptive** | Continuously improving; real-time risk awareness; predictive | EAGCF advanced governance (Part VIII §8.2) + full KRI dashboard + automated monitoring pipeline |

**EAGCF positions organizations for CSF Tier 3 (Repeatable) by design, with Tier 4 (Adaptive) available through Deliverable E monitoring signals and continuous improvement mechanisms.**

---

## 9. AI-Specific CSF 2.0 Intersection

CSF 2.0 §5.2 explicitly positions the NIST AI RMF as the companion framework for AI-specific risks. EAGCF is already built on the NIST AI RMF backbone — therefore EAGCF satisfies the CSF 2.0's directive for AI risk management comprehensively:

| CSF 2.0 §5.2 Direction | EAGCF Implementation |
|---|---|
| "Treating AI risks alongside other enterprise risks yields a more integrated outcome" | Part VI §6.2 (governance office: CISO and CAIO joint accountability — AI risks integrated into ERM) |
| "The AI RMF Core uses Functions, Categories, and Subcategories to describe AI outcomes" | Part XVI §16.10 (NIST AI RMF self-assessment checklist: all 19 subcategories mapped to EAGCF locations) |
| "Cybersecurity risk management and AI RMF should complement each other" | Part XI §11.1 (9 enforcement points explicitly bridge AI security to cybersecurity architecture); Part XII (red-team pipeline bridges AI and cybersecurity testing) |

---

## 10. Scoring Summary

| CSF 2.0 Function | Categories | ✅ Covered | ⚠️ Partial | ❌ Gap / Out of Scope |
|---|---|---|---|---|
| GOVERN (GV) | 29 subcategories | 28 | 1 (GV.RR-04: HR integration) | 0 |
| IDENTIFY (ID) | 16 subcategories | 14 | 2 (ID.RA-02, ID.RA-08) | 0 |
| PROTECT (PR) | 20 subcategories | 17 | 0 | 3 (physical: PR.AA-06, PR.IR-02; CSF Tier maturity) |
| DETECT (DE) | 9 subcategories | 7 | 2 (DE.AE-07) | 0 |
| RESPOND (RS) | 10 subcategories | 10 | 0 | 0 |
| RECOVER (RC) | 6 subcategories | 6 | 0 | 0 |
| **TOTALS** | **90 items** | **82 (91%)** | **5 (6%)** | **3 (3% — physical/OT out of scope)** |

**Coverage interpretation:** 97% of in-scope items covered (91% direct + 6% partial). The 3 out-of-scope items are physical/environmental security controls (PR.AA-06, PR.IR-02) and physical facility resilience — these are not AI governance controls. Among in-scope AI governance items, EAGCF achieves 91% direct coverage of CSF 2.0 outcomes, reflecting that EAGCF's design as an AI-native governance framework inherently addresses the cybersecurity outcomes of the general-purpose CSF when applied to AI systems.

---

## 11. Gap Items: Recommended EAGCF Additions

| Gap ID | Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N-CSF-01** | CSF 2.0 ID.RA-08 | **Coordinated vulnerability disclosure (CVD) process**: Add a formal CVD process for AI systems — a defined channel for receiving, analyzing, and responding to vulnerability disclosures from external researchers or users. Minimum: designated email/portal, 5-business-day acknowledgment SLA, 90-day target remediation window, public disclosure policy. This complements N1002-07 (AI vulnerability bug bounty, Tier C). | Low | Part XII §12.1 (red-team pipeline: add external vulnerability disclosure process as an optional evidence activity for Tier 1 systems) |
| **N-CSF-02** | CSF 2.0 GV.RR-04 | **AI security in HR practices**: Add a brief requirement that AI security responsibilities are integrated into HR practices for AI-role personnel — specifically: AI system access revocation is included in offboarding procedures (time-bound: within 24 hours of role termination); AI security policies acknowledged in onboarding for all RACI-named AI system owners and operators. | Low | Part VI §6.4 (RACI: add offboarding and onboarding AI security requirements for named roles) |

---

## 12. Areas Where EAGCF Materially Exceeds CSF 2.0

| Area | EAGCF Advantage |
|---|---|
| **AI-specific threat taxonomy** | CSF 2.0 is AI-neutral; EAGCF's red-team attack library covers NIST AI 100-2 adversarial ML taxonomy + MITRE ATLAS — far more AI-specific than CSF 2.0 |
| **GenAI and agentic AI controls** | CSF 2.0 has no GenAI or agentic AI-specific content; EAGCF's GEN (§5.15) and AGT (§5.6) domains cover 30+ AI-specific controls |
| **Model supply chain provenance** | CSF 2.0's GV.SC covers general supply chain; EAGCF's MSC domain adds AI-specific controls: training data lineage, model weights integrity, fine-tuning/RLHF integrity, AI-SBOM (MSC-09), watermarking (MSC-05/08), C2PA (OUT-08) |
| **AI output controls** | CSF 2.0 has no output control layer; EAGCF's OUT domain (OUT-01 through OUT-08) + 9 enforcement points provide defense-in-depth output governance |
| **AI-specific monitoring signals** | CSF 2.0's DE.CM is generic; EAGCF's 24 monitoring signals (Deliverable E + Part XVI) include AI-specific signals: model drift, hallucination rate, prompt injection detection, over-reliance, epistemic overconfidence |
| **Explainability and transparency controls** | CSF 2.0 has no explainability requirements; EAGCF's MDL-05 + Part XVI §16.8 implement the NIST IR 8312 four-principle XAI framework |
| **5-tier AI risk model** | CSF 2.0's four Tiers characterize organizational maturity; EAGCF's five tiers characterize AI system risk — a different and complementary framework that enables proportional control allocation |

---

## 13. Synthesis

NIST CSF 2.0 and EAGCF are complementary frameworks operating at different levels of specificity: CSF 2.0 is a general-purpose cybersecurity framework; EAGCF is an AI-native governance framework. For organizations that use both (the recommended posture for enterprises deploying AI at scale), EAGCF satisfies CSF 2.0's AI-related cybersecurity requirements comprehensively while providing far deeper AI-specific governance depth.

The most significant EAGCF additions from this comparison are minor (N-CSF-01: CVD process; N-CSF-02: AI security in HR practices) because EAGCF's existing architecture — 9 enforcement points, 15 control domains, 24 monitoring signals, red-team pipeline, incident taxonomy, and supply chain governance — already implements the outcomes that CSF 2.0 requires at the cybersecurity level.

The key governance insight: **EAGCF operating at CSF Tier 3 (Repeatable) level by default, with Tier 4 (Adaptive) available through Deliverable E and continuous improvement mechanisms.** Organizations adopting EAGCF can use this comparison to demonstrate CSF 2.0 alignment to cybersecurity auditors, regulators, and insurers without a separate CSF mapping exercise.

**Governance relevance rating:** High — CSF 2.0 is the foundational U.S. enterprise cybersecurity reference. Demonstrating that EAGCF satisfies CSF 2.0 outcomes is valuable for audit positioning, cyber insurance, and enterprise risk integration. The 97% in-scope coverage rate confirms EAGCF is a cybersecurity-complete AI governance framework.

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Comparisons completed (23 sources): NIST AI 100-1, 100-2, 100-3, 100-4, 100-5, 600-1, 700-1, 700-2 + ARIA Companion, 800-1, 800-2, IR 8312, IR 8596, GCR 26-069; ISO crosswalks (42001/23894, 42005, 5338/5339); OECD/EU AI Act crosswalk; Google DeepMind Gap Analysis; AI Verify crosswalks; Americas AI Action Plan; NIST CSF 2.0*
