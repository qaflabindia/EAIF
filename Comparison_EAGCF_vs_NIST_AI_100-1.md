# Side-by-Side Comparison: EAGCF v1.2 vs NIST AI 100-1 (AI RMF 1.0)
**Date:** April 2026 | **Method:** Control-to-subcategory mapping across all 4 functions and 7 trustworthiness characteristics

---

## Reading Guide
- ✅ **Covered** — EAGCF has direct, explicit, operational equivalent
- ⚡ **Stronger** — EAGCF goes materially beyond NIST on this dimension
- ⚠️ **Partial** — EAGCF covers intent but with less depth or specificity
- ❌ **Gap** — NIST element has no substantive EAGCF equivalent
- ➕ **EAGCF-only** — Capability in EAGCF with no NIST equivalent

---

## 1. GOVERN Function — Side by Side

### GOVERN 1: Policies, Processes, and Procedures

| NIST AI RMF Subcategory | NIST Description (summary) | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| GOVERN 1.1 | Legal/regulatory requirements understood, managed, documented | Section 4.5 (regulatory mapping table); Deliverable G.1 (AI policy); VND-02 (contractual obligations) | ✅ Covered | EAGCF maps 5 regulatory instruments with enterprise delta requirements |
| GOVERN 1.2 | Trustworthiness characteristics integrated into policies, processes | Section 4.2 (all 6 principles → controls translation with owner + evidence + monitoring signal per principle) | ⚡ Stronger | EAGCF translates each principle into control objective, owner, evidence artifact, and monitoring signal. NIST states the goal; EAGCF operationalizes it |
| GOVERN 1.3 | Risk tolerance levels determine level of risk management activities | Deliverable B (5-tier risk model); Section 4.3 (governance operating model) | ⚡ Stronger | EAGCF's 5-tier model (Prohibited → Low) explicitly wires risk tolerance to approval authority, evidence depth, monitoring intensity, and review cadence. NIST describes the principle; EAGCF makes it binding |
| GOVERN 1.4 | Risk management outcomes through transparent policies and controls | Deliverable G.1 (AI policy template); Deliverable D (lifecycle governance map) | ✅ Covered | |
| GOVERN 1.5 | Ongoing monitoring and periodic review; roles defined; frequency set | Deliverable E (18 runtime signals); Section 6.3 (review cadences by tier); KPI/KRI/KCI framework | ⚡ Stronger | EAGCF specifies 18 named runtime signals with thresholds, alerting, and escalation. NIST says "define frequency"; EAGCF defines weekly/monthly/quarterly cadences by tier |
| GOVERN 1.6 | Mechanisms to inventory AI systems, resourced per risk priorities | INT-01 (mandatory inventory registration); Deliverable G.9 (evidence pack index); AI system inventory spec | ✅ Covered | |
| GOVERN 1.7 | Safe decommissioning and phase-out procedures | Deliverable D Stage 10 (retirement gate); data retention confirmation; log archiving; inventory flagging | ✅ Covered | |

### GOVERN 2: Accountability Structures

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| GOVERN 2.1 | Roles, responsibilities, and communication lines documented and clear | Section 6.1 (8 governance bodies fully specified); Section 6.2 (RACI matrix); INT-05 (ownership declaration) | ⚡ Stronger | EAGCF provides a named RACI with 13 roles across 10 governance processes. NIST says "document roles"; EAGCF assigns Accountable, Responsible, Consulted, Informed per process |
| GOVERN 2.2 | Personnel receive AI risk management training | Section 8.8 (workforce enablement table — 8 audiences × delivery mechanism × cadence) | ✅ Covered | |
| GOVERN 2.3 | Executive leadership takes responsibility for AI risk decisions | Section 6.1 (Executive AI Council with named decision rights); Board/Risk Committee accountability | ✅ Covered | |

### GOVERN 3: Workforce Diversity, Equity, Inclusion

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| GOVERN 3.1 | Diverse teams inform AI risk decisions throughout lifecycle | ❌ Not present | ❌ Gap | **EAGCF does not require diverse/multidisciplinary team composition as a governance obligation. NIST explicitly flags this. Note: also surfaced in AIUC-1 crosswalk recon.** |
| GOVERN 3.2 | Policies define human-AI configurations and oversight structures | Section 4.2 (Principle 6 — Human Oversight); AGT-03 (HITL thresholds); Archetype definitions | ✅ Covered | |

### GOVERN 4: Culture of Risk

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| GOVERN 4.1 | Safety-first and critical thinking mindset policies | Section 8.7 (anti-patterns — governance theater); Part I Section 1.5 (design principles) | ⚠️ Partial | EAGCF addresses culture through anti-pattern identification and design principles but does not prescribe a formal "safety culture" policy or measurement |
| GOVERN 4.2 | Teams document and communicate risks and impacts broadly | Deliverable G.4 (system card — known limitations section); Deliverable G.12 (board reporting) | ✅ Covered | |
| GOVERN 4.3 | Practices to enable testing, incident identification, information sharing | Part XII (red-team pipeline); Section 7.2 (incident taxonomy); Section 7.3 (post-incident reporting) | ✅ Covered | |

### GOVERN 5: Engagement with AI Actors

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| GOVERN 5.1 | Collect and integrate feedback from external stakeholders on impacts | ❌ Not present | ❌ Gap | **EAGCF has no mechanism for soliciting or integrating external stakeholder / affected community feedback. This is a structural gap vs NIST's sociotechnical intent.** |
| GOVERN 5.2 | Mechanisms to incorporate adjudicated feedback into design | ⚠️ MON-08 (human override rate as a proxy for user feedback) | ⚠️ Partial | EAGCF captures user escalation as a monitoring signal (MON-13) but has no formal feedback integration loop for external affected communities |

### GOVERN 6: Third-Party and Supply Chain

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| GOVERN 6.1 | Policies addressing third-party risks including IP infringement | Domain 9 (VND-01–07); A004/A007 (IP protection); Deliverable G.13 (vendor due diligence template) | ⚡ Stronger | EAGCF provides 7 vendor controls, a vendor risk scoring model (Part XIV), performance SLAs by tier, and a 13-field vendor due diligence template |
| GOVERN 6.2 | Contingency processes for high-risk third-party failures | Part XIV Section 14.2 (multi-model fallback architecture); VND-06 (vendor incident notification) | ⚡ Stronger | EAGCF provides 4 explicit fallback options (active-active, warm standby, degraded-mode, human escalation) with RTO requirements |

---

## 2. MAP Function — Side by Side

### MAP 1: Context Establishment

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MAP 1.1 | Intended purposes, laws, norms, prospective settings documented | Deliverable G.2 (intake form — purpose, jurisdiction, user population, regulatory obligations) | ✅ Covered | |
| MAP 1.2 | Interdisciplinary teams with diverse expertise; participation documented | ❌ Not present | ❌ Gap | Mirrors GOVERN 3.1 gap — no explicit diverse team requirement in intake or design gate |
| MAP 1.3 | Organization's mission and AI goals documented | Deliverable G.1 (AI policy — strategic intent section) | ⚠️ Partial | EAGCF's policy template references strategic intent but does not require formal documentation of how each use case aligns with organizational AI mission |
| MAP 1.4 | Business value clearly defined or re-evaluated | INT-06 (business justification and success metrics at intake) | ✅ Covered | |
| MAP 1.5 | Organizational risk tolerances determined and documented | Deliverable B (risk appetite statement); Section 4.1 (governance objectives) | ✅ Covered | |
| MAP 1.6 | System requirements elicited; socio-technical implications addressed | Deliverable D Stage 2 (design gate — system requirements); Deliverable G.4 (system card) | ✅ Covered | |

### MAP 2: Categorization of AI System

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MAP 2.1 | Specific tasks and methods defined (classifier, generative, recommender) | INT-04 (archetype assignment); Deliverable G.3 (risk-tiering template) | ✅ Covered | |
| MAP 2.2 | Knowledge limits and human oversight mechanisms documented | Deliverable G.4 (system card — known limitations section); AGT-03 (HITL specification) | ✅ Covered | |
| MAP 2.3 | Scientific integrity and TEVV considerations documented | Deliverable D Stage 4 (validation gate evidence); Part XII (control validation framework) | ✅ Covered | |

### MAP 3: Capabilities, Goals, Costs and Benefits

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MAP 3.1 | Potential benefits documented | INT-06 (success metrics at intake) | ⚠️ Partial | EAGCF captures success metrics but no formal benefit documentation requirement separate from business justification |
| MAP 3.2 | Potential costs including non-monetary costs from errors | Part XIV Section 14.1 (governance cost model); Section 1.4 (why bad governance slows adoption) | ⚠️ Partial | EAGCF's cost model covers governance costs, not explicitly the operational cost of AI errors to affected parties |
| MAP 3.3 | Targeted scope specified and documented | Deliverable G.4 (system card — intended use, out-of-scope use); PRM-04 (scope enforcement) | ✅ Covered | |
| MAP 3.4 | Operator proficiency processes defined and documented | Section 8.8 (workforce enablement); Deliverable G.1 (acceptable use policy) | ⚠️ Partial | EAGCF addresses enablement but not formal proficiency certification per system |
| MAP 3.5 | Human oversight processes defined and documented | Section 4.2 Principle 6; AGT-03; EP-8 (HITL queue); Deliverable D gate requirements | ✅ Covered | |

### MAP 4: Risk and Benefit Mapping for All Components

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MAP 4.1 | Technology and legal risk mapping including third-party and IP | Section 4.5 (regulatory mapping); Domain 9 (vendor); Domain 11 (supply chain) | ✅ Covered | |
| MAP 4.2 | Internal risk controls for all components including third-party | Deliverable C (master control matrix — architecture applicability column); Section 5.3 (archetype control deltas) | ⚡ Stronger | EAGCF's control matrix includes an "Applicability by Architecture" column and 10-archetype control deltas — more granular than NIST's component-level framing |

### MAP 5: Impact Characterization

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MAP 5.1 | Likelihood and magnitude of impacts documented | Deliverable B (tier criteria include consequence magnitude); Deliverable G.3 (risk-tiering template) | ✅ Covered | |
| MAP 5.2 | Practices for stakeholder feedback integration in place | ❌ Not present | ❌ Gap | Mirrors GOVERN 5.1/5.2 — no formal affected community feedback loop |

---

## 3. MEASURE Function — Side by Side

### MEASURE 1: Methods and Metrics

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MEASURE 1.1 | Risk measurement approaches selected starting with most significant risks | Deliverable E (18 signals by tier/priority); KRI framework; Section 8.5 (misallocation diagnostic) | ⚡ Stronger | EAGCF assigns monitoring intensity by tier (continuous vs periodic vs spot-check) — a practical prioritization mechanism |
| MEASURE 1.2 | Metric appropriateness and control effectiveness regularly assessed | Part XII (control validation matrix with cadence); Section 12.5 (control degradation detection) | ⚡ Stronger | EAGCF specifies per-control test cadence, pass criteria, and degradation detection signals — not just "assess regularly" |
| MEASURE 1.3 | Independent assessors involved in assessments | Section 6.1 (Model Validation Function — independent from development); Internal Audit (third line) | ✅ Covered | |

### MEASURE 2: AI System Trustworthiness Evaluation

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MEASURE 2.1 | Test sets, metrics, and TEVV tools documented | Part XII Section 12.3 (control validation matrix — test method, pass criterion, cadence per control) | ✅ Covered | |
| MEASURE 2.2 | Human subject evaluations meet requirements; representative populations | ❌ Not present | ❌ Gap | **EAGCF has no explicit control requiring human subject evaluations to be representative or compliant with human subjects protection standards** |
| MEASURE 2.3 | Performance measured against criteria for deployment-similar conditions | MDL-03 (performance evaluation before deployment); Deliverable D Stage 4 | ✅ Covered | |
| MEASURE 2.4 | AI system functionality and behavior monitored in production | Deliverable E (18 signals); EP-9 (monitoring sidecar); MON-10–12 (drift + degradation) | ✅ Covered | |
| MEASURE 2.5 | System validity, reliability, and generalization limits demonstrated | MDL-03 (validation against thresholds); Deliverable G.5 (model card — evaluation section) | ✅ Covered | |
| MEASURE 2.6 | Safety risks evaluated; system shown to fail safely | Section 4.2 Principle 4 (safety controls); OUT-01 (safety classifier); Part VIII Overlay C (fail-safe design mandate) | ✅ Covered | |
| MEASURE 2.7 | Security and resilience evaluated and documented | Part XII red-team pipeline; Domain 8 (IAM); Domain 9 (vendor); Domain 15 (SOC-01/02) | ✅ Covered | |
| MEASURE 2.8 | Transparency and accountability risks examined | Section 4.2 Principle 2 (transparency → controls); E-controls mapping; Deliverable G.12 | ✅ Covered | |
| MEASURE 2.9 | AI model explained, validated, documented; outputs interpreted in context | Deliverable G.5 (model card — evaluation + limitations); Archetype 8 (explainability requirement) | ✅ Covered | |
| MEASURE 2.10 | Privacy risks examined and documented | DAT-02 (PIA); DAT-06 (output monitoring); Section 4.2 Principle 5 (Privacy → controls) | ✅ Covered | |
| MEASURE 2.11 | Fairness and bias evaluated and documented | Section 4.2 Principle 3 (Fairness → Fairness Assessment); MON-18 (fairness metric signal) | ✅ Covered | |
| MEASURE 2.12 | Environmental impact and sustainability assessed | ❌ Not present | ❌ Gap | **EAGCF has no environmental impact or sustainability assessment requirement. NIST MEASURE 2.12 is explicit on this.** |
| MEASURE 2.13 | Effectiveness of TEVV metrics and processes evaluated | Section 12.5 (control degradation detection); KCI framework | ✅ Covered | |

### MEASURE 3: Risk Tracking Over Time

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MEASURE 3.1 | Approaches to identify and track existing, unanticipated, emergent risks | Deliverable E (runtime signals); KRI framework; CHG-02 (risk re-evaluation at change) | ✅ Covered | |
| MEASURE 3.2 | Risk tracking for hard-to-measure or metric-lacking domains | Section 7.1 KRI framework — residual risk documentation; exception register | ⚠️ Partial | EAGCF acknowledges residual risk via exception register but has no specific provision for tracking risks without available metrics |
| MEASURE 3.3 | Feedback processes for end users to report problems and appeal outcomes | MON-13 (user escalation rate); OUT-06 (output rollback capability) | ⚠️ Partial | EAGCF captures user escalation as a monitoring signal but has no formal user appeal or output challenge mechanism |

### MEASURE 4: Measurement Feedback

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MEASURE 4.1 | Measurement approaches connected to deployment context via domain experts | Deliverable D (lifecycle map contextualizes monitoring by tier and archetype) | ✅ Covered | |
| MEASURE 4.2 | Measurement results validated through domain expert input | Model Validation Function (independent validation for Tier 1); Internal Audit | ⚠️ Partial | EAGCF's independent validation is limited to Tier 1 systems; NIST implies broader consultation |
| MEASURE 4.3 | Performance improvements/declines from field data and actor consultation | MON-10–12 (drift/degradation signals); CHG-05 (post-change monitoring); Section 8.2 (advanced model — continuous improvement) | ✅ Covered | |

---

## 4. MANAGE Function — Side by Side

### MANAGE 1: Risk Prioritization and Response

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MANAGE 1.1 | Go/no-go determination for development or deployment | Deliverable D (pre-deployment gate per tier — explicit approval/rejection decision) | ✅ Covered | |
| MANAGE 1.2 | Risk treatment prioritized by impact, likelihood, resources | Deliverable B (tier → treatment mapping); Part XIV Section 14.1 (control cost vs risk reduction matrix) | ⚡ Stronger | EAGCF provides a control cost vs risk reduction priority matrix — NIST states the principle without the prioritization mechanism |
| MANAGE 1.3 | Responses to high-priority risks developed and documented | Deliverable B Tier 1 required controls; Deliverable D Tier 1 gate evidence requirements | ✅ Covered | |
| MANAGE 1.4 | Residual risks to downstream users documented | Deliverable G.4 (system card — known limitations); Section 4.4 (exception/waiver model — compensating controls document residual risk) | ✅ Covered | |

### MANAGE 2: Strategies to Maximize Benefits, Minimize Harms

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MANAGE 2.1 | Resources for AI risk management considered; non-AI alternatives evaluated | Part XIV Section 14.1 (governance cost model); Section 8.1 (MVGM — resource-appropriate model) | ✅ Covered | |
| MANAGE 2.2 | Mechanisms to sustain value of deployed AI systems | Deliverable D Stage 7 (ongoing monitoring); MDL-05 (performance degradation monitoring); CHG-01–05 (change management) | ✅ Covered | |
| MANAGE 2.3 | Procedures for responding to previously unknown risks | Section 7.2 (incident taxonomy — S4 unknown anomaly); Section 7.3 (post-incident corrective action) | ✅ Covered | |
| MANAGE 2.4 | Mechanisms to disengage or deactivate underperforming systems | MDL-06/07 (retirement and rollback); AGT-09 (kill-switch for agentic systems) | ⚡ Stronger | EAGCF has an explicit kill-switch control (AGT-09) with mandatory testing for agentic systems — beyond NIST's general deactivation framing |

### MANAGE 3: Third-Party Risks and Benefits

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MANAGE 3.1 | Third-party resource risks regularly monitored; controls applied | VND-07 (annual vendor review); Domain 9 (VND-01–07); MON-17 (security misuse signal) | ✅ Covered | |
| MANAGE 3.2 | Pre-trained models monitored as part of regular maintenance | MDL-04/05 (drift + degradation monitoring); Part XIV (silent model update controls — behavioral fingerprinting) | ⚡ Stronger | EAGCF adds behavioral fingerprinting, version pinning, and contractual notification requirements for silent model updates — not in NIST |

### MANAGE 4: Communication, Response, Recovery

| NIST Subcategory | NIST Description | EAGCF Equivalent | Status | Notes |
|---|---|---|---|---|
| MANAGE 4.1 | Post-deployment monitoring plans implemented; appeal, override, decommission, incident response, change management | Deliverable D Stages 7–11; Deliverable E; Section 7.2/7.3 (incident taxonomy + corrective action) | ✅ Covered | |
| MANAGE 4.2 | Measurable improvement activities integrated into system updates | CHG-01–05 (change management); Section 8.2 (advanced governance model — continuous improvement) | ✅ Covered | |
| MANAGE 4.3 | Incidents and errors communicated to relevant actors; processes followed | Section 7.2 (severity model — escalation paths by S1–S4); Deliverable G.11 (incident report template) | ⚡ Stronger | EAGCF provides a 7-category incident taxonomy, 4-level severity model with SLAs, escalation paths, regulatory notification assessment, and a standardized incident report template |

---

## 5. Seven Trustworthiness Characteristics — Side by Side

| NIST Characteristic | NIST Definition | EAGCF Treatment | Status | Notes |
|---|---|---|---|---|
| **Valid and Reliable** | Outputs accurately reflect design objectives; consistent across conditions | MDL-03 (performance evaluation); MDL-05 (degradation monitoring); MON-12 (performance degradation signal); D001–D002 (hallucination controls) | ✅ Covered | |
| **Safe** | Operates within acceptable parameters; fails safely | Section 4.2 Principle 4; OUT-01 (safety classifier); Part VIII Overlay C (fail-safe mandate for safety-critical); AGT-09 (kill-switch) | ⚡ Stronger | EAGCF adds architecture-specific safety controls (agentic kill-switch, open-weight safety layer mandate) |
| **Secure and Resilient** | Withstands adversarial events; degrades safely | Domain 8 (IAM); Domain B controls; Part XII (red-team); Part XV (SOC-01/02, PRM-09 multi-modal injection) | ⚡ Stronger | EAGCF's 9-enforcement-point architecture, red-team pipeline, and control implementation specs go significantly beyond NIST's framing |
| **Accountable and Transparent** | Information available; accountability presupposes transparency | Section 4.2 Principle 1 (Accountability → controls); Principle 2 (Transparency → controls); RACI; Domain 14 (logging) | ⚡ Stronger | EAGCF translates each characteristic into owner + evidence + monitoring signal. NIST defines it; EAGCF operationalizes it |
| **Explainable and Interpretable** | Mechanisms (explainability) and meaning (interpretability) of AI outputs | Archetype 8 (Decision-Support explainability requirement); NIST.SP.1270 referenced | ⚠️ Partial | EAGCF scopes explainability to Decision-Support archetype only. NIST applies it more broadly across all AI systems |
| **Privacy-Enhanced** | Safeguards autonomy, identity, dignity; data minimization | Domain 2 (DAT-01–08); Section 4.2 Principle 5; PIA (DAT-02); DAT-06 (PII leakage); Domain 12 (cross-border) | ✅ Covered | |
| **Fair – Bias Managed** | Equality, equity; manages systemic, computational, human-cognitive bias | Section 4.2 Principle 3; MON-18 (fairness signal); Fairness Assessment gate (Tier 1); MSC-08 (training data quality) | ✅ Covered | |
| **Environmental Sustainability** (MEASURE 2.12) | Assessment of training and management environmental impact | ❌ Not present | ❌ Gap | No EAGCF equivalent |

---

## 6. Summary Scorecard

### By NIST Function

| Function | Total subcategories | ✅ Covered | ⚡ Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| **GOVERN** | 19 | 12 | 5 | 1 | 3 |
| **MAP** | 17 | 11 | 2 | 3 | 3 |
| **MEASURE** | 13 | 9 | 3 | 3 | 2 |
| **MANAGE** | 12 | 7 | 5 | 0 | 0 |
| **Trustworthiness** | 8 | 4 | 3 | 1 | 1 |
| **TOTAL** | **69** | **43 (62%)** | **18 (26%)** | **8 (12%)** | **9 (13%)** |

> EAGCF covers 88% of NIST AI RMF content (covered + stronger).
> EAGCF exceeds NIST on 26% of subcategories.
> Genuine gaps: 9 subcategories (13%).

---

## 7. Gaps Requiring EAGCF Additions

| Gap ID | NIST Reference | Gap Description | Priority | Recommended EAGCF Addition |
|---|---|---|---|---|
| **N-01** | GOVERN 3.1 / MAP 1.2 | **Diverse/multidisciplinary team requirement** — No obligation to involve diverse demographics, disciplines, or domain experts in risk decisions | High | Add governance principle: diverse team composition as an intake/design gate requirement for Tier 1 and Tier 2 use cases |
| **N-02** | GOVERN 5.1 / MAP 5.2 | **External stakeholder and affected community feedback** — No formal mechanism to collect, consider, or integrate feedback from those outside the development team | Medium | Add to Section 6.1 or intake process: structured external feedback pathway for Tier 1 use cases with external-facing impact |
| **N-03** | GOVERN 5.2 | **Adjudicated feedback loop** — No mechanism to incorporate resolved external feedback into system design and implementation | Medium | Combine with N-02: feedback register + resolution record as Tier 1 governance requirement |
| **N-04** | GOVERN 4.1 | **Safety culture measurement** — No formal policy or measurement for organizational AI safety culture (critical thinking, safety-first mindset) | Low | Add to Deliverable G.1 policy template: safety culture statement; to Section 8.8: culture measurement KPI |
| **N-05** | MEASURE 2.2 | **Human subject evaluation compliance** — No requirement that human participant evaluations meet applicable protections and be representative | High | Add to Deliverable D Stage 4 (validation gate): human subjects protection confirmation where evaluation involves human participants |
| **N-06** | MEASURE 2.12 | **Environmental impact and sustainability** — No assessment of AI model training or operational environmental footprint | Medium | Add ENV-01 (Environmental Impact Assessment) to Domain 2 or new Domain 17; add MON-21 (inference carbon/energy metric) to Deliverable E |
| **N-07** | MEASURE 3.2 | **Tracking risks without available metrics** — No provision for governing risks that cannot yet be measured | Low | Add to KRI framework: "unmeasurable risk register" — explicit documentation of known risks with no current metric, with review cadence |
| **N-08** | MEASURE 3.3 | **User appeal mechanism** — No formal process for end users to appeal or challenge AI system outputs | Medium | Add to Section 7 or Deliverable G.11: user appeal pathway (particularly for Tier 1 Decision-Support and Autonomous archetypes) |
| **N-09** | Explainability (characteristic) | **Explainability scoped too narrowly** — EAGCF requires explainability only for Decision-Support archetype; NIST applies it more broadly | Medium | Extend explainability obligation to all Tier 1 systems and all Chat-First/Agentic systems producing consequential outputs |

---

## 8. Where EAGCF Leads NIST (Summary of 18 "Stronger" Ratings)

| EAGCF Capability | NIST Gap |
|---|---|
| 5-tier risk model bound to lifecycle gate intensity | NIST defines risk tolerance; does not wire it to gate intensity |
| 18 named runtime monitoring signals with thresholds and escalation | NIST says "monitor"; does not name signals |
| 9-enforcement-point control implementation architecture | NIST does not specify where controls live in the stack |
| Prompt governance as versioned governed artifact (PRM-01–08) | NIST addresses prompt-related risks but not prompt as an artifact |
| RAG-specific control domain (7 controls) | NIST GenAI Profile partially addresses; 100-1 does not |
| Agentic kill-switch (AGT-09) with mandatory testing | NIST MANAGE 2.4 describes deactivation generally |
| Behavioral fingerprinting for silent model update detection | Not in NIST |
| Multi-model fallback architecture with 4 options and RTO | Not in NIST |
| 13-field vendor due diligence template with risk scoring | NIST GOVERN 6 describes the need; no template or scoring model |
| Vendor performance SLAs by tier | Not in NIST |
| Control validation matrix (unit tests per control with cadence) | NIST MEASURE describes assessment; no per-control test spec |
| Red-team pipeline architecture (attack library → generator → runner) | NIST MEASURE 2.7 describes adversarial testing; no pipeline spec |
| Control degradation detection signals | Not in NIST |
| Developer CI/CD governance integration (5 gates, 6 pre-commit hooks) | Not in NIST |
| Governance cost model with time-to-approval SLAs | Not in NIST |
| RACI matrix (13 roles × 10 processes) | NIST GOVERN 2 describes roles; no RACI |
| 10-archetype control deltas | NIST does not differentiate controls by system architecture |
| Governance misallocation diagnostic | Not in NIST |

---

## 9. NIST AI RMF Concepts Not Directly Addressed in EAGCF

These are conceptual dimensions from Part 1 of NIST AI 100-1 that inform the framework's philosophy but are not translated into EAGCF controls:

| NIST Concept | Where it appears | EAGCF position |
|---|---|---|
| AI-specific risks vs traditional software (Appendix B) | Foundational context | EAGCF implicitly addresses via archetype-specific controls but does not explain the distinction explicitly |
| Human-AI interaction principles (Appendix C) | Interaction design | Referenced via HITL and user escalation but not a standalone governance domain |
| AI lifecycle dimensions (Plan/Design → Data → Model → Task → Application) | Framework structure | Mapped to EAGCF's 11-stage lifecycle in Deliverable D |
| Bias typology — systemic, computational, human-cognitive | Trustworthiness | Partially in MSC-08 (training data quality) and MON-18; no explicit three-category bias management plan |
| Environmental and sustainability considerations | MEASURE 2.12 | Gap N-06 — not addressed |

---

*Comparison produced April 2026. NIST AI 100-1 publication date: January 2023.*
*EAGCF version: 1.2 | Coverage: 88% of NIST AI RMF subcategories (covered + stronger)*
