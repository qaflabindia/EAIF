Below is a **Master Table of Contents (TOC)** that you can use as the spine of an **AI Quality + Governance Playbook**, covering **all 5 pillars**, with **app-first vs chat-first architectural nuances baked into every pillar**, plus a **complete template library** spanning **Big 4 + Google + AWS + Microsoft + IBM + NVIDIA**.

I’m going to be explicit and “no lazy goose”: **every pillar has (A) intent, (B) app-first controls, (C) chat-first controls, (D) required artifacts/evidence, (E) mandatory reviews/gates, (F) KPIs**.

---

# Master TOC — AI Quality & Governance Framework (5 Pillars)

## Front Matter

0.1 Purpose, Scope, Definitions
0.2 What “Quality” means for AI (multi-dimensional)
0.3 What “Governance” means (decision rights + controls + evidence)
0.4 Roles & Accountability (Model Owner, System Owner, Risk Owner, Data Owner, Security Owner, Product Owner)
0.5 Risk Tiering Standard (Prohibited / High / Medium / Low)
0.6 Architecture Typology: **App-First vs Chat-First vs Hybrid vs Agentic**
0.7 Evidence Philosophy: “If it isn’t evidenced, it didn’t happen.”
0.8 Control Philosophy: Preventive / Detective / Corrective controls

---

## Pillar 1 — Architecture (Build governance into the system)

### 1.1 Architecture Objectives & Non-negotiables

* 1.1.1 Boundaries (data, tools, actions)
* 1.1.2 Control points (gates, overrides, policy decisions)
* 1.1.3 Least privilege & segmentation
* 1.1.4 Traceability by design
* 1.1.5 Safe failure modes (fail-closed, degrade safely)
* 1.1.6 Change containment (versioning, rollback)

### 1.2 Reference Architectures (with governance insertion points)

* 1.2.1 **App-First (workflow-led)**: UI → Workflow Engine → AI Step → Validators → Human Gate → Action
* 1.2.2 **Chat-First (conversation-led)**: Chat UI/API → Policy Layer → Orchestrator → LLM/RAG/Tools → Response
* 1.2.3 **Hybrid**: Chat for discovery → App workflow for execution
* 1.2.4 **Agentic**: Planner/Orchestrator → Tool Router → Sandboxed Executors → Verification layer

### 1.3 Architectural Control Patterns (minimum catalog)

* 1.3.1 Policy Decision Point outside prompts (policy-as-code)
* 1.3.2 Tool firewall (allow-list + scoped permissions + confirmations)
* 1.3.3 RAG boundaries (source allow-list, tenant isolation, retrieval filters)
* 1.3.4 Prompt-injection isolation (treat retrieved text as untrusted)
* 1.3.5 Schema-first outputs + validators (critical for app-first & agentic)
* 1.3.6 Secrets isolation (model never sees keys)
* 1.3.7 Version pinning (model/prompt/policy/tools/data snapshots)
* 1.3.8 Kill switches (disable tools, disable retrieval, rollback model)
* 1.3.9 Audit logging architecture (immutable logs, lineage)
* 1.3.10 Data minimization + redaction pipeline for logs

### 1.4 Architecture Nuances by Build Type

* 1.4.1 **App-First**: bounded intent, deterministic rules, schema validation, action governance
* 1.4.2 **Chat-First**: open intent, output governance, refusal strategies, citation/grounding governance
* 1.4.3 “When to choose which” decision rubric

### 1.5 Architecture Evidence Pack (required artifacts)

* System diagram + data flow diagram
* Tool permission matrix
* Threat model + abuse case model
* Data classification + boundary map
* Versioning/rollback design note
* Logging & retention design note

---

## Pillar 2 — Practices (Lifecycle discipline: how teams work)

### 2.1 End-to-End Lifecycle (gated)

* 2.1.1 Use-case intake & registration (no shadow AI)
* 2.1.2 Risk tiering & stakeholder impact mapping
* 2.1.3 Data readiness & rights verification
* 2.1.4 Build discipline (secure SDLC for AI)
* 2.1.5 Pre-release evaluation gate (quality + safety + security + privacy)
* 2.1.6 Deployment readiness gate (rollback, monitoring readiness)
* 2.1.7 Post-release monitoring & drift ops
* 2.1.8 Retirement/decommission + evidence archival

### 2.2 Practice Cadences (operating rhythm)

* Weekly AI Risk Ops (signals, incidents, changes)
* Monthly AI Governance Council (approvals, exceptions, KPI reviews)
* Quarterly Assurance (sampling audit, tabletop incident drills)

### 2.3 App-First vs Chat-First Delivery Practices

* 2.3.1 **App-First**: schema contracts, validators, test harnesses, change control per workflow step
* 2.3.2 **Chat-First**: prompt/policy versioning, conversation test sets, grounding requirements, refusal tuning
* 2.3.3 Agentic practice add-ons: tool simulation tests, permission testing, “rogue action” scenarios

### 2.4 Practice Artifacts (required every build)

* Use-case record + owner assignment
* Risk tier decision record
* Data approval record
* Model/System Card draft
* Evaluation plan + test cases
* Release checklist + signoffs
* Monitoring plan draft
* Incident playbook reference

---

## Pillar 3 — Controls (enforceable mechanisms)

### 3.1 Control Taxonomy

* Preventive controls
* Detective controls
* Corrective controls
* Control ownership & evidence requirements

### 3.2 Control Domains (full catalog)

* 3.2.1 Identity & Access (RBAC/ABAC, SSO/MFA, environment separation)
* 3.2.2 Data controls (classification, minimization, encryption, retention, redaction)
* 3.2.3 Model/prompt/policy controls (registry, approvals, versioning, rollback)
* 3.2.4 Output controls (content filters, refusal patterns, truthfulness constraints, citations)
* 3.2.5 Action controls (tool allow-lists, scoped permissions, confirmations, sandboxing)
* 3.2.6 Supply-chain controls (vendor risk, SBOM, dependency scanning)
* 3.2.7 Compliance controls (disclosures, record-keeping)
* 3.2.8 Exception controls (risk acceptance with expiry, compensating controls)

### 3.3 App-First vs Chat-First Control Minimums

* 3.3.1 **App-First minimum**: schema validation, deterministic rule enforcement, human gates for irreversible actions
* 3.3.2 **Chat-First minimum**: policy layer outside prompt, RAG governance, refusal strategy, trace logs
* 3.3.3 Agentic minimum: tool firewall + execution sandbox + verification layer + kill switches

### 3.4 Control Effectiveness & Testing

* Control testing methods (unit/CI gates, red team, audit sampling)
* Control coverage mapping (risk → control → evidence)

### 3.5 Control Evidence Pack (audit-ready)

* Control matrix (control ID, owner, frequency, evidence artifact)
* Evaluation reports and change logs
* Access reviews, data lineage proofs
* Exception register

---

## Pillar 4 — Monitoring (runtime governance: drift, harm, misuse)

### 4.1 Monitoring Objectives

* Detect harm early
* Detect drift
* Detect misuse/abuse
* Maintain reconstructability
* Close the loop (alerts → action)

### 4.2 Monitoring Layers

* 4.2.1 Platform health (latency, uptime, errors, cost)
* 4.2.2 Model quality (task success, user satisfaction, regression-in-prod)
* 4.2.3 Safety/security/compliance (policy violations, PII leaks, injection success)

### 4.3 Signal Catalog (complete minimum set)

* Safety harm signals (severity-weighted)
* Privacy leakage signals (PII output rate, sensitive retrieval hits)
* Security misuse signals (prompt injection success, tool abuse, exfiltration patterns)
* Quality signals (task success, escalation rate, citation correctness)
* Drift signals (input distribution, retrieval corpus drift, behavior regression)
* Fairness drift signals (if applicable)
* Cost and capacity signals (token/cost runaway)

### 4.4 App-First vs Chat-First Monitoring Nuances

* 4.4.1 **App-First**: tool/action telemetry, schema validation failures, unauthorized action attempts
* 4.4.2 **Chat-First**: unsafe output sampling, refusal rate balance, citation/grounding audits
* 4.4.3 Agentic: action graph monitoring + tool call anomaly detection

### 4.5 Alerting & Runbooks

* Thresholds, severity, on-call ownership
* First containment action per signal
* Evidence retention requirements

### 4.6 Monitoring Evidence Pack

* Dashboards + weekly/monthly risk ops report
* Sampling/audit logs
* Alert history + actions taken

---

## Pillar 5 — Incidents, Transparency, and Assurance (response + proof)

> This pillar intentionally bundles “incident handling” + “explainability/transparency” + “assurance,” because in practice they converge into **accountability**.

### 5.1 Incident Taxonomy (AI-specific)

* Safety harm incident
* Privacy incident
* Security incident (prompt injection, tool compromise)
* Reliability incident (hallucination spike, regression failure)
* Fairness incident (disparity/complaints)
* Compliance/IP incident

### 5.2 Severity Model & SLAs

* Sev0 near-miss → Sev1 critical
* Time-to-detect and time-to-contain targets

### 5.3 Incident Lifecycle & Playbooks

* Detect → Triage → Contain → Investigate → Remediate → Communicate → Postmortem → Prevent recurrence
* Containment levers (rollback, disable tools, disable retrieval, tighten policies)

### 5.4 Transparency & Explainability Requirements (right-sized)

* 5.4.1 Level 0: disclosure (AI notice, limitations)
* 5.4.2 Level 1: rationale + uncertainty + safe-use guidance
* 5.4.3 Level 2: traceability (versions, sources, tool calls, policy decisions)
* 5.4.4 Level 3: decision accountability (reason codes, contestability, human review)

### 5.5 Assurance & Audit Readiness

* Evidence pack completeness checks
* Control effectiveness sampling
* Tabletop exercises & red team cycle
* Exception governance and risk acceptance records

### 5.6 Pillar 5 Evidence Pack

* Incident tickets + postmortems + corrective actions
* Transparency notes / disclosures
* Audit logs + trace extracts
* Assurance reports

---

# Architectural Appendix — App-First vs Chat-First Quick Index

A.1 App-First Governance Advantages (bounded intent, schema constraints, deterministic enforcement)
A.2 Chat-First Governance Challenges (open intent, output unpredictability, grounding + refusal required)
A.3 Hybrid Pattern (chat for discovery → app for execution)
A.4 Agentic Addendum (tool risk: “rogue actions”)

---

# Template Library — Complete Master Index (by Provider)

## T0 — Universal Templates (your internal “standard pack”)

These are the *canonical artifacts* you should standardize regardless of vendor:

* T0.1 AI Policy (principles, scope, roles, tiering, exceptions)
* T0.2 Use-Case Intake Form
* T0.3 AI Inventory / Register
* T0.4 Risk & Impact Assessment Worksheet
* T0.5 Threat Model & Abuse Case Worksheet
* T0.6 Data Card / Dataset Sheet
* T0.7 Model/System Card (incl. intended use, limits, evals)
* T0.8 Evaluation Plan + Evaluation Report (quality/safety/privacy/security)
* T0.9 Red Team Plan + Findings Report
* T0.10 Release Checklist + Signoffs
* T0.11 Monitoring Spec (signals/thresholds/runbooks)
* T0.12 Incident Playbook + Postmortem Template
* T0.13 Exception Register (risk acceptance, expiry, compensating controls)
* T0.14 Vendor/Supply-chain Assessment Questionnaire (model provider, tool plugins, data suppliers)

---

## T1 — Big 4 “Template Packs” (what they typically deliver + public anchors)

### T1.1 Deloitte (Trustworthy AI / Ethics of AI)

* Typical deliverables: governance operating model, risk tiering rubric, control mapping, roadmap, evidence pack structure. ([Deloitte][1])

### T1.2 PwC (AI Trust / Trust Governance)

* Typical deliverables: board AI policy outline, risk classification framework, governance structure and reporting pack. ([PwC][2])

### T1.3 EY (Responsible AI Principles + governance approach)

* Typical deliverables: principles-to-controls mapping, governance lifecycle, oversight + “agile governance” practices. ([EY][3])

### T1.4 KPMG (Trusted AI governance)

* Typical deliverables: AI inventory repository template, operating model, governance cadence, trusted AI pillars mapped to controls. ([KPMG Assets][4])

> Note: Big 4 editable templates are often engagement deliverables; the above are the publicly anchored baselines they build from.

---

## T2 — Google Template Stack

* T2.1 **SAIF (Secure AI Framework)** — security governance checklist + map for AI threats/controls. ([Safety Center][5])
* T2.2 **Model Cards** (template concept + examples) — standard model/system documentation artifact. ([Google Research][6])
* T2.3 **Data Cards** + Data Cards Playbook — dataset documentation artifact and playbook activities. ([arXiv][7])

---

## T3 — AWS Template Stack

* T3.1 **Well-Architected Responsible AI Lens** — architecture review checklist/questions.
* T3.2 **CAF for AI (Governance perspective)** — operating model/capabilities template.
* T3.3 **Responsible Use of AI Guide** — lifecycle governance guidance convertible into internal templates.
* T3.4 **Bedrock prompt injection guidance** — LLM app security checklist.
* T3.5 **Bedrock Guardrails (policy configuration template)** — guardrail policy as enforceable config.

*(If you want, I’ll also include the exact AWS artifact folder layout for “evidence packs.”)*

---

## T4 — Microsoft Template Stack

* T4.1 **Responsible AI Standard v2 (General Requirements)** — requirements/control baseline for all AI systems. ([Microsoft CDN][8])
* T4.2 **Responsible AI Impact Assessment Template** — structured impact worksheet template (public).
* T4.3 **Transparency Notes pattern** (Azure AI services) — disclosure template style you can mirror internally.
* T4.4 **AI Red Team guidance** — red team planning + execution scaffolding.
* T4.5 **Responsible AI Dashboard / Scorecard** — evaluation artifact outputs for ML quality/fairness/explainability.

---

## T5 — IBM Template Stack

* T5.1 **AI Factsheets** — governance documentation template + lifecycle lineage artifact.
* T5.2 **Factsheet sample assets** (starter examples) — practical adoption templates.
* T5.3 **OpenPages Model Risk Governance workflows** — inventory + workflow templates for governance.

---

## T6 — NVIDIA Template Stack

* T6.1 **NVIDIA Trust Center / Trustworthy AI** — governance posture + tooling pointers (including model card tooling). ([NVIDIA][9])
* T6.2 **Model Card Generator** — automated model card creation workflow/tooling. ([NVIDIA][9])
* T6.3 **NeMo Guardrails** — guardrail configuration patterns for safety, privacy, jailbreak prevention. ([NVIDIA Developer][10])
* T6.4 **NeMo Guardrails Evaluation Tooling & Methodology** — evaluation templates + metrics for guardrails as a release/monitoring gate. ([NVIDIA Docs][11])
* T6.5 **Trustworthy-AI GitHub repo** — reusable trustworthy AI tools/resources pack (CC0). ([GitHub][12])
* T6.6 **Frontier AI Risk Assessment (PDF)** — example of frontier model risk assessment structure you can adapt. ([NVIDIA Images][13])

---

# How to Use This TOC (the “assembly instructions”)

1. Pick architecture: **App-First / Chat-First / Hybrid / Agentic**
2. Set risk tiering rules (what becomes High-risk internally)
3. Adopt **T0 universal templates** as your standard evidence pack
4. Overlay vendor templates for acceleration (T1–T6)
5. Operationalize through Pillar 2 cadence + Pillar 4 alerts + Pillar 5 incident drills

---

## Next step (so we make it usable, not just “complete”)

Tell me which build you’re governing first:

* **App-first workflow**, **Chat-first assistant**, or **Agent with tools**?

And I’ll convert this TOC into a **fillable template pack** (tables + headings) aligned to that architecture, with:

* the exact artifacts required at each gate,
* owners,
* evidence retention rules,
* and a control matrix that maps every artifact to a pillar.

[1]: https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/services/ethics-of-ai-framework.html?utm_source=chatgpt.com "Trustworthy AI services"
[2]: https://www.pwc.in/assets/pdfs/ai-trust-governance-enabling-innovation-responsibility.pdf?utm_source=chatgpt.com "ai-trust-governance-enabling-innovation-responsibility. ..."
[3]: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/insights/ai/documents/ey-gl-responsible-ai-principles-09-2024.pdf?utm_source=chatgpt.com "Responsible AI principles"
[4]: https://assets.kpmg.com/content/dam/kpmgsites/au/pdf/2024/kpmg-trusted-ai-governance-2024.pdf.coredownload.inline.pdf?utm_source=chatgpt.com "Trusted AI governance - KPMG agentic corporate services"
[5]: https://safety.google/intl/en_in/safety/saif/?utm_source=chatgpt.com "Google's Secure AI Framework (SAIF)"
[6]: https://research.google/pubs/model-cards-for-model-reporting/?utm_source=chatgpt.com "Model Cards for Model Reporting"
[7]: https://arxiv.org/abs/2204.01075?utm_source=chatgpt.com "Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI"
[8]: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf?country=us&culture=en-us&utm_source=chatgpt.com "Microsoft Responsible AI Standard v2 General Requirements"
[9]: https://www.nvidia.com/en-us/ai-trust-center/trustworthy-ai/?utm_source=chatgpt.com "Trustworthy AI For A Better World"
[10]: https://developer.nvidia.com/nemo-guardrails?utm_source=chatgpt.com "NVIDIA NeMo Guardrails for Developers"
[11]: https://docs.nvidia.com/nemo/guardrails/latest/user-guides/eval/tooling.html?utm_source=chatgpt.com "Evaluation Tooling — NVIDIA NeMo Guardrails ..."
[12]: https://github.com/NVIDIA/Trustworthy-AI?utm_source=chatgpt.com "NVIDIA's repository for enabling trustworthy AI."
[13]: https://images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf?utm_source=chatgpt.com "FRONTIER AI RISK ASSESSMENT"
