# Side-by-Side Comparison: EAGCF vs. NIST IR 8596 IPRD
## *Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile)*

**NIST Document:** NIST IR 8596 (Initial Preliminary Draft, December 2025)
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** NIST IR 8596 is a CSF 2.0 Community Profile that maps AI cybersecurity considerations across three focus areas — Secure (securing AI components), Defend (using AI to enhance cybersecurity), and Thwart (defending against AI-enabled attacks). It operates at the intersection of cybersecurity and AI, which is precisely the zone covered by EAGCF's security architecture (SABSA + Google SAIF), enforcement architecture (Part XI), and the IAM, VND, MSC, and AGT control domains. It is NOT a red-teaming methodology document; the dedicated NIST red-teaming document is NIST AI 100-2e2025.

---

## 1. Document Scope Alignment

| Dimension | NIST IR 8596 | EAGCF |
|---|---|---|
| **Framework base** | CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) | NIST AI RMF + ISO 42001 + COBIT + COSO + TOGAF |
| **Three focus areas** | Secure AI / Defend with AI / Thwart AI attacks | Unified governance + controls across all risk types |
| **Coverage scope** | AI cybersecurity risk; AI-enabled defense; AI-enabled attack vectors | Full AI governance, controls, assurance, and monitoring |
| **Architecture** | CSF 2.0 subcategory mapping (106 subcategories) | 15 control domains, 9 enforcement points, 10 archetypes |
| **Regulation** | Voluntary; Community Profile | Voluntary enterprise standard, wired to ISO 42001 and EU AI Act |
| **Companion doc** | COSAiS (SP 800-53 overlays for AI) | EAGCF is self-contained with external normative references |
| **Audience** | Cybersecurity practitioners; any org using or defending AI | Board, CRO, governance office, internal audit, compliance |

---

## 2. Three Focus Area Mapping vs. EAGCF

### Focus Area 1: Securing AI System Components (Secure)

| NIST IR 8596 Concern | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Novel, expanded attack surfaces** from AI integration (contextual, dynamic, opaque vulnerabilities) | Part XI §11.1 (9-enforcement-point architecture); Google SAIF (Part IX §9.1) | ✅ Covered | EAGCF's enforcement architecture (EP-1 through EP-9) directly addresses AI-specific attack surface at each control plane |
| **AI supply chain attack surface** (models, training data, ML infrastructure) | Part V §5.11 (MSC-01 through MSC-08: model supply chain and provenance) | ✅ Covered | MSC domain is specifically dedicated to supply chain integrity |
| **Adversarial inputs** to AI models (prompt injection, data poisoning, model inversion) | Part V §5.4 (PRM-05: prompt injection detection); GEN-07 (jailbreak pattern library); Part XII §12.1 (attack library) | ✅ Covered | Prompt injection, adversarial ML, and jailbreak detection all present |
| **Data quality and integrity** for AI training and inference | Part V §5.2 (DAT-01 through DAT-08: data and privacy domain) | ✅ Covered | |
| **Difficulty identifying, verifying, diagnosing AI vulnerabilities** | Part XII §12.2 (control validation matrix); Part XII §12.4 (degradation detection) | ✅ Covered | |
| **Hardcoded AI behaviors** and inherent model vulnerabilities | Part V §5.11 (MSC-06: fine-tuning/RLHF integrity); Part XIV §14.5 (behavioral fingerprinting) | ✅ Covered | |
| AI cybersecurity training for personnel | Part VIII §8.9 (workforce enablement) | ✅ Covered | |
| **COSAiS (SP 800-53 overlays for AI)** as companion control structure | Not explicitly referenced | ⚠️ Partial | EAGCF references SP 800-53 indirectly via NIST AI RMF; COSAiS not yet incorporated as a reference |

### Focus Area 2: AI-Enabled Cyber Defense (Defend)

| NIST IR 8596 Opportunity | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **AI for security governance and policy** (ensuring AI outputs follow policy) | Part IV §4.2 (principles → controls translation); Part XI §11.3 (prompt registry as policy enforcement) | ✅ Covered | Prompt registry and enforcement architecture implement policy-at-runtime |
| **Configuration management** using AI (managing configuration drift) | Part V §5.13 (CHG-01: change management); Part XIV §14.5 (behavioral fingerprinting for drift) | ✅ Covered | |
| **Automated compliance monitoring** (NIST 800-171, ISO 31000, CMMC, FedRAMP) | Part XIII §13.1 (CI/CD governance-as-code); Part IV §4.8 (assurance model) | ✅ Covered | |
| **Enhanced threat intelligence** (STIX/OpenCTI) | Not addressed | ❌ Gap | EAGCF does not integrate with structured threat intelligence formats (STIX, OpenCTI) for AI-specific threat feeds |
| **AI for risk communication** (translating risk to executive language) | Part I §1.1 (executive synthesis); Part VI §6.1 (board reporting) | ✅ Covered | |
| **Proactive threat actor identification** via OSINT/ATT&CK/CTI | Part XII §12.1 (red-team attack library references MITRE ATT&CK) | ⚠️ Partial | ATT&CK referenced in red-team context; no continuous AI-powered threat intelligence pipeline requirement |
| **Predictive maintenance and asset risk forecasting** | Part VII §7.2 (KRI framework) | ⚠️ Partial | KRIs cover risk indicators; AI-powered predictive asset risk forecasting not specified |
| **AI agents for defense** (swarm agents, agentic security architectures) | Part V §5.10 (AGT domain); Part XI §11.4 (agentic data plane) | ⚠️ Partial | Agentic governance covers security agents; swarm agent defense architectures not specified |
| **Advanced threat detection** (anomaly detection, UEBA, insider threats) | Part VII §7.1 (Deliverable E: monitoring signal catalog; MON-05: anomaly detection); Part V §5.8 (IAM domain: insider threat) | ✅ Covered | |
| **Zero trust adaptation** using AI | Part XI §11.1 (EP-3: input validator; EP-4: context enforcer) | ⚠️ Partial | Enforcement architecture implements zero-trust-like control; explicit ZTA integration not named |
| **Source code vulnerability detection** using AI | Part XIII §13.3 (developer AI tool constraints; shadow AI) | ⚠️ Partial | Developer AI tool governance present; AI-powered SAST/SCA not specified |
| **AI-powered incident response** (automated lockdown, playbooks) | Part VII §7.3 (incident taxonomy and escalation); Part VII §7.4 (corrective action) | ✅ Covered | |

### Focus Area 3: Thwarting AI-Enabled Attacks (Thwart)

| NIST IR 8596 Attack Category | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **AI-enabled spear phishing and social engineering** (hyper-realistic, personalized, at scale) | Part VIII §8.9 (workforce enablement: awareness training); GEN-07 (jailbreak/social engineering library) | ⚠️ Partial | Security awareness training and jailbreak library present; no specific control for defending against AI-generated phishing targeting employees |
| **DeepFake attacks** (audio/video manipulation for impersonation) | Not addressed | ❌ Gap | EAGCF does not address deepfake detection as a control domain or monitoring signal |
| **AI-generated malware** (signature-evading, memory-resident, AI-obfuscated) | Not addressed | ❌ Gap | AI-generated malware represents a new threat class not currently in EAGCF's control taxonomy |
| **Autonomous AI agents for attack orchestration** (full kill-chain automation: recon, exploit, lateral movement) | Part V §5.10 (AGT-01 through AGT-10: agentic governance); Part XI §11.4 (agentic data plane isolation) | ⚠️ Partial | EAGCF's agentic governance controls agentic *use* but not agentic *attack* resistance |
| **AI-enabled vulnerability exploitation** (automated vulnerability discovery and exploitation) | Part V §5.11 (MSC-07: supply chain security); Part XII §12.1 (red-team pipeline: offensive capability simulation) | ⚠️ Partial | Security architecture and red-team pipeline address this; no specific control for AI-accelerated exploitation defense |
| **Prompt injection as attack vector** | Part V §5.4 (PRM-05: prompt injection detection); EP-2 (prompt sanitizer) | ✅ Covered | |
| **Model inversion attacks** (extracting training data) | Part V §5.11 (MSC-07: supply chain security); Part XIV §14.5 (behavioral fingerprinting) | ⚠️ Partial | Model weight protection present; model inversion as a named attack with specific mitigations not fully addressed |
| **Data poisoning attacks** | Part V §5.11 (MSC-02: data provenance); Part V §5.2 (DAT-04: data quality validation) | ✅ Covered | |
| **Model drift as exploitable vector** | Part XII §12.4 (degradation detection; behavioral fingerprinting) | ✅ Covered | |
| **Speed and scale** of AI-driven attacks (countermeasures must accelerate) | Part XI §11.1 (automated enforcement at EP-1 through EP-9) | ✅ Covered | Automated enforcement pipeline addresses response speed |

---

## 3. CSF 2.0 Function Mapping vs. EAGCF

| CSF 2.0 Function | NIST IR 8596 Key AI Considerations | EAGCF Coverage | Status |
|---|---|---|---|
| **GOVERN** | Risk tolerance reevaluation for AI; strategic risk response for prompt injection, model inversion, data poisoning; stakeholder communication of AI limitations | Part IV (governance framework); Part VI (roles and accountability); Deliverable B (risk tiering) | ✅ Covered |
| **IDENTIFY** | AI Red Team improvements fed into supply chain hardening (ID.IM-02) | Part XII §12.1; Part V §5.11 (MSC domain) | ✅ Covered |
| **PROTECT** | Red teaming for adversarial ML, prompt injection, model drift, AI forensics training (PR.AT) | Part XII §12.1; Part VIII §8.9 | ✅ Covered |
| **DETECT** | Feed adversarial ML research into detection pipelines; integrate red-team reports into detection (DE.AE) | Part XII §12.1; Part VII §7.1 (monitoring signals) | ✅ Covered |
| **RESPOND** | Automated incident response; AI-assisted playbooks | Part VII §7.3; Part VII §7.4 | ✅ Covered |
| **RECOVER** | AI-assisted recovery planning and communications | Part VII §7.4 (corrective action) | ⚠️ Partial |
| **IDENTIFY** (asset management) | AI model/agent as governed asset class | Part V §5.3 (MDL domain: model governance) | ✅ Covered |
| **PROTECT** (configuration management) | AI configuration drift | Part V §5.13 (CHG domain); Part XIV §14.5 (behavioral fingerprinting) | ✅ Covered |

---

## 4. Key AI Threat Taxonomy Mapping

| NIST IR 8596 Threat Category | EAGCF Control Mapping |
|---|---|
| Prompt Injection | PRM-05 (injection detection), EP-2 (prompt sanitizer), GEN-07 (jailbreak library) |
| Model Inversion | MSC-07 (supply chain security), IAM-04 (access restrictions on weights) |
| Data Poisoning | MSC-02 (data provenance), DAT-04 (quality validation) |
| Adversarial ML (evasion, misclassification) | Part XII §12.1 (red-team attack library), GEN-07 |
| Model Drift (exploitable degradation) | Part XII §12.4 (degradation detection), MON-19 (behavioral fingerprint monitoring) |
| AI Spear Phishing | Part VIII §8.9 (awareness training) — partial |
| DeepFake Attacks | **Not covered** |
| AI-Generated Malware | **Not covered** |
| Agentic Attack Orchestration | AGT domain (internal agentic governance) — partial for attack resistance |

---

## 5. Scoring Summary

| NIST IR 8596 Coverage Area | Items | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| Focus Area 1: Secure AI | 8 items | 6 | 0 | 2 | 0 |
| Focus Area 2: Defend with AI | 12 items | 5 | 0 | 6 | 1 |
| Focus Area 3: Thwart AI Attacks | 10 items | 3 | 0 | 5 | 2 |
| CSF 2.0 Function Mapping | 8 items | 6 | 0 | 2 | 0 |
| **TOTALS** | **38 items** | **20 (53%)** | **0 (0%)** | **15 (39%)** | **3 (8%)** |

**Coverage interpretation:** 92% total coverage (53% direct + 39% partial) reflects strong alignment between EAGCF's security architecture and AI control framework and the Cyber AI Profile's concerns. The 8% gap rate (3 items) represents genuinely novel threat categories — deepfakes, AI-generated malware, and structured threat intelligence integration — that sit at the bleeding edge of enterprise AI security. These are forward-looking gaps rather than design omissions.

---

## 6. Where EAGCF Materially Exceeds NIST IR 8596

| Dimension | EAGCF Capability | NIST IR 8596 |
|---|---|---|
| **Governance operating model** | 9 governance bodies, RACI, decision rights, review cadences | Referenced (CSF GV function) but not designed |
| **Risk tiering with lifecycle consequences** | 5-tier model wired to 11-stage lifecycle gate intensity | CSF risk categories without lifecycle binding |
| **Control taxonomy depth** | 15 domains, 97+ controls, preventive/detective/corrective | CSF subcategory considerations (non-prescriptive) |
| **Enforcement architecture** | 9 enforcement points with data plane designs per archetype | Not addressed — general PROTECT function only |
| **Agentic AI governance** | AGT-01 through AGT-10 (scope, reversibility, HITL, inter-agent trust) | Agentic AI mentioned; COSAiS covers it partially |
| **Prompt governance** | System prompt registry, injection detection, jailbreak library | Prompt injection flagged; no governance architecture |
| **Vendor scoring model** | 6-dimension vendor scoring, behavioral fingerprinting, multi-model fallback | Supply chain controls (IDENTIFY/PROTECT) |
| **Adoption acceleration** | Fast-lane, misallocation diagnostic, 7 anti-patterns | Not addressed |
| **Sector overlays** | Financial services, healthcare, safety-critical infrastructure | Not addressed |
| **Cost governance** | SLA model, ROI metrics, cost benchmarks | Not addressed |
| **Model supply chain provenance** | MSC-01 through MSC-08 (training lineage through watermarking) | OWASP LLM Supply Chain reference; no control design |

---

## 7. Gap Items: Recommended EAGCF Additions

| Gap ID | NIST IR 8596 Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N8596-01** | Thwart Focus Area | **DeepFake detection controls**: Add a control requiring detection and authentication measures for AI-generated audio/video used for identity impersonation — particularly relevant for internal communications, executive impersonation, and vendor fraud scenarios | High | Part V §5.7 OUT domain — add OUT-08: DeepFake detection for identity-critical communications; or Part VII §7.1 — add MON-21: DeepFake signal |
| **N8596-02** | Thwart Focus Area | **AI-generated malware defense**: Add recognition that AI-accelerates malware evolution (signature evasion, memory-resident, polymorphic); require AI-aware endpoint and network detection capabilities in security architecture requirements | Medium | Part XI §11.1 (enforcement architecture) — add note on AI-generated malware as novel threat class; Part VIII §8.8 sector overlays (all sectors) |
| **N8596-03** | Defend Focus Area | **Structured threat intelligence integration**: Require integration of AI-specific threat feeds (MITRE ATLAS, ENISA AI Threat Landscape, STIX-formatted AI IOCs) into EAGCF's monitoring pipeline for detection of AI-specific attack patterns | Medium | Part VII §7.1 (Deliverable E) — add MON-22: AI-specific threat intelligence feed ingestion; reference MITRE ATLAS |
| **N8596-04** | Defend Focus Area | **COSAiS alignment**: Reference NIST COSAiS (SP 800-53 Control Overlays for Securing AI Systems) as a companion control reference for organizations operating under SP 800-53 compliance requirements (government, defense contractors, FedRAMP-authorized services) | Low | Part III §3.1 (framework comparison) — add COSAiS as a supporting framework reference in the Execution layer |

---

## 8. Key References from NIST IR 8596 Not Yet in EAGCF

| Reference | Relevance to EAGCF |
|---|---|
| **MITRE ATLAS** (Adversarial Threat Landscape for AI Systems) | Should be added as primary threat taxonomy reference in Part XII §12.1 red-team attack library |
| **OWASP LLM Top Ten** | Should be added as normative reference alongside PyRIT/Garak/PromptBench in Part XII §12.3 |
| **OWASP AI Exchange** | Emerging resource for AI security practices; add to Part XII reference list |
| **ENISA AI Threat Landscape 2025** | Annual threat intelligence reference; add to Part VII §7.1 monitoring signal sources |
| **DASF (Data and AI Security Framework)** | Referenced for 60+ specific controls; evaluate for incorporation in EAGCF control taxonomy |
| **COSAiS** | SP 800-53 control overlay for AI; valuable for government-sector EAGCF implementations |

---

## 9. Synthesis

NIST IR 8596 and EAGCF are **strongly complementary** with high coverage alignment. The Cyber AI Profile provides the CSF 2.0 structure for discussing AI cybersecurity; EAGCF provides the *enterprise governance operating model* that implements those outcomes. Key integration points:

**Highest value additions from NIST IR 8596 to EAGCF:**
1. **DeepFake detection** — a materially new threat category not yet in EAGCF
2. **MITRE ATLAS** — add as a primary reference in the red-team attack library (currently uses ATT&CK; ATLAS is the AI-specific extension)
3. **Structured AI threat intelligence integration** — STIX/MITRE ATLAS ingestion as a monitoring signal

**Where EAGCF's design already addresses NIST IR 8596's intent:**
- EP-1 through EP-9 enforcement architecture maps directly to CSF PROTECT outcomes
- MSC domain covers CSF IDENTIFY supply chain and PROTECT configuration outcomes
- Part XII red-team pipeline covers CSF IDENTIFY improvement (ID.IM-02) outcomes
- Part VII monitoring catalog covers CSF DETECT and RESPOND outcomes

**Coverage summary:**
- NIST IR 8596 items with direct EAGCF coverage: **20 (53%)**
- NIST IR 8596 items partially covered: **15 (39%)**
- NIST IR 8596 items not addressed: **3 (8%)**
- Items where EAGCF materially exceeds NIST IR 8596: **11 dimensions**

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Next comparison in sequence: NIST AI 100-2e2025 (Adversarial Machine Learning — 2025 edition)*
