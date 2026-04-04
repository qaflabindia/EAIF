# Side-by-Side Comparison: EAGCF vs. NIST AI 800-2 IPD
## *Practices for Automated Benchmark Evaluations of Language Models*

**NIST Document:** NIST AI 800-2 (Initial Public Draft, January 2026)
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** NIST AI 800-2 is a specialized measurement science document focused on benchmark evaluation methodology for language models and AI agents. It does not function as a governance framework; it provides practices for how to *design, run, analyze, and report* AI evaluations rigorously. The primary EAGCF coverage zone is Parts XII (Control Validation), XIV (Cost Model), and VII (Monitoring/Assurance).

---

## 1. Document Scope Alignment

| Dimension | NIST AI 800-2 | EAGCF |
|---|---|---|
| **Primary audience** | AI evaluators, ML engineers, safety teams | Board, CRO, AI governance office, internal audit |
| **Primary function** | Evaluation methodology specification | Enterprise governance and control operating model |
| **Coverage depth** | Deep on evaluation methodology; silent on governance | Deep on governance; moderate on evaluation methodology |
| **Agentic scope** | Includes agentic evaluation specifics (agent budgets, sandboxing, execution environments) | Covers agentic governance and control extensively (Domain 10, Archetypes 5–6) |
| **Regulation** | Voluntary US guidance | Voluntary enterprise standard (regulatory-defensible) |
| **Certification** | No certification path | Wired to ISO/IEC 42001 certification path |

---

## 2. Three-Stage Evaluation Process vs. EAGCF Control Validation

NIST AI 800-2 structures evaluation across three stages. The table below maps each stage to EAGCF.

### Stage 1: Define Evaluation Objectives and Select Benchmarks

| NIST AI 800-2 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **1.1** — Define evaluation objectives (intended use, measurement construct) | Part XII §12.2 (Control Validation Matrix); MDL-04 (model performance baseline) | ⚠️ Partial | EAGCF specifies *what* to test; does not require pre-registration of evaluation objectives before testing |
| **1.2** — Select benchmarks: survey, assess relevance, suitability, quality | Part XII §12.3 (tooling: PyRIT, Garak, PromptBench); MDL-05 (model card) | ⚠️ Partial | EAGCF specifies tooling categories but not benchmark selection criteria (contamination risk, difficulty, baseline availability) |
| Benchmark suitability: direct vs. proxy vs. predictive measures | Not addressed | ❌ Gap | EAGCF does not distinguish between direct measurement, proxy tasks, and downstream outcome prediction as evaluation design choices |
| Training data contamination risk assessment | Not addressed | ❌ Gap | EAGCF covers data lineage (MSC-01/02) but not benchmark contamination as a distinct evaluation validity threat |
| Pre-registration of evaluation decisions | Not addressed | ❌ Gap | No requirement to document and lock benchmark selection decisions before evaluation execution |

### Stage 2: Implement and Run Evaluations

| NIST AI 800-2 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **2.1** — Design evaluation protocol (comparability, external validity, cost control, performance optimization) | Part XII §12.1 (red-team pipeline); Part XIV §14.1 (SLA model) | ⚠️ Partial | EAGCF addresses red-teaming and performance SLAs; does not formalize an *evaluation protocol* with inference, scaffolding, task, and scoring settings |
| Inference settings (temperature, reasoning effort, sampling) | Not addressed | ❌ Gap | EAGCF does not specify inference setting governance for evaluation contexts |
| Scaffolding settings (safeguards on/off, provider, agent budget, prompts, tools, execution environment) | Part XI §11.2 (enforcement point architecture); Domain 4 (PRM), Domain 6 (TOL) | ⚠️ Partial | EAGCF governs scaffolding in production; does not address scaffolding configuration *for evaluation purposes* specifically |
| Agent budget controls for agentic evaluations | Part V §5.10 (AGT-03: action scope limits); Part XI §11.4 (agentic data plane stack) | ✅ Covered | EAGCF's agentic action scope limits and reversibility classification cover this intent |
| Scoring settings (LLM-as-judge governance) | Not addressed | ❌ Gap | No governance for LLM-as-judge quality, interrater agreement, or judge prompt testing |
| **2.2** — Write evaluation code (frameworks, parsers, benchmark versioning, sandboxing, modularity) | Part XII §12.3 (tooling); Part XI §11.7 (sandbox/isolation reference) | ⚠️ Partial | EAGCF references tool categories; lacks benchmark versioning as a governed artifact class |
| Benchmark versioning with semantic version control | Part V §5.13 (CHG-01: change records) | ⚠️ Partial | General change management covers this partially; no specific benchmark versioning requirement with major/minor/patch semantics |
| Sandboxing agents during evaluation | Part XI §11.4 (agentic data plane); Part V §5.10 (AGT-05) | ✅ Covered | EAGCF's isolation controls for agentic systems cover evaluation sandboxing intent |
| **2.3** — Run evaluation and track results (log management, model version tagging, metadata) | Part V §5.14 (LOG-01 through LOG-05); Part VII §7.1 (Deliverable E) | ✅ Covered | EAGCF's logging domain and monitoring signal catalog cover log completeness, version tagging, and metadata requirements |
| **2.4** — Debug evaluation (degraded serving, tool call errors, refusal behavior, evaluation cheating, evaluation awareness) | Part XII §12.4 (degradation detection); Part V §5.15 (GEN-07: jailbreak pattern library) | ⚠️ Partial | EAGCF covers degradation detection and jailbreak patterns; does not specifically address *evaluation* validity threats (cheating, evaluation awareness) |
| Evaluation cheating detection (solution contamination, grader gaming) | Part V §5.4 (PRM-05: prompt injection) | ⚠️ Partial | Injection detection is present; grader gaming and evaluation awareness as distinct evaluation validity threats are not |
| Evaluation awareness as external validity threat | Not addressed | ❌ Gap | EAGCF does not address the possibility that models behave differently when they detect they are being evaluated |

### Stage 3: Analyze and Report Results

| NIST AI 800-2 Practice | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **3.1** — Statistical analysis and uncertainty quantification (confidence intervals, sources of variation, statistical tests) | Part XIV §14.2 (performance SLA table); Part VII §7.2 (KPI/KRI framework) | ⚠️ Partial | EAGCF defines performance thresholds and KPIs; does not require formal statistical uncertainty quantification (confidence intervals, interrater agreement) |
| Pre-defined analysis procedure aligned with objectives | Part VII §7.1 (monitoring signal catalog); Part XII §12.2 (control validation matrix) | ⚠️ Partial | Monitoring signals and control validation procedures exist; formal pre-registration of statistical analysis method not required |
| Decompose and report variance sources separately | Not addressed | ❌ Gap | EAGCF does not distinguish model sampling variance from benchmark item sampling variance in evaluation reporting |
| **3.2** — Share evaluation details and data (transparency, cost reporting, transcript release, code publication) | Part V §5.14 (LOG); Part IX §9.3 (Microsoft Transparency Notes) | ⚠️ Partial | Logging requirements exist; no specific transparency requirements for *evaluation* reporting (benchmark version, protocol settings, costs alongside performance) |
| Report costs alongside performance | Part XIV §14.3 (ROI metrics); Part XIV §14.4 (vendor cost model) | ⚠️ Partial | Financial cost modelling present; no requirement to report inference costs co-located with evaluation performance results |
| Release evaluation transcripts (with contamination controls) | Not addressed | ❌ Gap | EAGCF has no transcript retention and controlled release policy for evaluation outputs |
| Publish evaluation code | Part XIII §13.2 (CI/CD governance-as-code) | ⚠️ Partial | Code management present; no specific requirement to publish evaluation code for reproducibility |
| **3.3** — Report qualified claims (distinguish observation vs. inference vs. prediction; generalization caveats; evaluation awareness impact) | Part IV §4.3 (transparency requirements); Part V §5.7 (OUT-04: output labeling) | ⚠️ Partial | Output transparency requirements exist; no structured claim qualification framework for evaluation reports |

---

## 3. EAGCF Agentic Evaluation Controls vs. NIST AI 800-2 Agent-Specific Guidance

NIST AI 800-2 introduces several agent-specific evaluation concerns. The table below maps these to EAGCF.

| NIST AI 800-2 Agent-Specific Item | EAGCF Control | Status |
|---|---|---|
| Agent budget (resource limits for indefinite runs) | AGT-03 (action scope limits), AGT-06 (HITL threshold) | ✅ Covered |
| Execution environment (Docker, VM, networked) isolation | Part XI §11.4 (agentic data plane stack) | ✅ Covered |
| Scaffolding variability (ReAct, Claude Code, etc.) as evaluation setting | Part V §5.10 (AGT controls for multi-agent trust) | ⚠️ Partial |
| Cost-control for agentic evaluations (prevent infinite runs) | AGT-03 | ✅ Covered |
| Tool affordances as evaluation variable (internet search cheating) | TOL-01 through TOL-07 | ✅ Covered |
| Context-compression decision as scaffolding variable | Not addressed | ❌ Gap |
| Evaluation cheating in flexible coding agents | PRM-05 (injection), GEN-07 (jailbreak) | ⚠️ Partial |

---

## 4. EAGCF Control Validation vs. NIST AI 800-2 Quality Assurance Techniques

| NIST AI 800-2 QA Technique | EAGCF Coverage | Status |
|---|---|---|
| Manual transcript review (detect unexpected behaviors, diagnose bugs) | Part XII §12.1 (red-team pipeline: classifier stage) | ✅ Covered |
| Automated transcript review (LLM-based analysis, tool call error rates) | Part XII §12.2 (automated red-team runner); GEN-08 (output monitoring) | ✅ Covered |
| Task review (instruction clarity, multiple reviewers) | Part VI §6.4 (AI governance office review); Part IV §4.7 (exception model) | ⚠️ Partial |
| Comparison to existing evidence (baseline comparison, developer-reported numbers) | MDL-04 (performance baseline); Part XIV §14.4 (vendor benchmarks) | ✅ Covered |
| Item pattern analysis (empirical structure validation) | Not addressed | ❌ Gap |

---

## 5. Scoring Summary

| NIST AI 800-2 Section | Practices | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| Stage 1: Objectives and Benchmark Selection | 5 items | 0 | 0 | 2 | 3 |
| Stage 2: Implementation and Running | 14 items | 3 | 0 | 7 | 4 |
| Stage 3: Analysis and Reporting | 10 items | 1 | 0 | 6 | 3 |
| Agent-Specific Items | 7 items | 3 | 0 | 2 | 2 |
| QA Techniques | 5 items | 3 | 0 | 2 | 0 |
| **TOTALS** | **41 items** | **10 (24%)** | **0 (0%)** | **19 (46%)** | **12 (29%)** |

**Coverage interpretation:** NIST AI 800-2 is a specialized measurement science document. EAGCF was not designed as a benchmark evaluation methodology guide; it was designed as a governance and control operating model. The 29% gap rate reflects genuine evaluation methodology gaps (statistical rigor, protocol formalization, transparency in reporting) rather than governance design flaws. Conversely, EAGCF provides extensive governance context that NIST AI 800-2 entirely lacks.

---

## 6. Where EAGCF Materially Exceeds NIST AI 800-2

| Dimension | EAGCF Capability | NIST AI 800-2 |
|---|---|---|
| **Governance operating model** | 9 governance bodies, RACI, decision rights, review cadences | Not addressed |
| **Risk tiering** | 5-tier model (Prohibited → Low) wired to lifecycle gate intensity | Not addressed |
| **Control taxonomy** | 15 domains, 97+ controls across preventive/detective/corrective | Not addressed |
| **Enforcement architecture** | 9 enforcement points (EP-1 through EP-9) with data plane design | Not addressed |
| **Agentic governance** | AGT-01 through AGT-10 (action scope, reversibility, inter-agent trust, HITL) | Budget and environment only |
| **Regulatory alignment** | EU AI Act, ISO 42001, SR 11-7, COBIT, COSO | Cites NIST AI 100-1 only |
| **Sector overlays** | Financial services, healthcare, safety-critical infrastructure | Not addressed |
| **Incident taxonomy** | 7 categories, 4 severity levels, escalation paths | Not addressed |
| **Vendor governance** | 6-dimension scoring model, multi-model fallback, behavioral fingerprinting | Not addressed |
| **Cost governance** | Time-to-approval SLAs, governance ROI metrics, misallocation diagnostic | Cost-performance reporting (narrow) |
| **Prompt governance** | System prompt registry, injection detection, jailbreak library | Refusal handling in evaluations only |
| **CI/CD integration** | 5-gate pipeline, 6 pre-commit hooks, shadow AI detection | Benchmark versioning only |

---

## 7. Gap Items: Recommended EAGCF Additions

The following gaps from NIST AI 800-2 represent genuine evaluation methodology requirements not currently addressed in EAGCF. These should be incorporated as additions to Part XII (Control Validation) and Part VII (Monitoring and Assurance).

| Gap ID | NIST AI 800-2 Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N800-01** | Practice 1.1 | **Evaluation objective pre-registration**: Require documentation and lock of evaluation construct, intended use, and comparison baselines *before* evaluation execution to prevent post-hoc result selection | High | Part XII §12.2 — add EVL-01 control |
| **N800-02** | Practice 1.2 | **Benchmark contamination assessment**: Require assessment of training data contamination risk for any benchmark used in model validation or procurement | High | Part V §5.3 MDL domain — add MDL-12 control |
| **N800-03** | Practice 2.1 | **Evaluation protocol specification**: Formalize evaluation protocol as a governed artifact with documented inference settings, scaffolding settings, task settings, and scoring settings | High | Part XII §12.2 — add to control validation matrix |
| **N800-04** | Practice 2.1 | **LLM-as-judge governance**: Require quality assurance for LLM-as-judge scoring (comparison to human judges, interrater agreement, judge prompt testing) when used in model evaluation or incident classification | Medium | Part XII §12.2; Part VII §7.3 (incident taxonomy) |
| **N800-05** | Practice 2.2 | **Benchmark versioning policy**: Require semantic versioning of evaluation benchmarks with major/minor/patch classification and change records | Medium | Part V §5.13 CHG domain — extend CHG-01 |
| **N800-06** | Practice 2.4 | **Evaluation awareness detection**: Include model evaluation-awareness as a validity threat in red-team pipeline; detect when models modify behavior upon detecting evaluation context | Medium | Part XII §12.1 — add to red-team attack library |
| **N800-07** | Practice 2.4 | **Grader gaming detection**: Include grader gaming (exploiting implementation loopholes) as a distinct attack class in agentic evaluation suites | Medium | Part XII §12.1 — add to attack library, agentic category |
| **N800-08** | Practice 3.1 | **Statistical uncertainty requirements**: Require confidence intervals or credible intervals alongside point estimates in model evaluation reports; require separation of model sampling variance from benchmark item variance | High | Part XII §12.2 — add statistical rigor requirement |
| **N800-09** | Practice 3.2 | **Evaluation transparency requirements**: Require evaluation reports to include benchmark version, protocol settings, cost alongside performance, and model exact version | Medium | Part XII §12.2 — extend control validation matrix reporting requirements |
| **N800-10** | Practice 3.2 | **Evaluation transcript retention and controlled release**: Define retention policy for evaluation transcripts; define conditions for internal and external release with contamination controls | Low | Part V §5.14 LOG domain — add LOG-06 |
| **N800-11** | Practice 3.3 | **Evaluation claim qualification standard**: Require evaluation reports to formally distinguish observations, inferences, predictions, and normative claims; add generalization caveats for out-of-distribution claims | Medium | Part XII §12.2 — add claim qualification template |
| **N800-12** | Practice 1.2 | **Benchmark selection documentation**: Require documented rationale for benchmark selection including suitability criteria (difficulty, baseline availability, test item format alignment to use case) | Low | Part VII §7.1 — add to assurance evidence pack |

---

## 8. Synthesis: Nature of the NIST AI 800-2 Relationship to EAGCF

NIST AI 800-2 and EAGCF are **complementary, non-competing documents** operating at different abstraction levels:

**EAGCF** answers: *How does an enterprise govern, control, assure, and monitor AI systems?*
**NIST AI 800-2** answers: *How does an evaluation team rigorously design, run, and report AI benchmark evaluations?*

The primary integration point is **EAGCF Part XII (Control Validation)**. EAGCF specifies *that* red-team pipelines, degradation detection, and tooling must exist; NIST AI 800-2 specifies *how* to run those evaluations with scientific rigor.

**Recommended integration posture:**
- Incorporate N800-01 through N800-05 (high/medium priority evaluation governance items) into EAGCF Part XII as formal control requirements
- Reference NIST AI 800-2 as the normative technical standard for evaluation methodology within EAGCF §12.3 (Tooling and Methodology Reference)
- Add evaluation protocol specification template to Deliverable G (Template G.14: Evaluation Protocol Specification)

**Coverage summary:**
- NIST AI 800-2 items with direct EAGCF coverage: **10 (24%)**
- NIST AI 800-2 items partially covered: **19 (46%)**
- NIST AI 800-2 items not addressed: **12 (29%)**
- Items where EAGCF materially exceeds NIST AI 800-2: **14 dimensions** (governance, controls, assurance, enforcement, sector overlays — NIST AI 800-2 is silent on all)

The partial coverage rate is high (46%) because EAGCF addresses evaluation *activities* (validation, monitoring, red-teaming) but lacks the formal *methodology* specification that NIST AI 800-2 provides. This is an evaluation rigor gap, not a governance design gap.

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Next comparison in sequence: NIST AI 800-1 IPD (Managing Misuse Risk for Dual-Use Foundation Models)*
