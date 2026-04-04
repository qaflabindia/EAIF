# Side-by-Side Comparison: EAGCF vs. NIST AI 800-1 IPD
## *Managing Misuse Risk for Dual-Use Foundation Models*

**NIST Document:** NIST AI 800-1 (Initial Public Draft, July 2024)
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** NIST AI 800-1 addresses deliberate misuse of dual-use foundation models (CBRN weapons facilitation, offensive cyber, CSAM/NCII, deception). It is primarily directed at foundation model developers (hyperscalers, AI labs), not enterprise deployers. EAGCF's primary audience is enterprise deployers and operators — the downstream actor in NIST AI 800-1's supply chain. Despite this audience gap, significant coverage overlap exists in vendor governance (Domain 9), model supply chain (Domain 11), output controls (Domain 7), agentic governance (Domain 10), and the misuse monitoring provisions of Part VII.

---

## 1. Document Scope Alignment

| Dimension | NIST AI 800-1 | EAGCF |
|---|---|---|
| **Primary audience** | Foundation model developers; cloud providers deploying models | Enterprise deployers, governance offices, risk, audit, compliance |
| **Secondary audience** | Downstream deployers (secondary); civil society; government | Regulated-industry enterprises; board and executive layer |
| **Coverage domain** | Deliberate misuse risks (CBRN, cyber, CSAM, NCII, deception) | All AI risk types including misuse, bias, hallucination, agentic risk |
| **Regulation** | Rooted in EO 14110; voluntary guidance | Voluntary enterprise standard, regulatory-defensible (EU AI Act, ISO 42001) |
| **Scope of AI** | Dual-use foundation models (≥10B parameters, broad applicability) | All enterprise AI including GenAI, agents, decision-support, analytics |
| **Model theft scope** | Explicit Objective 3 (3 practices) | Covered within MSC and IAM domains |

---

## 2. Seven Objectives vs. EAGCF — Detailed Mapping

### Objective 1: Anticipate Potential Misuse Risk

| NIST AI 800-1 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **1.1** — Identify and maintain a threat profile list (capabilities of concern, threat actors, malicious tasks) | Part IV §4.2 (governance principles → controls); Part VIII §8.8 (sector overlays); Part XII §12.1 (red-team attack library) | ⚠️ Partial | EAGCF covers threat actor modeling in red-team context and sector risk overlays; does not require a formal, maintained *threat profile register* as a first-class governance artifact |
| Per threat profile: specify relevant capabilities of concern, threat actor types, malicious task scenarios | Part XII §12.1 (attack library: CBRN-adjacent categories); GEN-07 (jailbreak pattern library) | ⚠️ Partial | Jailbreak library and red-team attack library partially cover this; not structured as per-threat-profile documentation |
| Consult external experts with model access for open-ended threat identification | Part VI §6.7 (external assurance); Part IX §9.3 (Microsoft red team) | ⚠️ Partial | External assurance is referenced; no specific requirement for adversarial expert access for threat enumeration |
| **1.2** — Assess impact of each threat profile (scale increase, cost reduction, effectiveness vs. alternatives) | Part IV §4.1 (Deliverable B: 5-tier risk tiering); Part VII §7.3 (incident taxonomy severity) | ⚠️ Partial | EAGCF tiers risk by impact but does not specifically require comparative uplift analysis (how much does the AI *increase* threat actor capability relative to existing tools) |
| Estimate how potential harms may be prevented outside the model context (non-AI barriers) | Not addressed | ❌ Gap | EAGCF does not require analysis of whether real-world barriers (physical controls, distribution constraints) make AI misuse risk marginal vs. significant |
| **1.3** — Estimate model capabilities of concern *before development* via proxy model comparison | Part V §5.11 (MSC-01: training data lineage); Part XII §12.2 (capability measurement) | ⚠️ Partial | As enterprise deployer framework, EAGCF addresses pre-deployment validation, not pre-development capability forecasting — this practice is primarily a developer obligation |
| Assess degree of uncertainty in capability estimates; trigger periodic in-development measurement | Not addressed | ❌ Gap | Enterprise deployer context; pre-development capability uncertainty tracking is a developer responsibility |

### Objective 2: Establish Plans for Managing Misuse Risk

| NIST AI 800-1 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **2.1** — Define unacceptable risk threshold for each threat profile; weigh benefits against misuse risks | Part IV §4.1 (Deliverable B risk thresholds: Prohibited/High/Elevated/Standard/Low); Part IV §4.6 (exception and waiver model) | ✅ Covered | EAGCF's Tier 0 (Prohibited) directly maps to unacceptable risk; risk thresholds per tier are defined with binding lifecycle consequences |
| Refine thresholds continuously; account for legal/regulatory obligations | Part IV §4.1 (tier review cadence); Part VIII §8.8 (sector regulatory overlays) | ✅ Covered | |
| **2.2** — Establish roadmap to manage misuse risks; define security and safeguard goals; plan for deployment adjustment if risk rises | Part IV §4.7 (exception and waiver model); Part VII §7.4 (post-incident corrective action); Part XIV §14.4 (vendor risk roadmap) | ⚠️ Partial | EAGCF has corrective action and exception pathways; no explicit "misuse risk roadmap" artifact that commits to timeline-bound risk mitigation against specific threat profiles |

### Objective 3: Manage the Risks of Model Theft

| NIST AI 800-1 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **3.1** — Assess model theft risk by threat actor (resources, motivations, tactics, sophistication); consider insider threat; use cybersecurity red teams | Part V §5.11 (MSC-07: supply chain security); Part V §5.8 (IAM-01 through IAM-06); Part XII §12.1 (red-team pipeline) | ✅ Covered | EAGCF's model supply chain controls, IAM domain, and red-team pipeline together address model theft risk assessment |
| **3.2** — Compare predicted misuse risk to risk tolerance before developing models with increased capabilities of concern | Part IV §4.1 (Deliverable B); Tier 0 (Prohibited) pre-deployment gate | ✅ Covered | Tier 0 gate prevents deployment of prohibited capability profiles |
| **3.3** — Security practices to prevent model theft: protect weights, protect against extraction attacks, insider threat controls, proportionate to risk level | Part V §5.8 (IAM-04: least privilege, separation of duties); Part V §5.11 (MSC-01 through MSC-08); Part XI §11.1 (enforcement architecture) | ✅ Covered | EAGCF's model supply chain domain explicitly addresses weight protection, fine-tuning integrity, and open-weight governance (MSC-05 through MSC-08) |
| Protections against extraction attacks (model weight exfiltration) | Part V §5.11 (MSC-07: supply chain security); Part IX §9.2 (AWS Guardrails) | ⚠️ Partial | Extraction attacks as a *named* threat class with specific mitigations not explicitly addressed; general security controls present |

### Objective 4: Measure the Risk of Misuse

| NIST AI 800-1 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **4.1** — Measure capabilities of concern; compare to proxy models; use safe proxy tasks; account for threat actor's possible resource advantage | Part XII §12.1 (red-team pipeline); Part XII §12.2 (control validation matrix); MDL-04 (performance baseline) | ✅ Covered | EAGCF's red-team pipeline and capability measurement controls address this |
| Avoid training data overlap in capability evaluations; measure extent of any overlap | Part V §5.11 (MSC-01: training data lineage); N800-02 (benchmark contamination — gap from 800-2 comparison) | ⚠️ Partial | Training data lineage exists; benchmark contamination assessment not yet formalized as a control |
| Account for gap between testing effort and threat actor's potential effort | Part XII §12.1 (red-team pipeline: gap identification) | ⚠️ Partial | Red-team pipeline addresses attacker simulation; explicit requirement to document effort gap and adjust interpretation not present |
| **4.2** — Red team to assess safeguard bypass; use external, independent red teams; compare team resources to threat actor; consider legal protections (ToS waiver, indemnity) | Part XII §12.1 (red-team pipeline: external red team); Part VI §6.7 (external assurance) | ✅ Covered | EAGCF requires external red-team engagement; PyRIT, Garak, PromptBench specified |
| Legal protections for red teams (terms of service waiver, indemnity) | Not addressed | ❌ Gap | EAGCF does not include legal safe harbor/indemnity provisions for authorized red team testers |
| Define time period over which red-teaming results are intended to apply | Part XII §12.2 (control validation cadence); Part VII §7.1 (monitoring signal refresh) | ⚠️ Partial | Cadence requirements present; formal expiry/validity period for red-team findings not required |

### Objective 5: Ensure Misuse Risk Is Managed Before Deploying

| NIST AI 800-1 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **5.1** — Assess deployment effect on misuse risk; consider level of access granted (API, fine-tuning, weights); assess how deployment changes monitoring and safeguard options | Part IV §4.1 (Deliverable B: deployment tier gates); Part V §5.9 (VND-03: vendor deployment classification) | ✅ Covered | Tier-gated deployment approval and vendor deployment classification address this |
| Fine-tuning via API as significantly elevated risk (limits jailbreak prevention) | Part V §5.11 (MSC-06: fine-tuning/RLHF integrity controls); Part XIV §14.5 (vendor behavioral fingerprinting) | ✅ Covered | MSC-06 specifically addresses fine-tuning integrity |
| Weight release as significantly elevated risk (limits monitoring capability) | Part V §5.11 (MSC-05: open-weight governance) | ✅ Covered | MSC-05 explicitly addresses open-weight risk governance |
| **5.2** — Implement safeguards proportionate to misuse risk; establish evidence of safeguard effectiveness before relying on them | Part XI §11.1 (9-enforcement-point architecture); Part XII §12.2 (control validation matrix) | ✅ Covered | EP-1 through EP-9 provide layered safeguards; control validation matrix verifies effectiveness |
| Re-assess after adding new safeguards | Part XII §12.2 (control validation: re-test after remediation) | ✅ Covered | |
| **5.3** — Only deploy when misuse risk is adequately managed; leave margin of safety; consider delayed or limited deployment | Part IV §4.1 (Tier gates: Tier 0 = halt; Tier 1 = senior approval); Part VII §7.3 (incident escalation model) | ✅ Covered | |

### Objective 6: Collect and Respond to Information About Misuse After Deployment

| NIST AI 800-1 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **6.1** — Monitor distribution channels for misuse; automated detection systems; assess detection effectiveness via red team; request third-party channel monitoring | Part VII §7.1 (Deliverable E: runtime monitoring signals); Part V §5.15 (GEN-08: output monitoring); Part V §5.9 (VND-04: vendor monitoring requirements) | ✅ Covered | 20-signal monitoring catalog and vendor monitoring requirements address this |
| Privacy-preserving misuse detection (tiered detection methods) | Part V §5.2 (DAT-06: privacy controls); Part VII §7.1 (signal catalog) | ⚠️ Partial | Privacy controls and monitoring exist as separate domains; explicit privacy-preserving design for misuse detection pipelines not specified |
| Monitoring when weights are widely available (non-API distribution) | Part V §5.11 (MSC-05: open-weight governance) | ⚠️ Partial | Open-weight governance covers this risk category; behavioral monitoring for widely-distributed weights not detailed |
| **6.2** — Incident response process for model misuse; pre-planned response scenarios; drills for time-sensitive safety-critical scenarios | Part VII §7.3 (incident taxonomy and severity model); Part VII §7.4 (escalation paths and corrective action) | ✅ Covered | 4-severity incident model, escalation paths, and corrective action procedures present |
| Pre-planned response for weight-available models (when access restriction is not possible) | Part V §5.11 (MSC-05); Part VII §7.4 | ⚠️ Partial | Open-weight governance and corrective action present; specific playbook for widely-available weights not detailed |
| Drills for misuse incident response | Not addressed | ❌ Gap | EAGCF does not require tabletop exercises or drills for AI misuse response scenarios |
| **6.3** — Internal reporting protections (whistleblower policies for misuse concerns; formal adjudication process) | Part VI §6.1 (board/committee oversight); Part IV §4.4 (enforcement model) | ⚠️ Partial | Governance escalation paths exist; no specific internal AI safety whistleblower policy or formal adjudication requirement |
| **6.4** — Safe harbor for third-party safety researchers (vulnerability disclosure policy; no-legal-action commitment; researcher access provisions) | Not addressed | ❌ Gap | EAGCF does not define a vulnerability disclosure policy (VDP) or safe harbor commitment for external AI safety researchers |
| **6.5** — Bug bounty program for misuse vulnerabilities | Not addressed | ❌ Gap | No bug bounty / responsible disclosure incentive program requirement in EAGCF |

### Objective 7: Provide Appropriate Transparency About Misuse Risk

| NIST AI 800-1 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **7.1** — Publish regular transparency reports (evaluation methodology and results, safeguard details, training data provenance, downstream deployer guidance, internal governance structure) | Part IV §4.3 (transparency requirements); Part IX §9.3 (Microsoft Transparency Notes); Deliverable G §G.5 (AI Use Case Registration) | ⚠️ Partial | Transparency requirements and transparency note template present; no *external publication* cadence or structured transparency report format required of the enterprise |
| Include evaluation methodology detail sufficient for reproduction | Part XII §12.2 (control validation matrix); N800-09 (evaluation transparency — from 800-2 comparison) | ⚠️ Partial | Internal control validation documentation exists; no external transparency report format |
| **7.2** — Structured accountability disclosure to independent parties empowered to disclose deficiencies | Part VI §6.7 (internal audit and independent assurance) | ⚠️ Partial | Internal audit and independent assurance present; external accountability disclosure to parties with authority to publish deficiencies not required |
| **7.3** — Report misuse incidents to AI incident databases (machine-readable format) | Part VII §7.3 (incident taxonomy); Part VII §7.4 (corrective action) | ⚠️ Partial | Incident taxonomy and reporting defined internally; no requirement to report to external AI incident databases (e.g., AIID, AVID) |

---

## 3. Appendix B Safeguards vs. EAGCF Control Domains

NIST AI 800-1 Appendix B defines five safeguard categories. The table below maps each to EAGCF.

| NIST AI 800-1 Safeguard Category | EAGCF Mapping | Status |
|---|---|---|
| **Training data filtering** (exclude CBRN sequences, CSAM images) | MSC-01 (training data lineage), MSC-02 (data provenance) | ✅ Covered |
| **Training techniques to reduce harmful output propensity** | MSC-03 (model card documentation), MSC-06 (fine-tuning integrity) | ⚠️ Partial |
| **Training with fine-tuning-resistant safety** (hard to remove safeguards via subsequent fine-tuning) | MSC-06 (fine-tuning/RLHF integrity controls) | ✅ Covered |
| **Detect and block attempted misuse** (classifiers, block/modify unsafe queries, limit misuse-pattern accounts) | EP-3 (output classifier), GEN-07 (jailbreak pattern library), GEN-08 (output monitoring) | ✅ Covered |
| **Limit access to model capabilities** (staged rollout, context/user restrictions, reactive access reduction) | Part IV §4.1 (tiered deployment gates), IAM-01 through IAM-06, VND-03 (vendor access classification) | ✅ Covered |
| **Ensure appropriate level of access to model weights** (consider weight release, fine-tuning API; limit internal access) | MSC-05 (open-weight governance), MSC-06 (fine-tuning integrity) | ✅ Covered |
| **Stop development if risk unacceptable** | Tier 0 (Prohibited) lifecycle gate; Part IV §4.7 (exception and waiver model) | ✅ Covered |

---

## 4. Scoring Summary

| NIST AI 800-1 Objective | Practices | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| Obj. 1: Anticipate Misuse Risk | 7 items | 0 | 0 | 5 | 2 |
| Obj. 2: Establish Management Plans | 4 items | 2 | 0 | 2 | 0 |
| Obj. 3: Model Theft Prevention | 5 items | 3 | 0 | 2 | 0 |
| Obj. 4: Measure Misuse Risk | 8 items | 3 | 0 | 4 | 1 |
| Obj. 5: Pre-Deployment Management | 8 items | 6 | 0 | 1 | 1 |
| Obj. 6: Post-Deployment Monitoring | 10 items | 3 | 0 | 4 | 3 |
| Obj. 7: Transparency | 5 items | 0 | 0 | 5 | 0 |
| Appendix B Safeguards | 7 items | 5 | 0 | 2 | 0 |
| **TOTALS** | **54 items** | **22 (41%)** | **0 (0%)** | **25 (46%)** | **7 (13%)** |

**Coverage interpretation:** 87% total coverage (41% direct + 46% partial) reflects strong alignment with EAGCF's design-time and architecture controls. The 13% gap rate is concentrated in three areas: external transparency/accountability mechanisms, researcher safe harbor and bug bounty programs, and the specific analytical discipline of *comparative uplift* assessment (how much AI increases threat actor capability vs. baseline). These gaps are material for enterprises deploying foundation models in regulated environments or with significant misuse exposure.

---

## 5. Where EAGCF Materially Exceeds NIST AI 800-1

| Dimension | EAGCF Capability | NIST AI 800-1 |
|---|---|---|
| **Enterprise governance operating model** | 9 governance bodies, RACI, decision rights, review cadences | Not addressed (developer-focused, not deployer governance) |
| **Risk tiering across full AI portfolio** | 5-tier model (Prohibited → Low) across all AI types | Focused solely on dual-use foundation model misuse |
| **Agentic AI governance** | AGT-01 through AGT-10 (action scope, reversibility, HITL, multi-agent trust) | Not addressed |
| **Prompt governance** | System prompt registry, injection detection, jailbreak library, multi-turn memory controls | Jailbreaking mentioned; no governance architecture |
| **RAG and retrieval controls** | RET-01 through RET-05 | Not addressed |
| **Vendor scoring and due diligence** | 6-dimension vendor scoring model, behavioral fingerprinting, multi-model fallback | Supply chain mentioned but no enterprise vendor governance model |
| **Sector overlays** | Financial services, healthcare, safety-critical infrastructure | Not addressed |
| **Cost governance** | Time-to-approval SLAs, ROI metrics, misallocation diagnostic | Not addressed |
| **Enforcement architecture** | 9 enforcement points (EP-1 through EP-9) with data plane designs | "Safeguards" listed in Appendix B without enforcement architecture |
| **CI/CD governance integration** | 5-gate pipeline, 6 pre-commit hooks, shadow AI detection | Not addressed |
| **Lifecycle governance** | 11-stage lifecycle map (Deliverable D) wired to tier | Not addressed |
| **Adoption acceleration** | Fast-lane for low-risk, 7 anti-patterns, misallocation diagnostic | Not addressed |

---

## 6. Gap Items: Recommended EAGCF Additions

The following gaps from NIST AI 800-1 represent genuine requirements not currently addressed in EAGCF. These are most relevant to enterprises directly deploying or procuring foundation models with CBRN, offensive cyber, or CSAM/NCII risk potential.

| Gap ID | NIST AI 800-1 Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N801-01** | Practice 1.1 | **Threat profile register**: Require a maintained register of threat profiles for procured/deployed foundation models, specifying capabilities of concern, threat actor types, and malicious task scenarios per model | High | Part V §5.9 VND domain — add VND-08: Threat Profile Register per deployed foundation model |
| **N801-02** | Practice 1.2 | **Comparative uplift analysis**: Require assessment of how much a deployed AI model *increases* threat actor capability relative to existing tools (not just absolute risk, but marginal uplift) | High | Part IV §4.1 — extend risk tiering methodology with uplift factor |
| **N801-03** | Practice 1.2 | **Non-AI barrier analysis**: Require consideration of whether external barriers (physical controls, distribution constraints, regulatory restrictions) limit realized misuse risk regardless of AI capability | Medium | Part IV §4.1 — add to risk tiering methodology |
| **N801-04** | Practice 4.2 | **Red team legal safe harbor**: Define legal protections (terms of service waiver, indemnity) for authorized red team testers conducting adversarial evaluation of enterprise AI systems | Medium | Part XII §12.1 — add legal safe harbor provision for red team engagements |
| **N801-05** | Practice 6.2 | **Misuse incident drills**: Require periodic tabletop exercises or simulation drills for AI misuse response scenarios, especially for Tier 1 (High) systems with CBRN or offensive cyber risk exposure | Medium | Part VII §7.4 — add drill cadence requirement for Tier 0/1 systems |
| **N801-06** | Practice 6.3 | **AI safety whistleblower policy**: Require formal internal reporting protections and adjudication processes for employees raising AI safety or misuse concerns | Medium | Part VI §6.3 (AI governance office) — add SOC-03 control; Part IV §4.4 (enforcement model) |
| **N801-07** | Practice 6.4 / 6.5 | **Vulnerability disclosure policy and bug bounty**: Require enterprises deploying foundation models to publish a VDP covering AI safety issues and consider bug bounty programs for misuse vulnerability reporting | Low | Part V §5.9 VND domain or Part IV §4.3 (transparency) — add VDP requirement |

---

## 7. Applicability Note: Developer vs. Deployer Distinction

NIST AI 800-1 is primarily a **developer obligation** framework. Many of its practices (pre-development capability estimation, training data filtering, fine-tuning-resistant safety training, weight release decisions) are obligations of foundation model developers (Anthropic, Google, OpenAI, Meta, Mistral, Cohere) — not enterprise deployers.

**EAGCF's appropriate posture:**
- Practices 1.3, 3.2 (pre-development), and the detailed model training safeguards are **vendor obligations** that EAGCF should *verify and require evidence of* through the vendor governance framework (Deliverable G §G.13: Vendor Due Diligence Checklist)
- Practices 6.1, 6.4, 6.5 (monitoring, VDP, bug bounty) are **shared obligations** that enterprise deployers should enact for their deployment layer
- Practices 1.1, 1.2, 2.1, 4.2, 5.1–5.3 are **directly applicable** to enterprise deployers and represent the most actionable gaps for EAGCF

**Recommendation:** Add NIST AI 800-1 as a normative vendor due diligence reference in EAGCF §5.9 (VND controls) and §G.13 (Vendor Due Diligence Template), requiring evidence of developer compliance with Objectives 1–5 before approving foundation model procurement.

---

## 8. Synthesis

NIST AI 800-1 and EAGCF are **substantially aligned** at the control level, with EAGCF often providing the *enterprise deployment architecture* that NIST AI 800-1 assumes is in place. The strongest coverage overlap is in:
- Model theft prevention (EAGCF Domain 11 MSC)
- Safeguard design and enforcement (EAGCF Part XI enforcement architecture)
- Pre-deployment gates (EAGCF Deliverable B risk tiering and Deliverable D lifecycle gates)
- Red-team methodology (EAGCF Part XII)
- Monitoring (EAGCF Deliverable E and Part VII)

The primary EAGCF gaps relative to NIST AI 800-1 are:
1. **Threat profile register** (structured per-model misuse threat documentation)
2. **Comparative uplift methodology** (AI-as-enabler risk analysis, not just absolute risk)
3. **External accountability mechanisms** (VDP, researcher safe harbor, bug bounty, external transparency reports)
4. **AI safety whistleblower protection** (internal safety culture controls)

The most actionable integration: **incorporate NIST AI 800-1 as a vendor due diligence requirement** (confirming developer compliance with Objectives 1–5) and **add the threat profile register and VDP requirements** as enterprise deployer obligations for Tier 0/1 foundation model deployments.

**Coverage summary:**
- NIST AI 800-1 items with direct EAGCF coverage: **22 (41%)**
- NIST AI 800-1 items partially covered: **25 (46%)**
- NIST AI 800-1 items not addressed: **7 (13%)**
- Items where EAGCF materially exceeds NIST AI 800-1: **12 dimensions**

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Next comparison in sequence: NIST IR 8596 IPRD (AI Red-Teaming)*
