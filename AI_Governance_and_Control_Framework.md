# Enterprise AI Governance and Control Framework
### For Scaled Corporate Adoption

**Version:** 1.0
**Date:** April 2026
**Classification:** Internal Governance — Board, Risk, Audit, and Executive Distribution
**Status:** Active

---

> **Central Design Objective**
> Accelerate AI adoption across the enterprise without losing control, assurance, accountability, or regulatory defensibility.

---

## Table of Contents

- [Part I — Executive Synthesis](#part-i--executive-synthesis)
- [Part II — Scope and Conceptual Model](#part-ii--scope-and-conceptual-model)
- [Part III — Comparative Framework Analysis](#part-iii--comparative-framework-analysis)
- [Part IV — Enterprise AI Governance Framework](#part-iv--enterprise-ai-governance-framework)
- [Part V — Detailed Enterprise Control Framework](#part-v--detailed-enterprise-control-framework)
- [Part VI — Governance Forums, Roles, and Accountability](#part-vi--governance-forums-roles-and-accountability)
- [Part VII — Monitoring, Incidents, and Assurance](#part-vii--monitoring-incidents-and-assurance)
- [Part VIII — Adoption Acceleration Blueprint](#part-viii--adoption-acceleration-blueprint)
- [Part IX — Corporate Template Stacks and Enterprise Synthesis](#part-ix--corporate-template-stacks-and-enterprise-synthesis)
- [Part X — Final Synthesis](#part-x--final-synthesis)

---

# Part I — Executive Synthesis

## 1.1 Executive Summary

Enterprise AI adoption is accelerating. Most large organizations now operate dozens to hundreds of AI systems spanning employee productivity tools, customer-facing assistants, automated decision pipelines, and increasingly autonomous agentic workflows. The governance infrastructure supporting this estate has not kept pace.

This framework provides the operating architecture for governing enterprise AI at scale. It is not a policy statement or an ethics document. It is a control system: a structured set of accountability assignments, control designs, evidence requirements, monitoring mechanisms, and review processes that allow enterprises to adopt AI aggressively while remaining in control of risk, regulatorily defensible, and auditable.

The framework is built on a composite of the most operationally proven governance standards — NIST AI RMF as the control backbone, ISO/IEC 42001 as the management system shell, ISO/IEC 23894 for AI risk methodology, COBIT and COSO for enterprise control integration, TOGAF for architecture authority, CRISP-ML(Q) and MLOps maturity for lifecycle execution discipline — supplemented by critical artifacts from the major AI platform providers: Google, AWS, Microsoft, IBM, NVIDIA, OpenAI, and Anthropic.

It is designed to work in both centralized and federated enterprise operating models and to differentiate governance intensity by risk tier and AI system architecture. Low-risk systems move fast. High-risk systems receive proportionate scrutiny. Prohibited uses are stopped at intake.

The framework is organized into ten parts and eight mandatory deliverables. Each deliverable is a usable enterprise artifact, not a summary.

---

## 1.2 Core Thesis

**Fact:** Most enterprise AI governance programs fail not because the enterprise lacks principles, but because those principles are never translated into operational controls, evidence requirements, or monitoring signals.

**Fact:** Most AI governance frameworks in the market address one of four enterprise needs — strategy, governance, architecture, or execution — but not all four. Enterprises that rely on a single framework inevitably develop blind spots.

**Fact:** Governance intensity applied uniformly across all AI systems — regardless of risk, architecture, or audience — is the most common cause of governance-induced adoption slowdown. The consequence is not better control; it is governance theater layered over uncontrolled high-risk systems while low-risk productivity tools are tied up in unnecessary approval cycles.

**Inference:** The enterprise governance failure mode is not excessive governance overall — it is governance misallocated to the wrong systems, at the wrong lifecycle stages, with the wrong evidence requirements, and disconnected from runtime monitoring.

**Recommendation:** Build an AI governance operating system — not a one-time policy exercise. That system must be risk-tiered, architecture-aware, lifecycle-integrated, evidence-led, and continuously monitored. It must be fast for low-risk use cases and rigorous for high-risk ones. It must produce audit-ready evidence automatically, not on demand. And it must assign unambiguous accountability at every decision point.

---

## 1.3 Why Enterprises Fail at AI Governance

Six failure modes recur across enterprise AI governance programs:

**Failure Mode 1 — Principles without controls.**
The enterprise publishes a Responsible AI policy listing values such as transparency, fairness, and accountability. No control objective is defined. No owner is assigned. No evidence is required. No monitoring signal is specified. The policy exists. Control does not.

**Failure Mode 2 — Controls without monitoring.**
Control designs exist on paper. System prompts are defined, model versions are logged, human review gates are described. But no one is checking at runtime whether controls are functioning. Drift, prompt injection, output degradation, and policy violations accumulate undetected until an incident occurs.

**Failure Mode 3 — Governance theater.**
Approval committees meet. Risk assessments are submitted. Documentation grows. But the documentation is produced to satisfy the process, not to inform a decision. Assessors lack access to the actual system. Approvers lack AI literacy. The committee is a rubber stamp with delay attached.

**Failure Mode 4 — One-size-fits-all governance.**
A low-risk internal summarization tool and a customer-facing credit decisioning engine go through identical approval processes. The result: developers abandon governance to ship faster on low-risk tools, while the genuinely high-risk system receives the same superficial review.

**Failure Mode 5 — Model governance without system governance.**
The enterprise governs models — version numbers, training data, evaluation scores. But the system — the prompts, retrieval pipeline, tools, integrations, output handling, user access, and deployment environment — is ungoverned. The model is audited; the system is not. Risk lives in the system.

**Failure Mode 6 — Vendor dependency without vendor governance.**
The enterprise governs its own-built models but has no vendor due diligence process for third-party AI providers. Model behavior, data retention, output jurisdiction, fine-tuning practices, and security posture of external providers are unassessed.

---

## 1.4 Why Bad Governance Slows AI Adoption

**Fact:** Every unnecessary approval gate costs calendar time, developer attention, and organizational willingness to use governance channels at all. Developers route around friction. When governance is painful enough, they route around it entirely.

**Fact:** Uniform documentation requirements for all AI systems — regardless of risk — impose the full cost of high-risk governance on low-risk tools. A 40-page AI impact assessment for a spell-checker is not risk management; it is adoption tax.

**Fact:** Manual evidence collection delays deployment. Evidence that cannot be automated becomes a bottleneck in fast-moving delivery pipelines.

**Inference:** Bad governance does not reduce AI risk. It concentrates risk by pushing development outside governance channels while creating an illusion of control for leadership.

**Recommendation:** Governance must be designed as an adoption accelerator for low-risk systems and a genuine control mechanism for high-risk ones. The design test for every governance requirement is: does this control reduce real risk, or does it reduce the speed of adoption without improving safety or auditability?

---

## 1.5 Design Principles for Adoption-Accelerating Governance

The following principles govern the design of this framework. Each is paired with its operational implication.

| Principle | Operational implication |
|---|---|
| **Risk proportionality** | Governance intensity scales with risk tier. A Low-risk use case requires a lightweight intake form and automated monitoring. A High-risk use case requires documented validation, independent challenge, and enhanced runtime monitoring. Prohibited uses are stopped at intake regardless of business priority. |
| **Control before documentation** | Controls must be operational, not documented. If a control exists only in a policy document and is not enforced at runtime or at a lifecycle gate, it is not a control. |
| **Evidence by design** | Evidence for audit and regulatory purposes must be produced automatically as a byproduct of normal operations — logs, model cards, system cards, validation reports, monitoring dashboards — not assembled retrospectively on request. |
| **Accountability without ambiguity** | Every AI system must have a named Business Owner, Model Owner, and System Owner. Every control must have a named control owner. Shared accountability is unaccountability. |
| **Architecture-aware governance** | A RAG system has different risks from an agentic multi-agent orchestration. A decision-support system has different obligations from a chat assistant. Controls must be differentiated by architecture, not applied uniformly. |
| **Fast lane for low-risk** | Low-risk and pre-approved architecture patterns must have a streamlined intake and approval path. Speed is a governance design objective, not an enemy of governance. |
| **Monitoring as a control** | Runtime monitoring is not optional reporting. It is a primary detective control. Policy violations, drift, unsafe output, and misuse detected at runtime are governance events requiring documented response. |
| **Separation of governance layers** | Governance (who decides, who is accountable), controls (what prevents or detects bad outcomes), assurance (what evidences that controls work), and monitoring (what signals runtime behavior) are distinct disciplines. Conflating them produces frameworks that are simultaneously over-documented and under-controlled. |

---

*End of Part I.*

---

# Part II — Scope and Conceptual Model

## 2.1 Purpose and Scope

### Purpose

This framework establishes the governance structure, control system, assurance model, and monitoring architecture for enterprise AI. It defines what must be governed, who is accountable, what controls must exist, what evidence must be produced, and how the enterprise detects and responds to control failures.

It applies to all AI systems that are built, procured, operated, or materially influenced by the enterprise — regardless of whether those systems are hosted internally, operated via third-party API, embedded in vendor products, or developed by business units outside the central AI function.

### In Scope

- All AI systems in production or in a pre-production approval stage
- All AI models, including foundation models accessed via API, fine-tuned models, open-weight self-hosted models, and custom-trained models
- All AI-adjacent systems that materially determine AI behavior: retrieval pipelines, prompt management systems, tool/action integrations, orchestration layers, output post-processors
- All enterprise use cases involving generative AI, predictive AI, classification AI, recommendation AI, and agentic AI
- All vendors, platform providers, and third parties who supply AI models, infrastructure, or AI-enabled software to the enterprise

### Out of Scope

- Academic or sandbox research with no path to production
- Purely statistical analytics and rule-based systems with no learned model component
- AI features embedded in commercial off-the-shelf software where the enterprise has no configuration authority and no data input (passive consumption only)

---

## 2.2 Definitions

Precise definitions prevent the most common governance failure: conflating disciplines, which causes accountability gaps and assurance gaps simultaneously.

| Term | Definition |
|---|---|
| **AI system** | A machine-based system that infers outputs — predictions, decisions, content, recommendations, or actions — from inputs, using one or more AI models. |
| **AI model** | A trained computational artifact that takes inputs and produces outputs based on learned patterns. Includes foundation models, fine-tuned models, classifiers, rankers, and embedding models. |
| **Governance** | The set of structures, accountabilities, decision rights, and policies that determine who may approve what, who is accountable for outcomes, and what principles constrain AI use. Governance answers: *who decides and who is responsible?* |
| **Controls** | Specific mechanisms — preventive, detective, or corrective — that reduce the likelihood or impact of a risk materializing. Controls answer: *what stops, detects, or corrects bad outcomes?* |
| **Risk management** | The process of identifying, analyzing, evaluating, treating, and monitoring AI-related risks across the lifecycle. Risk management answers: *what could go wrong, how likely is it, and what is the treatment?* |
| **Assurance** | Evidence-based activities that provide confidence that controls are designed appropriately and operating effectively. Assurance answers: *how do we know the controls are working?* |
| **Compliance** | Adherence to applicable laws, regulations, standards, and internal policies. Compliance answers: *are we meeting external and internal obligations?* |
| **Model governance** | The subset of AI governance focused on the model artifact: training, versioning, evaluation, documentation (model cards), drift monitoring, and retirement. |
| **System governance** | The subset of AI governance focused on the AI system as a whole: the prompts, retrieval, tools, integrations, outputs, users, and deployment environment in which a model operates. |
| **Monitoring** | Continuous runtime observation of AI system behavior against defined thresholds and signals. Monitoring answers: *is the system behaving as expected right now?* |
| **Incident response** | The structured process for detecting, classifying, containing, remediating, and learning from AI control failures or adverse events. |
| **Business Owner** | The accountable business leader who sponsors an AI use case, owns the outcomes it produces, and is responsible for ensuring it operates within policy. |
| **Model Owner** | The technical owner responsible for the model artifact: training, evaluation, versioning, and retirement. |
| **System Owner** | The technical owner responsible for the full AI system: deployment, integration, prompt governance, retrieval, tool/action governance, and monitoring. |

---

## 2.3 Governance Boundary Model

Effective governance requires clarity on what is being governed (the object), what is being controlled (the mechanism), and what is being assured (the evidence).

### What Is Being Governed

| Governance object | Examples | Primary accountability |
|---|---|---|
| AI use cases | Credit scoring, customer service chatbot, internal copilot, fraud detection | Business Owner |
| AI models | Foundation model, fine-tuned classifier, embedding model | Model Owner |
| AI systems | Full stack: prompts + retrieval + model + tools + output handling | System Owner |
| AI prompts and instructions | System prompts, instruction sets, few-shot examples, retrieval queries | System Owner |
| AI data | Training data, retrieval corpora, user inputs, outputs stored for retraining | Data Owner |
| AI vendors and providers | Foundation model APIs, AI SaaS, AI-enabled platforms | Procurement / Vendor Risk |
| AI lifecycle changes | Model version updates, prompt changes, retrieval corpus changes, tool additions | Change Control / System Owner |
| AI users and roles | Who can access what AI capability at what permission level | Identity / Access Owner |

### What Is Being Controlled

Three control types apply across all governance objects:

- **Preventive controls** stop a risk from materializing (e.g., prohibited use blocklist at intake, system prompt access restriction, tool-use scope limits)
- **Detective controls** identify when a risk has materialized (e.g., prompt injection monitoring, output safety classification, audit log review, drift alerting)
- **Corrective controls** reduce the impact after a risk has materialized (e.g., output rollback, model version rollback, session termination, incident escalation)

### What Is Being Assured

Assurance covers three levels:

- **Design assurance:** the control design is appropriate for the risk (evidenced by risk assessment, control mapping)
- **Operating assurance:** the control is functioning as designed (evidenced by testing, monitoring, internal audit)
- **Outcome assurance:** the AI system is producing acceptable outcomes within defined tolerances (evidenced by performance monitoring, bias testing, user feedback analysis)

---

## 2.4 Enterprise AI System Archetypes

Governance requirements differ materially by AI system architecture. This framework defines ten archetypes. Every AI use case at intake must be classified into one or more archetypes; classification drives control delta selection in Part V.

### Archetype 1 — App-First

**Definition:** AI capability embedded in a structured enterprise application (ERP, CRM, ITSM) where the AI produces outputs consumed within a defined application workflow.

**Characteristic risks:** Output reliability in business-process context; data sovereignty of application data processed by external model; change management when application vendor updates the AI component.

**Distinguishing governance need:** Vendor AI governance and change management controls are primary. The enterprise governs what it sends to the model and how it uses the output, but rarely governs the model itself.

---

### Archetype 2 — Chat-First

**Definition:** A conversational interface (chatbot, assistant, copilot) where users interact in natural language. The AI generates free-form responses.

**Characteristic risks:** Output accuracy and hallucination; prompt injection via user input; content policy violation; inappropriate disclosure; session data handling; user over-reliance.

**Distinguishing governance need:** Output validation controls, content safety filters, session memory governance, user expectation management, and prompt injection detection are primary.

---

### Archetype 3 — Hybrid

**Definition:** A system combining structured AI (classification, recommendation) and generative AI (text generation, summarization) within a single user workflow.

**Characteristic risks:** Risk inheritance across components; output attribution ambiguity (which component produced which output); inconsistent governance applied to different components of the same system.

**Distinguishing governance need:** End-to-end system card covering all components; unified output monitoring; component-level control ownership mapped to system-level accountability.

---

### Archetype 4 — RAG (Retrieval-Augmented Generation)

**Definition:** A generative AI system that retrieves content from a corpus (vector database, document store, knowledge base) at inference time and uses it to ground model outputs.

**Characteristic risks:** Retrieval of stale, incorrect, or policy-violating content; retrieval corpus poisoning; attribution of retrieved content; hallucination at the interface between retrieved and generated content; data sovereignty of the retrieval corpus.

**Distinguishing governance need:** Retrieval corpus governance (access controls, freshness, content review), retrieval pipeline versioning, grounding validation, and citation controls are primary.

---

### Archetype 5 — Agentic Single-Agent

**Definition:** An AI system where a single AI model is given tools (web search, code execution, API calls, file system access, database queries) and autonomously sequences actions toward a goal.

**Characteristic risks:** Unauthorized tool use; irreversible action execution without human approval; scope creep beyond authorized action space; prompt injection through tool outputs (indirect injection); memory persistence beyond session boundary.

**Distinguishing governance need:** Tool-use scope controls, reversibility classification of tool outputs, HITL trigger thresholds for irreversible actions, session-scoped memory enforcement, and indirect prompt injection detection are primary.

---

### Archetype 6 — Agentic Multi-Agent Orchestrated

**Definition:** A system of multiple AI agents where an orchestrator agent delegates tasks to subagents, which may themselves use tools or delegate further.

**Characteristic risks:** Cascading tool misuse across the agent chain; credential or permission escalation through agent delegation; cross-agent trust boundary violation; action chain audit gaps; orchestrator manipulation via subagent outputs.

**Distinguishing governance need:** Inter-agent credential isolation, trust boundary enforcement between orchestrator and subagents, action chain audit logging, cross-agent scope inheritance controls, and cascading misuse prevention are primary. Each agent in the chain must be independently governed.

---

### Archetype 7 — Workflow Automation

**Definition:** AI embedded in automated business process workflows (RPA, integration pipelines, scheduled jobs) with minimal or no human interaction at execution time.

**Characteristic risks:** Silent failure with no human detection; automated propagation of erroneous AI outputs into downstream systems; absence of human-in-the-loop for consequential decisions; change management when AI component is updated in a live workflow.

**Distinguishing governance need:** Automated output validation gates, exception queuing for human review, workflow-level monitoring with automated alerting, and strict change management for AI component updates are primary.

---

### Archetype 8 — Decision-Support

**Definition:** An AI system that produces recommendations, scores, or assessments that a human uses to make a consequential decision (lending, hiring, medical triage, legal analysis).

**Characteristic risks:** Automation bias (human over-reliance on AI recommendation); fairness and disparate impact; inadequate explainability for the decision-maker; regulatory obligation to explain decisions to affected individuals.

**Distinguishing governance need:** Explainability requirements, bias testing at validation and post-deployment, human decision-maker training, documentation of how AI recommendations are used in the decision process, and regulatory disclosure controls are primary.

---

### Archetype 9 — Autonomous / Semi-Autonomous

**Definition:** An AI system that takes consequential actions — financial transactions, physical system commands, communications sent on behalf of individuals — with limited or no human approval per action.

**Characteristic risks:** High-consequence irreversible action without human oversight; cascading failure from erroneous autonomous decisions; accountability gap when no human approved the action; regulatory non-compliance in domains requiring human authorization.

**Distinguishing governance need:** Mandatory human-in-the-loop for defined action categories, action consequence classification (reversible vs irreversible), hard action scope limits, automated kill-switch capability, and post-action audit trail are primary. This archetype receives the highest governance intensity of any non-prohibited system.

---

### Archetype 10 — Open-Weight Self-Hosted

**Definition:** An AI system built on an open-weight foundation model (Llama, Mistral, Falcon, etc.) hosted on enterprise-controlled infrastructure, with no vendor SLA or hosted safety layer.

**Characteristic risks:** No vendor-provided safety filtering; enterprise bears full responsibility for output safety; model tamper-evidence (quantization, distillation, or fine-tuning may introduce vulnerabilities); no upstream model update channel; open-weight model training data lineage typically unprovable.

**Distinguishing governance need:** Enterprise-owned safety and content filtering layer (not delegated to vendor), model tamper-evidence controls, red-teaming and adversarial testing before deployment, explicit data lineage documentation of what is known and unknown, and enhanced monitoring are primary.

---

*End of Part II.*

---

# Part III — Comparative Framework Analysis

## 3.1 The 4-Layer Stack Logic

No single framework covers all four enterprise needs. Enterprises that rely on one framework develop predictable blind spots: strong on principles, weak on controls; strong on lifecycle, weak on board governance; strong on architecture, silent on assurance. This section establishes the comparative baseline and recommends the composite stack.

| Layer | What it answers | Best primary | Best supporting |
|---|---|---|---|
| **Strategy / Policy** | Why AI, where to play, risk appetite, principles | ISO/IEC 38507 (board mandate) | EU AI Act applicability, TOGAF |
| **Governance / Controls** | Who approves, who is accountable, what is evidenced | NIST AI RMF 1.0 + ISO/IEC 42001 | ISO 23894, COBIT, COSO ERM |
| **Architecture / Design** | How systems, data, models, and controls are structured | TOGAF | SABSA, Google SAIF |
| **Execution / Lifecycle** | How use cases are built, validated, deployed, monitored, retired | CRISP-ML(Q) + MLOps maturity | NIST AI RMF Playbook, GenAI Profile |

---

## 3.2 NIST AI RMF 1.0 — Deep Analysis

**What it is:** A voluntary, sector-agnostic risk management framework organized around four functions — **Govern, Map, Measure, Manage** — published by the US National Institute of Standards and Technology in January 2023. Supported by a Playbook of suggested actions and a Generative AI Profile (NIST AI 600-1).

**Practical enterprise value:**
The RMF is the single most actionable cross-industry AI governance reference available. Its four-function structure maps cleanly onto enterprise operating model design: Govern creates the accountability and policy layer; Map identifies what AI systems exist and what risks they carry; Measure defines how risk is assessed; Manage specifies treatment, response, and recovery actions. The Playbook converts these functions into specific suggested actions that can be directly translated into control objectives and evidence requirements.

**Governance utility — High.** Govern function addresses organizational roles, policies, culture, and accountability. Sufficient to anchor the governance operating model.

**Control utility — High.** Map, Measure, and Manage functions collectively cover risk identification, impact assessment, control selection, testing, monitoring, and incident response. The most control-complete of any voluntary framework.

**Assurance utility — Medium.** The RMF provides a structure for evidencing risk management activities but does not prescribe a management system or certification pathway. It must be paired with ISO/IEC 42001 for formal assurance.

**Adoption ease — High.** Voluntary, free, and widely understood in enterprise governance, risk, and compliance teams. No certification body required.

**Key strength:** Best cross-industry control taxonomy. Govern/Map/Measure/Manage is intuitive, MECE, and directly translatable into operational programs.

**Key blind spot:** Thin on architecture design authority. Does not address how AI systems should be designed from a platform, data, or security architecture perspective. No certification path, which limits its leverage in procurement and regulatory contexts where evidenced management systems are preferred.

**Enterprise use:** Use NIST AI RMF as the control structure backbone. Use its Govern function to design the governance operating model, Map function for use-case risk classification, Measure function for evaluation and testing requirements, and Manage function for treatment, monitoring, and incident response. Overlay the GenAI Profile for all generative AI and agentic use cases.

---

## 3.3 NIST AI RMF Generative AI Profile (NIST AI 600-1) — Deep Analysis

**What it is:** A companion profile to the AI RMF specifically addressing risks unique to generative AI systems, including large language models. Published in 2024.

**Practical enterprise value:**
The GenAI Profile identifies twelve generative-AI-specific risk categories not adequately covered by the base RMF: confabulation (hallucination), data privacy, data poisoning, harmful bias, homogenization, human-AI configuration failure, information integrity, information security, intellectual property, obscene/toxic/unsafe content, privacy, and value chain/component integration. For each risk, it maps suggested actions across the Govern/Map/Measure/Manage functions.

**Governance utility — Medium.** Primarily execution-focused. Does not redesign the governance operating model; it extends the control vocabulary for GenAI risks within the existing RMF structure.

**Control utility — High.** The most specific and actionable publicly available control reference for generative AI. The twelve risk categories and their associated actions translate directly into control objectives for chat-first, RAG, and agentic archetypes.

**Assurance utility — Medium.** Provides a testing and evaluation vocabulary but does not define a management system or evidence pack.

**Adoption ease — High.** Free, voluntary, directly extends the RMF, which most enterprises already reference.

**Key strength:** Best available publicly sourced GenAI-specific control reference. The confabulation, data poisoning, and information security categories are particularly actionable.

**Key blind spot:** Narrow scope — applies only to generative AI risks. Does not cover traditional ML, decision-support, or workflow automation archetypes. Requires the base RMF for full coverage.

**Enterprise use:** Apply the GenAI Profile as the control extension for all Chat-First, Hybrid, RAG, Agentic Single-Agent, and Agentic Multi-Agent Orchestrated archetypes. Map all twelve risk categories to control domains in Part V of this framework.

---

## 3.4 ISO/IEC 42001:2023 — Deep Analysis

**What it is:** The world's first certifiable AI management system standard, published by ISO/IEC in December 2023. Modeled on the ISO High Level Structure (the same architecture used by ISO 27001 and ISO 9001), making it integrable into existing enterprise management system programs.

**Practical enterprise value:**
ISO/IEC 42001 provides the management system shell that NIST AI RMF lacks: leadership commitment, policy, organizational roles and responsibilities, planning, support, operation, performance evaluation, and continual improvement — all designed to produce auditable evidence. Its certifiability creates procurement leverage (suppliers can demonstrate certification), regulatory leverage (regulators recognize management systems), and audit leverage (internal and external auditors have a structured evidence surface).

**Governance utility — High.** The standard requires documented AI policy, defined roles and responsibilities, risk assessment methodology, and management review — all core governance requirements. Clause 6 (Planning) maps to risk classification; Clause 9 (Performance evaluation) maps to monitoring and audit.

**Control utility — Medium.** ISO/IEC 42001 does not prescribe specific controls. It requires the organization to determine appropriate controls based on its risk assessment. Annex A provides a list of controls (similar to ISO 27001's Annex A) but they are high-level. NIST AI RMF or ISO/IEC 23894 must be used to fill control depth.

**Assurance utility — High.** Certification by an accredited body provides the strongest publicly recognizable assurance signal available in AI governance. The management system audit structure produces the evidence pack that regulators and boards need.

**Adoption ease — Medium.** Requires management system discipline, documented processes, internal audit, and management review. Organizations already operating ISO 27001 or ISO 9001 have significant reuse opportunity. Organizations without management system experience face higher implementation effort.

**Key strength:** Certifiability. No other AI governance framework produces a third-party-auditable certificate. This is increasingly a procurement requirement and a regulatory expectation.

**Key blind spot:** Does not prescribe specific controls. The management system shell must be filled with control content from NIST AI RMF, ISO/IEC 23894, or sector-specific standards. An ISO 42001 certificate without rigorous underlying control design provides assurance theater, not real assurance.

**Enterprise use:** Use ISO/IEC 42001 as the formal governance shell — the management system that wraps and evidences the control framework. Use it to structure leadership accountability, policy documentation, management review, internal audit, and continual improvement. Use NIST AI RMF to populate the control content within that shell.

---

## Deliverable A — Framework Comparative Matrix

| Dimension | NIST AI RMF 1.0 | NIST GenAI Profile | ISO/IEC 42001 |
|---|---|---|---|
| **Legal status** | Voluntary (US) | Voluntary (US) | International standard; certifiable |
| **Primary layer** | Governance + Execution | Execution (GenAI) | Governance |
| **Implementation style** | Function-based (Govern/Map/Measure/Manage) + Playbook actions | Risk-category-based action mapping | Management system (Plan-Do-Check-Act) |
| **Governance utility** | High — Govern function is strong | Medium — extends existing governance | High — leadership, policy, roles, review |
| **Control utility** | High — most control-complete voluntary framework | High — best GenAI-specific control vocabulary | Medium — controls are organization-defined |
| **Assurance utility** | Medium — no certification path | Medium — no certification path | High — certifiable; structured evidence surface |
| **Adoption ease** | High — free, widely known | High — free, RMF extension | Medium — management system discipline required |
| **Key strength** | Cross-industry control taxonomy; Playbook operationalizes it | 12 GenAI risk categories; directly actionable | Certifiability; integrates with ISO 27001/9001 |
| **Key limitation** | No certification; thin on architecture | GenAI-only scope | No prescribed controls; must fill with content |
| **Enterprise adoption value** | Backbone of control framework | GenAI and agentic control extension | Management system shell; audit and certification |
| **Best combined with** | ISO 42001 (shell), ISO 23894 (risk), COBIT (assurance) | NIST AI RMF (base), Part V control domains | NIST AI RMF (controls), COBIT (IT governance) |
| **Regulatory recognition** | High in US; referenced by SEC, FTC, sector regulators | Emerging; referenced for GenAI guidance | High globally; EU AI Act-compatible |
| **Cost / access** | Free | Free | Standard purchase + certification fees |

### Supporting Framework Summary

| Framework | Layer | Key enterprise contribution | Main limitation |
|---|---|---|---|
| ISO/IEC 23894 | Governance (risk) | Deep AI risk method integrated with ISO 31000 | Companion only; needs 42001 shell |
| ISO/IEC 38507 | Strategy (board) | Board-level AI governance obligations | High-level; no control detail |
| EU AI Act | Compliance overlay | Risk classification with legal obligations | Jurisdiction-bounded; compliance-framed |
| COBIT | Governance + Assurance | Bridges AI to IT governance, audit, assurance | Requires AI-specific mapping |
| COSO ERM | Governance (board/risk) | Board and internal control integration | Not AI-native |
| TOGAF | Architecture | Converts strategy to architecture and capability maps | Not a governance or control framework |
| SABSA | Architecture (security) | Business-driven, risk-traceable security architecture | High complexity; specialist skills |
| Google SAIF | Architecture (AI security) | AI-specific threat and control reference | Vendor-authored; no operating model |
| CRISP-ML(Q) | Execution | Lifecycle phase gates with QA tasks | No board or audit integration |
| Google MLOps maturity | Execution | Production ML pipeline discipline | Platform-biased; no governance model |
| SR 11-7 | Governance (banking) | Model validation gold standard in regulated finance | Banking-sector only; pre-GenAI |
| Microsoft RAI Standard | Governance + Execution | Best hyperscaler policy-to-implementation translation | Vendor-authored; not portable as-is |
| IBM watsonx.governance | Governance + Execution | Model inventory, lifecycle workflow, regulated-industry depth | Product-bundled; patterns must be extracted |
| NVIDIA NeMo Guardrails | Execution (agentic) | Best agentic/RAG guardrail and evaluation tooling | No governance operating model |

---

*End of Part III.*

---

# Part IV — Enterprise AI Governance Framework

## 4.1 Governance Objectives

The enterprise AI governance framework exists to achieve four outcomes:

1. **Accountability clarity** — every AI system has a named owner accountable for its behavior and outcomes. No AI system operates without an identifiable responsible party.
2. **Decision discipline** — decisions about what AI systems to build, deploy, and retire are made at the appropriate level of authority, with appropriate evidence, not by default or by inertia.
3. **Regulatory defensibility** — the enterprise can demonstrate, through documented evidence, that it identified AI risks, applied proportionate controls, monitored outcomes, and responded to failures. This demonstration must be available on demand to regulators, auditors, and boards.
4. **Adoption velocity** — governance mechanisms are designed to accelerate, not impede, AI adoption for low-risk and pre-approved use cases. High-risk use cases receive proportionate scrutiny. Prohibited uses are stopped early.

---

## 4.2 Principles Translated into Controls

Governance principles without operational translation are aspirational text. Each principle below is defined, assigned a control objective, given an owner, and mapped to an evidence requirement and monitoring signal.

### Principle 1 — Accountability

**Principle statement:** Every AI system has a named, accountable human owner.

**Control objective:** No AI system reaches production without a documented Business Owner, Model Owner, and System Owner, each of whom has accepted their accountability in writing.

**Preventive control:** Intake form requires ownership assignment before any design or build activity begins. Systems without complete ownership assignments are blocked from progressing through lifecycle gates.

**Evidence:** Signed ownership declaration in the system card; recorded in the AI system inventory.

**Monitoring signal:** AI system inventory audit — monthly sweep for systems without current named owners (owners who have left the organization or changed roles).

**Escalation:** Any production system without a valid named owner is escalated to the AI Governance Office within five business days for resolution or decommissioning.

---

### Principle 2 — Transparency

**Principle statement:** The enterprise knows what AI systems it operates, what they do, how they make decisions, and what risks they carry.

**Control objective:** All AI systems in scope are registered in the enterprise AI inventory. System cards document purpose, architecture, data inputs, model, decision logic, risk tier, controls in place, and owner. User-facing AI systems disclose AI involvement to users.

**Preventive control:** Inventory registration is a gate-zero requirement. No system proceeds to design without inventory entry.

**Evidence:** AI system inventory (maintained); system cards (version-controlled); user disclosure records.

**Monitoring signal:** Inventory completeness rate (percentage of known production systems with current system cards); user disclosure compliance rate.

**Escalation:** Inventory gaps detected by internal audit trigger mandatory remediation within 30 days.

---

### Principle 3 — Fairness and Non-Discrimination

**Principle statement:** AI systems do not produce outputs that constitute unlawful discrimination or cause unjustified disparate impact on protected groups.

**Control objective:** AI systems in the Decision-Support and Autonomous archetypes undergo mandatory fairness assessment at validation and at defined post-deployment intervals. Fairness metrics are defined at intake and documented in the system card.

**Preventive control:** Fairness assessment is a mandatory gate for High-risk and Elevated-risk tier systems before production deployment.

**Detective control:** Post-deployment fairness monitoring at defined cadence (monthly for High-risk; quarterly for Elevated-risk).

**Evidence:** Fairness assessment report; monitoring dashboard outputs; remediation records.

**Monitoring signal:** Disparate impact ratio by protected attribute; demographic parity gap; equalized odds gap (where applicable).

**Escalation:** Fairness metric breach triggers mandatory review by AI Risk Committee within ten business days. Deployment pause pending remediation is at the discretion of the AI Risk Committee.

---

### Principle 4 — Safety and Reliability

**Principle statement:** AI systems operate within defined performance boundaries and do not cause harm to users, third parties, or the organization.

**Control objective:** Safety thresholds and performance boundaries are defined at intake and encoded in the system card. Systems are monitored against these thresholds at runtime. Systems operating outside thresholds trigger automated alerts and defined response actions.

**Preventive control:** Safety testing (adversarial, red-team, edge-case) is a mandatory gate for High-risk and Elevated-risk tiers. Output safety classifiers are required for all Chat-First, RAG, and Agentic archetypes.

**Detective control:** Runtime output safety classification; safety threshold monitoring with automated alerting.

**Corrective control:** Automated output filtering; session termination; deployment pause protocol.

**Evidence:** Safety test reports; red-team records; output safety monitoring logs; incident records.

**Monitoring signal:** Unsafe output rate; safety classifier flag rate; user-reported harm rate; escalation rate from human reviewers.

**Escalation:** Unsafe output rate exceeding defined threshold triggers automated alert and mandatory review within 24 hours.

---

### Principle 5 — Privacy

**Principle statement:** AI systems process personal data only to the extent necessary for the defined purpose and in compliance with applicable data protection obligations.

**Control objective:** Personal data processed by AI systems is identified at intake, minimized, and governed under the enterprise data protection framework. AI-specific privacy risks (training data memorization, output disclosure, cross-context leakage) are assessed and controlled.

**Preventive control:** Privacy impact assessment is mandatory for systems processing personal data. Data minimization design review is a gate requirement.

**Detective control:** Output monitoring for personal data disclosure patterns; training data audit for memorization risk.

**Evidence:** Privacy impact assessment; data processing records; output monitoring logs.

**Monitoring signal:** Personal data disclosure detection rate in outputs; privacy incident rate.

**Escalation:** Any detected personal data disclosure in AI outputs is treated as a privacy incident with mandatory response per the enterprise privacy incident procedure.

---

### Principle 6 — Human Oversight

**Principle statement:** Consequential AI decisions and actions are subject to meaningful human oversight and, where required, human approval.

**Control objective:** Human oversight requirements are defined at intake based on risk tier and archetype. For High-risk and Autonomous archetypes, human-in-the-loop (HITL) requirements are designed into the system, not added retrospectively.

**Preventive control:** Mandatory HITL design review for High-risk and Autonomous archetypes before build begins.

**Detective control:** Human override rate monitoring (high override rates signal the AI system is underperforming or miscalibrated); HITL bypass detection.

**Evidence:** HITL design documentation; override rate monitoring reports; HITL audit records.

**Monitoring signal:** Human override rate; HITL bypass event count; time-in-queue for human review (long queues signal that HITL is becoming a bottleneck, which creates pressure to bypass it).

**Escalation:** HITL bypass detected → immediate investigation. Override rate materially above baseline → model performance review.

---

## Deliverable B — Enterprise AI Risk-Tiering Model

Risk tier is assigned at intake and is the primary determinant of governance intensity throughout the lifecycle. A use case classified High-risk at intake faces materially different gate requirements at every subsequent lifecycle stage than a Standard-risk use case. Tier assignment is not advisory; it is binding on the lifecycle governance model in Deliverable D.

---

### Tier 0 — Prohibited

**Definition:** AI uses that are categorically banned regardless of business justification, risk mitigations proposed, or approval level sought. No exception or waiver process applies.

**Examples:**
- AI systems that manipulate individuals through subliminal techniques to cause harm
- Biometric categorization based on protected characteristics for surveillance purposes
- Social scoring systems applied to individuals by public or private actors to determine access to services
- Real-time remote biometric identification in public spaces for law enforcement purposes (unless explicitly lawful in jurisdiction)
- AI used to generate child sexual abuse material
- AI systems designed to autonomously make lethal targeting decisions without meaningful human oversight
- AI-generated deepfakes of real individuals used for deception without disclosure

**Approval level:** None — intake is automatically rejected. Prohibited use classification is logged and reported to Legal, Compliance, and the AI Governance Office.

**Required controls at intake:** Hard block in intake system; automatic rejection notification; log to prohibited use register; Legal review notification.

**Evidence required:** Intake rejection record; prohibited use register entry.

**Monitoring intensity:** Post-deployment monitoring of the prohibited use register; periodic audit of rejected intakes to identify attempted circumvention.

**Review cadence:** Prohibited use list reviewed annually by Legal and the AI Governance Office; updated as regulation and enterprise policy evolve.

---

### Tier 1 — High Risk

**Definition:** AI systems that make or materially influence consequential decisions affecting individuals' legal status, economic outcomes, health, safety, or fundamental rights; OR AI systems operating autonomously with significant real-world action capability; OR AI systems in regulated domains with explicit supervisory AI obligations.

**Examples:**
- Credit, insurance, or employment decision-support or decisioning
- Criminal justice risk scoring or recidivism prediction
- Medical diagnosis, clinical decision support, or treatment recommendation
- AI systems taking autonomous financial transactions above defined thresholds
- AI in critical infrastructure control (energy, water, transportation)
- AI systems generating regulated communications (financial advice, medical guidance, legal advice)
- Autonomous or semi-autonomous agentic systems with access to consequential tools (payment APIs, system administration)

**Approval level:** AI Risk Committee + Legal/Compliance sign-off + Executive Sponsor. For regulated-sector systems: Compliance pre-approval before any build activity.

**Required controls:**
- Full system card and model card
- Mandatory Privacy Impact Assessment
- Mandatory Fairness Assessment (where applicable)
- Mandatory Security Risk Assessment
- Independent model validation (challenge function separate from the build team)
- Red-team testing before deployment
- HITL design review and enforcement
- Post-deployment monitoring with enhanced signal set
- Defined rollback and kill-switch capability

**Evidence required:** Full evidence pack (see Deliverable G template). Retention: minimum 7 years or as required by applicable regulation, whichever is longer.

**Monitoring intensity:** Continuous runtime monitoring; weekly KRI review; monthly risk committee reporting; annual independent assurance review.

**Review cadence:** Quarterly operational review; annual full governance review; mandatory re-classification review at every material change.

---

### Tier 2 — Elevated Risk

**Definition:** AI systems that significantly affect user experience, enterprise reputation, operational integrity, or regulatory posture but do not directly determine individual legal or economic outcomes; OR AI systems that interact externally with customers or regulators; OR AI systems processing significant volumes of personal data.

**Examples:**
- Customer-facing chat assistants and copilots
- Internal AI tools with access to confidential business data
- AI-generated content published externally (marketing, communications)
- RAG systems retrieving from sensitive document corpora
- AI-enabled fraud detection (where the AI flags, a human decides)
- Multi-agent systems for internal workflow automation with broad system access

**Approval level:** AI Governance Office sign-off + Business Owner + Security and Privacy review.

**Required controls:**
- System card and model card
- Privacy screening and data classification review
- Security assessment
- Output safety testing
- Prompt injection testing (for Chat-First and RAG archetypes)
- Post-deployment monitoring with standard signal set
- Rollback capability

**Evidence required:** Standard evidence pack. Retention: minimum 3 years.

**Monitoring intensity:** Continuous runtime monitoring; monthly KRI review; quarterly governance reporting.

**Review cadence:** Semi-annual operational review; annual governance review; mandatory review at material change.

---

### Tier 3 — Standard Risk

**Definition:** AI systems used internally, with limited external exposure, processing non-sensitive data, making recommendations that humans routinely review, and with limited consequence of error.

**Examples:**
- Internal productivity copilots (code assistance, document drafting, summarization) without access to sensitive data
- Internal FAQ or knowledge-base chatbots with restricted retrieval corpora
- Classification or tagging systems for internal content
- Predictive analytics for internal operational planning (non-HR, non-finance)
- AI-assisted data quality tools

**Approval level:** AI Governance Office intake review + Business Owner sign-off.

**Required controls:**
- System card (lightweight)
- Data classification review
- Output quality check before deployment
- Standard logging

**Evidence required:** Lightweight evidence pack. Retention: minimum 1 year.

**Monitoring intensity:** Standard runtime monitoring; quarterly KRI review.

**Review cadence:** Annual governance review; review at material change.

---

### Tier 4 — Low Risk

**Definition:** AI systems with minimal consequence of failure, no access to sensitive or personal data, fully human-reviewed outputs, and no external-facing exposure.

**Examples:**
- AI spell-check, grammar correction, and autocomplete in internal tools
- AI-powered search ranking for internal document libraries
- AI summarization tools with human-reviewed outputs and no data retention
- Vendor-provided AI features in standard SaaS tools (e.g., AI-suggested meeting times in calendar tools) where the enterprise has no configuration authority

**Approval level:** Business Owner self-certification with AI Governance Office notification.

**Required controls:**
- Basic intake registration
- Vendor AI data handling confirmation (for third-party tools)
- Standard logging

**Evidence required:** Intake registration record. Retention: 1 year.

**Monitoring intensity:** Periodic spot-check; annual review.

**Review cadence:** Annual review; escalation to Tier 3 or higher if scope expands.

---

### Risk Tier Summary Table

| Dimension | Tier 0 — Prohibited | Tier 1 — High Risk | Tier 2 — Elevated | Tier 3 — Standard | Tier 4 — Low |
|---|---|---|---|---|---|
| **Approval level** | Hard block | AI Risk Committee + Legal + Exec | AI Governance Office + Business Owner + Security/Privacy | AI Governance Office + Business Owner | Business Owner self-cert |
| **System card** | N/A | Full | Full | Lightweight | Registration only |
| **Model card** | N/A | Required | Required | Optional | Not required |
| **PIA** | N/A | Mandatory | Required if personal data | Screening only | Not required |
| **Fairness assessment** | N/A | Mandatory (decision systems) | Where applicable | Not required | Not required |
| **Red-team / adversarial testing** | N/A | Mandatory | Recommended | Not required | Not required |
| **Independent validation** | N/A | Required | Not required | Not required | Not required |
| **HITL design review** | N/A | Mandatory | Where applicable | Not required | Not required |
| **Runtime monitoring** | N/A | Continuous + enhanced signals | Continuous + standard signals | Periodic + standard signals | Periodic spot-check |
| **Monitoring cadence** | N/A | Weekly KRI review | Monthly KRI review | Quarterly review | Annual review |
| **Evidence retention** | Intake rejection log | 7 years minimum | 3 years minimum | 1 year minimum | 1 year minimum |
| **Governance review** | — | Quarterly + annual + at change | Semi-annual + annual + at change | Annual + at change | Annual |

---

## 4.3 Governance Operating Model

The enterprise may operate under a centralized, federated, or hybrid AI governance model. Each variant has distinct strengths and failure modes. The framework accommodates all three; the choice of operating model is an enterprise decision but must be explicit.

### Centralized Model

**Description:** A central AI Governance Office owns all AI governance processes: intake, risk classification, approval, monitoring, audit readiness, and policy maintenance.

**Strength:** Consistency; clear accountability; efficient evidence management.

**Failure mode:** Bottleneck at scale; insufficient domain knowledge for sector-specific risks; perception of governance as a gatekeeping function hostile to business velocity.

**Recommended for:** Enterprises with fewer than 50 active AI systems; enterprises in early AI program stages; highly regulated enterprises (financial services, healthcare) where centralized oversight is a supervisory expectation.

### Federated Model

**Description:** Business units own AI governance for their own use cases within a central policy and standards framework. The central AI Governance Office sets standards, provides tooling, and conducts periodic oversight.

**Strength:** Domain knowledge within business units; faster approval for domain-specific use cases; scales with AI program growth.

**Failure mode:** Inconsistent governance quality across units; policy drift; gaps in cross-unit risk visibility.

**Recommended for:** Enterprises with more than 100 active AI systems; enterprises with mature business-unit AI capabilities; diverse industry segments within the enterprise.

### Hybrid Model

**Description:** High-risk and Elevated-risk use cases are centrally governed. Standard-risk and Low-risk use cases are federated with central oversight and audit.

**Strength:** Concentrates governance resource on highest-risk systems; allows business-unit velocity on lower-risk use cases; maintains central visibility.

**Failure mode:** Risk tier misclassification (deliberately or inadvertently) to exploit the federated fast lane; inconsistent quality in federated governance.

**Recommended for:** Most large enterprises. This is the recommended default operating model for enterprises with mature AI programs and diverse use-case risk profiles.

---

## 4.4 Exception and Waiver Model

No governance framework survives contact with reality without an exception process. The absence of a formal exception process does not prevent exceptions — it forces them underground, where they are undocumented and unmonitored.

**Exception eligibility:** Exceptions may be requested for Tier 1 and Tier 2 control requirements only. Tier 0 prohibitions have no exception process.

**Exception request requirements:**
- Documented business justification
- Risk assessment for the specific control being waived
- Compensating controls proposed
- Time-bound scope (all exceptions are temporary; maximum 90 days without renewal)
- Named accountable executive sponsor

**Approval authority:**
- Tier 1 exception: AI Risk Committee Chair + Chief Risk Officer (or equivalent)
- Tier 2 exception: AI Governance Office Director + relevant Risk / Compliance leader

**Evidence requirements:** Exception register entry; signed approval; compensating control implementation record; expiry date and renewal reminder.

**Monitoring:** All active exceptions are reported in the quarterly AI Risk Committee pack. Exceptions not renewed before expiry are treated as control failures.

---

## 4.5 Regulatory Mapping Summary

This framework is designed to be regulator-defensible across the following primary regulatory contexts. The mapping is a delta to the base framework, not a replacement for it.

| Regulatory instrument | Applicability trigger | Primary obligations driving enterprise control delta |
|---|---|---|
| **EU AI Act** | Enterprise places AI systems on EU market; provides AI services to EU persons; uses AI in EU operations | Risk classification (prohibited / high-risk / GPAI); conformity assessment for Annex III high-risk systems; technical documentation; human oversight; accuracy, robustness, cybersecurity; AI literacy obligations; GPAI model obligations |
| **GDPR / Data Protection** | Personal data processed by AI systems | Lawful basis for AI processing; automated decision-making rights (Article 22); data minimization in training and inference; data subject rights in AI context; DPIA for high-risk processing |
| **UK AI Regulatory Framework** | UK operations or AI affecting UK persons | Cross-sectoral principles applied by sector regulators; DSIT guidance; sector-specific AI expectations |
| **US sector regulation** | Sector-specific (banking, healthcare, insurance) | SR 11-7 (model risk management, banking); OCR guidance (AI in healthcare); state-level AI laws (Colorado AI Act, Illinois AIAA) |
| **SEC AI guidance** | Public companies; investment advisers | Disclosure obligations; AI in investment decisions; conflicts of interest in AI-generated advice |

*Note on OECD AI Principles:* The OECD AI Principles (adopted by 47 governments) provide the primary international policy anchor for board-level cross-border AI policy alignment. Enterprises operating across multiple jurisdictions may reference them in board-level policy statements as a cross-border normative baseline. They do not substitute for any of the above regulatory instruments and do not appear in control design, assurance design, or monitoring specifications within this framework.¹

---

¹ *OECD AI Principles (2019, updated 2024): oecd.ai/en/ai-principles. 47-adherent intergovernmental standard; first internationally agreed upon AI policy reference.*

---

*End of Part IV.*

---

# Part V — Detailed Enterprise Control Framework

## 5.1 Control Philosophy

Controls are organized into three types across fifteen domains. Every control in this framework specifies: type (Preventive / Detective / Corrective), owner, evidence artifact, and monitoring signal. Architecture-specific control deltas appear in Section 5.3.

**Preventive (P):** Stops a risk from occurring. Applied at design, intake, and configuration stages.
**Detective (D):** Identifies that a risk has occurred or is occurring. Applied at runtime and in review cycles.
**Corrective (C):** Reduces impact after a risk has materialized. Applied as response actions.

---

## 5.2 Control Domains

### Domain 1 — Strategy and Use-Case Intake

**Control objective:** No AI system enters the design or build phase without a documented, risk-classified intake record that assigns ownership, defines purpose, classifies architecture archetype, assigns risk tier, and confirms business justification.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| INT-01 | Mandatory intake form submission before any design or build activity | P | AI Governance Office | Intake records in AI inventory | Intake completeness rate |
| INT-02 | Prohibited use check at intake (automatic block for Tier 0) | P | AI Governance Office | Rejected intake log | Prohibited use detection rate |
| INT-03 | Risk tier classification with rationale documented | P | AI Governance Office + Business Owner | Risk classification record | Tier reclassification rate at audit |
| INT-04 | Architecture archetype assignment | P | System Owner | System card — archetype field | Archetype accuracy at post-deployment review |
| INT-05 | Business Owner, Model Owner, System Owner named and accepted in writing | P | AI Governance Office | Signed ownership declaration | Ownership completeness in inventory |
| INT-06 | Business justification and success metrics documented | P | Business Owner | Intake form — justification section | — |
| INT-07 | Annual review of all active use cases for continued justification | D | AI Governance Office | Annual review records | Percentage of systems reviewed on schedule |

---

### Domain 2 — Data and Privacy

**Control objective:** Personal and sensitive data processed by AI systems is identified, minimized, protected, and governed in accordance with data protection obligations and enterprise data classification standards.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| DAT-01 | Data classification review at intake (what data enters the system, at what classification) | P | Data Owner + Privacy | Data classification record | Data classification completeness |
| DAT-02 | Privacy Impact Assessment for systems processing personal data | P | Privacy | PIA record | PIA completion rate for in-scope systems |
| DAT-03 | Data minimization design review (is all data collected necessary?) | P | System Owner + Privacy | Design review record | — |
| DAT-04 | Training data documentation (source, lineage, consent basis where applicable) | P | Model Owner | Data card / model card — data section | — |
| DAT-05 | Retrieval corpus data classification and access controls | P | System Owner + Data Owner | Corpus access control record | Unauthorized access attempts |
| DAT-06 | Output monitoring for personal data disclosure | D | System Owner | Output monitoring logs | Personal data disclosure detection rate |
| DAT-07 | Data retention and deletion controls for AI inputs, outputs, and logs | P | Data Owner | Retention schedule; deletion records | Retention compliance rate |
| DAT-08 | Cross-border data transfer assessment for systems where inference runs in a different jurisdiction from the data subject | P | Privacy + Legal | Transfer mechanism documentation | — |

---

### Domain 3 — Model Controls

**Control objective:** All AI models in production are versioned, documented, evaluated against defined performance thresholds, monitored for drift and degradation, and have a defined deprecation pathway.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| MDL-01 | Model card for every model in production | P | Model Owner | Model card (version-controlled) | Model card completeness rate |
| MDL-02 | Model versioning with immutable version identifiers | P | Model Owner | Model registry entries | — |
| MDL-03 | Performance evaluation against defined thresholds before deployment | P | Model Owner + Validation | Evaluation report | — |
| MDL-04 | Drift monitoring (input distribution drift, output distribution drift) | D | System Owner | Drift monitoring dashboard | Drift alert rate; time-to-detection |
| MDL-05 | Performance degradation monitoring against baseline at deployment | D | System Owner | Performance monitoring dashboard | Degradation alert rate |
| MDL-06 | Model retirement procedure (planned and emergency) | C | Model Owner | Retirement record | — |
| MDL-07 | Rollback capability to previous model version | C | System Owner | Rollback test record | Rollback success rate |
| MDL-08 | Model update change management (any model version change treated as a material change) | P | Change Management | Change record | Unauthorized model update detection |

---

### Domain 4 — Prompt and Instruction Governance

**Control objective:** System prompts, instruction sets, and user prompt scope limits are treated as governed artifacts — versioned, access-controlled, audited, and monitored — not as ad hoc configuration.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| PRM-01 | System prompt version control (system prompt treated as a code artifact: versioned, reviewed, approved before change) | P | System Owner | System prompt registry (version history, approval records) | Unauthorized system prompt change events |
| PRM-02 | System prompt access control (only authorized personnel may modify system prompts in production) | P | System Owner + Identity | Access control records | Unauthorized access attempts to prompt configuration |
| PRM-03 | System prompt audit trail (all changes logged with author, timestamp, change description, and approval reference) | D | System Owner | Audit log | — |
| PRM-04 | User prompt scope enforcement (system enforces boundaries on what users can request; out-of-scope requests are rejected or redirected, not silently degraded) | P | System Owner | Scope enforcement configuration; test records | Out-of-scope request rate; bypass detection |
| PRM-05 | Multi-turn session memory and context boundary controls (what persists across turns, what is session-scoped, what is not retained) | P | System Owner | Memory governance specification; session test records | Context boundary violation events |
| PRM-06 | Prompt injection detection as a dedicated detective control (separate from output safety monitoring) | D | Security + System Owner | Injection detection log; alert records | Prompt injection attempt rate; successful injection rate |
| PRM-07 | Jailbreak pattern library maintenance (known jailbreak patterns catalogued; detection rules updated at defined cadence) | D | Security | Jailbreak pattern library (version-controlled); update log | Jailbreak detection rate; new pattern identification lag |
| PRM-08 | Indirect prompt injection detection for agentic systems (tool outputs and retrieved content scanned for injected instructions before model ingestion) | D | Security + System Owner | Indirect injection monitoring log | Indirect injection attempt rate |

---

### Domain 5 — Retrieval Controls (RAG)

**Control objective:** For RAG systems, the retrieval corpus is governed, access-controlled, version-tracked, and tested for content accuracy, freshness, and policy compliance. Retrieval behavior is validated and monitored.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| RET-01 | Retrieval corpus registration and data classification | P | System Owner + Data Owner | Corpus registry | — |
| RET-02 | Corpus access controls (who may read/write/delete corpus content) | P | System Owner + Identity | Access control records | Unauthorized access attempts |
| RET-03 | Corpus freshness controls (stale content identification and refresh schedule) | P | System Owner | Freshness monitoring records | Stale content rate |
| RET-04 | Corpus content policy review (periodic review for content that violates enterprise policy or is factually discredited) | D | System Owner + Content Owner | Content review records | Policy-violating content detection rate |
| RET-05 | Retrieval pipeline versioning (changes to retrieval configuration treated as material changes) | P | System Owner | Pipeline version registry | — |
| RET-06 | Grounding validation (spot-check that model outputs are grounded in retrieved content, not hallucinated) | D | System Owner | Grounding validation test records | Hallucination rate; grounding score |
| RET-07 | Citation controls (where outputs reference retrieved content, citations are accurate and verifiable) | P | System Owner | Citation accuracy test records | Citation accuracy rate |

---

### Domain 6 — Tool and Action Controls

**Control objective:** Tools available to AI systems are explicitly authorized, scoped, and monitored. Tool-use scope limits prevent unauthorized actions. Irreversible actions require additional controls.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| TOL-01 | Tool authorization register (explicit list of tools the AI system is authorized to use; all tools not on the list are blocked) | P | System Owner | Tool authorization register | Unauthorized tool invocation attempts |
| TOL-02 | Least-privilege tool scope (tools authorized at minimum scope required; no broad system access where narrow access suffices) | P | System Owner | Tool configuration; design review record | — |
| TOL-03 | Reversibility classification of tool outputs (tools classified as producing reversible or irreversible actions; irreversible action tools receive enhanced controls) | P | System Owner | Tool reversibility classification document | — |
| TOL-04 | Mandatory HITL for irreversible actions above defined thresholds (e.g., financial transactions above threshold; external communications; system configuration changes) | P | System Owner + Business Owner | HITL configuration; test records | Irreversible action rate without HITL; HITL bypass events |
| TOL-05 | Tool-use audit log (all tool invocations logged with inputs, outputs, timestamp, session ID) | D | System Owner | Tool audit log | — |
| TOL-06 | Tool output validation before action execution (AI-generated tool call parameters validated before execution, not after) | P | System Owner | Validation configuration; test records | Validation failure rate |
| TOL-07 | Tool misuse detection (anomalous tool invocation patterns flagged for review) | D | Security + System Owner | Tool misuse detection log | Tool misuse alert rate |

---

### Domain 7 — Output Controls

**Control objective:** AI system outputs are validated for safety, accuracy, policy compliance, and appropriate disclosure before delivery to users or downstream systems.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| OUT-01 | Output safety classification (automated classifier on all outputs before delivery) | P | System Owner | Safety classifier configuration; test records | Unsafe output rate; classifier false negative rate |
| OUT-02 | Content policy filtering (outputs violating content policy blocked or flagged before delivery) | P | System Owner | Filter configuration; test records | Policy violation rate |
| OUT-03 | Hallucination and factuality monitoring (for systems where factual accuracy is a stated requirement) | D | System Owner | Factuality evaluation records; monitoring logs | Hallucination rate; factuality score |
| OUT-04 | AI disclosure in outputs (user-facing outputs disclose AI involvement where required by policy or regulation) | P | System Owner + Legal | Disclosure implementation record; compliance test | Disclosure compliance rate |
| OUT-05 | Output logging (all outputs logged for audit, monitoring, and incident investigation) | D | System Owner | Output log | Log completeness rate |
| OUT-06 | Output rollback capability (ability to suppress or retract outputs in the event of a control failure) | C | System Owner | Rollback capability test record | — |

---

### Domain 8 — Identity and Access

**Control objective:** Access to AI systems, AI configuration interfaces, AI data, and AI audit logs is governed by role-based access control with least-privilege enforcement and full auditability.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| IAM-01 | Role-based access control for AI system user access | P | Identity + System Owner | Access control matrix; provisioning records | Unauthorized access attempts |
| IAM-02 | Privileged access control for AI system configuration (system prompts, model configuration, tool authorization) | P | Identity + System Owner | Privileged access records | Privileged access anomalies |
| IAM-03 | Access review at defined cadence (quarterly for High-risk systems; annually for others) | D | Identity + System Owner | Access review records | Review completion rate; access anomalies identified |
| IAM-04 | Service account governance for AI-to-AI and AI-to-tool authentication (service accounts have minimum scope; no shared credentials) | P | Identity + System Owner | Service account registry | Shared credential detection |
| IAM-05 | Session management controls (session tokens scoped and time-limited; no persistent sessions with broad access) | P | System Owner | Session configuration; test records | Anomalous session events |

---

### Domain 9 — Vendor and Supply-Chain Controls

**Control objective:** Third-party AI models, platforms, and AI-enabled software are assessed, contracted, and monitored with governance requirements proportionate to the risk tier of the enterprise AI systems that depend on them.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| VND-01 | Vendor AI risk assessment before procurement (data handling, model behavior, security posture, audit rights, SLA) | P | Procurement + Security + Privacy | Vendor assessment record | Assessment completion rate before go-live |
| VND-02 | Contractual AI governance obligations (data use restrictions, output jurisdiction, model disclosure, audit rights, incident notification) | P | Legal + Procurement | Contract clauses; review record | — |
| VND-03 | Vendor model change notification requirement (vendor must notify enterprise of material model updates) | P | Procurement + System Owner | Contract clause; notification log | Model update notification lag |
| VND-04 | Open-source model governance (open-weight models assessed for license compliance, training data lineage, safety evaluation, and tamper-evidence before deployment) | P | System Owner + Security | Open-source model assessment record | — |
| VND-05 | Third-party AI audit rights (contracts include right to audit vendor AI governance and data handling practices) | P | Legal + Procurement | Contract clauses | — |
| VND-06 | Vendor AI incident reporting (vendor notifies enterprise of AI-related incidents affecting enterprise data or systems) | P | Procurement + Security | Contract clause; incident notification log | Vendor incident notification rate |
| VND-07 | Annual vendor AI governance review | D | Procurement + Risk | Annual review records | Review completion rate |

---

### Domain 10 — Agentic Action Governance

**Control objective:** AI agents operating with tool access and autonomous action capability are bounded by explicit action scope limits, reversibility controls, inter-agent trust rules, memory governance, and human-in-the-loop thresholds that are designed into the system, not applied retrospectively.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| AGT-01 | Action authorization scope definition (explicit, documented list of what the agent is authorized to do; all actions not authorized are blocked by default) | P | System Owner | Action authorization specification | Unauthorized action attempts |
| AGT-02 | Reversibility classification (all agent actions classified as reversible or irreversible before deployment; irreversible action classes documented) | P | System Owner | Reversibility classification document | Irreversible action rate |
| AGT-03 | HITL trigger thresholds for autonomous execution (defined thresholds above which HITL is mandatory — by action type, value threshold, or consequence class) | P | System Owner + Business Owner | HITL threshold specification; enforcement test | HITL bypass events |
| AGT-04 | Session-scoped memory enforcement (agent memory persists only within defined session scope; cross-session retention requires explicit design approval and governance) | P | System Owner | Memory governance specification; test records | Cross-session data leakage events |
| AGT-05 | Agent memory governance (what the agent remembers, for how long, who can access agent memory, and how memory is cleared) | P | System Owner + Privacy | Memory governance specification | — |
| AGT-06 | Inter-agent trust isolation (subagents do not inherit orchestrator credentials; each agent operates at minimum necessary permission; agent-to-agent trust explicitly declared) | P | System Owner + Identity | Trust boundary specification; architecture diagram | Credential escalation events |
| AGT-07 | Action chain audit log (complete audit trail of every action in an agentic chain: agent, tool called, inputs, outputs, timestamp, human review events) | D | System Owner | Action chain audit log | Log completeness; orphaned action events |
| AGT-08 | Cross-agent scope inheritance controls (orchestrator cannot delegate broader permissions than it holds; subagents cannot exceed orchestrator-granted scope) | P | System Owner | Scope inheritance design review | Scope escalation events |
| AGT-09 | Kill-switch capability (ability to halt agent execution immediately, with defined trigger conditions and authorization level) | C | System Owner + AI Governance Office | Kill-switch test record; trigger condition specification | — |

---

### Domain 11 — Model Supply Chain and Provenance

**Control objective:** The provenance of all AI models — including base model training data lineage, fine-tuning practices, and open-weight model integrity — is documented to the extent knowable, with residual unknowns explicitly acknowledged.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| MSC-01 | Base model training data lineage documentation (what is known about training data; what is unknown; source of knowledge) | P | Model Owner | Model card — training data section | — |
| MSC-02 | Fine-tuning and RLHF integrity controls (where third-party fine-tuning services are used, data governance obligations apply to fine-tuning data) | P | Model Owner + Privacy | Fine-tuning data governance record | — |
| MSC-03 | Open-weight model tamper-evidence (checksums or cryptographic signatures for open-weight models; verification at each deployment) | P | System Owner + Security | Tamper-evidence verification log | Checksum mismatch events |
| MSC-04 | Quantized and distilled model integrity (quantization and distillation processes documented; integrity verified before production use) | P | Model Owner | Quantization/distillation record | — |
| MSC-05 | Model watermarking (where enterprise produces or fine-tunes models, watermarking applied where feasible to support provenance tracing) | P | Model Owner | Watermarking implementation record | — |
| MSC-06 | Model provenance register (all models in production registered with provenance information: source, version, training data summary, known limitations) | P | Model Owner | Model provenance register | Register completeness rate |

---

### Domain 12 — Cross-Border Data Flow and Output Jurisdiction

**Control objective:** Inference routing, training data flows, and AI outputs are governed for cross-border compliance — including data adequacy, transfer mechanisms, and the jurisdiction of AI output used in individual-affecting decisions.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| CBJ-01 | Inference routing constraints (where data subject jurisdiction determines routing requirements, inference is routed to compliant regions) | P | System Owner + Privacy + Legal | Routing configuration; compliance assessment | Routing compliance rate |
| CBJ-02 | Data adequacy and transfer mechanism documentation (where inference runs in a different jurisdiction from the data subject, adequate transfer mechanism documented) | P | Privacy + Legal | Transfer mechanism record | — |
| CBJ-03 | Output jurisdiction assessment (where AI outputs are used in decisions affecting individuals, the jurisdiction of the affected individual and applicable rights are documented) | P | Legal + Privacy | Jurisdiction assessment record | — |
| CBJ-04 | Cross-border incident response coordination (incidents involving cross-border data or output must engage relevant jurisdictional response obligations) | C | Privacy + Legal | Incident response plan — cross-border section | — |

---

### Domain 13 — Change Management

**Control objective:** All material changes to AI systems — model version, system prompt, retrieval corpus, tool configuration, architecture — are subject to a formal change process that re-evaluates risk tier, updates the system card, and confirms control adequacy before go-live.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| CHG-01 | Material change definition (documented list of what constitutes a material change requiring formal change management: model version update, system prompt change, tool addition, retrieval corpus change, architecture change, deployment environment change) | P | AI Governance Office | Change management policy | — |
| CHG-02 | Pre-change risk re-evaluation (material changes trigger re-evaluation of risk tier; tier change may escalate approval requirements) | P | System Owner + Risk | Change risk assessment record | Tier escalation rate at change |
| CHG-03 | System card update at every material change | P | System Owner | System card version history | System card currency rate |
| CHG-04 | Change approval gate (material changes require approval at the same level as the original deployment approval for the system's tier) | P | Change Authority (per tier) | Change approval record | Unauthorized change detection |
| CHG-05 | Post-change monitoring period (enhanced monitoring for defined period following material change) | D | System Owner | Post-change monitoring log | Anomaly rate in post-change period |

---

### Domain 14 — Logging and Evidence

**Control objective:** All AI systems produce audit-grade logs that provide a complete, tamper-evident record of system behavior, control events, and governance activities.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| LOG-01 | Audit log completeness (all interactions, tool invocations, system prompt changes, access events, and output events logged) | P | System Owner | Log configuration; completeness test | Log completeness rate |
| LOG-02 | Log tamper-evidence (logs stored in write-once or cryptographically protected storage; modification alerts in place) | P | Security + System Owner | Log integrity controls; test records | Log tampering attempts |
| LOG-03 | Log retention per risk tier (Tier 1: 7 years minimum; Tier 2: 3 years; Tier 3: 1 year; aligned to regulatory requirements where longer) | P | System Owner + Data Owner | Retention configuration; compliance verification | Retention compliance rate |
| LOG-04 | Log accessibility for audit and investigation (logs retrievable by authorized audit and investigation functions within defined SLA) | P | System Owner | Log access SLA; test records | Log retrieval SLA compliance |
| LOG-05 | Evidence pack assembly (at defined intervals and on demand, evidence pack for each Tier 1 and Tier 2 system is compiled and reviewed for completeness) | D | AI Governance Office | Evidence pack records | Evidence pack completeness rate |

---

### Domain 15 — GenAI and Agentic-Specific Controls

**Control objective:** Risks specific to generative AI and agentic AI systems — confabulation, content safety, grounding, homogenization, value chain dependency — are addressed by controls additional to the base control set.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| GEN-01 | Confabulation (hallucination) controls (grounding, retrieval, citation, and output confidence controls appropriate to the use case and archetype) | P | System Owner | Confabulation control design; test records | Confabulation rate |
| GEN-02 | Homogenization risk assessment (where AI outputs influence large-scale decisions or communications, the risk of homogenized or monoculture outputs is assessed) | P | Risk + System Owner | Homogenization risk assessment | — |
| GEN-03 | GPAI model governance (where a general-purpose AI model is deployed, obligations applicable to GPAI deployment are assessed and documented) | P | Legal + System Owner | GPAI governance assessment | — |
| GEN-04 | Value chain dependency mapping (all external model and service dependencies in the AI system documented; single points of failure identified) | P | System Owner + Risk | Dependency map | Dependency change events |
| GEN-05 | Content safety layer for open-weight deployments (enterprise-operated safety and content classification layer required for all open-weight self-hosted systems, replacing the vendor-provided safety layer) | P | System Owner + Security | Safety layer configuration; test records | Safety layer bypass events |

---

## 5.3 Architecture-Specific Control Deltas

In addition to the base control set, each archetype receives the following mandatory additional controls. These are deltas — additions to, not replacements for, the base domains.

| Archetype | Mandatory additional controls |
|---|---|
| **App-First** | VND-01 through VND-07 (full vendor suite); CHG-03 applied to vendor AI component updates |
| **Chat-First** | PRM-06 (injection detection); PRM-07 (jailbreak library); OUT-01 through OUT-05 (full output suite); IAM-05 (session management) |
| **Hybrid** | System card must cover all components end-to-end; output attribution controls (which component produced which output); unified monitoring dashboard |
| **RAG** | Full Domain 5 (Retrieval Controls); PRM-06 (injection detection); PRM-08 (indirect injection); GEN-01 (confabulation) |
| **Agentic Single-Agent** | Full Domain 10 (AGT-01 through AGT-09); TOL-01 through TOL-07 (full tool suite); PRM-05 (session memory); PRM-08 (indirect injection) |
| **Agentic Multi-Agent** | Full Domain 10; AGT-06 (inter-agent trust isolation — each agent governed independently); AGT-07 (action chain audit log covering full chain); AGT-08 (scope inheritance); cross-agent credential isolation tested at deployment |
| **Workflow Automation** | OUT-05 (output logging); exception queuing design (automated workflows must have an exception queue for human review of anomalous outputs); CHG-01 through CHG-05 (change management — workflow AI component updates are material changes) |
| **Decision-Support** | Fairness Assessment (mandatory, see Principle 3); Explainability design (output must include explanation sufficient for human decision-maker); decision-maker training documented; OUT-04 (disclosure); post-deployment fairness monitoring |
| **Autonomous / Semi-Autonomous** | AGT-03 (HITL thresholds — highest intensity); AGT-09 (kill-switch — mandatory, tested); TOL-03 and TOL-04 (reversibility and HITL for irreversible); independent safety review before deployment |
| **Open-Weight Self-Hosted** | GEN-05 (enterprise safety layer — mandatory); MSC-03 (tamper-evidence — mandatory); MSC-01 (training data lineage — document knowns and unknowns); red-team testing before deployment (mandatory regardless of tier) |

---

*End of Part V.*

---

# Part VI — Governance Forums, Roles, and Accountability

## 6.1 Governance Bodies

### Board / Risk and Audit Committee

**Accountability:** Ultimate fiduciary accountability for AI risk and governance. Approves the enterprise AI governance framework and risk appetite. Receives periodic AI risk reporting.

**Decision rights:** Approve AI risk appetite; receive escalated AI risk events; approve changes to prohibited use list; receive material incident reports.

**Minimum cadence:** Quarterly AI risk update in Board Risk Committee; annual AI governance framework review.

**Evidence received:** Board AI risk dashboard; material incident reports; annual assurance report; regulatory correspondence relating to AI.

---

### Executive AI Council

**Accountability:** Cross-functional executive body that owns AI strategy execution, resource allocation, and cross-enterprise risk trade-offs. Typically chaired by the CEO or COO. Membership: CRO, CIO/CTO, CDO, CLO (Legal), CISO, CPO (Privacy), CFO, and senior business leaders.

**Decision rights:** Approve AI strategy and investment priorities; approve enterprise AI risk appetite (subject to Board ratification); approve material use case escalations from the AI Risk Committee; approve enterprise-wide AI policy changes; receive and act on the enterprise AI risk register.

**Minimum cadence:** Monthly or quarterly depending on AI program maturity.

---

### AI Governance Office (AGO)

**Accountability:** Operational ownership of the AI governance framework. Manages the AI use-case intake process, maintains the AI system inventory, issues and maintains governance standards and templates, coordinates cross-functional review, provides governance advisory to business units, and reports to the Executive AI Council.

**Decision rights:** Approve Tier 3 (Standard Risk) and Tier 4 (Low Risk) use cases; escalate Tier 1 and Tier 2 cases to the AI Risk Committee; issue governance standards; manage the exception and waiver register; manage the prohibited use register.

**Minimum cadence:** Weekly operations; monthly reporting to the Executive AI Council.

**Key outputs:** AI system inventory; intake decisions; governance standards; exception register; prohibited use register; quarterly AI risk report.

---

### AI Risk Committee

**Accountability:** Cross-functional risk body that approves high-risk and elevated-risk use cases, reviews the enterprise AI risk register, manages material AI incidents, and provides independent challenge to the AI Governance Office. Membership typically: CRO (chair), AI Governance Office Director, CISO, CPO, Head of Compliance, Head of Legal, business unit CROs or equivalent.

**Decision rights:** Approve Tier 1 (High Risk) and Tier 2 (Elevated Risk) use cases; approve exception requests for Tier 1 and Tier 2 controls; escalate material incidents to the Executive AI Council; recommend changes to the risk appetite and prohibited use list; commission independent model or system validation reviews.

**Minimum cadence:** Monthly; ad hoc for material incidents.

---

### Model Validation Function

**Accountability:** Provides independent challenge to model performance, methodology, data, and documentation for High-risk (Tier 1) systems. Must be organizationally independent from the model development team (no shared management up to and including the CRO level, in line with SR 11-7 model risk management principles for regulated environments).

**Decision rights:** Issue validation findings and required remediation actions; recommend approval or rejection of model deployment for Tier 1 systems; escalate unresolved findings to the AI Risk Committee.

**Minimum cadence:** Full validation before Tier 1 deployment; annual re-validation or at material model change.

---

### Business Owner

**Accountability:** The named senior business leader who sponsors the AI use case, owns the business outcomes it is intended to produce, and is accountable for its compliance with governance requirements within their business domain.

**Decision rights:** Approve business justification; accept risk tier classification; approve system card (business sections); commission and fund the AI use case; approve decommissioning.

**Minimum cadence:** At intake, at each lifecycle gate, and at annual review.

---

### System Owner

**Accountability:** The named technical owner responsible for the full AI system: system prompt governance, retrieval, tool/action configuration, output controls, access management, monitoring, and change management.

**Decision rights:** Approve technical design decisions within governance constraints; manage system-level change; approve system card (technical sections); approve tool authorization register; declare readiness for lifecycle gate review.

**Minimum cadence:** Continuous operational responsibility; at each lifecycle gate.

---

### Model Owner

**Accountability:** The named technical owner responsible for the AI model artifact: training, evaluation, versioning, model card, drift monitoring, and retirement.

**Decision rights:** Approve model card; manage model versioning; declare readiness for model validation; initiate model deprecation.

**Minimum cadence:** Continuous for monitoring; at each model update.

---

### Risk, Compliance, Privacy, and Security Functions

Each function provides a specific review and advisory service at defined lifecycle gates and in ongoing operations:

| Function | Primary responsibility in AI governance | Gate involvement |
|---|---|---|
| **Risk** | AI risk register; risk assessment methodology; risk appetite calibration | Tier 1 and Tier 2 intake; AI Risk Committee |
| **Compliance** | Regulatory mapping; regulatory change tracking; compliance attestation | Tier 1 intake; regulated-sector overlays |
| **Privacy** | Privacy Impact Assessment; data protection compliance; cross-border transfer | Tier 1 and Tier 2 intake (where personal data); ongoing PIA review |
| **Security (CISO)** | Security risk assessment; prompt injection; adversarial testing; model supply chain; SAIF alignment | Tier 1 and Tier 2 intake; pre-deployment security gate |
| **Legal** | Regulatory interpretation; contractual AI obligations; prohibited use list; IP and copyright | Tier 1 intake; EU AI Act applicability |

---

### Internal Audit

**Accountability:** Independent assurance that AI governance controls are designed and operating effectively. Internal Audit is not part of the governance or control function; it provides the third line of defense assurance.

**Activities:**
- Annual AI governance framework audit
- Tier 1 and Tier 2 system control effectiveness audits (risk-based selection)
- Prohibited use register audit (annual)
- AI system inventory completeness audit (annual)
- Vendor AI governance audit (risk-based selection)
- Post-incident audit for material AI incidents

**Reporting:** Direct report to Board Audit Committee; findings reported to the AI Risk Committee and Executive AI Council.

---

## 6.2 RACI Matrix

For the primary AI governance processes:

| Process | Board/RAC | Exec AI Council | AI Gov Office | AI Risk Committee | Business Owner | System Owner | Model Owner | Risk | Compliance | Privacy | Security | Legal | Internal Audit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI risk appetite setting | A | R | C | C | I | I | I | C | C | I | I | C | I |
| Prohibited use list maintenance | I | A | R | C | I | I | I | C | C | I | I | R | I |
| Tier 0 intake rejection | I | I | R/A | I | I | I | I | I | I | I | I | I | I |
| Tier 1 use case approval | I | I | C | A/R | C | C | C | R | R | R | R | R | I |
| Tier 2 use case approval | I | I | A/R | C | C | C | C | C | C | R | R | C | I |
| Tier 3/4 use case approval | I | I | A/R | I | R | C | I | I | I | I | I | I | I |
| System card sign-off | I | I | R | C (T1) | A | R | C | I | I | I | I | I | I |
| Model validation (Tier 1) | I | I | I | A | I | I | R | C | I | I | I | I | I |
| Exception / waiver approval (T1) | I | I | C | A | R | I | I | R | C | I | I | I | I |
| Material incident escalation | A | R | R | R | C | R | C | R | C | C | R | C | I |
| Annual governance audit | I | I | C | C | I | I | I | I | I | I | I | I | A/R |

*A = Accountable; R = Responsible; C = Consulted; I = Informed*

---

## 6.3 Review Cadences and Gate Structure

| Governance event | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| **Intake gate** | AI Risk Committee + Legal + Exec Sponsor | AI Gov Office + Security + Privacy | AI Gov Office + Business Owner | Business Owner self-cert |
| **Design gate** | AI Risk Committee review | AI Gov Office review | AI Gov Office acknowledgment | None |
| **Pre-deployment gate** | Full evidence pack; independent validation; security gate; legal sign-off | Standard evidence pack; security gate; privacy gate | Lightweight checklist | None |
| **Post-deployment (initial)** | 30-day enhanced monitoring review | 30-day monitoring review | None | None |
| **Operational review** | Quarterly | Semi-annual | Annual | Annual |
| **Annual governance review** | Full re-assessment | Standard review | Lightweight review | Registration check |
| **Material change gate** | Same as Tier 1 deployment gate | Same as Tier 2 deployment gate | AI Gov Office + Business Owner | Business Owner notification |
| **Decommissioning gate** | AI Risk Committee sign-off; data retention confirmed | AI Gov Office sign-off | Business Owner notification | Business Owner notification |

---

# Part VII — Monitoring, Incidents, and Assurance

## Deliverable D — Lifecycle Governance Map

The lifecycle has eleven stages. Risk tier determines gate intensity, evidence requirements, and approval level at every stage. The table below specifies these for each tier.

### Stage 1 — Intake and Classification

| Element | Tier 1 — High | Tier 2 — Elevated | Tier 3 — Standard | Tier 4 — Low |
|---|---|---|---|---|
| Gate intensity | Full intake review; risk classification by AI Gov Office; Legal and Compliance screening | AI Gov Office review; Privacy and Security screening | AI Gov Office review | Self-certification |
| Evidence required | Completed intake form; ownership declaration; preliminary risk assessment; business justification | Completed intake form; ownership declaration; data classification | Basic intake form; ownership | Notification record |
| Approval level | AI Risk Committee (preliminary endorsement to proceed to design) | AI Gov Office | AI Gov Office | Business Owner |

### Stage 2 — Design

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Gate intensity | Design review by AI Risk Committee; architecture review; HITL design review; PIA initiation | Design review by AI Gov Office; security architecture review | AI Gov Office acknowledgment | None |
| Evidence required | Design specification; architecture diagram; control design mapping; HITL design; initial PIA | Design specification; architecture diagram; security review record | Design record | None |
| Approval level | AI Risk Committee | AI Gov Office + Security + Privacy | AI Gov Office | None |

### Stage 3 — Build

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Gate intensity | Ongoing security reviews; model card initiated; system card drafted; prompt governance implemented | Model card initiated; system card drafted | System card (lightweight) | None |
| Evidence required | Build checklist; model card draft; system prompt version record; data governance confirmation | Build checklist; model card; system prompt record | Lightweight checklist | None |
| Approval level | No gate (build phase); gate at end = Validation gate | No gate; gate at end = Pre-deployment | AI Gov Office at pre-deployment | None |

### Stage 4 — Validation

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Gate intensity | Independent model validation (challenge function); red-team testing; fairness assessment; security penetration test; output safety testing; HITL testing | Output safety testing; security testing; functional testing | Output quality check | None |
| Evidence required | Validation report (independent); red-team report; fairness assessment report; pen-test report; safety testing report; HITL test record | Testing records; safety test report | Quality check record | None |
| Approval level | Model Validation Function (required to pass before deployment gate) | AI Gov Office | Business Owner | None |

### Stage 5 — Approval / Pre-Deployment Gate

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Gate intensity | Full evidence pack review; AI Risk Committee approval; Legal sign-off; Compliance attestation; security clearance; Privacy confirmation | Standard evidence pack; AI Gov Office approval; security clearance; Privacy confirmation | Lightweight approval; AI Gov Office + Business Owner | Business Owner self-cert |
| Evidence required | Full evidence pack (all Domains documented); all validation reports; system card (final); model card (final); PIA (final); compliance attestation | Standard evidence pack; system card; model card; security and privacy sign-off | Lightweight checklist; system card | Registration record |
| Approval level | AI Risk Committee + Legal + Exec Sponsor | AI Gov Office + Security + Privacy | AI Gov Office + Business Owner | Business Owner |

### Stage 6 — Deployment

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Gate intensity | Staged rollout; 30-day enhanced monitoring window; rollback plan activated | Monitored deployment; rollback plan | Standard deployment | Standard deployment |
| Evidence required | Deployment record; rollback plan; monitoring dashboard active; escalation contacts confirmed | Deployment record; monitoring active | Deployment record | Deployment record |
| Approval level | System Owner (execution); AI Risk Committee informed | System Owner | System Owner | System Owner |

### Stage 7 — Monitoring (Ongoing)

See Deliverable E for the runtime signal catalog. Monitoring intensity by tier:

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Signal set | Enhanced (all signals in Deliverable E) | Standard (core signals) | Basic (output quality, error rate) | Periodic spot-check |
| Review cadence | Weekly KRI review | Monthly review | Quarterly review | Annual review |
| Reporting | Monthly AI Risk Committee; quarterly Board | Quarterly AI Gov Office | Annual summary | Annual summary |

### Stage 8 — Incident Response

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Severity assessment | Mandatory within 1 hour of detection | Within 4 hours | Within 24 hours | Within 5 business days |
| Escalation | AI Risk Committee within 24 hours for Severity 1–2 | AI Gov Office within 24 hours for Severity 1–2 | AI Gov Office for Severity 1–2 | Business Owner |
| Post-incident review | Mandatory root-cause analysis; corrective action plan; AI Risk Committee sign-off | Mandatory for Severity 1–2 | Required for Severity 1 | Not required |

### Stage 9 — Change Management

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Material change gate | Same intensity as deployment gate; AI Risk Committee re-approval | Same as Tier 2 pre-deployment | AI Gov Office + Business Owner | Business Owner notification |
| Evidence required | Change risk assessment; updated system card; updated model card (if model changed) | Change record; updated system card | Change record | Change note |

### Stage 10 — Retirement / Decommissioning

| Element | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Gate intensity | AI Risk Committee sign-off; data retention confirmed; audit log archiving confirmed; regulatory notification where required | AI Gov Office sign-off; data retention confirmed | Business Owner notification; data retention confirmed | Business Owner notification |
| Evidence required | Retirement record; data disposition certificate; log archiving confirmation | Retirement record; data disposition | Retirement note | Retirement note |

### Stage 11 — Post-Retirement Monitoring

All retired Tier 1 and Tier 2 systems remain in the AI system inventory (marked retired) for the full evidence retention period. Regulatory inquiries and audit requests may require evidence from retired systems.

---

## Deliverable E — Runtime Monitoring Signal Catalog

The following signals are mandatory for all in-scope AI systems at the intensity level specified by tier. Systems must produce these signals automatically; retrospective assembly of monitoring data is not acceptable.

| Signal ID | Signal | Definition | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Escalation threshold |
|---|---|---|---|---|---|---|---|
| MON-01 | **Policy violation rate** | Rate of outputs or actions that violate defined enterprise AI policy | Continuous | Continuous | Periodic | Spot | >0.1% triggers alert |
| MON-02 | **Unsafe output rate** | Rate of outputs flagged by output safety classifier | Continuous | Continuous | Periodic | Spot | Any sustained rate >0.05% triggers review |
| MON-03 | **Prompt injection attempt rate** | Rate of detected prompt injection attempts (direct and indirect) | Continuous | Continuous | Not required | Not required | Any successful injection triggers incident |
| MON-04 | **Successful injection rate** | Rate of prompt injections that bypassed detection and altered system behavior | Continuous | Continuous | Not required | Not required | Any >0 triggers immediate incident |
| MON-05 | **Hallucination / factuality failure rate** | Rate of outputs assessed as factually incorrect or ungrounded (for systems where factual accuracy is a stated requirement) | Continuous | Continuous | Periodic | Not required | >defined threshold triggers review |
| MON-06 | **Tool misuse rate** | Rate of tool invocations that are anomalous, unauthorized, or outside scope | Continuous | Continuous | Not required | Not required | Any unauthorized invocation triggers alert |
| MON-07 | **Unauthorized action attempt rate** | Rate of agent action attempts that were outside the authorized action scope | Continuous | Continuous | Not required | Not required | Any >0 triggers incident |
| MON-08 | **Human override rate** | Rate at which human reviewers override AI recommendations or outputs | Continuous | Continuous | Periodic | Not required | Material increase from baseline triggers model review |
| MON-09 | **HITL bypass event count** | Number of instances where HITL was bypassed without authorization | Continuous | Continuous | Not required | Not required | Any >0 triggers incident |
| MON-10 | **Input drift rate** | Rate of change in input distribution from the distribution at validation (concept drift indicator) | Continuous | Continuous | Periodic | Not required | Threshold breach triggers model review |
| MON-11 | **Output distribution drift** | Change in output distribution from baseline at deployment | Continuous | Continuous | Periodic | Not required | Threshold breach triggers model review |
| MON-12 | **Performance degradation rate** | Decline in model performance metrics from baseline (accuracy, precision, recall as applicable) | Continuous | Continuous | Periodic | Not required | >defined threshold triggers model review |
| MON-13 | **User escalation rate** | Rate at which users escalate AI interactions to human agents or submit feedback indicating AI failure | Continuous | Continuous | Periodic | Not required | Material increase from baseline triggers review |
| MON-14 | **Audit log completeness rate** | Percentage of system interactions that produce complete, well-formed audit log entries | Continuous | Continuous | Periodic | Spot | <99% triggers investigation |
| MON-15 | **Privacy leakage detection rate** | Rate of outputs containing potential personal data disclosures detected by output monitoring | Continuous | Continuous | Periodic | Not required | Any >0 triggers privacy incident |
| MON-16 | **Cost runaway signal** | Anomalous surge in inference cost or volume indicating potential misuse, runaway agent loop, or system error | Continuous | Continuous | Periodic | Not required | >3x baseline spend triggers alert |
| MON-17 | **Security misuse signal** | Indicators of AI system use for unauthorized purposes (credential theft, social engineering, code generation for attack) | Continuous | Continuous | Not required | Not required | Any confirmed event triggers security incident |
| MON-18 | **Fairness metric breach** | Fairness metrics (disparate impact ratio, demographic parity) outside defined tolerance | Continuous | Continuous (where applicable) | Not required | Not required | Any breach triggers mandatory review |

---

## 7.1 KPI / KRI / KCI Framework

### Key Performance Indicators (operational AI program health)

| KPI | Target | Reporting cadence |
|---|---|---|
| AI system inventory completeness | 100% of known production systems registered | Monthly |
| System card currency rate | >95% of production systems with current system card | Monthly |
| Intake SLA compliance | >90% of intakes processed within SLA | Monthly |
| Evidence pack completeness (Tier 1 and Tier 2) | 100% | Quarterly |
| Governance review completion rate | 100% of systems reviewed on schedule | Quarterly |

### Key Risk Indicators (early warning)

| KRI | Threshold | Response |
|---|---|---|
| Tier 1 systems without current validation | >0 | Immediate escalation to AI Risk Committee |
| Active exceptions approaching expiry | >3 without renewal in progress | AI Gov Office escalation |
| Model drift alerts unresolved >7 days | Any | System Owner escalation |
| Vendor AI incident notifications unacknowledged >24h | Any | Procurement + Security escalation |
| Prohibited use register — attempted resubmission of rejected intake | Any | Legal + AI Gov Office investigation |
| HITL bypass events | Any | Immediate incident |
| Prompt injection success events | Any | Immediate security incident |

### Key Control Indicators (control effectiveness)

| KCI | Target | Reporting cadence |
|---|---|---|
| Prompt injection detection rate (of known test injections) | >99% | Monthly (from red-team testing program) |
| Safety classifier precision (true positive rate) | >95% | Monthly |
| Log completeness rate | >99.5% | Continuous |
| Access review completion rate | 100% on schedule | Quarterly |
| Change management gate bypass rate | 0% | Monthly |

---

## 7.2 Incident Taxonomy and Severity Model

### Incident Categories

| Category | Definition | Examples |
|---|---|---|
| **Safety incident** | AI output causes or materially risks harm to a user, third party, or the enterprise | Harmful content generated; dangerous instruction provided; unsafe autonomous action taken |
| **Privacy incident** | AI system discloses personal data or violates data protection obligations | PII disclosed in output; training data memorization exposed; cross-context data leakage |
| **Security incident** | AI system is compromised, misused, or used as an attack vector | Prompt injection breach; jailbreak success; model extraction; AI used for social engineering |
| **Fairness incident** | AI system produces outputs or decisions with unjustified disparate impact | Fairness metric breach confirmed; discriminatory output detected |
| **Compliance incident** | AI system violates regulatory obligation or policy prohibition | Prohibited use detection; regulatory disclosure failure; AI Act obligation breach |
| **Operational incident** | AI system fails to perform within defined parameters, causing operational impact | Runaway agent; cost explosion; system prompt failure; model performance collapse |
| **Governance incident** | AI governance control is bypassed, circumvented, or found to be non-operational | Unauthorized system prompt change; HITL bypass; change without approval |

### Severity Model

| Severity | Definition | Response SLA | Escalation |
|---|---|---|---|
| **S1 — Critical** | Confirmed harm to individuals; regulatory breach; significant data loss; widespread safety failure | Immediate containment; 1-hour escalation to CISO + CRO; Board notification within 24h | Board, Executive AI Council, AI Risk Committee, Legal, Regulators (where required) |
| **S2 — High** | Potential harm; control failure confirmed; significant policy breach; regulatory notification risk | Containment within 4 hours; AI Risk Committee notification within 24 hours | AI Risk Committee, CISO, CRO, Legal, AI Gov Office |
| **S3 — Medium** | Control degradation; anomalous behavior confirmed; no confirmed harm | Investigation within 24 hours; AI Gov Office notification within 48 hours | AI Gov Office, System Owner, Risk |
| **S4 — Low** | Anomaly detected; investigation required; no evidence of control failure | Investigation within 5 business days | System Owner, AI Gov Office (monitoring) |

### Post-Incident Requirements (by severity)

| Requirement | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| Root-cause analysis | Mandatory (external if material) | Mandatory | Required | Recommended |
| Corrective action plan | Mandatory; AI Risk Committee sign-off | Mandatory | Required | Recommended |
| Regulatory notification assessment | Mandatory | Mandatory | Required | Not required |
| System suspension pending review | Mandatory | At AI Risk Committee discretion | Not required | Not required |
| Evidence pack update | Mandatory | Mandatory | Required | Recommended |
| Board reporting | Mandatory | At CRO discretion | Not required | Not required |
| Post-incident audit | Mandatory | Recommended | Not required | Not required |

---

## 7.3 Assurance Evidence Pack

For each Tier 1 and Tier 2 system, the following evidence pack must be maintained and available for audit and regulatory review on demand:

| Evidence item | Description | Owner | Retention |
|---|---|---|---|
| System card (current version + version history) | Full description of the AI system: purpose, architecture, archetype, data, model, controls, risk tier, ownership | System Owner | Full retention period |
| Model card (current + history) | Model documentation: training data, evaluation results, limitations, intended use | Model Owner | Full retention period |
| Intake and classification record | Original intake form; risk tier classification; approval record | AI Gov Office | Full retention period |
| PIA (current + history) | Privacy Impact Assessment and update history | Privacy | Full retention period |
| Fairness assessment (Tier 1 decision systems) | Fairness evaluation results; metrics; remediation records | System Owner + Risk | Full retention period |
| Validation report (Tier 1) | Independent model validation findings and resolution | Model Validation | Full retention period |
| Red-team report | Adversarial testing results; findings; remediations | Security | Full retention period |
| Security assessment | Security risk assessment; penetration test results; remediation | Security | Full retention period |
| Pre-deployment approval record | Signed approval by required approvers at the pre-deployment gate | AI Gov Office | Full retention period |
| Monitoring dashboard (historical) | Historical monitoring signal data at required retention period | System Owner | Full retention period |
| Incident records (if any) | All incidents, severity assessments, root-cause analyses, corrective actions | AI Gov Office | Full retention period |
| Change records | All material change approvals and associated re-assessments | Change Management | Full retention period |
| Audit log (system) | System-generated audit logs | System Owner | Per tier retention requirement |
| Vendor assessment records | Third-party AI provider assessment records | Procurement + Security | Full retention period |
| Exception records (if any) | All exceptions granted; compensating controls; expiry and renewal records | AI Gov Office | Full retention period |

*Tier 1 retention: 7 years minimum. Tier 2 retention: 3 years minimum.*

---

*End of Parts VI and VII.*

---

# Part VIII — Adoption Acceleration Blueprint

## 8.1 Minimum Viable Governance Model

The minimum viable governance model (MVGM) is the lowest-overhead governance configuration that still provides meaningful control and audit defensibility. It is appropriate for enterprises in the early stages of AI program maturity (fewer than 20 active use cases; no Tier 1 systems in production; no regulated-sector obligations).

**MVGM components:**

| Component | Minimum viable specification |
|---|---|
| AI system inventory | Spreadsheet or lightweight tool; minimum fields: system name, archetype, risk tier, Business Owner, System Owner, deployment date, status |
| Intake process | Single standardized intake form; AI Gov Office review (one person is sufficient at this stage); email-based approval |
| Risk tiering | Self-classification using the Deliverable B tiering criteria; AI Gov Office spot-check review |
| System card | Lightweight template (purpose, archetype, tier, data used, model or service, outputs, owner); 1–2 pages |
| Monitoring | Manual periodic review using the MON-01 through MON-08 core signals; no automated tooling required at this stage |
| Incident process | Defined escalation contact; documented severity model; post-incident record |
| Governance review | Quarterly 30-minute review of inventory; annual policy refresh |

**MVGM is NOT appropriate when:**
- Any Tier 1 (High Risk) system is in production
- Any regulated-sector obligation applies (SR 11-7, HIPAA, EU AI Act high-risk)
- The AI estate exceeds 30 active use cases
- Customer-facing AI systems are deployed

---

## 8.2 Advanced Governance Model

The advanced governance model is appropriate for enterprises with a mature AI program (50+ active use cases; Tier 1 systems in production; regulated-sector presence; federated business unit AI development).

**Advanced model additions over MVGM:**

| Dimension | Advanced specification |
|---|---|
| Inventory | Automated AI system registry integrated with CI/CD pipeline (auto-registers new deployments); API-connected monitoring dashboards |
| Intake | Automated intake portal; automated tier pre-classification (human confirmation); automated gate tracking |
| Governance bodies | Full AI Risk Committee; Model Validation Function; dedicated AI Governance Office team |
| Controls | Automated prompt injection detection; automated output safety classification; automated drift monitoring; automated audit log completeness check |
| Monitoring | Real-time dashboards with automated alerting for all Deliverable E signals; automated KRI breach notification |
| Assurance | Annual ISO/IEC 42001 external audit; internal audit AI governance program; continuous control monitoring |
| Templates | Full template pack (Deliverable G); pre-approved architecture patterns in architecture review board |

---

## 8.3 Fast-Lane Approval for Low-Risk Use Cases

The fast lane is a streamlined governance pathway for Tier 3 (Standard Risk) and Tier 4 (Low Risk) use cases. Its purpose is to remove unnecessary friction from low-risk adoption without creating a governance gap.

**Fast-lane eligibility criteria (all must be met):**
- Risk tier is Tier 3 or Tier 4 (self-certified; AI Gov Office may spot-check)
- Use case falls within a pre-approved use-case category (see below)
- System uses a pre-approved AI service or platform (see pre-approved service register)
- No personal data processed beyond what is already covered by existing enterprise data agreements with the service provider
- Business Owner accepts accountability in writing

**Pre-approved use-case categories (Tier 3 fast lane):**
- Internal text summarization using enterprise-approved AI service; no sensitive data
- Internal code assistance using enterprise-approved AI service; no proprietary algorithm disclosure
- Internal document Q&A using enterprise-approved AI service; restricted to non-confidential corpus
- Meeting transcription and summarization using enterprise-approved service; standard enterprise data terms apply

**Fast-lane process:**
1. Business Owner completes simplified intake form (10 fields maximum)
2. Automated tier and eligibility check
3. AI Gov Office notification (no active approval required; 5-business-day silent approval unless AI Gov Office objects)
4. Lightweight system card completed
5. Deployment with standard logging

**Fast-lane is suspended if:**
- Scope of the use case expands beyond the original intake declaration
- Personal or sensitive data is introduced
- The use case is modified to interact with customers or external parties

---

## 8.4 High-Risk Escalation Model

Tier 1 (High Risk) use cases receive a dedicated escalation track designed to provide rigorous governance without unnecessary delay.

**Key acceleration mechanisms for Tier 1 (without reducing control):**

| Mechanism | Description |
|---|---|
| Pre-intake advisory | AI Gov Office provides advisory session before formal intake to identify control requirements, data governance issues, and regulatory obligations early — reducing rework at later gates |
| Parallel workstreams | PIA, security assessment, and fairness assessment are conducted in parallel (not sequentially); gate is held open until all are complete |
| Pre-approved control patterns | If the system uses a pre-approved architecture pattern (e.g., standard RAG with enterprise-approved retrieval stack), the architecture portion of the review is shortened |
| Dedicated validation calendar | Model Validation Function maintains a published capacity calendar; Tier 1 projects book validation slots at design gate to avoid scheduling delays at validation gate |
| Rollback as a deployment accelerator | Robust rollback capability, documented at pre-deployment gate, gives AI Risk Committee confidence to approve deployment without full market-scale testing |

---

## 8.5 Governance Misallocation Diagnostic

**The most common and most dangerous enterprise governance failure is not excessive governance broadly — it is governance intensity applied to the wrong systems at the wrong stages.**

**Fact:** Low-risk internal productivity tools (document summarization, code assistance, internal search) are frequently over-governed. They face the same approval cycles, documentation requirements, and committee reviews as genuinely high-risk systems. The result: developers route around governance, use unsanctioned services, and governance loses credibility.

**Fact:** Customer-facing AI systems, decision-support systems, and agentic systems are frequently under-governed. They are treated as standard software deployments. Model performance, fairness, explainability, and monitoring are not designed in. Incidents occur and governance cannot respond because evidence does not exist.

**Recommendation:** Perform a governance misallocation audit against the following diagnostic:

### Misallocation Diagnostic Table

| Diagnostic question | Over-governance indicator | Under-governance indicator | Corrective action |
|---|---|---|---|
| What is the approval time for an internal productivity tool? | >10 business days for Tier 3/4 | N/A | Implement fast-lane for pre-approved categories |
| What documentation is required for a Tier 4 use case? | Same as Tier 1 | N/A | Differentiate documentation requirements by tier |
| Do Tier 1 systems have runtime monitoring? | N/A | No monitoring in production | Mandate monitoring as pre-deployment gate requirement |
| Do Tier 1 decision-support systems have fairness metrics defined? | N/A | No fairness metrics defined | Make fairness assessment mandatory at design gate |
| Are agentic systems treated as standard software? | N/A | No tool-use scope limits; no HITL thresholds | Apply agentic control delta (Domain 10) |
| Are developer teams bypassing governance channels? | Yes — indicates governance friction is too high for low-risk | N/A | Investigate root cause; likely over-governance of low-risk |
| Do high-risk systems have complete evidence packs? | N/A | Evidence assembled retrospectively for audits | Mandate evidence-by-design at Tier 1 |
| Are open-weight self-hosted models treated as equivalent to vendor-hosted models? | N/A | No enterprise safety layer; no tamper-evidence | Apply open-weight control delta |

---

## 8.6 Pre-Approved Architecture and Control Patterns

Pre-approved patterns reduce governance cycle time by allowing projects to select a validated, pre-cleared architecture rather than designing controls from scratch.

| Pattern ID | Pattern name | Archetype | Description | Pre-approved controls | Maximum tier eligible |
|---|---|---|---|---|---|
| PAT-01 | Standard internal RAG | RAG | Enterprise-approved LLM API + enterprise-approved vector store + enterprise data classification compliant corpus | Domain 5 full; PRM-06; GEN-01 | Tier 2 |
| PAT-02 | Chat assistant (internal) | Chat-First | Enterprise-approved LLM API + enterprise SSO + no sensitive data | Domain 4 + Domain 7 core controls | Tier 3 |
| PAT-03 | Decision-support with human review | Decision-Support | AI recommendation + mandatory human approval + output logging | Domain 7 + OUT-04 + MON-08 | Tier 2 (Tier 1 if regulated domain) |
| PAT-04 | Single-agent with restricted tool set | Agentic Single-Agent | Enterprise-approved LLM + pre-approved tool list (read-only tools only) + HITL for all writes | Domain 10 full; reversible-only tool set | Tier 2 |
| PAT-05 | App-First with vendor AI | App-First | Standard enterprise SaaS with AI feature; vendor assessment completed; standard data terms | VND-01 through VND-04 | Tier 3 |

---

## 8.7 Anti-Patterns — Governance Theater and How to Avoid It

The following anti-patterns produce the appearance of governance without its substance. Each is a control failure.

**Anti-Pattern 1 — Documentation-heavy, control-light governance.**
The system card, PIA, and risk assessment are completed. No one checks whether the controls described in them are actually implemented. Fix: implement control verification as a distinct pre-deployment gate item, separate from documentation review.

**Anti-Pattern 2 — Human-in-the-loop theater.**
HITL is designed in as a control. In production, the queue of AI outputs awaiting human review grows faster than reviewers can process it. Reviewers begin approving batches without reading them. Fix: design HITL capacity requirements at design gate; monitor HITL queue depth and review dwell time as KCIs; if HITL is not functioning, treat it as a control failure, not a resourcing issue.

**Anti-Pattern 3 — Excessive central approvals.**
All AI use cases — regardless of tier — go through the same central committee. The committee becomes a bottleneck. Business units route around it. Fix: implement the fast-lane model (Section 8.3) and the risk-tiered approval model (Deliverable B). Reserve committee review for Tier 1 and material exceptions only.

**Anti-Pattern 4 — One-size-fits-all governance.**
Every AI system — chat assistant, credit decisioning engine, code helper — goes through the same governance process. Fix: implement the archetype-specific control delta model (Part V, Section 5.3). Governance intensity must match the actual risk profile of the system.

**Anti-Pattern 5 — Policy without monitoring.**
The enterprise has a Responsible AI policy. No runtime monitoring signals are defined. The policy states controls; no one checks whether they operate. Fix: mandate runtime monitoring as a pre-deployment gate requirement. A control without a monitoring signal is a claim, not a control.

**Anti-Pattern 6 — Model governance without system governance.**
Model cards exist. Model evaluation reports exist. But the system prompt — the primary behavioral governor of the AI system — is unversioned, unaudited, and accessible to anyone with admin credentials. Fix: implement Domain 4 (Prompt and Instruction Governance) with the same discipline as model governance.

**Anti-Pattern 7 — Vendor dependency without vendor governance.**
The enterprise governs its own-built systems but relies on vendor API providers without assessing their data handling, model update practices, or security posture. Fix: implement Domain 9 (Vendor and Supply-Chain Controls) for all third-party AI services and platforms.

---

## 8.8 Workforce Enablement

Governance that is not understood is not followed. The AI governance framework requires a workforce enablement program covering:

| Audience | Required knowledge | Delivery mechanism | Cadence |
|---|---|---|---|
| Board and NED | AI risk landscape; governance obligations; material incident reporting; risk appetite | Board briefing; tabletop exercise | Annual minimum |
| Executive AI Council | Full framework; risk tiering; incident response; regulatory obligations | Facilitated workshop | At framework launch; annual refresh |
| Business Owners | Intake process; risk tiering; their accountability; system card requirements | Online module + facilitated session | Before first use-case sponsorship |
| System Owners and developers | Full technical controls; prompt governance; agentic controls; monitoring requirements | Technical training; hands-on workshop | At onboarding; annual refresh |
| Risk, Compliance, Privacy, Security | Framework review responsibilities; gate criteria; evidence requirements | Specialist training | At framework launch; at material update |
| Internal Audit | Framework scope; evidence pack structure; audit criteria | Specialist briefing | Annual |
| All employees | What AI systems they may use; prohibited uses; how to report concerns | Enterprise AI use policy; mandatory e-learning | Annual |

---

## 8.9 Sector-Specific Governance Overlays

The following overlays are **deltas** to the base framework. They specify only the additional or modified requirements for each regulated sector. They do not repeat base framework requirements. Enterprises in other regulated sectors should use these as templates to derive their own sector delta.

---

### Overlay A — Financial Services

**Primary regulatory anchors:** SR 11-7 (Model Risk Management Guidance, Federal Reserve / OCC); EU AI Act high-risk classification for AI in credit, insurance, and employment decisions; SEC AI guidance; relevant CFPB AI guidance.

**Delta requirements:**

| Area | Delta requirement |
|---|---|
| **Model Risk Management alignment** | All Tier 1 AI models used in credit, trading, underwriting, or fraud detection must comply with SR 11-7 model risk management principles: independent validation by a function separate from development; model documentation (purpose, assumptions, limitations, validation results); ongoing monitoring; challenge and validation at material change |
| **Model validation independence** | The validation function must be organizationally independent from development and from the business using the model. In large institutions, this typically means a dedicated Model Risk Management function reporting to the CRO. |
| **Validation depth for credit models** | Credit risk, fraud, and AML AI models require validation of: conceptual soundness of the approach; data quality and representativeness; performance on out-of-time and out-of-sample data; sensitivity analysis; fairness and disparate impact analysis; backtesting against realized outcomes |
| **Supervisory disclosure** | In jurisdictions where model risk management is a supervisory expectation, the AI governance framework (or a summary) must be available for examiner review on request. Validation reports and model inventories are typically subject to examiner access. |
| **AI in trading and market risk** | AI systems used in trading decisions or market risk management require: pre-deployment supervisory notification in applicable jurisdictions; enhanced stress testing; limit structures on AI-generated positions or recommendations; mandatory human override capability |
| **Consumer credit decisions** | AI systems used in consumer credit decisions must: comply with applicable adverse action notice requirements; document the specific factors used in each decision (explainability obligation); be tested for disparate impact under ECOA/Fair Housing Act equivalents in applicable jurisdictions |

---

### Overlay B — Healthcare

**Primary regulatory anchors:** HIPAA (US); applicable clinical device regulation (FDA Software as a Medical Device where applicable; EU MDR/IVDR); relevant GDPR provisions for health data; clinical governance standards.

**Delta requirements:**

| Area | Delta requirement |
|---|---|
| **HIPAA adjacency** | AI systems that process, generate, or store Protected Health Information (PHI) are governed under the enterprise HIPAA compliance program in addition to this AI governance framework. AI inputs, outputs, and logs containing PHI are subject to HIPAA security, privacy, and breach notification rules. |
| **Clinical decision support governance** | AI systems that provide clinical decision support (diagnosis, treatment recommendation, triage) require: clinical validation by qualified clinical personnel before deployment; clinical governance review by the relevant clinical governance committee; documentation of intended user (clinician vs patient), intended use, known limitations, and contra-indications |
| **Patient-affecting output audit trail** | Any AI output that directly influences a clinical decision affecting a patient must be logged at the individual-interaction level with: patient identifier (where lawful); AI system version; AI output; treating clinician identifier; clinical decision made; outcome (where accessible). This audit trail must be retained for the applicable clinical records retention period. |
| **Software as a Medical Device** | AI systems that meet the definition of Software as a Medical Device under applicable regulation (FDA, EU MDR/IVDR) require regulatory clearance or certification before deployment. This governance framework does not substitute for regulatory clearance; it complements the QMS requirements of the applicable medical device regulation. |
| **Human override** | Clinical AI systems must have a clear and accessible human override pathway. Clinicians must not be constrained by the AI system from overriding its recommendation. Override rates must be monitored as a KCI (high override rates indicate clinical distrust or poor AI performance). |

---

### Overlay C — Safety-Critical Infrastructure

**Applies to:** Energy (generation, transmission, distribution); aviation (ATC, flight management, maintenance); industrial control systems (SCADA, DCS); water and wastewater; rail and mass transit.

**Primary regulatory anchors:** Relevant sector-specific regulation (NERC CIP for energy in North America; EASA for aviation in Europe; NIS2 Directive in EU for critical infrastructure); IEC 61508 functional safety standards where applicable.

**Delta requirements:**

| Area | Delta requirement |
|---|---|
| **Fail-safe design mandate** | All AI systems that interact with or produce outputs that control physical systems must be designed to fail safe. The system must continue to operate safely if the AI component fails, produces erroneous output, or is unavailable. AI failure must not propagate to physical system failure. This is a design-time requirement, not a runtime control. |
| **Consequence-based escalation thresholds** | Risk tier assignment for safety-critical infrastructure AI systems must be based on the physical consequence of AI error, not only the information-layer risk. An AI system that controls a valve in a water treatment plant carries physical safety consequences; it must be classified Tier 1 regardless of its information-layer risk profile. |
| **Human override — mandatory and tested** | Human override of AI recommendations or commands must be available at all times, accessible without AI system involvement, and tested at defined intervals. Override capability must be documented in the system card and verified in the pre-deployment gate. |
| **Mandatory safety review by domain-qualified engineers** | Tier 1 AI systems in safety-critical infrastructure must be reviewed by engineers qualified in the applicable functional safety standard (e.g., IEC 61508 SIL assessment) before deployment. This review is in addition to, not a substitute for, the base framework validation gate. |
| **Incident consequence classification** | Incidents involving safety-critical infrastructure AI systems are assessed for physical consequence (potential for injury, equipment damage, environmental impact, service disruption) in addition to the standard AI incident severity model. Any incident with potential physical consequence is classified S1 regardless of its information-layer severity. |

---

*End of Part VIII.*

---

# Part IX — Corporate Template Stacks and Enterprise Synthesis

This section assesses the major AI platform providers as governance and control reference implementations — not as product marketing. The purpose is to identify what each provider contributes to enterprise governance, where each falls short, and how enterprises should extract and internalize useful patterns without becoming dependent on any single provider's framing.

---

## 9.1 Google Template Stack

### Primary artifacts
- **Secure AI Framework (SAIF)** — AI-specific security architecture
- **Model Cards** — model documentation template
- **Data Cards / Data Cards Playbook** — dataset documentation template
- **MLOps maturity guidance** — production ML pipeline discipline
- **Responsible AI practices** — general guidance

### Assessment

**Governance utility — Medium.** Google provides no published governance operating model (no intake process, no committee structure, no RACI). SAIF is a security architecture framework, not a governance framework. Responsible AI practices are principle-level statements.

**Control utility — High.** SAIF is the best publicly available AI-specific security threat and control reference. It addresses six core elements: secure AI design; robust AI operation; AI supply chain integrity; AI model access controls; AI testing and red-teaming; AI monitoring. These translate directly into enterprise control requirements in Domains 8, 9, 10, and the security portions of Domain 4.

**Assurance utility — Medium.** Model Cards and Data Cards are the strongest documentation templates publicly available. They produce evidence artifacts (model documentation, dataset documentation) that are directly usable in an enterprise evidence pack and in audit. They do not, however, constitute a management system or assurance program.

**Monitoring utility — High (MLOps).** Google's MLOps maturity model (three levels: manual process, ML pipeline automation, CI/CD pipeline automation) provides the clearest published reference for production ML monitoring and automation maturity. It is directly usable as a monitoring maturity target for enterprises operating traditional ML systems.

**Enterprise adoption usefulness — High.** Model Cards are the de facto industry template for model documentation. Data Cards fill the dataset documentation gap. SAIF is the best security architecture reference for AI. All three should be internalized into the enterprise standard template pack.

**Implementation burden — Low to Medium.** Model Cards and Data Cards require no tooling. SAIF implementation requires security architecture capability.

**Audit / regulatory defensibility — Medium.** Model Cards are increasingly referenced by regulators as an example of model documentation best practice. SAIF is not a regulatory standard but is referenced in AI security guidance.

**Portability into internal framework — High.** All three artifacts are conceptual frameworks and templates, not platform-specific. They port directly into the enterprise template pack.

**Main blind spots:**
- No governance operating model; no board or executive accountability structure
- No intake, approval, or lifecycle gate process
- MLOps guidance is Google Cloud-biased and requires adaptation for multi-cloud or on-premises environments
- No regulatory compliance mapping

**Enterprise extraction:** Adopt Model Card and Data Card templates directly (with enterprise-specific additions for risk tier, control status, and approval record). Extract SAIF's six-element structure as the enterprise AI security architecture checklist. Use MLOps maturity levels as the enterprise monitoring maturity target.

---

## 9.2 AWS Template Stack

### Primary artifacts
- **Responsible AI Lens for AWS Well-Architected Framework** — AI architecture review
- **Amazon Bedrock Guardrails** — configurable runtime content and policy controls
- **Prompt injection and GenAI security guidance** — attack surface and control reference

### Assessment

**Governance utility — Medium.** The Responsible AI Lens provides a structured set of questions for architecture review, organized around responsible AI pillars (fairness, explainability, privacy, security, safety, controllability, governance, transparency). These map well to the enterprise governance domains. However, it is an architecture review tool, not a governance operating model.

**Control utility — High.** Bedrock Guardrails provides the clearest published example of configurable runtime AI controls: topic filters, content filters, word filters, PII detection, grounding checks, and prompt attack detection. These controls are architecture-specific to Bedrock but the control design patterns are portable. Enterprises not using Bedrock can use Guardrails as a reference for what runtime controls should exist in any GenAI system.

**Assurance utility — Medium.** The Responsible AI Lens produces an architecture review output that functions as a pre-deployment design assurance artifact. It does not replace a management system or independent validation.

**Monitoring utility — Medium.** Bedrock Guardrails produces monitoring signals (content filter triggers, grounding failure rates, PII detection events) that map directly to Deliverable E runtime signals. These are platform-specific but the signal design is portable.

**Enterprise adoption usefulness — High.** The Responsible AI Lens architecture review questions are a practical pre-deployment checklist that can be adapted for the enterprise pre-deployment gate (Tier 2 and Tier 3). Bedrock Guardrails serves as the reference design for enterprise AI runtime controls, regardless of platform.

**Implementation burden — Low (for design review); Medium (for Guardrails if not using Bedrock).**

**Portability — High (Responsible AI Lens); Medium (Bedrock Guardrails — platform-specific).** The Lens is portable as a review checklist. Guardrails patterns are portable as control design references but require reimplementation on other platforms.

**Main blind spots:**
- No governance operating model
- No lifecycle gate process
- Bedrock Guardrails is platform-specific — multi-cloud enterprises must implement equivalent controls outside Bedrock
- No board-level or committee governance structure

**Enterprise extraction:** Adapt the Responsible AI Lens architecture review questions into the enterprise pre-deployment gate checklist (particularly useful for Tier 2 and Tier 3). Use Bedrock Guardrails control categories as the reference list for enterprise runtime controls (topic filters, content filters, PII detection, grounding checks, prompt attack detection) regardless of deployment platform.

---

## 9.3 Microsoft Template Stack

### Primary artifacts
- **Responsible AI Standard v2** — enterprise AI policy and review standard
- **Transparency Notes** — system-level AI documentation
- **AI Impact Assessment template** — pre-deployment impact assessment
- **AI Red Team guidance and tooling (PyRIT)** — adversarial testing methodology
- **Responsible AI Maturity Model** — program maturity assessment

### Assessment

**Governance utility — High.** The Responsible AI Standard is the most complete published enterprise AI governance operating standard from any major provider. It defines: sensitive use categories, accountability owners, review requirements, documentation requirements, and deployment conditions. It is the closest available analog to an enterprise AI governance policy.

**Control utility — High.** The Standard defines specific control requirements for sensitive use cases (including healthcare, financial services, criminal justice, and consequential decisions). It links principles to review requirements to control obligations — the translation that most frameworks leave undone.

**Assurance utility — High.** Transparency Notes are the best published model for system-level AI documentation: they describe what the system does, how well it does it, what it is not designed to do, and how it should and should not be used. They function as the user-facing component of an enterprise system card. The AI Impact Assessment template provides a structured pre-deployment impact assessment that maps to the enterprise evidence pack. PyRIT is the most mature open-source AI red-team tooling available.

**Monitoring utility — Medium.** The Standard references monitoring requirements but does not provide a detailed signal catalog or dashboard specification.

**Enterprise adoption usefulness — High.** The Responsible AI Standard is the most directly adoptable provider document for an enterprise AI governance policy. Transparency Notes are the best template for user-facing system documentation. The AI Impact Assessment template is the best starting point for the enterprise PIA/impact assessment template.

**Implementation burden — Medium.** The Standard requires internal process design to implement. Transparency Notes require content expertise to produce well. PyRIT requires security engineering capability.

**Main blind spots:**
- Vendor-authored and Microsoft-specific in some areas; requires adaptation for platform-independence
- Monitoring signal catalog and runtime monitoring design are underdeveloped
- Does not address agentic AI controls at the depth required
- No ISO/IEC 42001 integration path

**Enterprise extraction:** Use the Responsible AI Standard as the reference policy template for the enterprise AI policy (Deliverable G). Adapt Transparency Notes as the user-facing section of the enterprise system card. Adapt the AI Impact Assessment as the enterprise impact assessment template. Adopt PyRIT in the enterprise adversarial testing program for GenAI systems.

---

## 9.4 IBM Template Stack

### Primary artifacts
- **AI Factsheets** — lifecycle AI documentation (training, evaluation, deployment)
- **OpenPages Model Risk Governance** — model risk workflow and compliance
- **watsonx.governance** — model inventory, lifecycle governance, monitoring, compliance
- **IBM Responsible AI framework** — governance principles and practices

### Assessment

**Governance utility — High.** IBM's governance approach is the most operationally structured of any major provider. AI Factsheets capture the full lifecycle of a model: from training data documentation through evaluation, deployment, monitoring, and retirement. OpenPages provides a workflow-based governance and compliance management system. watsonx.governance provides a model inventory, lifecycle tracking, risk and compliance mapping, and automated monitoring — essentially the technology layer that the enterprise AI inventory and evidence pack requirements in this framework describe.

**Control utility — High.** The IBM governance pattern — model inventory + lifecycle workflow + risk/compliance mapping + monitoring dashboard — is the most complete published operational reference for regulated enterprises. The pattern is portable regardless of whether the enterprise uses IBM products.

**Assurance utility — High.** AI Factsheets produce structured evidence artifacts covering the full model lifecycle. OpenPages produces audit trails for governance decisions. watsonx.governance produces monitoring evidence. This combination provides the closest published approximation of the enterprise evidence pack defined in Section 7.3.

**Monitoring utility — High.** watsonx.governance includes drift monitoring, fairness monitoring, quality monitoring, and explainability monitoring — corresponding directly to the Deliverable E signals MON-10 through MON-12 and MON-18.

**Enterprise adoption usefulness — High for regulated industries.** IBM's patterns are particularly relevant for financial services, healthcare, and insurance enterprises, where model risk management, audit trails, and regulatory reporting are central requirements.

**Implementation burden — Medium to High** if using IBM products; **Low to Medium** if extracting patterns for platform-independent implementation.

**Main blind spots:**
- Governance patterns are partly obscured by product marketing; patterns must be extracted from the product narrative
- Less detail on agentic AI governance and prompt governance
- Less detail on vendor/supply chain controls

**Enterprise extraction:** Use AI Factsheets as the reference template for the enterprise model card (adapted without IBM tooling). Use the IBM model inventory pattern as the reference design for the enterprise AI system inventory. Use watsonx.governance's monitoring capability categories (drift, fairness, quality, explainability) as the reference set for enterprise monitoring signal design.

---

## 9.5 NVIDIA Template Stack

### Primary artifacts
- **NeMo Guardrails** — open-source guardrail framework for LLM applications
- **NeMo evaluation and observability tooling** — model and system evaluation
- **Trustworthy AI and agent safety materials** — agentic AI safety guidance
- **Model safety and red-team guidance**

### Assessment

**Governance utility — Low.** NVIDIA provides no governance operating model. NeMo Guardrails is a technical enforcement framework, not a governance framework.

**Control utility — High.** NeMo Guardrails is the most mature open-source technical control library for LLM applications. It supports: topical rails (keeping conversations on topic), safety rails (preventing harmful outputs), dialog rails (controlling conversation flow), and fact-checking rails. These correspond directly to Domain 4 and Domain 7 controls, and to the GEN-01, OUT-01, and OUT-02 controls in the master control matrix.

**Assurance utility — Medium.** NeMo evaluation tooling provides structured model evaluation and output quality assessment. The outputs function as pre-deployment testing evidence for the enterprise evidence pack.

**Monitoring utility — High (agentic and RAG).** NVIDIA's tooling is the strongest available for agentic AI safety monitoring: action audit logging, output monitoring, and evaluation in RAG pipelines. This maps directly to Domain 10 and the AGT-07 audit log requirement.

**Enterprise adoption usefulness — High for GenAI and agentic systems.** For enterprises deploying Chat-First, RAG, or Agentic archetypes, NeMo Guardrails is a strong candidate for the enterprise runtime control enforcement layer (particularly for open-weight self-hosted models where no vendor-provided safety layer exists).

**Implementation burden — Medium.** Open-source; requires engineering capability to implement and configure.

**Main blind spots:**
- No governance operating model; no board, committee, or lifecycle governance
- Primarily technical enforcement; does not address evidence documentation, audit trails, or policy mapping
- Documentation and policy templates absent

**Enterprise extraction:** Adopt NeMo Guardrails as the enterprise technical control library reference for GenAI runtime controls (mandatory for Open-Weight Self-Hosted archetype; recommended for Chat-First and RAG archetypes). Use the guardrail category structure (topical, safety, dialog, fact-checking) as the reference design for enterprise output controls. Use NVIDIA evaluation tooling outputs as pre-deployment testing evidence artifacts.

---

## 9.6 OpenAI Enterprise Template Stack

### Primary artifacts
- **OpenAI Enterprise privacy and security commitments** — data handling controls
- **API data processing and retention controls** — enterprise API governance
- **Usage policies** — policy and prohibited use reference
- **Enterprise admin controls** — SSO, access management, audit logs
- **System prompt confidentiality** — prompt governance at API level

### Assessment

**Governance utility — Medium.** OpenAI's enterprise commitments address the vendor-side governance question: what does the provider do with enterprise data? This is essential input to the enterprise vendor assessment (Domain 9, VND-01 through VND-07). It is not a governance operating model.

**Control utility — Medium.** OpenAI provides strong vendor-side controls: no training on enterprise API data (with standard API); data retention controls (enterprise can configure zero-day retention); admin console for access management; SSO integration; audit logs. These are vendor controls that reduce, but do not eliminate, the enterprise's governance obligations.

**Assurance utility — Low to Medium.** OpenAI publishes a System Card for major model releases (GPT-4, o1 series) that documents safety evaluations and red-team findings. These are useful inputs to the enterprise vendor assessment and to understanding the base model's safety properties. They do not replace enterprise validation.

**Monitoring utility — Low.** OpenAI does not provide enterprise monitoring dashboards or runtime signal feeds. Enterprise monitoring must be implemented at the application layer.

**Enterprise adoption usefulness — High for vendor assessment.** The OpenAI enterprise privacy and security documentation is the primary input to the enterprise vendor due diligence template for OpenAI as a provider. The admin controls (SSO, audit logs, data retention configuration) are the enterprise-configurable controls that should be verified and configured before any OpenAI-based system is deployed.

**Main blind spots:**
- No enterprise governance operating model templates
- No lifecycle governance or evidence pack templates
- Runtime monitoring must be entirely enterprise-implemented
- System Cards are model-level, not system-level; enterprise system governance remains entirely the enterprise's responsibility

**Enterprise extraction:** Translate OpenAI enterprise documentation into: (a) vendor due diligence record template items (data handling, retention, security posture, audit rights); (b) pre-deployment configuration checklist (zero-day retention enabled; SSO configured; audit logging active; usage policies confirmed; system prompt confidentiality requirement understood). Do not use OpenAI's System Card as a substitute for enterprise system card or validation.

---

## 9.7 Anthropic / Claude Template Stack

### Primary artifacts
- **Responsible Scaling Policy (RSP)** — capability risk governance and safety levels
- **Claude's Constitution / model spec** — model behavior specification
- **Tool use and agent use documentation** — agentic architecture guidance
- **Enterprise and API safety documentation** — deployment governance

### Assessment

**Governance utility — Medium.** The Responsible Scaling Policy is a governance innovation: it defines AI Safety Levels (ASL-2, ASL-3, ASL-4) with capability thresholds that trigger enhanced safety obligations. This is a model for capability-risk-based governance escalation — analogous to the enterprise risk-tiering model in Deliverable B, applied at the model-capability level. For enterprise AI governance, the RSP is a useful reference for designing escalation thresholds tied to AI capability rather than only use-case context.

**Control utility — Medium.** Anthropic's tool use and agent documentation provides the clearest published guidance on agentic control design: minimal footprint principle (agents should request only necessary permissions, prefer reversible actions, confirm with users when uncertain), which maps directly to Domain 10 controls AGT-01, AGT-02, and AGT-03. The model specification (Constitution) provides the reference for understanding what behaviors Claude is and is not designed to perform — essential for enterprise system prompt design and scope enforcement.

**Assurance utility — Medium.** Anthropic publishes safety evaluations and third-party audit results in its RSP commitments. These are inputs to the enterprise vendor assessment. The RSP's commitment to independent evaluation at capability thresholds is a model for enterprise model capability review requirements.

**Monitoring utility — Low.** Anthropic does not provide enterprise monitoring tooling. Enterprise monitoring must be implemented at the application layer.

**Enterprise adoption usefulness — High for agentic AI governance.** The RSP's ASL framework is the best published reference for capability-level risk escalation. The minimal footprint principle from the tool-use documentation is the most concise published statement of the agentic action governance principle underlying Domain 10. For enterprises building agentic systems on Claude, the model specification provides the behavioral reference that informs scope enforcement design.

**Main blind spots:**
- No enterprise governance operating model templates
- No lifecycle gate, evidence pack, or board reporting templates
- Safety Level framework is provider-internal; enterprise governance cannot rely on RSP compliance as a substitute for enterprise controls

**Enterprise extraction:** Translate the RSP's ASL framework into enterprise capability risk review criteria: if an AI system exhibits capabilities that would trigger ASL-3 evaluation criteria in the RSP, the enterprise should treat the system as requiring enhanced review regardless of tier. Extract the minimal footprint principle as the enterprise statement of agentic action governance design philosophy (Domain 10). Use Claude's tool-use documentation as the reference for enterprise tool authorization scope design (TOL-01, TOL-02).

---

## Deliverable F — Corporate Template Stack Comparative Matrix

| Dimension | Google | AWS | Microsoft | IBM | NVIDIA | OpenAI | Anthropic |
|---|---|---|---|---|---|---|---|
| **Primary artifacts** | SAIF, Model Cards, Data Cards, MLOps | Responsible AI Lens, Bedrock Guardrails | RAI Standard, Transparency Notes, AI Impact Assessment, PyRIT | AI Factsheets, OpenPages, watsonx.governance | NeMo Guardrails, evaluation tooling | Enterprise privacy/security, admin controls | RSP, model spec, tool-use guidance |
| **Governance layer addressed** | Architecture + Execution | Architecture + Execution | Governance + Execution | Governance + Execution | Execution | Vendor controls | Strategy + Execution |
| **Best use in enterprise adoption** | Model and data documentation; AI security architecture | Architecture review checklist; runtime control reference | AI policy template; system documentation; red-team | Model inventory; lifecycle workflow; regulated-industry depth | GenAI/agentic runtime controls; RAG evaluation | Vendor due diligence; provider control configuration | Agentic control design; capability risk escalation |
| **Best use in regulated environments** | Model Cards for model documentation evidence | Responsible AI Lens for pre-deployment review | AI Impact Assessment for impact evidence; transparency notes for disclosure | Model risk workflow; compliance mapping; audit trail | Agentic safety enforcement | Vendor assessment record | Agentic governance design reference |
| **Control strength** | High (SAIF security controls) | High (Guardrails runtime) | High (Standard + PyRIT) | High (lifecycle + monitoring) | High (guardrail enforcement) | Medium (vendor-side controls) | Medium (agentic design principles) |
| **Assurance strength** | Medium (Model/Data Cards as evidence) | Medium (Lens as design assurance) | High (Impact Assessment + Transparency Notes) | High (Factsheets + audit trail) | Medium (evaluation outputs) | Low | Low |
| **Monitoring strength** | High (MLOps maturity) | Medium (Guardrails signals) | Medium | High (watsonx.governance signals) | High (agentic/RAG monitoring) | Low | Low |
| **Portability into internal framework** | High | High (Lens); Medium (Guardrails) | High | High (patterns); Medium (products) | High (NeMo is open-source) | High (as vendor assessment input) | High |
| **Main implementation burden** | Model/Data Card content production | Guardrails: platform-specific if not on Bedrock | Standard requires internal process design | Pattern extraction from product narrative | Security engineering for NeMo | Configuration management | Agentic system design discipline |
| **Key blind spots** | No governance operating model | No governance operating model | Limited agentic depth; no ISO 42001 path | Agentic governance underdeveloped | No governance operating model or evidence templates | No enterprise governance templates | No governance operating model or lifecycle templates |

---

## Deliverable G — Enterprise Synthesis: Consolidated Internal Standard Pack

This is the single authoritative template set for this framework. All templates below are consolidated here. No duplicate template set exists elsewhere in this document.

The enterprise should implement these templates in its chosen governance tooling (SharePoint, Confluence, GRC platform, or equivalent). The template structure below specifies required fields; format is at enterprise discretion.

---

### G.1 — Enterprise AI Policy Template

**Document purpose:** The enterprise AI policy is the top-level governing document. It states the enterprise's intent, principles, scope, accountabilities, and boundaries for AI use.

**Required sections:**
1. Policy statement and purpose
2. Scope (in and out of scope)
3. AI principles (translated into control obligations per Section 4.2)
4. Prohibited uses (Tier 0 list, reviewed annually)
5. Risk appetite statement
6. Governance model reference (links to governance operating model)
7. Key accountabilities (Board, Executive, AI Gov Office, Business Owner)
8. Review and approval cadence
9. Related policies (Data Protection, Information Security, Model Risk)

**Owner:** AI Governance Office
**Approval:** Executive AI Council (ratified by Board Risk Committee)
**Review cadence:** Annual; at material regulatory change

---

### G.2 — AI Use-Case Intake Form

**Required fields:**
- Use case name and description
- Business Owner (named individual)
- System Owner (named individual)
- Model Owner (named individual, if applicable)
- Business justification and success metrics
- AI system archetype (select from 10 archetypes)
- Data inputs: types, classification, source, jurisdiction
- Model or AI service: name, version or API endpoint, vendor or open-weight
- Output type and destination (who or what receives the output)
- User population (internal / external / both; approximate volume)
- Geographic deployment (jurisdictions affected)
- Self-assessed risk tier (with rationale)
- Known regulatory obligations (EU AI Act, GDPR, SR 11-7, HIPAA, etc.)
- Proposed go-live date
- Confirmation of ownership acceptance (Business Owner signature)

---

### G.3 — Risk-Tiering Template

**Purpose:** Documents the risk tier classification for each AI use case, with rationale.

**Required fields:**
- Use case name and intake reference
- Archetype classification
- Risk tier assigned (Tier 0–4)
- Tier rationale: which criteria triggered this tier (consequence to individuals, regulatory domain, output autonomy, external exposure, personal data volume)
- Tier assigned by (name and role)
- Date of classification
- AI Governance Office confirmation
- Next review date (at material change or annual, whichever is sooner)

---

### G.4 — System Card Template

**Adapted from:** Microsoft Transparency Notes structure; Google Model Card concept applied at system level.

**Required sections:**

*Header:* System name; version; date; archetype; risk tier; Business Owner; System Owner; Model Owner; deployment status.

*Purpose and intended use:* What the system is designed to do; intended users; intended use contexts; out-of-scope uses.

*AI model(s) used:* Model name(s) and version(s); source (vendor API / open-weight / internally trained); link to model card.

*Data inputs:* Data types; classification; sources; jurisdictions; any personal data processed.

*Retrieval corpus (RAG only):* Corpus name; data types; classification; freshness controls; access controls.

*Tools and actions (agentic systems):* Authorized tool list; action scope limits; reversibility classification; HITL thresholds.

*Key controls in place:* Summary of primary controls by domain (prompt governance, output controls, access controls, monitoring).

*Known limitations:* Performance limitations; known failure modes; populations or contexts for which the system has not been validated.

*Fairness and bias:* Fairness metrics defined; assessment results; monitoring approach (for decision-support systems).

*Risk tier and governance:* Tier; approval record reference; evidence pack location; next review date.

*Change history:* Version history; material changes logged.

---

### G.5 — Model Card Template

**Adapted from:** Google Model Card; IBM AI Factsheet; Anthropic model documentation.

**Required sections:**

*Model details:* Model name; version; type (LLM / classifier / embedding / other); architecture (if known); training date or cut-off; source (vendor / open-weight / internally trained).

*Intended use:* Primary intended use cases; out-of-scope uses.

*Training data:* Data sources; data types; known limitations or biases in training data; consent basis where applicable; what is unknown about training data (particularly for open-weight models).

*Evaluation:* Performance metrics and results on evaluation datasets; out-of-sample and out-of-time performance where applicable; fairness evaluation results.

*Known limitations:* Known failure modes; edge cases; populations for which the model has not been validated.

*Ethical considerations:* Potential harms; mitigation measures applied.

*Versioning and lineage:* Version history; predecessor models; fine-tuning history.

*Owner and approval:* Model Owner; approval record reference.

---

### G.6 — Data Documentation Template

**Adapted from:** Google Data Cards Playbook; IBM AI Factsheet (data section).

**Required sections:**

*Dataset name and description*
*Data source(s) and collection method*
*Data types and classification*
*Volume and date range*
*Jurisdiction(s) of data subjects*
*Known quality issues or gaps*
*Consent and legal basis (where personal data)*
*Access controls*
*Retention and deletion schedule*
*Use restrictions*
*Version and update history*

---

### G.7 — Prompt / Retrieval / Tool Governance Template

**Purpose:** Documents the governed configuration of system prompts, retrieval settings, and tool authorizations for a given AI system.

**System prompt section:**
- Current system prompt version and hash
- Approval record for current version
- Change history (version, change description, approver, date)
- Access control list (who may modify in production)

**Retrieval section (RAG systems):**
- Corpus name and version
- Data classification
- Freshness standard and last refresh date
- Access controls
- Content review history

**Tool authorization section (agentic systems):**
- Authorized tool list (name, scope, reversibility classification, HITL threshold)
- Unauthorized tool block confirmation
- Tool audit log location

---

### G.8 — Control Matrix (per system)

Each Tier 1 and Tier 2 system maintains a system-level control matrix that maps the applicable controls from the master control matrix (Part V) to the specific system, documents implementation status, and records the evidence artifact for each control.

**Columns:** Control ID | Control description | Applicability to this system | Implementation status | Evidence artifact location | Control owner | Last tested | Next review

---

### G.9 — Evidence Pack Index

**Purpose:** The evidence pack index for each Tier 1 and Tier 2 system lists all required evidence items, their location, currency, and completeness status.

**Required items per Section 7.3:** System card; model card; intake and classification record; PIA; fairness assessment (Tier 1 decision systems); validation report (Tier 1); red-team report; security assessment; pre-deployment approval record; monitoring dashboard (historical); incident records; change records; audit log; vendor assessment records; exception records.

**Columns:** Evidence item | Required (Y/N for this system) | Location | Version / date | Complete (Y/N) | Owner

---

### G.10 — Monitoring Dashboard Specification

**Purpose:** Defines the runtime monitoring dashboard for each AI system. Specifies which signals from Deliverable E are active, their threshold values, alerting configuration, and review cadence.

**Required fields:**
- System name and tier
- Active monitoring signals (from Deliverable E — MON-01 through MON-18)
- Threshold value for each active signal
- Alert recipient(s) for each threshold breach
- Review cadence (who reviews the dashboard, how often)
- Dashboard tool / location

---

### G.11 — AI Incident Report Template

**Required fields:**
- Incident ID and date
- System name and tier
- Incident category (from Section 7.2 taxonomy)
- Severity assigned (S1–S4)
- Incident description (what happened, when detected, how detected)
- Immediate actions taken (containment)
- Root-cause analysis (for S1 and S2: mandatory; for S3 and S4: required or recommended)
- Impact assessment (users affected, data affected, regulatory notification required)
- Corrective actions (planned and completed)
- Verification of corrective action effectiveness
- Regulatory notification record (if applicable)
- Approval of closure (AI Risk Committee for S1/S2; AI Gov Office for S3)

---

### G.12 — Board / Regulator Reporting Template

**Purpose:** Provides the quarterly board AI risk dashboard and the regulatory reporting pack.

**Board AI risk dashboard — required items:**
- AI system inventory: total systems by tier and status
- New use cases approved in period (by tier)
- Use cases rejected or prohibited in period
- Active exceptions (count; material details)
- KRI status (traffic-light; breaches and response)
- Material incidents in period (summary; status)
- Governance review completion rate
- Open audit findings (count; age)
- Regulatory developments material to enterprise AI

**Regulatory reporting pack — additional items (on demand or at regulatory request):**
- AI system inventory (full detail for relevant systems)
- Evidence pack for requested system(s)
- Validation reports for requested model(s)
- Incident reports for specified period
- Governance framework document (this document)
- Regulatory mapping (Section 4.5)

---

### G.13 — Vendor Due Diligence Template

**Required fields:**
- Vendor name and AI product / service
- Data handling: what data is sent to the vendor; vendor's data use restrictions; confirmation of no training on enterprise data
- Data retention: vendor retention period; enterprise control over retention; zero-retention option availability
- Model transparency: what model is used; does vendor disclose model updates; model change notification SLA
- Security posture: relevant certifications (SOC 2, ISO 27001, etc.); penetration test frequency; vulnerability disclosure program
- Privacy compliance: applicable adequacy or transfer mechanism; DPA executed; GDPR/CCPA compliance confirmation
- Audit rights: does the contract include enterprise right to audit; scope of audit right
- Incident notification: vendor obligation to notify enterprise of AI-related incidents affecting enterprise data; notification SLA
- SLA and uptime: service level commitments; consequences of breach
- Model system card or safety documentation available: Y/N; location
- Overall vendor AI risk rating: Low / Medium / High (with rationale)
- Assessment completed by; date; next review date

---

*End of Part IX.*

---

# Part X — Final Synthesis

## Deliverable H — Adoption-Acceleration Operating Model

The governance operating model accelerates AI adoption through seven structural mechanisms:

### Mechanism 1 — Standard Templates (Reuse Over Recreation)

**Fact:** The most common governance delay is not committee time — it is the time to produce governance documentation from scratch for each new use case.

**Design:** The enterprise template pack (Deliverable G) provides 13 pre-built templates. Business Owners and System Owners select and complete the appropriate template for their tier rather than designing documentation from scratch. Tier 3 and Tier 4 use lightweight versions. Tier 1 and Tier 2 complete full versions with AI Governance Office support.

**Acceleration mechanism:** Eliminates documentation design time. Reduces governance documentation effort by approximately 60-70% compared with ad hoc documentation.

---

### Mechanism 2 — Pre-Approved Controls and Architecture Patterns

**Fact:** The most common technical governance delay is the security and architecture review of systems that use identical underlying patterns.

**Design:** The enterprise maintains a register of pre-approved architecture patterns (Section 8.6, PAT-01 through PAT-05). Systems using pre-approved patterns skip the architecture design review gate; they confirm pattern selection and complete any system-specific additions.

**Acceleration mechanism:** Eliminates architecture review for standard patterns. Tier 2 systems on pre-approved patterns can reach the pre-deployment gate in approximately half the calendar time of bespoke architecture review.

---

### Mechanism 3 — Risk-Based Review Intensity

**Fact:** Applying Tier 1 review intensity to Tier 3 and Tier 4 systems is the single largest source of avoidable governance delay.

**Design:** The five-tier risk model (Deliverable B) explicitly differentiates review intensity. Tier 4 systems require only Business Owner self-certification. Tier 3 requires a lightweight AI Gov Office review. Tier 1 receives full committee review. The fast-lane model (Section 8.3) operationalizes this for the most common low-risk patterns.

**Acceleration mechanism:** Tier 3 and Tier 4 systems (which typically represent 60-70% of enterprise AI use cases) move through governance in days, not weeks.

---

### Mechanism 4 — Evidence Automation

**Fact:** Manual evidence assembly for audit and regulatory purposes is a significant post-deployment burden that creates retrospective compliance risk.

**Design:** Monitoring dashboards, audit logs, and system cards are designed as living documents produced automatically by normal operations. The evidence pack index (Deliverable G.9) is maintained continuously, not assembled on demand. Automated monitoring signals (Deliverable E) produce runtime evidence automatically.

**Acceleration mechanism:** Eliminates pre-audit evidence assembly scrambles. Reduces audit preparation time from weeks to hours. Enables real-time regulatory readiness.

---

### Mechanism 5 — Fast-Lane Approvals

**Design:** Pre-approved use-case categories (Section 8.3) allow Tier 3 systems within defined parameters to proceed with a 5-business-day silent approval from the AI Governance Office. No committee meeting required.

**Acceleration mechanism:** Reduces approval cycle for pre-approved categories from 2-6 weeks to 5-10 business days.

---

### Mechanism 6 — Centralized Support (Governance as a Service)

**Fact:** Federated governance fails when business units lack governance expertise. Central review queues back up when business units submit incomplete or incorrect documentation.

**Design:** The AI Governance Office operates as a governance service function, not a gatekeeping function. It provides: pre-intake advisory sessions for Tier 1 use cases; template completion support; training for Business Owners and System Owners; a shared services model for PIA initiation, vendor assessment coordination, and monitoring dashboard setup.

**Acceleration mechanism:** Reduces first-submission rejection rates. Reduces total time in governance process by supporting proactive preparation.

---

### Mechanism 7 — Governance Maturity Progression

**Design:** The governance model is tiered by maturity: enterprises begin with the MVGM (Section 8.1) and progress to the advanced model (Section 8.2) as the AI program scales. Governance tooling investment is staged to match program maturity, avoiding the failure mode of over-investing in governance infrastructure before the program is large enough to need it.

**Acceleration mechanism:** Prevents early-stage governance paralysis caused by building enterprise-scale governance before enterprise-scale adoption exists.

---

## 10.1 What a Good Enterprise AI Governance Framework Must Contain

**Fact:** Most published AI governance frameworks — voluntary standards, industry guidance, and vendor responsible AI programs — are incomplete as enterprise operating systems. Individually, they address one to two of the four layers (strategy, governance, architecture, execution).

A complete enterprise AI governance framework must contain all of the following. Their absence is not a simplification; it is a governance gap.

| Required element | Why it matters | Where in this framework |
|---|---|---|
| Explicit risk tiering with binding lifecycle consequences | Without tiers, governance is uniform; uniform governance slows adoption without improving real control | Deliverable B; Deliverable D |
| Named accountability for every system | Shared accountability is unaccountability; incidents reveal this gap | Part VI RACI; Section 4.2 |
| Control matrix with evidence requirements | Principles without controls and controls without evidence are theater | Deliverable C; Part V |
| Lifecycle governance map wired to risk tier | Stage-by-stage intensity must differ by tier or tiering is classification without treatment | Deliverable D |
| Runtime monitoring signal catalog | Controls without monitoring signals are unverifiable; incidents are undetectable | Deliverable E |
| Evidence pack by design (not by assembly) | Retrospective evidence assembly creates compliance risk and audit delays | Section 7.3; Deliverable G.9 |
| Architecture-specific control differentiation | RAG, agentic, and open-weight systems have materially different risks | Part V Section 5.3 |
| Agentic action governance as a distinct domain | Agentic systems are the highest-risk emerging architecture; they require specific control design | Domain 10 (AGT-01–AGT-09) |
| Model supply chain and provenance controls | Open-weight and third-party models introduce supply chain risks invisible to model evaluation | Domain 11 (MSC-01–MSC-06) |
| Cross-border jurisdiction controls | Inference routing and output jurisdiction are legally material; they are absent from most frameworks | Domain 12 (CBJ-01–CBJ-04) |
| Prompt governance as a governed artifact | The system prompt is the primary behavioral governor; it must be versioned, access-controlled, and audited | Domain 4 (PRM-01–PRM-08) |
| Vendor due diligence framework | Vendor AI risk is enterprise AI risk; undisclosed model updates, data handling failures, and security posture gaps flow directly to enterprise risk | Domain 9; Deliverable G.13 |
| Adoption acceleration mechanisms | Governance that impedes all adoption equally is not good governance; speed for low-risk is a design requirement | Part VIII |
| Sector-specific overlays | Regulated enterprises face obligations that the base framework does not address; overlays are required, not optional | Part VIII Section 8.9 |

---

## 10.2 What Weak Corporate AI Governance Systematically Misses

**Inference:** These are the gaps most commonly present in enterprise AI governance programs that appear mature on paper but fail under audit or incident pressure.

| Gap | Manifestation | Consequence |
|---|---|---|
| **Runtime monitoring not designed in** | Monitoring discussed in governance documents; no monitoring implemented at deployment | Control failures accumulate undetected; incidents are discovered by users, not by governance |
| **System governance absent; model governance present** | Model cards exist; system prompt is unversioned and accessible to anyone with admin credentials | The primary behavioral control (system prompt) is ungoverned; any change to it bypasses the governance record |
| **Risk tiering without lifecycle wiring** | Five tiers defined; all systems go through the same approval process | Tiering produces classification with no treatment differentiation; all overhead, no risk reduction |
| **Evidence assembled retrospectively** | Audit requested; 3-week internal scramble to produce evidence | Audit reveals gaps; regulatory defensibility compromised; key evidence cannot be reconstructed |
| **Agentic systems governed as chat systems** | Agentic multi-agent systems with tool access governed under the Chat-First control set | No action scope limits; no reversibility controls; no inter-agent trust isolation; first autonomous action incident reveals the gap |
| **Vendor AI treated as neutral infrastructure** | Third-party AI APIs used in production systems with no vendor assessment | Model update by vendor changes system behavior undetected; data handling terms not assessed; vendor security incident impacts enterprise system |
| **HITL designed as a gate, not a sustained control** | Human review required before deployment; not monitored in production | HITL queue grows; reviewers approve without reviewing; HITL becomes theater within 3 months of deployment |
| **Governance theater for low-risk; under-governance for high-risk** | Same committee review for code assistant and credit decisioning engine | Developer routes around governance for productivity tools; credit engine receives same superficial review and passes |
| **No prohibited use operationalization** | Prohibited use list exists in policy; no intake-stage enforcement | Prohibited use cases are submitted, not automatically rejected; some proceed through governance due to committee oversight gap |
| **Cross-border and jurisdiction risk ignored** | AI system infers in US data center on EU resident data; no adequacy mechanism documented | GDPR violation; regulatory action; legal exposure when individual exercises data subject rights |

---

## 10.3 Final Recommended Enterprise Framework

**Recommendation:** The enterprise should implement this framework as the composite operating model described below. This is the most defensible, adoption-accelerating, and audit-ready enterprise AI governance design available as of 2026.

### The Recommended Composite Stack

```
STRATEGIC LAYER
├── ISO/IEC 38507  .............. Board AI governance mandate
├── EU AI Act  .................. Regulatory classification and compliance overlay
└── Enterprise AI Policy  ....... Deliverable G.1 (enterprise-specific)

GOVERNANCE AND CONTROLS LAYER
├── NIST AI RMF 1.0  ............ Control structure backbone (Govern/Map/Measure/Manage)
├── ISO/IEC 42001  .............. Management system shell + certification path
├── ISO/IEC 23894  .............. AI risk management methodology
├── COBIT  ...................... Enterprise IT governance and assurance integration
└── COSO ERM  ................... Board and internal control integration

ARCHITECTURE LAYER
├── TOGAF  ...................... Enterprise capability and reference architecture
├── Google SAIF  ................ AI security architecture and threat controls
└── SABSA  ...................... Business-driven security architecture (where required)

EXECUTION LAYER
├── CRISP-ML(Q)  ................ Lifecycle phase gates + QA
├── Google MLOps maturity  ...... Production ML pipeline discipline
├── NIST AI RMF Playbook  ....... Control activities per lifecycle stage
└── NIST GenAI Profile  ......... GenAI-specific risk and control extension

TEMPLATE AND TOOLING LAYER
├── Google Model Cards + Data Cards  .... Documentation templates
├── Microsoft RAI Standard  ............. Policy template reference
├── Microsoft Transparency Notes  ....... System documentation reference
├── IBM watsonx.governance patterns  .... Model inventory + monitoring reference
├── NVIDIA NeMo Guardrails  ............. GenAI/agentic runtime control library
├── Anthropic RSP + minimal footprint   . Agentic governance design principles
└── Deliverable G (13 templates)  ....... Enterprise consolidated template pack
```

---

### What the Composite Gives the Enterprise

| Enterprise need | Provided by |
|---|---|
| Control backbone | NIST AI RMF |
| Management system and certification path | ISO/IEC 42001 |
| AI risk methodology | ISO/IEC 23894 |
| Board governance mandate | ISO/IEC 38507 |
| Enterprise IT governance and audit integration | COBIT |
| Board and internal control integration | COSO ERM |
| Architecture design authority | TOGAF |
| AI security architecture | Google SAIF |
| Lifecycle discipline | CRISP-ML(Q) + MLOps maturity |
| GenAI-specific controls | NIST GenAI Profile |
| Model documentation | Google Model Cards |
| Policy template | Microsoft RAI Standard |
| System documentation | Microsoft Transparency Notes |
| Model inventory and monitoring patterns | IBM watsonx.governance |
| Runtime control enforcement | NVIDIA NeMo Guardrails |
| Agentic design principles | Anthropic RSP / tool-use guidance |
| Full enterprise template pack | Deliverable G |

---

## 10.4 Executive Action Checklist

The following actions are sequenced for enterprise program launch. Items marked **Critical** must be completed before any Tier 1 or Tier 2 AI system is deployed in production.

### Immediate (0–30 days)

- [ ] **[Critical]** Appoint AI Governance Office lead and define its reporting line
- [ ] **[Critical]** Adopt enterprise AI policy (Deliverable G.1) and obtain Executive AI Council approval
- [ ] **[Critical]** Establish and publish the prohibited use list (Tier 0)
- [ ] **[Critical]** Stand up AI system inventory (minimum: spreadsheet with required fields)
- [ ] **[Critical]** Implement intake process for all new AI use cases
- [ ] Conduct inventory sweep of all AI systems currently in production; classify by tier
- [ ] Identify all Tier 1 systems currently in production without complete governance documentation; initiate remediation
- [ ] Identify the operating model (centralized / federated / hybrid) appropriate for current program scale

### Short-term (30–90 days)

- [ ] **[Critical]** Stand up AI Risk Committee with defined membership, decision rights, and cadence
- [ ] **[Critical]** Implement Deliverable B risk-tiering model as the operative classification standard
- [ ] **[Critical]** Implement Deliverable D lifecycle governance map for all new use cases proceeding through the lifecycle
- [ ] Complete system cards for all Tier 1 and Tier 2 systems currently in production
- [ ] Implement runtime monitoring (at minimum MON-01 through MON-08) for all Tier 1 and Tier 2 systems
- [ ] Complete vendor AI due diligence (Deliverable G.13) for top 5 AI providers by dependency
- [ ] Implement prompt versioning and access control (PRM-01 through PRM-03) for all Chat-First and RAG systems
- [ ] Brief the Board / Risk Committee on the framework, the risk appetite, and the current AI estate

### Medium-term (90–180 days)

- [ ] Implement full Deliverable E signal catalog for all Tier 1 systems
- [ ] Implement the fast-lane approval process for Tier 3 and Tier 4 use cases
- [ ] Implement pre-approved architecture patterns (Section 8.6)
- [ ] Complete workforce enablement program (Section 8.8) for Business Owners and System Owners
- [ ] Complete Domain 10 (agentic controls) for all agentic systems in production or in the pipeline
- [ ] Complete Domain 11 (model supply chain) for all open-weight and third-party models in production
- [ ] Conduct first internal audit of framework implementation against Deliverable D and Deliverable E
- [ ] Initiate ISO/IEC 42001 gap assessment if certification pathway is a governance objective
- [ ] Conduct governance misallocation audit (Section 8.5) against current AI estate

### Ongoing

- [ ] Monthly AI Risk Committee meetings
- [ ] Quarterly Board AI risk dashboard
- [ ] Annual governance framework review
- [ ] Annual internal audit of AI governance controls
- [ ] Annual prohibited use list review
- [ ] Annual vendor AI governance review for top dependencies
- [ ] Annual workforce enablement refresh
- [ ] Continuous monitoring against Deliverable E signal catalog
- [ ] Continuous maintenance of AI system inventory (new systems registered; retired systems flagged)

---

## 10.5 Framework Validation Checklist

Before this framework is published and adopted, the following validation questions must be answered affirmatively:

- [x] Is this a corporate governance and control framework, not an ethics essay? **Yes.**
- [x] Does it accelerate AI adoption for low-risk systems while preserving control for high-risk systems? **Yes — fast-lane, pre-approved patterns, and risk-tiered review.**
- [x] Does it distinguish governance, controls, assurance, and monitoring as separate disciplines? **Yes — Section 2.3.**
- [x] Does it differentiate all 10 archetypes including agentic single-agent, multi-agent, and open-weight? **Yes — Part II and Part V Section 5.3.**
- [x] Does it provide actual operating mechanisms, not just principles? **Yes — RACI, gates, signal catalog, templates.**
- [x] Are templates consolidated in a single location? **Yes — Deliverable G (G.1–G.13).**
- [x] Does it include all 7 providers (Google, AWS, Microsoft, IBM, NVIDIA, OpenAI, Anthropic)? **Yes — Part IX.**
- [x] Is OECD restricted to a single board-level footnote? **Yes — footnote 1 in Part IV only.**
- [x] Is it board-usable, audit-usable, and regulator-defensible? **Yes — governance bodies, evidence pack, board reporting template.**
- [x] Is risk tiering wired to lifecycle gate intensity? **Yes — Deliverable B explicitly wired to Deliverable D at every stage.**
- [x] Does it include a governance misallocation diagnostic? **Yes — Section 8.5.**
- [x] Does it include sector overlays for financial services, healthcare, and safety-critical infrastructure? **Yes — Section 8.9.**
- [x] Are agentic action governance, model supply chain, and cross-border jurisdiction distinct control domains? **Yes — Domains 10, 11, and 12.**
- [x] Does it treat prompt governance as a governed artifact with versioning, access control, and audit trail? **Yes — Domain 4, PRM-01 through PRM-08.**

---

*End of Framework.*

---

## Document Control

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | April 2026 | Enterprise AI Governance Office | Initial framework |

**Next review date:** April 2027, or at material regulatory change (EU AI Act full applicability; significant supervisory guidance), whichever is earlier.

**Distribution:** Board Risk and Audit Committee; Executive AI Council; AI Governance Office; AI Risk Committee; Business Owners (AI systems); Chief Risk Officer; CISO; Chief Privacy Officer; General Counsel; Internal Audit.

---

*© Enterprise. Internal governance document. Not for external distribution without authorization.*

---

# Part XI — Control Implementation Architecture

## Review Finding Addressed

> *"You define controls, monitoring, and evidence — but you don't define where and how these controls are implemented in the engineering stack."*

This part resolves that gap. It specifies the control plane, data plane, and enforcement points for every control domain in Part V. Without this, the framework is well-specified at design time but weakly implemented at runtime.

---

## 11.1 Control Plane vs Data Plane

Enterprise AI controls operate across two planes:

| Plane | Definition | Examples |
|---|---|---|
| **Control Plane** | Configuration, policy, and governance state — what the system is authorized to do, under what conditions, with what evidence | System prompt registry; tool authorization register; risk tier record; model version registry; user access control matrix |
| **Data Plane** | The runtime flow of prompts, tokens, retrieved content, tool calls, and outputs — where controls are enforced in real time | Prompt injection detector; output safety classifier; action scope enforcer; audit log writer; drift monitor |

**Key principle:** Control plane settings determine what is allowed. Data plane enforcement ensures it. A control that exists only in the control plane but has no data plane enforcement point is a policy claim, not a control.

---

## 11.2 Enforcement Point Architecture

The following diagram describes the canonical enforcement point architecture for an enterprise AI system. All controls in Part V map to one or more of these enforcement points.

```
┌─────────────────────────────────────────────────────────────────┐
│                     ENTERPRISE AI SYSTEM                        │
│                                                                 │
│  User / Application                                             │
│       │                                                         │
│       ▼                                                         │
│  ┌──────────────────────────────────────┐                       │
│  │  EP-1: API Gateway / Entry Point     │ ← IAM, rate limiting, │
│  │         (first enforcement point)    │   session init        │
│  └───────────────────┬──────────────────┘                       │
│                      │                                          │
│                      ▼                                          │
│  ┌──────────────────────────────────────┐                       │
│  │  EP-2: Prompt Processing Middleware  │ ← PRM controls        │
│  │   • System prompt injection          │   Injection detection │
│  │   • User prompt scope enforcement    │   Context boundary    │
│  │   • Injection detection              │   Jailbreak check     │
│  └───────────────────┬──────────────────┘                       │
│                      │                                          │
│          ┌───────────┴───────────┐                              │
│          ▼                       ▼                              │
│  ┌───────────────┐      ┌─────────────────────┐                │
│  │  EP-3:        │      │  EP-4: Retrieval     │                │
│  │  Model API    │      │  Pipeline            │ ← RET controls  │
│  │  (inference)  │      │  • Corpus access     │   Grounding     │
│  │               │      │  • Freshness check   │   Citation      │
│  └───────┬───────┘      │  • Indirect inject   │                │
│          │              └──────────┬────────────┘               │
│          └───────────┬─────────────┘                            │
│                      │                                          │
│                      ▼                                          │
│  ┌──────────────────────────────────────┐                       │
│  │  EP-5: Output Processing Layer       │ ← OUT controls        │
│  │   • Safety classification            │   GEN controls        │
│  │   • Content policy filter            │   Privacy leak detect │
│  │   • PII detection                    │   Hallucination check │
│  │   • Disclosure injection             │                       │
│  └───────────────────┬──────────────────┘                       │
│                      │                                          │
│          ┌───────────┴───────────┐                              │
│          ▼                       ▼                              │
│  ┌───────────────┐      ┌─────────────────────┐                │
│  │  EP-6: Tool   │      │  EP-7: Audit Log     │ ← LOG controls  │
│  │  Execution    │      │  Writer              │   Tamper-evident│
│  │  Gate         │      │  (all events)        │                │
│  │  (agentic)    │      └─────────────────────┘                │
│  └───────┬───────┘                                              │
│          │                                                       │
│          ▼                                                       │
│  ┌──────────────────────────────────────┐                       │
│  │  EP-8: HITL Queue (where required)   │ ← AGT-03, TOL-04      │
│  │   • Irreversible action hold         │   Human review        │
│  │   • Threshold-triggered review       │   Override logging    │
│  └──────────────────────────────────────┘                       │
│                                                                 │
│  ┌──────────────────────────────────────┐                       │
│  │  EP-9: Monitoring Sidecar           │ ← Deliverable E signals│
│  │   • Signal collection               │   Drift detection      │
│  │   • Threshold alerting              │   Cost runaway         │
│  │   • KRI breach notification         │                        │
│  └──────────────────────────────────────┘                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 11.3 Control-to-Enforcement-Point Mapping

| Control domain | Primary enforcement point | Implementation technology options |
|---|---|---|
| **IAM (Domain 8)** | EP-1 (API Gateway) | OAuth2/OIDC; enterprise SSO; API key management; RBAC at gateway layer |
| **Prompt governance — system prompt (Domain 4, PRM-01–03)** | EP-2 (Prompt Middleware) + Control Plane | **Prompt registry service** (Git-backed version store with signed commits; deployment pipeline reads current approved version only); runtime injection of approved system prompt at EP-2 |
| **Prompt governance — user scope + injection (Domain 4, PRM-04–08)** | EP-2 (Prompt Middleware) | Custom middleware or open-source guardrail library (NeMo Guardrails, Guardrails AI); pattern-matching + LLM-based classification for injection detection |
| **Retrieval controls (Domain 5)** | EP-4 (Retrieval Pipeline) | Vector database access controls (role-based); freshness metadata in document store; content classification tags at index time |
| **Output safety (Domain 7, OUT-01–02)** | EP-5 (Output Layer) | Safety classifier API (Azure Content Safety, AWS Bedrock Guardrails, enterprise-deployed classifier); middleware post-processor |
| **Privacy leak detection (DAT-06, MON-15)** | EP-5 (Output Layer) | PII detection model (Microsoft Presidio, AWS Comprehend, custom); regex + ML hybrid |
| **Tool execution gate (Domain 6, Domain 10)** | EP-6 (Tool Gate) | Tool call interceptor in agent framework; allowlist enforcement before execution; parameter validation before dispatch |
| **HITL enforcement (AGT-03, TOL-04)** | EP-8 (HITL Queue) | Workflow engine (Temporal, Airflow, custom); approval queue with SLA alerting; override event logging |
| **Audit logging (Domain 14)** | EP-7 (Audit Log Writer) | Write-once log store (AWS CloudTrail, GCP Cloud Audit Logs, Azure Monitor, on-prem SIEM); structured log schema; integrity hashing |
| **Monitoring signals (Deliverable E)** | EP-9 (Monitoring Sidecar) | OpenTelemetry instrumentation; Prometheus + Grafana; custom signal collectors; KRI alerting via PagerDuty or equivalent |
| **Drift detection (MON-10–12)** | EP-9 (Monitoring Sidecar) | Evidently AI, Arize AI, WhyLabs, or custom statistical drift detectors on input/output distributions |

---

## 11.4 Prompt Registry — Reference Implementation Design

The system prompt is the primary behavioral governor of any LLM-based AI system. It must be treated as a governed artifact with the same discipline as production code.

**Required components:**

| Component | Specification |
|---|---|
| **Storage** | Git repository (dedicated `prompts/` repo or directory) with branch protection; all changes via pull request; no direct commit to main |
| **Versioning** | Semantic versioning (`v1.2.3`); each version tagged and immutable after merge; SHA-256 hash of prompt content stored alongside version |
| **Access control** | Write access restricted to named System Owners + AI Governance Office; read access to deployment pipeline only (service account); no human read access to production system prompt outside this repo |
| **Approval workflow** | PR raised by System Owner; reviewed and approved by AI Gov Office (and AI Risk Committee for Tier 1 systems) before merge; approval record captured in PR metadata |
| **Deployment** | CI/CD pipeline reads approved version at deployment; runtime system injects approved prompt at EP-2; no manual prompt injection in production |
| **Audit trail** | Git log provides immutable audit trail of every change, author, reviewer, timestamp, and approval |
| **Change management** | Any prompt change = material change under CHG-01; triggers CHG-02 risk re-evaluation and CHG-05 post-change monitoring period |

---

## 11.5 Data Plane Control Implementation by Archetype

| Archetype | Critical EP | Minimum implementation stack |
|---|---|---|
| **Chat-First** | EP-2, EP-5, EP-7, EP-9 | Prompt middleware (NeMo / custom); output safety classifier; structured audit log; monitoring sidecar |
| **RAG** | EP-2, EP-4, EP-5, EP-7, EP-9 | Above + retrieval access controls; indirect injection scanner on retrieved chunks before model ingestion; grounding validator |
| **Agentic Single-Agent** | EP-2, EP-5, EP-6, EP-7, EP-8, EP-9 | Above + tool call interceptor; reversibility enforcer; HITL queue; action chain audit log |
| **Agentic Multi-Agent** | All EPs | Above, replicated per agent; inter-agent trust token; cross-agent scope inheritance enforcer; unified action chain log |
| **Open-Weight Self-Hosted** | EP-5 (mandatory enterprise layer), EP-7, EP-9 | Enterprise safety classifier deployed as mandatory post-processing layer; no reliance on model's intrinsic safety; tamper-evidence verification at startup |
| **Workflow Automation** | EP-6, EP-7, EP-8, EP-9 | Exception queue for anomalous outputs; scheduled output sampling for quality review; change detection on AI component |
| **Decision-Support** | EP-5, EP-7, EP-8, EP-9 | Fairness metric collector; explainability extractor; human decision logging (what the human decided vs AI recommendation) |

---

*End of Part XI.*

---

# Part XII — Control Validation and Red-Teaming System

## Review Finding Addressed

> *"You define monitoring signals, but not unit tests for controls or control validation pipelines. Controls exist but degrade silently."*

This part defines how controls are continuously tested and validated — not just at deployment, but throughout the production lifecycle. A control that passes at deployment but degrades silently is not a control.

---

## 12.1 Control Validation Philosophy

**Fact:** Controls degrade. Safety classifiers accumulate false negatives as adversaries adapt. Injection detectors miss new patterns. Drift thresholds become miscalibrated as model behavior shifts. HITL queues accumulate and stop being reviewed.

**Inference:** Designing a control at deployment and not testing it continuously is equivalent to installing a fire alarm and never testing the battery.

**Recommendation:** Every control in the master control matrix (Part V) must have: (a) a defined test, (b) a test cadence, and (c) a test failure response. Control testing is a first-class operational activity, not a one-time pre-deployment task.

---

## 12.2 Control Validation Framework

### Three types of control validation

| Type | Definition | Cadence | Triggered by |
|---|---|---|---|
| **Deployment validation** | Control is tested before any production deployment; gate cannot be passed without passing tests | Every deployment | Pre-deployment gate (Deliverable D Stage 5) |
| **Continuous validation** | Control is tested automatically on a schedule in production | Daily to monthly (by control criticality) | Automated CI/CD schedule or monitoring pipeline |
| **Event-triggered validation** | Control is tested immediately following a defined event (incident, model update, corpus change, system prompt change) | On event | Change management trigger; incident closure |

---

## 12.3 Control Validation Matrix

For each critical control, the following test design is mandatory:

| Control | Test type | Test method | Pass criterion | Cadence | Failure response |
|---|---|---|---|---|---|
| **PRM-06 — Prompt injection detection** | Adversarial | Synthetic injection test suite (see Section 12.4); known jailbreak pattern library | Detection rate >99% on known patterns; <1% false positive on benign inputs | Weekly automated | Immediate alert; injection pattern library update; control review within 48h |
| **PRM-07 — Jailbreak pattern library** | Coverage | New pattern identification: monitor public jailbreak disclosures; run against detection | Library updated within 72h of public disclosure of new pattern | Continuous (event-triggered) | Library update; re-run injection detection test |
| **OUT-01 — Output safety classifier** | Precision/recall | Holdout set of labeled safe/unsafe outputs; adversarial samples | Precision >95%; recall >95% on holdout set | Monthly; re-run at model update | Classifier retraining or replacement; deployment hold pending validation |
| **AGT-03 — HITL enforcement** | Functional | Synthetic irreversible action trigger; verify queue creation and SLA | 100% of triggered actions enter queue; queue SLA met | Weekly | HITL configuration review; immediate escalation to AI Gov Office |
| **TOL-01 — Tool authorization** | Functional | Attempt unauthorized tool invocation in test environment | 100% of unauthorized invocations blocked; zero false positives on authorized tools | At every deployment; weekly synthetic test | Tool gate configuration review; deployment hold |
| **LOG-01 — Audit log completeness** | Sampling | Random sample of 1000 interactions; verify log entry presence and schema completeness | >99.5% log completeness; zero schema violations in sample | Daily automated | Log pipeline investigation; escalation if >0.5% gap |
| **LOG-02 — Log tamper-evidence** | Integrity | Hash verification of log entries against stored checksums | Zero hash mismatches | Daily automated | Security incident; investigation |
| **DAT-06 — Privacy leak detection** | Precision/recall | Holdout set with synthetic PII patterns; adversarial PII obfuscation patterns | Precision >97%; recall >95% | Monthly | PII detector update; review of false negative patterns |
| **RET-03 — Corpus freshness** | Functional | Query for known stale documents; verify freshness metadata | Zero stale documents beyond defined threshold | Daily automated | Corpus refresh trigger; staleness alert |
| **MON-10/11 — Drift detection** | Statistical | Synthetic distribution shift injection on input/output | Drift alert within defined detection window | Monthly calibration; continuous signal | Threshold recalibration; model review |

---

## 12.4 Red-Team Pipeline Design

Red-teaming for AI systems must be a **continuous pipeline**, not a one-time pre-deployment exercise. The red-team pipeline runs on a defined schedule and on event triggers (model update, system prompt change, new jailbreak pattern disclosed publicly).

### Red-team pipeline architecture

```
┌─────────────────────────────────────────────────┐
│           RED-TEAM PIPELINE                     │
│                                                 │
│  1. Attack Library (version-controlled)         │
│     ├── Known jailbreak patterns                │
│     ├── Injection templates (direct)            │
│     ├── Injection templates (indirect / RAG)    │
│     ├── Adversarial fairness probes             │
│     ├── Privacy extraction attempts             │
│     └── Tool misuse scenarios (agentic)         │
│                          │                      │
│  2. Synthetic Attack     │                      │
│     Generator            │                      │
│     (automated          ▼                       │
│     permutation of  ┌──────────────┐            │
│     known patterns) │ Test Runner  │            │
│                     │ (isolated    │            │
│                     │  environment)│            │
│                     └──────┬───────┘            │
│                            │                    │
│  3. Result Classifier       ▼                   │
│     ├── Pass: control held                      │
│     ├── Warn: control held; pattern near edge   │
│     └── Fail: control breached                  │
│                            │                    │
│  4. Report + Alert          ▼                   │
│     ├── Auto-report to AI Gov Office            │
│     ├── Fail → block deployment / alert         │
│     └── Update attack library with new variants │
└─────────────────────────────────────────────────┘
```

### Red-team cadence by tier

| System tier | Minimum red-team cadence | Trigger-based red-team events |
|---|---|---|
| Tier 1 | Monthly full pipeline run | Model update; system prompt change; new public jailbreak disclosure; post-incident |
| Tier 2 | Quarterly full pipeline run | Model update; system prompt change; post-incident |
| Tier 3 | Annual (injection detection only) | Post-incident |
| Tier 4 | Not required | Not required |

### Tooling options

| Tool | Best for | Notes |
|---|---|---|
| **PyRIT (Microsoft)** | GenAI adversarial testing; multi-turn attack simulation | Open-source; well-documented; recommended for enterprise adoption |
| **Garak** | LLM vulnerability scanning; systematic probe library | Open-source; broad probe coverage |
| **PromptBench** | Robustness evaluation; adversarial prompt generation | Research-grade; useful for academic validation |
| **Custom synthetic attack generator** | Enterprise-specific attack patterns; proprietary use-case scenarios | Required for industry-specific attack surfaces (financial, healthcare) |
| **NeMo Guardrails test suite** | Rail-specific validation for NeMo-deployed systems | Platform-specific |

---

## 12.5 Control Degradation Detection

**Problem:** Controls degrade between red-team runs. Safety classifier accuracy decreases as adversaries adapt. Injection detection misses new patterns. Drift thresholds become miscalibrated.

**Solution:** Control degradation is detected through the following signals, in addition to scheduled red-team runs:

| Degradation signal | Detection mechanism | Response |
|---|---|---|
| Rising safety classifier flag rate without corresponding incident increase | Statistical process control on MON-02; alert on sustained trend | Classifier recalibration; red-team trigger |
| Falling user escalation rate with no service improvement change | MON-13 statistical trend; correlated with human override rate | Investigate whether users have stopped using escalation (learned helplessness) vs system improvement |
| HITL queue growing faster than review capacity | Queue depth KCI; dwell time KCI | HITL design review; capacity assessment; if queue is systematically skipped → control failure |
| Log completeness declining | MON-14 daily automated check | Log pipeline investigation; escalation |
| Drift alert threshold never triggering | Absence of alert where drift is expected (e.g., seasonal patterns) | Threshold calibration review; synthetic drift injection test |

---

*End of Part XII.*

---

# Part XIII — Developer Workflow Integration

## Review Finding Addressed

> *"Developers will bypass governance. You don't define how this integrates with actual developer workflows — CI/CD integration, PR checks, pre-commit hooks, agent usage constraints."*

This part specifies the developer-facing operating model: how governance is enforced in the build pipeline, not just in committee. Governance that is not embedded in developer workflows will be worked around.

---

## 13.1 Governance-as-Code Design Principle

**Fact:** Governance enforced only through committee review and documentation requirements will be circumvented under delivery pressure. Developers route around friction they cannot avoid technically.

**Recommendation:** Governance requirements that can be technically enforced must be technically enforced — in pre-commit hooks, CI/CD pipeline gates, and deployment checks. This is not a substitute for governance forums; it is the enforcement mechanism that makes governance reliable at scale.

**Governance-as-Code principle:** Every governance requirement that can be expressed as a machine-checkable condition should be expressed that way. Human review is reserved for conditions that require judgment.

---

## 13.2 CI/CD Integration Architecture

```
Developer Push / PR
        │
        ▼
┌─────────────────────────────────────────────────────┐
│            PRE-COMMIT HOOKS (local)                 │
│  ✓ System card presence check                       │
│  ✓ System prompt hash integrity (matches registry)  │
│  ✓ Prohibited dependency check (banned models/libs) │
│  ✓ Secret / credential scan                         │
└───────────────────────────┬─────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────┐
│            CI PIPELINE GATE 1: Intake Check         │
│  ✓ AI system registered in inventory                │
│  ✓ Risk tier assigned                               │
│  ✓ Business Owner and System Owner named            │
│  ✗ Fail → block merge; link to intake form          │
└───────────────────────────┬─────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────┐
│            CI PIPELINE GATE 2: Documentation Check  │
│  ✓ System card present and schema-valid             │
│  ✓ Model card present (Tier 1/2)                    │
│  ✓ Prompt registry reference valid (hash match)     │
│  ✓ Tool authorization register present (agentic)    │
│  ✗ Fail → block merge; generate missing-doc report  │
└───────────────────────────┬─────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────┐
│            CI PIPELINE GATE 3: Control Tests        │
│  ✓ Control validation tests pass (Section 12.3)     │
│  ✓ Injection detection test suite passes            │
│  ✓ Output safety test suite passes                  │
│  ✓ Tool authorization test passes (agentic)         │
│  ✓ Monitoring hooks present (sidecar config valid)  │
│  ✗ Fail → block merge; test failure report          │
└───────────────────────────┬─────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────┐
│            CI PIPELINE GATE 4: Security Scan        │
│  ✓ SAST / dependency vulnerability scan             │
│  ✓ Model supply chain integrity check (hash)        │
│  ✓ Open-weight model tamper-evidence verified       │
│  ✗ Fail → block merge; security finding report      │
└───────────────────────────┬─────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────┐
│         DEPLOYMENT GATE: Tier-Specific Approval     │
│  Tier 1 → AI Risk Committee approval token required │
│  Tier 2 → AI Gov Office approval token required     │
│  Tier 3 → AI Gov Office notification confirmed      │
│  Tier 4 → Business Owner self-cert recorded         │
│  ✗ Fail → block deployment; approval request sent   │
└───────────────────────────┬─────────────────────────┘
                            │
                            ▼
                     Production Deploy
                            │
                            ▼
┌─────────────────────────────────────────────────────┐
│         POST-DEPLOY: Monitoring Activation Check    │
│  ✓ Monitoring sidecar active (all Deliverable E     │
│    signals reporting)                               │
│  ✓ Audit log stream verified                        │
│  ✓ Alert routing confirmed                          │
│  ✗ Fail → deployment marked incomplete; alert       │
└─────────────────────────────────────────────────────┘
```

---

## 13.3 Pre-Commit Hook Specification

The following hooks are deployed to all developer machines and enforced via the enterprise developer toolchain (e.g., `pre-commit` framework):

| Hook | What it checks | Failure behavior |
|---|---|---|
| `ai-inventory-check` | Does the repo contain an AI system registration file? Is the system ID present in the central inventory? | Block commit; print inventory registration link |
| `system-card-schema` | Is `system-card.yaml` (or equivalent) present and schema-valid? | Block commit; print schema validation errors |
| `prompt-registry-integrity` | Does the system prompt file hash match the approved version in the prompt registry? | Block commit; print hash mismatch; direct to prompt change approval process |
| `banned-model-check` | Does the code reference any banned model endpoints or open-weight models not in the approved model register? | Block commit; print banned model reference |
| `secret-scan` | Are any API keys, tokens, or credentials hardcoded? | Block commit; print location of exposed secret |
| `monitoring-hook-check` | Are monitoring instrumentation calls present in the AI service code? (OpenTelemetry or equivalent) | Warn on commit; block deployment gate |

---

## 13.4 PR Review Requirements by Tier

Pull requests for AI systems include automated checks (above) plus required human review:

| Tier | Required human reviewers on PR | Additional PR requirements |
|---|---|---|
| Tier 1 | System Owner + AI Gov Office reviewer + Security reviewer | Red-team report attached; validation report reference; AI Risk Committee approval token |
| Tier 2 | System Owner + AI Gov Office reviewer | Security and privacy sign-off; approval token |
| Tier 3 | System Owner | AI Gov Office notified (automated); documentation checks pass |
| Tier 4 | Business Owner acknowledgment | Automated checks pass |

---

## 13.5 Agent Usage Constraints for Developers

Enterprises deploying AI coding assistants (GitHub Copilot, Cursor, internal coding agents) face a specific governance challenge: the development tool is itself an AI system that may generate AI governance artifacts (system cards, prompts, control configurations) that then require governance. Left ungoverned, the AI coding assistant becomes a shadow governance pathway.

**Controls for developer AI tool usage:**

| Control | Implementation |
|---|---|
| **Approved tool register** | Only enterprise-approved AI coding assistants are permitted on developer machines; enforced via endpoint management policy |
| **Data scope constraints** | AI coding tools configured to exclude: production data, model weights, system prompts in production repos, and access credentials from their context |
| **Generated artifact review** | AI-generated governance artifacts (system cards, risk assessments) must be human-reviewed and signed before submission; automated tools cannot self-approve governance documentation |
| **Prompt governance for coding agents** | Enterprise-wide system prompt for coding AI tools is centrally managed and version-controlled (same as PRM-01 principle applied to developer tools) |
| **Usage audit** | AI coding tool usage logged at the enterprise license level; anomalous usage patterns (e.g., bulk prompt injection pattern generation) flagged for security review |

---

## 13.6 Shadow AI Detection

**Problem:** Governance misallocation (Section 8.5) is worsened by shadow AI — AI systems deployed outside governance channels. Shadow AI is the most common consequence of governance that is too slow for low-risk use cases.

**Detection mechanisms:**

| Detection method | What it finds | Cadence |
|---|---|---|
| **Network egress analysis** | Outbound API calls to known AI provider endpoints (OpenAI, Anthropic, Cohere, Mistral, etc.) from non-registered service accounts or endpoints | Continuous; anomaly-based alerting |
| **Cloud cost anomaly detection** | Unexpected AI inference costs in cloud accounts not associated with registered AI systems | Weekly |
| **Application dependency scan** | CI/CD pipeline scans for AI SDK imports (openai, anthropic, langchain, llamaindex, etc.) in repos without corresponding AI inventory registration | At every build |
| **SaaS AI tool procurement monitoring** | Procurement and expense tracking for AI SaaS subscriptions not approved through the vendor assessment process | Monthly |
| **Employee survey (annual)** | Structured survey asking whether employees use AI tools not sanctioned by the enterprise | Annual |

**Response to shadow AI detection:**

1. Identify system and Business Owner
2. Classify system using Deliverable B tiering criteria
3. If Tier 3 or 4: fast-track into governance (fast-lane, Section 8.3); do not penalize proactively
4. If Tier 1 or 2: mandatory immediate review; deployment pause pending governance completion
5. Root cause analysis: was shadow AI driven by governance friction? → Governance process improvement required

---

*End of Part XIII.*

---

# Part XIV — Governance Cost Model and Enhanced Vendor Governance

## Review Finding Addressed (Cost Model)

> *"You argue governance should not slow adoption but you don't quantify cost of control, latency added, or developer friction. Without economics, governance drifts toward over-control."*

## Review Finding Addressed (Vendor Governance)

> *"No benchmarking model, no performance SLAs tied to risk, no fallback strategy. Missing: model degradation at vendor side, API outage impact, silent model updates."*

---

## 14.1 Governance Cost Model

### Principle

Governance has a real cost. Pretending otherwise leads to one of two failure modes: (a) governance is under-resourced and becomes a rubber stamp, or (b) governance is over-resourced and becomes a bottleneck. The cost model makes governance economics visible and manageable.

### Cost dimensions

| Cost dimension | Definition | Measurement |
|---|---|---|
| **Time-to-approval** | Calendar time from intake submission to approval to proceed (at each tier) | Days; tracked in intake system |
| **Documentation cost** | Effort to produce required governance documentation | Person-hours per use case; tracked by tier |
| **Review cost** | Committee and reviewer time per use case | Person-hours per use case; tracked by tier |
| **Control implementation cost** | Engineering effort to implement required controls | Story points or person-hours per control domain |
| **Monitoring cost** | Infrastructure and engineering cost of runtime monitoring | $ per month per system; scaled by signal set |
| **Compliance cost** | Effort for regulatory mapping, audit preparation, certification | Person-hours per system per year |

---

### Target SLAs by tier (time-to-approval)

These are governance performance commitments — the AI Governance Office must meet them to maintain credibility and prevent shadow AI.

| Tier | Intake-to-approval SLA | Design gate SLA | Pre-deployment gate SLA |
|---|---|---|---|
| **Tier 0** | Immediate (automated block) | N/A | N/A |
| **Tier 1** | 10 business days (intake to AI Risk Committee endorsement) | 10 business days | 15 business days (evidence pack review) |
| **Tier 2** | 5 business days | 5 business days | 7 business days |
| **Tier 3** | 3 business days | 2 business days | 2 business days |
| **Tier 4** | 1 business day (automated + silent approval) | None | None |

**SLA breach response:** Any governance SLA breach is logged and reported monthly to the Executive AI Council. Repeated SLA breaches in a tier are treated as a governance capacity problem requiring resource response, not as a justification for bypassing governance.

---

### Cost benchmarks by tier (indicative; enterprise-calibrate at program launch)

| Tier | Documentation effort | Review effort | Control implementation | Annual monitoring cost (indicative) |
|---|---|---|---|---|
| **Tier 1** | 40–80 person-hours | 20–40 person-hours (committee + legal + compliance) | 80–200 engineering hours | $15,000–$50,000/year per system |
| **Tier 2** | 15–30 person-hours | 8–15 person-hours | 30–80 engineering hours | $5,000–$15,000/year per system |
| **Tier 3** | 4–8 person-hours | 2–4 person-hours | 8–20 engineering hours | $1,000–$5,000/year per system |
| **Tier 4** | 1–2 person-hours | <1 person-hour | 2–4 engineering hours | <$1,000/year per system |

### Governance ROI metrics

| Metric | Definition | Target |
|---|---|---|
| **Cost of governance per system** | Total governance cost (documentation + review + controls + monitoring) divided by number of systems | Tracked and benchmarked annually; should decrease as templates and automation mature |
| **Incident cost avoided** | Estimated cost of incidents prevented by controls (using historical incident cost data) | Governance ROI = incident cost avoided / governance cost; target >3:1 |
| **Time-to-value** | Days from business idea to production deployment by tier | Decreasing trend as fast-lane and pre-approved patterns are adopted |
| **Shadow AI rate** | Percentage of AI systems discovered in production not registered at intake | Target: <5%; declining trend |
| **Governance SLA compliance** | Percentage of intakes processed within tier SLA | Target: >95% |
| **Audit finding rate** | Number of material audit findings per governance review | Decreasing trend; target: zero critical findings |

---

### Control cost vs risk reduction matrix

Not all controls have equal ROI. The following matrix guides investment prioritization:

| Control | Implementation cost | Risk reduction impact | Priority |
|---|---|---|---|
| PRM-01–03 (System prompt versioning) | Low (Git + access control) | High (primary behavioral governor) | **Critical — implement first** |
| LOG-01–02 (Audit log + integrity) | Low to Medium | High (enables all audit and incident response) | **Critical** |
| OUT-01 (Safety classifier) | Medium | High (primary detective control for harmful output) | **Critical** |
| PRM-06 (Injection detection) | Medium | High (primary attack vector for GenAI) | **Critical** |
| AGT-01–03 (Agentic scope + HITL) | Medium to High | Very High for agentic systems | **Critical for agentic** |
| INT-02 (Prohibited use block at intake) | Low (form validation) | High (stops Tier 0 at entry) | **Critical** |
| MON-10–12 (Drift detection) | Medium | Medium-High | High |
| DAT-06 (Privacy leak detection) | Medium | High (regulatory exposure) | High |
| MSC-03 (Tamper-evidence for open-weight) | Low | High for open-weight archetype | High for open-weight |
| RET-03 (Corpus freshness) | Low | Medium | Medium |
| VND-03 (Vendor model change notification) | Low (contractual) | Medium-High | High |

---

## 14.2 Enhanced Vendor Governance

### Vendor AI Risk Scoring Model

Each AI vendor or third-party AI service is assigned a vendor AI risk score at assessment and reviewed annually. The score determines the depth of due diligence and the contractual requirements.

**Scoring dimensions:**

| Dimension | Weight | Score criteria |
|---|---|---|
| **Data handling** | 25% | 5 = zero retention, no training, contractually guaranteed; 3 = opt-out available; 1 = unclear or adverse terms |
| **Model transparency** | 20% | 5 = full model card, training data documented, change notification SLA; 3 = partial; 1 = opaque |
| **Security posture** | 20% | 5 = SOC 2 Type II + ISO 27001 + pen test; 3 = SOC 2 Type II only; 1 = no certifications |
| **Reliability and SLA** | 15% | 5 = 99.9%+ SLA + compensation; 3 = 99.5% SLA; 1 = best-effort / no SLA |
| **Audit rights** | 10% | 5 = full audit rights contractually; 3 = questionnaire-based; 1 = no audit rights |
| **Incident notification** | 10% | 5 = <24h notification SLA contractually; 3 = reasonable efforts; 1 = no obligation |

**Score interpretation:**

| Score | Risk rating | Required action |
|---|---|---|
| 4.5–5.0 | Low vendor risk | Standard annual review |
| 3.5–4.4 | Medium vendor risk | Enhanced monitoring; annual review; contractual improvement plan |
| 2.5–3.4 | High vendor risk | Mandatory compensating controls; semi-annual review; executive awareness |
| <2.5 | Critical vendor risk | Use prohibited for Tier 1 systems; waiver required for Tier 2; immediate improvement plan or replacement |

---

### Vendor Performance SLAs Tied to Risk Tier

| SLA dimension | Tier 1 systems | Tier 2 systems | Tier 3/4 systems |
|---|---|---|---|
| **API availability SLA** | 99.9% monthly; compensation for breach | 99.5% monthly | Best effort acceptable |
| **Model change notification lead time** | 30 days minimum written notice before model version update | 14 days | Best effort |
| **Incident notification SLA** | <4 hours for AI incidents affecting enterprise data | <24 hours | <72 hours |
| **Security incident notification** | <2 hours | <4 hours | <24 hours |
| **Data deletion SLA** | <72 hours on request | <30 days | <90 days |
| **Audit response SLA** | <10 business days for questionnaire; right to on-site audit annually | <15 business days for questionnaire | <20 business days |

---

### Multi-Model Fallback Architecture

**Problem:** Single-vendor dependency for a Tier 1 AI system creates operational risk. A vendor API outage, silent model update, or security incident may require immediate failover.

**Recommendation:** For all Tier 1 systems, a documented fallback strategy is a mandatory pre-deployment gate requirement.

**Fallback strategy options (by risk and complexity):**

| Option | Description | When appropriate |
|---|---|---|
| **Active-active multi-model** | System routes inference across two or more models (e.g., primary: GPT-4o, fallback: Claude 3.5 Sonnet); load balanced or failover-triggered | High-availability Tier 1 systems; enterprises with multi-vendor contracts |
| **Warm standby** | Secondary model configured and tested but not receiving production traffic; automated failover within defined RTO | Standard Tier 1 requirement; acceptable RTO >15 minutes |
| **Degraded-mode operation** | System falls back to rule-based or pre-approved response templates when AI inference unavailable | Systems where partial service is preferable to no service; e.g., customer service (FAQ fallback) |
| **Human escalation** | System fails open to human agents on AI unavailability | Decision-support and autonomous systems where human fallback is the safety default |

**Minimum fallback requirements for Tier 1 systems:**

- Fallback strategy documented in system card
- Fallback RTO (Recovery Time Objective) defined
- Fallback tested at pre-deployment gate and quarterly thereafter
- Fallback activation is an automated or semi-automated operation (not manual-only)
- Fallback event is logged and reported as a monitoring signal

---

### Silent Model Update Controls

**Problem:** Vendor-hosted AI models can be silently updated without enterprise awareness, changing system behavior while the system card, validation reports, and monitoring baselines remain calibrated to the previous model version.

**Controls:**

| Control | Implementation |
|---|---|
| **Contractual notification requirement** | All Tier 1 and Tier 2 AI vendor contracts require written notice of model updates at least 14–30 days in advance (per SLA table above) |
| **Behavioral fingerprinting** | A defined set of reference prompts with expected outputs (behavioral fingerprints) is run daily against the production model; statistically significant output distribution shift triggers alert (VND-03 signal) |
| **Model version pinning** | Where the vendor API supports model version pinning (e.g., OpenAI `gpt-4o-2024-11-20`), Tier 1 systems pin to a specific version; migration to a new pinned version is treated as a material change |
| **Version detection** | API response metadata logged; model version field monitored; version change detected within 1 API call |
| **Update response procedure** | Vendor model update notification triggers: (1) behavioral fingerprint test against new version; (2) risk re-evaluation (CHG-02); (3) system card update (CHG-03); (4) approval if tier requires (CHG-04) |

---

*End of Part XIV.*

---

---

# Part XV — Supplementary Controls (AIUC-1 Crosswalk Gap Closure)

## Provenance

This part adds 13 controls identified as gaps through reconnaissance of the AIUC-1 crosswalk
coverage (see `AIUC1_Crosswalk_Recon.md`). Source frameworks surfacing these gaps include:
AIUC-1 (B003, C006, E005, E011, F001, F002), MITRE ATLAS (AML-M0007/M0008/M0014/M0022),
OWASP LLM10, OWASP AIVSS, Cisco AI Security Framework, and IBM AI Risk Atlas.

Controls are organized by domain and are additive to Parts V and VII.

---

## Domain 16 — Societal Harm Controls

**Control objective:** AI systems are designed and monitored to prevent their use for cyber attacks,
large-scale fraud, mass deception, and catastrophic harm including weapons of mass destruction
uplift, attacks on critical infrastructure, and national security threats.

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| SOC-01 | **Cyber misuse prevention** — AI system design explicitly constrains use for generating malware, attack payloads, phishing content, credential harvesting tools, and exploit code. System prompt, output filter, and content policy must name these as prohibited output categories, not only rely on model-level refusals. | P | System Owner + Security | System prompt scope specification; content filter configuration; test evidence | MON-17 (security misuse signal); security classifier flag rate |
| SOC-02 | **Catastrophic misuse prevention** — AI systems with access to scientific, chemical, biological, radiological, nuclear (CBRN) domain content must implement explicit output restrictions preventing uplift toward mass-casualty weapons, attack planning against critical infrastructure, or national security exploitation. This obligation is in addition to Tier 0 prohibition at intake. | P | Security + Legal + System Owner | CBRN restriction specification in system prompt and content filter; red-team test for CBRN uplift; legal sign-off | Red-team CBRN probe pass rate; any CBRN-category output detection event |

---

## Domain 4 Extension — Multi-Modal Injection Controls

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| PRM-09 | **Multi-modal input injection controls** — For AI systems accepting non-text inputs (images, audio, documents, video), injection scanning is applied to the non-text modality before model ingestion. Adversarial perturbations embedded in images or documents that could manipulate model behavior are treated as equivalent to text-based prompt injection. | P+D | Security + System Owner | Multi-modal injection test records; scanner configuration; applicable to Hybrid and any archetype processing non-text inputs | Multi-modal injection attempt rate; detection coverage rate |

---

## Domain 6 Extension — Resource Consumption Controls

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| TOL-08 | **Resource consumption limits** — AI system endpoints enforce token budget limits, request rate limits, and query quotas per session, user, and API key. Limits are defined at design time, documented in the system card, and enforced at EP-1 (API gateway). Prevents unbounded consumption, denial-of-service via resource exhaustion, and cost-harvesting attacks. | P | System Owner + Security | Rate limit configuration; quota enforcement test; architecture diagram confirming EP-1 enforcement | MON-16 (cost runaway signal); rate limit breach rate; quota exhaustion events |

---

## Domain 7 Extension — Code Security Output Control

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| OUT-07 | **AI-generated code security control** — For AI systems that generate executable code (code assistants, workflow automation generating scripts, agentic systems writing code for execution), output is scanned for common vulnerability patterns (injection flaws, hardcoded secrets, insecure cryptography, unsafe deserialization) before delivery. For systems where generated code is executed automatically (agentic systems), this control is mandatory and a gate to execution. | P+D | System Owner + Security | Code security scanner configuration; test evidence (known-vulnerable code samples); false positive/negative rate | Code vulnerability detection rate; vulnerable code execution events |

---

## Domain 10 Extension — Agent Identity Verification

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| AGT-10 | **Agent identity verification** — In multi-agent systems, each agent asserts a cryptographically verifiable identity before being granted execution scope by an orchestrator. Agent identity tokens are short-lived, scoped to the current task, and not transferable between sessions. Orchestrators reject agent interaction from unverified or impersonated agents. | P | System Owner + Identity | Agent identity token specification; trust boundary design review; test evidence for impersonation rejection | Agent identity verification failure events; unverified agent invocation attempts |

---

## Domain 11 Extensions — Model Supply Chain

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| MSC-07 | **Training data poisoning detection** — For models trained or fine-tuned by or on behalf of the enterprise, training data is scanned for poisoning indicators: statistical outliers in label distribution, anomalous data clusters, known adversarial poisoning patterns, and backdoor trigger candidate patterns. For externally trained models, vendor attestation of poisoning controls is required (maps to VND-01). | P+D | Model Owner + Security | Training data audit report; poisoning detection methodology; vendor attestation (for external models) | Anomalous training data cluster detection rate |
| MSC-08 | **Training data quality assessment** — For models trained or fine-tuned by or on behalf of the enterprise, training data is assessed for: representativeness of the intended deployment population, contamination with out-of-distribution data, demographic bias distribution, and label quality. Assessment results are documented in the model card (MDL-01). | P | Model Owner + Data Owner | Training data quality assessment report; model card — training data section | — |

---

## Domain 12 Extension — Processing Location

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| CBJ-05 | **AI processing location decision record** — For every AI system, the decision to process AI workloads in cloud, on-premises, or hybrid infrastructure is documented, including: the rationale (cost, latency, sovereignty, security), the jurisdictions involved, the data classification of workloads processed in each location, and the risk assessment for the chosen configuration. This record is maintained in the system card and reviewed at every material infrastructure change. | P | System Owner + Privacy + Legal | Processing location decision record (system card section); data classification confirmation; review record at change | Infrastructure change events triggering re-assessment |

---

## Domain 8 Extension — Technical Disclosure Control

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| SEC-01 | **Technical AI disclosure limits** — The enterprise defines and enforces limits on the public or third-party disclosure of: AI model architecture details, training data sources and volumes, system prompt content, tool authorization configurations, and model evaluation methodology. Disclosure decisions for each AI system are documented and approved by the System Owner and Legal. Over-disclosure increases extraction attack surface; this control limits that surface without preventing required regulatory transparency. | P | System Owner + Legal + Security | Disclosure classification decision per system; approved disclosure scope (public / restricted / confidential); review record | Unauthorized technical disclosure events |

---

## Part XII Extension — Backdoor and Alignment Validation

The following validation steps are added to the control validation matrix in Section 12.3:

| Control | Test type | Test method | Pass criterion | Cadence | Failure response |
|---|---|---|---|---|---|
| **Backdoor trigger testing (MDL — Tier 1 and open-weight)** | Adversarial | Known backdoor trigger pattern library applied to model inputs; verify model behavior does not change on trigger activation | Zero trigger-activated behavioral deviations | Pre-deployment (mandatory for Tier 1 and open-weight); at model update | Deployment hold; model rejection; vendor notification |
| **Cryptographic artifact verification (all production models)** | Integrity | SHA-256 or equivalent hash of model artifact verified against signed manifest at deployment and at each startup | Zero hash mismatches | At every deployment and at each service restart | Security incident; model halt; investigation |
| **Alignment verification (Tier 1 models)** | Functional | Structured evaluation against enterprise policy prohibitions and behavioral requirements using adversarial probes targeting value-misaligned outputs | Pass rate >99.9% on policy probe set | Pre-deployment; at model update | Model rejection or remediation before deployment |

---

## Deliverable E Extension — New Monitoring Signals

Two signals are added to the runtime monitoring catalog (Deliverable E):

| Signal ID | Signal | Definition | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Escalation threshold |
|---|---|---|---|---|---|---|---|
| MON-19 | **Cross-session memory integrity** | Detection of agent memory content that contains patterns inconsistent with the current session's legitimate inputs — indicating possible cross-session memory poisoning or injection via persistent memory | Continuous | Continuous | Not required | Not required | Any confirmed poisoning event triggers security incident |
| MON-20 | **Code vulnerability detection rate** | Rate of AI-generated code outputs flagged by OUT-07 code security scanner as containing known vulnerability patterns | Continuous (where OUT-07 applies) | Continuous (where OUT-07 applies) | Not required | Not required | Rising rate or any vulnerable code reaching execution triggers immediate review |

---

---

# Part XVI — Gap Closure: Comparative Framework Analysis Findings (V1.3)

## Provenance

This part addresses gaps identified through a systematic comparison of EAGCF against 20 external frameworks, standards, evaluation programs, and policy documents conducted April 2026. The comparison series covered: NIST AI 100-1, 100-2, 100-3, 100-4, 100-5, 600-1, 700-1, 700-2 + ARIA Companion, 800-1, 800-2, IR 8596; ISO crosswalks (42001/23894, 42005, 5338/5339); OECD/EU AI Act crosswalk; Google DeepMind RMF gap analysis template; Singapore AI Verify crosswalks; and America's AI Action Plan.

Full gap analysis documented in `EAGCF_Master_Gap_Consolidation.md`. This part incorporates Tier A (High priority, do now) and Tier B (Medium priority, near-term) gap closures.

---

## 16.1 Standards Watch and Normative Reference Updates (N-AP-03, N1005-01, N-42005-01)

### NIST AI RMF Revision Watch (N-AP-03)

The NIST AI Risk Management Framework (AI 100-1) — the governance backbone of this framework — is under revision per Executive Order 14179 ("Removing Barriers to American Leadership in Artificial Intelligence"), July 2025. The revision is expected to update the RMF's framing without materially altering its functional control architecture (Govern, Map, Measure, Manage functions and subcategories).

**Watch obligation:** The AI Governance Office must monitor NIST publications for the revised AI RMF. Upon publication:
1. Conduct a delta review comparing the revised RMF against EAGCF Part IV (governance framework) and Part V (control domains)
2. Update normative references in Part IV §4.2 and Part IV §4.5
3. Update the comparative matrix in Deliverable A (Part III) for the revised RMF
4. Report material changes to the AI Risk Committee within 60 days of revised RMF publication

**Current normative reference status:** NIST AI 100-1 (January 2023) — revision pending. All EAGCF controls remain grounded in the current RMF's functional architecture pending revision.

### Emerging ISO Standards (N1005-01, N-42005-01)

| Standard | Status | EAGCF Watch Action |
|---|---|---|
| **ISO/IEC 27090** — Cybersecurity — AI — Security threats and failures in AI systems | In development (CD stage) | When finalized: incorporate as normative reference in Part XI (enforcement architecture) and Part XII §12.3 (control validation) alongside NIST AI 100-2e2025. Designated as the primary ISO AI cybersecurity standard. |
| **ISO/IEC 27091** — Cybersecurity and Privacy — AI — Privacy protection | In development (WD stage) | When finalized: evaluate against Part V §5.2 (DAT domain) and Deliverable G §G.8 (DPIA template) for alignment gaps. |
| **ISO/IEC 42005** — AI System Impact Assessment | DIS stage (Draft International Standard) | When finalized: add to EAGCF normative reference stack alongside ISO 42001 and ISO 23894. EAGCF's AI Impact Assessment template (Deliverable G §G.3) and AI Use Case Registration (Deliverable G §G.5) together implement ISO 42005 requirements. |
| **ISO/IEC 42001 conformity assessment** | In development | When finalized: update Part IV §4.8 (assurance model) with formal audit and certification process guidance. |

*The AI Governance Office maintains a Standards Watch register updated quarterly.*

---

## 16.2 Tier 1 Gate Enhancements

### 16.2.1 Interdisciplinary Team Diversity (N-01)

**Gap identified by:** NIST AI 100-1, NIST AI 600-1, Google DeepMind RMF template, ISO 5338/5339 crosswalk (4 sources).

**Addition to Tier 1 Required Controls (extends Part IV §4.2 Tier 1):**

All Tier 1 AI systems must demonstrate that the core design and evaluation team includes representation from disciplines beyond technical AI development. At minimum, the following perspectives must be represented — by named individuals with relevant background — in the system card at pre-deployment gate:

| Perspective | Minimum requirement | Verification |
|---|---|---|
| **Technical / ML** | AI/ML engineers or data scientists responsible for model and pipeline | Named in system card |
| **Domain / business** | Subject matter expert for the specific use case domain (e.g., credit underwriter for credit AI; clinician for healthcare AI) | Named in system card |
| **Risk / compliance** | Risk, legal, or compliance professional with AI governance responsibility | Named in system card |
| **User / affected-population** | Individual with knowledge of the user population or affected community — may be internal (customer experience, accessibility team) or external (user research, community liaison) | Named in system card; external engagement documented if applicable |
| **Privacy / ethics** | Privacy officer or AI ethics reviewer | Named in system card |

**Evidence required:** System card — team composition section (mandatory field at Tier 1 pre-deployment gate).

**Approval impact:** Pre-deployment gate for Tier 1 is blocked if any required perspective is absent and no documented compensating engagement is on file.

---

### 16.2.2 External Stakeholder Feedback Mechanisms (N-02 / N-03)

**Gap identified by:** NIST AI 100-1, NIST AI 600-1, Google DeepMind RMF template, AI Verify crosswalk (4 sources).

**Addition to Tier 1 Required Controls:**

For Tier 1 AI systems deployed to external users or affecting external individuals:

1. **Pre-deployment**: The AI Impact Assessment (Deliverable G §G.3) must include documentation of how feedback from affected external stakeholders was sought during design and impact assessment. This may be satisfied by: user research sessions, community liaison engagement, public consultation, or documented rationale for why external engagement was not feasible.

2. **Post-deployment**: A mechanism for external users and affected individuals to submit feedback, raise concerns, or report harms from the AI system must be implemented and documented. This mechanism must:
   - Be accessible to the user population (not require technical knowledge to use)
   - Have a defined response process with SLA (feedback acknowledged within 5 business days)
   - Feed into the quarterly AI Risk Committee review as a monitoring input

**Evidence required:** Stakeholder engagement record in AI Impact Assessment; post-deployment feedback channel documentation in system card.

---

### 16.2.3 Structured Field Testing for Tier 1 Systems (N700-01 / N-ARIA-01)

**Gap identified by:** NIST AI 700-2, ARIA Companion Document (2 sources).

**Addition to Tier 1 Assurance Evidence Pack (extends Part VII §7.3):**

Before production deployment, Tier 1 AI systems with significant end-user interaction volume must complete **structured field testing** with representative end-users in addition to red-team adversarial testing. Field testing requirements:

| Field Testing Requirement | Specification |
|---|---|
| **User type** | Non-adversarial users representative of the intended deployment population (not red teamers or technical staff) |
| **Interaction mode** | Realistic use-case scenarios drawn from the AI Use Case Registration (Deliverable G §G.5) intended use cases |
| **Minimum sessions** | At least 20 unique user sessions covering the primary use case scenarios |
| **Post-session capture** | Structured post-session questionnaire capturing: task completion, AI output utility, unexpected behavior observed, trust calibration |
| **Analysis** | Findings documented in a field testing report; material gaps between field testing behavior and pre-deployment testing findings require investigation before deployment approval |

**Evidence required:** Field testing report added to Tier 1 assurance evidence pack. Field testing report is a mandatory gate item for Tier 1 systems with external user interaction.

**Scope exemption:** Tier 1 systems with no end-user interaction (e.g., back-office autonomous agents) are exempt from field testing; documented rationale for exemption required in system card.

---

### 16.2.4 EU AI Act Fundamental Rights Impact Assessment (N-OECD-01)

**Gap identified by:** OECD/EU AI Act crosswalk (EU AI Act Art. 27).

**Addition to Part IV §4.5 Regulatory Mapping — EU AI Act delta:**

For enterprises deploying Tier 1 AI systems to individuals in the European Union, the EU AI Act Article 27 Fundamental Rights Impact Assessment (FRIA) is required for deployers (as defined in Art. 3(4)) of high-risk AI systems listed in Annex III.

| FRIA Requirement | EAGCF Implementation |
|---|---|
| Identify use description and relevant fundamental rights affected | AI Use Case Registration §G.5 (extend to include fundamental rights impact field) |
| Describe risk assessment steps taken | AI Impact Assessment §G.3 (extend framing to include rights-impact characterization) |
| Document mitigation measures | AI Impact Assessment §G.3 — control mapping section |
| Named deployer with accountability | System card — System Owner |
| Where required by Member State: notification to market surveillance authority | Legal responsibility — outside EAGCF governance scope; Legal must track per deployment jurisdiction |

**Evidence required for EU-scoped Tier 1 systems:** FRIA documentation as a supplement to the standard AI Impact Assessment, cross-referencing EAGCF §G.3 sections to Art. 27.2 fields.

*Note: FRIA obligation applies to the deployer role. If the enterprise is acting only as a developer (as defined under EU AI Act), consult Legal for applicable obligations under Arts. 16–25.*

---

## 16.3 Concern-Raising and Whistleblower Pathway (N801-06)

**Gap identified by:** NIST AI 800-1, Google DeepMind RMF template (2 sources).

**Addition to Part IV §4.4 (Exception and Waiver Model) — extend to include concern-raising:**

### AI Concern-Raising Pathway

Beyond the formal exception/waiver process, the enterprise must provide a **documented pathway for employees to raise AI-related concerns** — including concerns about AI system behavior, governance control circumvention, ethical concerns, or safety observations — without requiring them to use the formal exception process or escalate through their direct management chain.

**Concern-raising pathway requirements:**

| Element | Requirement |
|---|---|
| **Channel** | Dedicated AI concern-reporting mechanism, distinct from general IT helpdesk and general compliance hotline. May be implemented via existing ethics hotline if AI-specific routing is added. |
| **Confidentiality** | Reports may be submitted anonymously (where legally permissible in the applicable jurisdiction). Named reporters receive confirmation of receipt and outcome within 30 days. |
| **Non-retaliation** | Explicit non-retaliation protection for good-faith AI concern submissions, consistent with applicable employment law. Non-retaliation policy documented and communicated to all employees with AI governance responsibilities. |
| **Review process** | All submissions reviewed by the AI Governance Office (or the Chief Ethics Officer where that function exists) within 5 business days. Material concerns escalated to the AI Risk Committee. |
| **Tracking** | All submissions logged in a concern register (separate from the exception register). Quarterly trend report to AI Risk Committee. Concern closure rate and average resolution time reported as KPIs. |
| **Scope** | Covers: AI system behavior concerns; governance control bypass observations; ethical concerns about AI use case or output; third-party AI vendor behavior concerns; safety observations |

**Evidence required:** Documented concern-raising mechanism (policy and channel specification); concern register; non-retaliation policy acknowledgment record for AI governance team.

---

## 16.4 External AI Incident Reporting (N801-07 / N600-05)

**Gap identified by:** NIST AI 800-1, NIST AI 600-1, Google DeepMind RMF template (3 sources).

**Addition to Part VII §7.2 (Incident Taxonomy) — external reporting requirement:**

### AI Incident External Reporting Obligation

For Severity 1 (S1 — Critical) AI incidents involving Tier 0/1 systems:

| Reporting Obligation | Requirement |
|---|---|
| **Regulatory notification** | Legal and Compliance must assess regulatory notification requirements within 24 hours of S1 incident classification. Applicable notification windows vary by jurisdiction and sector (EU AI Act Art. 73; GDPR Art. 33; sector-specific requirements). |
| **AI incident database** | For confirmed S1 AI incidents that do not require regulatory suppression, the enterprise should contribute an anonymized incident record to a recognized AI incident repository (AIID — AI Incident Database at incidentdatabase.ai; or CISA AI-ISAC when operational). Contribution is recommended, not mandatory, unless required by sector regulation. |
| **AI-ISAC participation** | Enterprises classified as critical infrastructure operators should subscribe to DHS AI Information Sharing and Analysis Center (AI-ISAC) when operational and report AI-specific vulnerability and incident data per AI-ISAC protocols. |

**Internal incident taxonomy addition** — extend the incident category table in Part VII §7.2:

| Category | Definition | Examples |
|---|---|---|
| **Deepfake fraud incident** | AI-generated synthetic media (voice, video, image) used to impersonate individuals for fraud, social engineering, or unauthorized authentication | Voice cloning used for executive impersonation to authorize wire transfers; video deepfake used to bypass identity verification; AI-generated phishing using executive likeness |

**Escalation for deepfake fraud incidents:** Classify as S1 (if financial loss or authentication bypass confirmed) or S2 (if attempt detected and blocked). Mandatory escalation to CISO + Legal within 1 hour of S1 classification.

---

## 16.5 Environmental Impact Monitoring Signals (N-06 / N600-01)

**Gap identified by:** NIST AI 600-1, NIST AI 100-5, Google DeepMind template, AI Verify crosswalk (4 sources).

**Addition to Deliverable E — Runtime Monitoring Signal Catalog:**

| Signal ID | Signal | Definition | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Escalation threshold |
|---|---|---|---|---|---|---|---|
| MON-21 | **Compute energy consumption** | Total energy consumption (kWh) for inference workloads per AI system, measured at the infrastructure layer. Baseline established at deployment; deviations tracked. | Monthly | Quarterly | Annual | Not required | >50% baseline deviation triggers cost and efficiency review |
| MON-22 | **Inference carbon estimate** | Estimated CO₂-equivalent emissions per inference workload, calculated from energy consumption and grid carbon intensity of the compute region. | Monthly | Quarterly | Not required | Not required | Material increases trigger infrastructure or optimization review |

*Note: Environmental monitoring is currently a recommended practice, not a mandatory control. It becomes mandatory for enterprises with public ESG reporting obligations or Tier 1 AI systems in jurisdictions with AI environmental disclosure requirements (e.g., EU sustainability reporting requirements where AI compute is material).*

---

## 16.6 Operational Risk Monitoring Signal Extensions

### Over-Reliance Monitoring (N-ARIA-02)

**Gap identified by:** ARIA Program Companion Document.

| Signal ID | Signal | Definition | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Escalation threshold |
|---|---|---|---|---|---|---|---|
| MON-23 | **User over-reliance signal** | Rate of AI interactions where human users accepted AI output without observable review or challenge — measured via: absence of follow-up questions, direct downstream action within <5 seconds of AI response, override rate decline trend over a rolling 30-day window | Continuous (where user interaction logging exists) | Monthly | Not required | Not required | Override rate decline >20% from 90-day baseline triggers model performance review and HITL configuration review |

### Epistemic Overconfidence Monitoring (N-ARIA-03)

| Signal ID | Signal | Definition | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Escalation threshold |
|---|---|---|---|---|---|---|---|
| MON-24 | **Epistemic overconfidence rate** | Rate of AI outputs expressing high confidence (via language markers: "definitely", "certainly", "I am certain", numeric confidence >90%) on topics classified as uncertain, contested, or outside the model's known competency boundary. Distinct from factual error detection (MON-05) — this signal targets calibration failure, not factual incorrectness. | Continuous | Continuous | Not required | Not required | Rate >defined threshold triggers output monitoring review; calibration testing to be added to next red-team cycle |

---

## 16.7 Model Supply Chain and Provenance Enhancements

### 16.7.1 AI Software Bill of Materials — SBOM (N1005-02)

**Gap identified by:** NIST AI 100-5, NIST AI 600-1 (2 sources).

**Extension to Domain 11 (Model Supply Chain) — new control MSC-09:**

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| MSC-09 | **AI Software Bill of Materials (AI-SBOM)** — For Tier 1 and Tier 2 AI systems using third-party models, fine-tuned models, or models with significant training data lineage complexity, an AI-SBOM is produced documenting: (1) base model identifier, version, and source; (2) training data sources (to the extent disclosed by the model provider); (3) third-party components integrated in the AI pipeline (retrieval systems, tool libraries, safety classifiers, embedding models); (4) fine-tuning or RLHF data summary (where enterprise-controlled). The AI-SBOM is maintained in the model card (MDL-05) and updated at each material component change. | P | Model Owner + System Owner | AI-SBOM artifact (structured or document form); model card — AI-SBOM section | Completeness audit at each model version update |

### 16.7.2 Watermarking Quality Requirements (N1004-01)

**Gap identified by:** NIST AI 100-4, NIST AI 100-5 (2 sources).

**Extension to Domain 11 control MSC-05 (Model Watermarking):**

Where watermarking is implemented (for enterprise-produced or fine-tuned model outputs), the watermarking implementation must be validated against the following quality attributes before production use:

| Quality Attribute | Requirement |
|---|---|
| **Robustness** | Watermark survives standard post-processing operations (compression, format conversion, paraphrasing for text). Test against defined set of post-processing operations at validation. |
| **Imperceptibility / low distortion** | Watermark does not materially degrade output quality as assessed by the output quality metrics defined for the system. |
| **Capacity** | Watermark carries sufficient information to identify the originating system and output timestamp at minimum. |
| **Security** | Watermark is resistant to known removal attacks for the threat model applicable to the system. For systems where adversarial watermark removal is a realistic threat, adversarial watermark removal testing is included in the red-team pipeline. |
| **Efficiency** | Watermarking adds no more than defined latency overhead to output generation (threshold set at design time). |

**Reference standards:** C2PA (Coalition for Content Provenance and Authenticity) specification for interoperable content provenance; SMPTE ST 2120 for media watermarking.

### 16.7.3 Content Provenance — C2PA Reference (N1004-02)

**Gap identified by:** NIST AI 100-4, NIST AI 100-5, NIST AI 600-1 (3 sources).

**Extension to Domain 7 (Output Controls) — new control OUT-08:**

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| OUT-08 | **Content provenance credentials** — For Tier 1 and Tier 2 AI systems producing synthetic or AI-assisted content for external distribution (images, video, audio, documents, or text published under the enterprise's brand), the enterprise evaluates adoption of the C2PA (Coalition for Content Provenance and Authenticity) specification for attaching verifiable provenance credentials to AI-generated content. For systems where content authenticity verification is a user-facing commitment or regulatory requirement, C2PA or equivalent interoperable provenance standard adoption is mandatory. For other systems, C2PA adoption is recommended and the decision to adopt (or rationale for non-adoption) is documented in the system card. | P | System Owner + Legal | System card — content provenance approach; C2PA implementation record (where adopted); decision rationale (where not adopted) | — |

### 16.7.4 Deepfake Fraud as Explicit Threat Category (N8596-01)

**Gap identified by:** NIST IR 8596 (Cyber AI Profile), NIST AI 100-4 (2 sources).

**Extension to Domain 11 (Model Supply Chain) — new control MSC-10:**

| Control ID | Control | Type | Owner | Evidence | Monitoring signal |
|---|---|---|---|---|---|
| MSC-10 | **AI-powered impersonation and deepfake fraud controls** — For enterprises operating AI systems with voice, video, or face interaction capabilities, and for any enterprise where AI-enabled impersonation fraud is in scope of the threat model (financial services, executive communications, customer authentication), explicit controls are implemented to detect and prevent deepfake-based fraud: (1) Executive voice and video authentication protocols that do not rely solely on audio/video for authorization of high-value transactions; (2) Liveness detection controls for AI-integrated identity verification systems; (3) AI-generated content detection at channels where external deepfake attacks are plausible (customer service voice lines, video calls for financial transactions); (4) Fraud escalation pathway for suspected deepfake impersonation events. | P+D | Security + Fraud + System Owner | Threat model entry for deepfake fraud; authentication protocol documentation; liveness detection configuration; detection capability test evidence | Deepfake detection events; liveness failure rate; suspected impersonation escalations |

---

## 16.8 Model Card Explainability Extension (N-09)

**Gap identified by:** NIST AI 100-1, NIST AI 100-5, OECD/EU AI Act crosswalk, AI Verify crosswalk, ISO 5339 (5 sources — highest corroboration count in comparison series).

**Extension to Part V Domain 3 (Model Controls) — MDL-05 (Model Card) mandatory fields:**

The model card (MDL-05) is extended with a mandatory explainability specification section:

| Required Explainability Field | Specification |
|---|---|
| **Explainability method** | The specific method(s) used to provide explanation of model decisions or outputs must be named (e.g., SHAP, LIME, counterfactual explanations, attention visualization, natural language explanation in output, human-readable decision tree approximation). "Inherently interpretable model" is an acceptable answer for simple models with documented justification. |
| **Explanation audience** | Who the explanation is designed for: (a) technical reviewers / model validators; (b) operational users (decision-makers using AI output); (c) end-users or affected individuals receiving AI-determined outcomes. For Tier 1 systems affecting individuals, explanation must be available at the affected-individual level. |
| **Explanation fidelity** | For post-hoc explanation methods: fidelity to underlying model behavior is assessed and documented (is the explanation an approximation or a ground-truth derivation?). Fidelity limitations are disclosed to explanation recipients. |
| **Regulatory compliance** | Where the applicable regulatory context requires explanations to affected individuals (EU AI Act Art. 13; GDPR Art. 22; US adverse action notice requirements), the explanation method must be capable of satisfying that obligation. Compliance confirmation documented in model card. |

*Note: This field is mandatory for Tier 1 systems (mandatory at pre-deployment gate) and recommended for Tier 2 systems. Tier 3/4 systems are exempt.*

---

## 16.9 Red-Team Attack Library Extension (N1002-01, N1004-05)

**Addition to Part XII §12.4 Red-Team Pipeline — Attack Library:**

The red-team attack library is extended with the following categories:

### MITRE ATLAS Integration (N1002-01)

MITRE ATLAS (Adversarial Threat Landscape for Artificial Intelligence Systems) is incorporated as a normative reference alongside NIST AI 100-2e2025 for the red-team attack library. ATLAS provides a tactic/technique taxonomy for AI adversarial attacks organized in a MITRE ATT&CK-compatible format.

**Implementation requirement:** The red-team attack library must cross-reference applicable MITRE ATLAS techniques for each attack category. At minimum, the following ATLAS tactics must be represented in the attack library for Tier 1 systems:

| ATLAS Tactic | Attack Library Coverage |
|---|---|
| **ML Attack Staging** | Reconnaissance against AI system capabilities; API probing |
| **ML Model Access** | Model extraction; inversion attacks against Tier 1 decision models |
| **Craft Adversarial Data** | Evasion attacks; data poisoning; backdoor triggers |
| **Exfiltration via ML Inference** | Membership inference; training data extraction |
| **Impact** | Model performance degradation; denial-of-model-service |

**Reference:** MITRE ATLAS at atlas.mitre.org; cross-mapped to NIST AI 100-2e2025 NISTAML attack identifiers.

### Audio Deepfake Detection (N1004-05)

For Tier 1 systems with voice interaction, voice synthesis, or voice cloning capabilities, the following attack categories are added to the red-team attack library:

| Attack Category | Description | Test requirement |
|---|---|---|
| **Voice cloning impersonation** | Synthetic voice generation mimicking authorized individual (executive, administrator, customer) to bypass voice-based authentication or authorization | Test voice authentication/authorization systems against synthetic voice samples generated by state-of-the-art TTS and voice cloning systems |
| **Text-to-speech injection** | Audio input crafted to trigger specific AI behaviors (analogous to adversarial audio perturbations) | Test STT → LLM pipeline for adversarial audio inputs |
| **Deepfake audio in enterprise communication channels** | AI-generated audio in phone/video calls for social engineering or authorization fraud | Test detection capability of any deployed audio authentication or liveness detection systems |

**Evidence required:** Audio deepfake test results added to red-team report for applicable Tier 1 systems.

---

## 16.10 NIST AI RMF Self-Assessment Checklist (N-DM-01)

**Gap identified by:** Google DeepMind RMF gap analysis template.

EAGCF users seeking to demonstrate NIST AI RMF 1.0 compliance using EAGCF as the implementation vehicle may use the following self-assessment mapping as evidence of subcategory-level coverage. This checklist maps each AI RMF subcategory to the primary EAGCF control or governance element that addresses it.

| AI RMF Subcategory | Primary EAGCF Location | Evidence Artifact |
|---|---|---|
| **GOVERN 1** — Policies, processes, procedures across organization | Part IV (governance framework); Part VI (operating model) | AI governance policy; framework document |
| **GOVERN 2** — Accountability structures | Part VI §6.4 (RACI); Part VI §6.2 (governance office) | RACI matrix; governance org chart |
| **GOVERN 3** — Workforce diversity, equity, inclusion | Part XVI §16.2.1 (team diversity gate); Part V §5.8 (FAI domain) | System card team composition; fairness assessment |
| **GOVERN 4** — Organizational culture | Part VIII §8.3 (workforce enablement); Deliverable H | Training records; adoption metrics |
| **GOVERN 5** — Robust stakeholder engagement | Part XVI §16.2.2 (stakeholder feedback); Part IV §4.3 | Stakeholder engagement record; feedback channel documentation |
| **GOVERN 6** — Third-party / supply chain policies | Part V §5.9 (VND domain); Part V §5.11 (MSC domain) | Vendor assessment records; AI-SBOM (MSC-09) |
| **MAP 1** — Context established | Deliverable G §G.5 (AI Use Case Registration) | Completed registration form |
| **MAP 2** — AI system categorization | Deliverable B (risk-tiering model); Deliverable G §G.5 | Risk tier classification record |
| **MAP 3** — Capabilities, usage, benefits and costs | Deliverable G §G.5; Part V §5.3 (MDL-05 model card) | Use case registration; model card |
| **MAP 4** — Risks and benefits mapped | Deliverable G §G.3 (AI Impact Assessment) | Impact assessment report |
| **MAP 5** — Impacts characterized | Deliverable G §G.3; Part IV §4.1 (risk tiering) | Impact assessment report; risk tier record |
| **MEASURE 1** — Methods and metrics identified | Part VII §7.2 (KPI/KRI/KCI framework); Deliverable E | KPI/KRI dashboard; monitoring signal catalog |
| **MEASURE 2** — Trustworthy characteristics evaluated | Part XII §12.2 (control validation matrix); Part V (15 control domains) | Control validation report; red-team report |
| **MEASURE 3** — Risk tracking over time | Deliverable E (runtime monitoring); Part VII §7.1 (KRI) | Monitoring dashboard; KRI reports |
| **MEASURE 4** — Feedback about measurement efficacy | Part VII §7.4 (corrective action); Part VI §6.6 (review cadences) | Corrective action records; governance review minutes |
| **MANAGE 1** — Risks prioritized and responded to | Part IV §4.1 (5-tier model); Part VII §7.3 (incident taxonomy) | Risk tier record; incident response records |
| **MANAGE 2** — Strategies to maximize benefits | Part VIII (adoption acceleration); Part XI (enforcement architecture) | Adoption metrics; enforcement configuration |
| **MANAGE 3** — Third-party risks managed | Part V §5.9 (VND domain); Part V §5.11 (MSC domain) | Vendor assessment records |
| **MANAGE 4** — Risk treatments documented and monitored | Part VII §7.4 (corrective action); Part VI §6.6 (review cadences) | Corrective action log; review cadence records |

*Full self-assessment: Use this table in conjunction with the Google DeepMind NIST AI RMF Gap Analysis template structure (Do we do this already? / Which team? / How?) to produce an evidence-backed RMF compliance self-assessment.*

---

## Appendix — Version History (Updated)

| Version | Date | Changes |
|---|---|---|
| 1.0 | April 2026 | Initial framework (Parts I–X, Deliverables A–H) |
| 1.1 | April 2026 | Added Parts XI–XIV: Control Implementation Architecture; Control Validation and Red-Teaming System; Developer Workflow Integration; Governance Cost Model; Enhanced Vendor Governance |
| 1.2 | April 2026 | Added Part XV: 13 supplementary controls (SOC-01/02, PRM-09, TOL-08, OUT-07, AGT-10, MSC-07/08, CBJ-05, SEC-01) and 3 validation extensions (backdoor testing, cryptographic artifact verification, alignment verification) and 2 new monitoring signals (MON-19/20), derived from AIUC-1 crosswalk reconnaissance across NIST AI RMF, ISO 42001, EU AI Act, OWASP LLM Top 10, OWASP AIVSS, MITRE ATLAS, IBM AI Risk Atlas, Cisco AI Security Framework, and CSA AI Controls Matrix |
| 1.3 | April 2026 | Added Part XVI: Gap closure from 20-source comparative framework analysis. Addresses Tier A (high priority) and Tier B (medium priority) gaps. Additions: standards watch register (N-AP-03, N1005-01); Tier 1 gate enhancements for interdisciplinary team diversity (N-01), external stakeholder feedback (N-02/N-03), structured field testing (N700-01), EU AI Act FRIA (N-OECD-01); concern-raising and whistleblower pathway (N801-06); external AI incident reporting (N801-07) and deepfake fraud incident category (N8596-01); environmental monitoring signals MON-21/22 (N-06); operational risk signals MON-23 (over-reliance, N-ARIA-02) and MON-24 (epistemic overconfidence, N-ARIA-03); supply chain enhancements: AI-SBOM (MSC-09, N1005-02), watermarking quality requirements (MSC-05 extension, N1004-01), C2PA provenance (OUT-08, N1004-02), deepfake fraud controls (MSC-10, N8596-01); model card explainability method specification (MDL-05 extension, N-09); red-team attack library extension: MITRE ATLAS integration (N1002-01), audio deepfake attacks (N1004-05); NIST AI RMF self-assessment checklist (N-DM-01) |

**Next review date:** April 2027 or at material regulatory change, whichever is earlier.

---

*© Enterprise. Internal governance document. Not for external distribution without authorization.*








