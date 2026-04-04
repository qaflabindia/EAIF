# Reconnaissance: Enterprise AI Governance and Control Framework
## vs. AIUC-1 Crosswalk Coverage

**Date:** April 2026
**Scope:** Comparison of the Enterprise AI Governance and Control Framework (EAGCF v1.1)
against all nine AIUC-1 crosswalk mappings published at aiuc-1.com/crosswalks
**Classification:** Internal — AI Governance Office

---

## 1. Executive Summary

AIUC-1 is the first enterprise-targeted **certifiable AI use certification standard**, built on six domains
(Data & Privacy, Security, Safety, Reliability, Accountability, Society) and cross-mapped against nine
external frameworks: NIST AI RMF, ISO 42001, EU AI Act, OWASP LLM Top 10, OWASP AIVSS,
MITRE ATLAS, IBM AI Risk Atlas, Cisco AI Security Framework, and CSA AI Controls Matrix.

This recon compares the EAGCF against AIUC-1's control set (49 controls, IDs A001–F002) and
identifies: (1) strong alignments, (2) areas where EAGCF is structurally stronger, (3) specific gaps in
EAGCF surfaced by AIUC-1's cross-framework coverage, and (4) recommended additions.

### Verdict

| Dimension | Finding |
|---|---|
| **Overall alignment** | Strong — EAGCF covers approximately 80% of AIUC-1 controls by intent, with greater depth in most domains |
| **Where EAGCF leads** | Governance operating model; risk-tiering with lifecycle wiring; prompt governance; RAG controls; agentic depth; model supply chain; developer integration; cost model |
| **Where AIUC-1 adds value** | Certifiability positioning; explicit external framework mapping; three specific control categories missing from EAGCF (technical disclosure limits, cloud/on-prem processing record, catastrophic misuse as a named control); adversarial ML mitigations from MITRE ATLAS; OWASP AIVSS agentic threat taxonomy |
| **Net gap count** | 7 specific control gaps and 6 adversarial ML mitigations not explicitly in EAGCF |
| **Recommended action** | Add 13 targeted controls to EAGCF; map existing EAGCF controls to AIUC-1 IDs for audit portability |

---

## 2. AIUC-1 Structure Summary

AIUC-1 organizes 49 controls across 6 domains:

| Domain | ID range | Control count | Domain purpose |
|---|---|---|---|
| Data & Privacy | A001–A007 | 7 | Data policies, PII prevention, IP protection, access limits |
| Security | B001–B009 | 9 | Adversarial testing, input filtering, access control, deployment protection |
| Safety | C001–C012 | 12 | Risk taxonomy, pre-deployment testing, harmful output prevention, third-party testing |
| Reliability | D001–D004 | 4 | Hallucination prevention, tool call restrictions, third-party tool testing |
| Accountability | E001–E017 | 17 | Failure plans, accountability assignment, vendor due diligence, logging, regulatory compliance, transparency |
| Society | F001–F002 | 2 | Cyber misuse prevention, catastrophic misuse prevention |

---

## 3. Control-by-Control Alignment Map

### Domain A — Data & Privacy

| AIUC-1 Control | AIUC-1 Description | EAGCF Equivalent | Alignment | Gap? |
|---|---|---|---|---|
| A001 | Input data policy | DAT-01 (data classification at intake) | ✅ Strong | No |
| A002 | Output data policy | OUT-05 (output logging); DAT-07 (retention) | ✅ Strong | No |
| A003 | Data collection limits; limit AI agent data collection | DAT-03 (data minimization); AGT-04 (session-scoped memory) | ✅ Strong | No |
| A004 | IP protection | OUT-04 (disclosure); GEN-02 (homogenization) | ⚠️ Partial | Partial — no specific IP violation prevention control in output layer |
| A005 | Prevent cross-customer data exposure | IAM-01 (RBAC); DAT-06 (output monitoring) | ✅ Strong | No |
| A006 | PII leakage prevention | DAT-06 (output monitoring); MON-15 (privacy leakage signal) | ✅ Strong | No |
| A007 | IP violation prevention in outputs | OUT-02 (content policy filter) | ⚠️ Partial | Partial — content policy filter covers this but IP is not named explicitly |

**Domain A summary:** 5 of 7 fully covered; 2 partial — IP-specific controls exist by intent but lack an explicit named IP prevention control in the output layer.

---

### Domain B — Security

| AIUC-1 Control | AIUC-1 Description | EAGCF Equivalent | Alignment | Gap? |
|---|---|---|---|---|
| B001 | Third-party adversarial robustness testing | Part XII (red-team pipeline); Section 12.3 (control validation matrix) | ✅ Strong | No |
| B002 | Detect adversarial input | PRM-06 (injection detection); PRM-07 (jailbreak library); MON-03 (injection signal) | ✅ Strong | No |
| B003 | Manage public release of technical information about AI stack | **NOT PRESENT** | ❌ Gap | **GAP — no control on limiting technical disclosure of AI architecture/model details** |
| B004 | Prevent AI endpoint scraping / extraction | IAM-01–05 (access controls); IAM-04 (service account governance) | ✅ Strong | No |
| B005 | Implement real-time input filtering | EP-2 (prompt middleware, Part XI); PRM-06 | ✅ Strong | No |
| B006 | Prevent unauthorized AI agent actions | AGT-01 (action authorization scope); TOL-01 (tool authorization) | ✅ Strong | No |
| B007 | Access control enforcement / access privileges | IAM-01–05 | ✅ Strong | No |
| B008 | Protect model deployment environment | MSC-03 (tamper-evidence); MSC-04 (quantization integrity); Part XI EP-1 | ✅ Strong | No |
| B009 | Limit output over-exposure / output verbosity control | OUT-01 (safety classifier); OUT-02 (content filter) | ⚠️ Partial | Partial — output limiting beyond safety/policy (e.g., limiting response detail to reduce model extraction) not explicit |

**Domain B summary:** 7 of 9 fully covered; 1 gap (B003 — technical disclosure limits); 1 partial (B009 — output verbosity restriction as extraction defense).

---

### Domain C — Safety

| AIUC-1 Control | AIUC-1 Description | EAGCF Equivalent | Alignment | Gap? |
|---|---|---|---|---|
| C001 | Define AI risk taxonomy | Deliverable B (5-tier risk model); Domain 1 (INT-03) | ✅ Strong | No |
| C002 | Pre-deployment testing | Deliverable D Stage 4 (validation gate); Part XII | ✅ Strong | No |
| C003 | Harmful output prevention | OUT-01 (safety classifier); OUT-02 (content filter); GEN-05 | ✅ Strong | No |
| C004 | Prevent out-of-scope outputs | PRM-04 (user prompt scope enforcement) | ✅ Strong | No |
| C005 | Prevent high-risk outputs | OUT-01; Tier 1 gate requirements | ✅ Strong | No |
| C006 | Prevent outputs containing vulnerable/malicious code | OUT-02 (content policy filter) | ⚠️ Partial | **Partial GAP — code-specific vulnerability in AI output (e.g., insecure code generation) not explicitly named** |
| C007 | Flag high-risk outputs for human review | MON-01 (policy violation); MON-02 (unsafe output); AGT-03 (HITL trigger) | ✅ Strong | No |
| C008 | Monitor AI risk categories | Deliverable E (18 runtime signals); Part IX monitoring sidecar | ✅ Strong | No |
| C009 | Enable real-time feedback and intervention / human-in-the-loop | AGT-03 (HITL thresholds); EP-8 (HITL queue, Part XI) | ✅ Strong | No |
| C010 | Third-party testing for harmful outputs | Part XII (red-team pipeline); adversarial test suite | ✅ Strong | No |
| C011 | Third-party testing for out-of-scope outputs | Part XII (scope enforcement testing in control validation matrix) | ✅ Strong | No |
| C012 | Third-party testing for cascading failures (agentic) | Part XII; AGT-06 (inter-agent trust isolation) | ⚠️ Partial | Partial — agentic cascading failure testing present but not an explicit standalone test type |

**Domain C summary:** 10 of 12 fully covered; 1 partial gap (C006 — AI-generated vulnerable code); 1 partial (C012 — cascading failure as explicit test category).

---

### Domain D — Reliability

| AIUC-1 Control | AIUC-1 Description | EAGCF Equivalent | Alignment | Gap? |
|---|---|---|---|---|
| D001 | Hallucination prevention | GEN-01 (confabulation controls); RET-06 (grounding validation) | ✅ Strong | No |
| D002 | Hallucination testing / third-party validation | Part XII (Section 12.3 — OUT-03 hallucination monitoring); control validation matrix | ✅ Strong | No |
| D003 | Tool call restrictions (unsafe tool calls) | TOL-01 (authorization); TOL-02 (least privilege); TOL-06 (validation before execution) | ✅ Strong | No |
| D004 | Third-party tool testing | Part XII (TOL-01 functional test) | ✅ Strong | No |

**Domain D summary:** 4 of 4 fully covered. No gaps.

---

### Domain E — Accountability

| AIUC-1 Control | AIUC-1 Description | EAGCF Equivalent | Alignment | Gap? |
|---|---|---|---|---|
| E001 | Failure plan — security breach | Section 7.2 (incident taxonomy S1-S4); incident response | ✅ Strong | No |
| E002 | Failure plan — harmful output | Section 7.2 (Safety incident category); Section 7.3 (post-incident requirements) | ✅ Strong | No |
| E003 | Failure plan — hallucination | Section 7.2 (Operational incident); MON-05 (hallucination signal) | ✅ Strong | No |
| E004 | Assign accountability (named owner per system) | Section 6.1 (Business Owner, Model Owner, System Owner); RACI; INT-05 | ✅ Strong | No |
| E005 | Assess cloud vs on-prem AI processing decision | CBJ-01 (inference routing); CBJ-02 (transfer mechanisms) | ⚠️ Partial | **Partial GAP — cloud vs on-prem processing decision assessment not an explicit standalone control** |
| E006 | Vendor due diligence | VND-01–07 (full vendor domain); Deliverable G.13 (vendor due diligence template) | ✅ Strong | No |
| E007 | Change approval documentation | CHG-04 (change approval gate); CHG-03 (system card update) | ✅ Strong | No |
| E008 | Internal review processes (internal audit) | Section 6.1 Internal Audit; annual governance audit | ✅ Strong | No |
| E009 | Monitor third-party access | VND-07 (annual vendor review); MON-17 (security misuse signal) | ✅ Strong | No |
| E010 | AI acceptable use policy | Deliverable G.1 (AI policy template); INT-02 (prohibited use block) | ✅ Strong | No |
| E011 | Record AI processing locations | CBJ-01 (routing constraints); CBJ-03 (output jurisdiction) | ⚠️ Partial | **Partial GAP — explicit "processing location record" artifact not defined; CBJ domain covers the concept** |
| E012 | Regulatory compliance documentation | Section 4.5 (regulatory mapping); Deliverable G.8 (evidence pack) | ✅ Strong | No |
| E013 | Quality management system (ISO 42001 equivalent) | ISO 42001 referenced as management system shell (Part III, Section 3.4) | ✅ Strong | No |
| E014 | Transparency reports (external-facing) | Deliverable G.12 (board/regulator reporting template) | ✅ Strong | No |
| E015 | Activity logging | LOG-01–05 (full logging domain); Domain 14 | ✅ Strong | No |
| E016 | AI disclosure mechanisms (user-facing) | OUT-04 (AI disclosure in outputs) | ✅ Strong | No |
| E017 | System transparency policy documentation | Deliverable G.1 (AI policy); Deliverable G.4 (system card) | ✅ Strong | No |

**Domain E summary:** 14 of 17 fully covered; 3 partial gaps (E005 — cloud/on-prem decision record; E011 — processing location record as explicit artifact).

---

### Domain F — Society

| AIUC-1 Control | AIUC-1 Description | EAGCF Equivalent | Alignment | Gap? |
|---|---|---|---|---|
| F001 | Cyber misuse prevention (prevent AI system use for attacks) | MON-17 (security misuse signal); INT-02 (prohibited use block) | ⚠️ Partial | **Partial GAP — cyber misuse as a distinct named preventive control not explicit; covered by monitoring and prohibited use but not as a proactive design control** |
| F002 | Catastrophic misuse prevention (CBRN, national security threats) | Tier 0 prohibited uses list (Part IV, Section 4.1 Deliverable B) | ⚠️ Partial | **Partial GAP — prohibited use list covers this but "catastrophic misuse" as a named control with specific design obligations (CBRN, WMD uplift prevention) not explicit** |

**Domain F summary:** 0 of 2 fully covered; both are partial. EAGCF has the substance (Tier 0 prohibitions + security misuse monitoring) but not the explicit named control design for cyber and catastrophic misuse as distinct preventive obligations.

---

## 4. Cross-Framework Gaps Surfaced by AIUC-1 Crosswalks

AIUC-1's nine crosswalks surface additional control obligations from source frameworks that are absent or weak in EAGCF.

### 4.1 From MITRE ATLAS Crosswalk

MITRE ATLAS defines 26 adversarial ML mitigations. AIUC-1 covers 15; 11 are unmapped. Of those 11, the following are relevant to EAGCF and currently absent:

| ATLAS ID | Mitigation | EAGCF coverage | Gap |
|---|---|---|---|
| AML-M0006 | Use ensemble of models to increase inference robustness | Not present | **Gap — no ensemble robustness design requirement** |
| AML-M0007 | Detect and remove poisoned training data | MSC-01 (lineage documentation) covers detection aspect partially | **Gap — active training data poisoning detection not explicit** |
| AML-M0008 | Validate AI models for backdoor triggers | Part XII covers robustness testing but backdoor specifically not named | **Gap — backdoor trigger testing as explicit validation step** |
| AML-M0010 | Preprocess all inference data to nullify adversarial perturbations | EP-2 (prompt middleware) covers filtering; pre-processing of non-text modalities absent | **Partial gap — non-text modality adversarial preprocessing not addressed** |
| AML-M0014 | Verify cryptographic checksum of all AI artifacts | MSC-03 (tamper-evidence) covers checksums but scope is open-weight only | **Gap — cryptographic artifact verification should apply to ALL models, not only open-weight** |
| AML-M0022 | Techniques to improve model alignment with safety/security policies | Referenced via ISO 42001 and training governance but no explicit EAGCF control | **Gap — alignment verification as a pre-deployment control** |

### 4.2 From OWASP LLM Top 10 Crosswalk

| OWASP Threat | Gap in EAGCF |
|---|---|
| LLM06:25 — Excessive Agency | AGT controls cover this well; no gap |
| LLM08:25 — Vector/Embedding Weaknesses | RET-01–07 covers this; no gap |
| LLM10:25 — Unbounded Consumption | MON-16 (cost runaway) exists but no **preventive** resource consumption control — rate limiting, query quotas, token budget enforcement not explicit | **Gap — token/resource consumption limits as preventive control** |

### 4.3 From OWASP AIVSS Crosswalk

AIUC-1's AIVSS mapping surfaces two gaps not explicitly in EAGCF:

| AIVSS Risk | EAGCF Gap |
|---|---|
| Agent Identity Impersonation | AGT-06 covers inter-agent trust isolation but **agent identity verification** (cryptographic identity assertion for agents) not explicit |
| Agent Memory and Context Manipulation (B008) | AGT-04/05 covers memory governance but **cross-session memory poisoning detection** not an explicit monitoring signal |

### 4.4 From Cisco AI Security Framework Crosswalk

Cisco's framework surfaces a coverage gap in EAGCF's approach to multi-modal attack surfaces:

| Cisco Technique | EAGCF Gap |
|---|---|
| AITech-1.4 Multi-Modal Injection | EAGCF addresses text-based injection (PRM-06) but does not address injection via image, audio, or document inputs — relevant for multi-modal LLMs | **Gap — multi-modal injection as a named threat and control** |
| AITech-13.1 Disruption of Availability | MON-16 (cost runaway) covers this partially; no explicit **denial-of-service resilience** control for AI endpoints | **Gap — AI endpoint availability control** |
| AITech-7.3 Data Source Abuse (RAG poisoning) | RET-04 (corpus content policy) partially covers this; active **corpus poisoning detection** not explicit | **Partial gap — active RAG corpus poisoning detection** |

### 4.5 From IBM AI Risk Atlas Crosswalk

IBM Risk Atlas surfaces the following unmapped risks not explicitly in EAGCF:

| IBM Risk Area | EAGCF Gap |
|---|---|
| IBM 17–22: Societal impacts (discrimination, dignity, agency, jobs, environment) | EAGCF's fairness controls (Principle 3) partially cover discrimination but societal/environmental/employment impacts are not named controls | Gap — within acceptable scope for an enterprise framework, but noted |
| IBM 23–28: Training data quality (representativeness, contamination, bias) | MSC-01 covers lineage; **training data quality assessment** as a pre-training or procurement-stage control not explicit | **Partial gap — training data quality assessment** |
| IBM 75–78: Explainability/attribution gaps | Decision-support archetype (Archetype 8) requires explainability but no cross-archetype **explainability standard** | Partial gap — explainability scoped to decision-support only |

### 4.6 From CSA AI Controls Matrix Crosswalk

CSA AICM surfaces infrastructure-layer gaps that are intentionally outside most AI governance frameworks but worth acknowledging:

| CSA Domain | EAGCF Position |
|---|---|
| BCR — Business Continuity | **Out of scope** for EAGCF (enterprise BCR program owns this); but AI system availability within BCR is not referenced | Note only — recommend BCR program references EAGCF system criticality tiers |
| Ethics committees | AIUC-1 does not require ethics committees; CSA AICM does. EAGCF has AI Risk Committee but not a named ethics committee. | **Judgment call** — AI Risk Committee can absorb ethics review function |

---

## 5. Where EAGCF Is Structurally Stronger Than AIUC-1

AIUC-1 is a certification standard (certifiable, auditable, concise). EAGCF is a full governance operating system. The following dimensions are materially stronger in EAGCF and have no AIUC-1 equivalent:

| EAGCF Capability | AIUC-1 Equivalent | EAGCF Advantage |
|---|---|---|
| 5-tier risk model bound to lifecycle gate intensity | C001 defines a risk taxonomy (no tiers, no lifecycle wiring) | EAGCF is operational; AIUC-1 classifies without treating |
| 11-stage lifecycle governance map (Deliverable D) | Pre-deployment testing (C002); some monitoring requirements | EAGCF covers full lifecycle with tier-specific gate intensity |
| Prompt governance as versioned artifact (Domain 4, PRM-01–08) | B002/B005 cover injection detection; B003 covers disclosure | EAGCF governs the prompt itself as an artifact; AIUC-1 governs threats to prompts |
| RAG-specific control domain (Domain 5, 7 controls) | LLM08 and B001/B002 partially address embedding weaknesses | EAGCF provides corpus-level governance; AIUC-1 does not |
| Agentic action governance (Domain 10, 9 controls) | B006 (unauthorized actions); AIVSS mapping | EAGCF covers reversibility, HITL thresholds, inter-agent trust, action chain audit; AIUC-1 covers perimeter |
| Model supply chain and provenance (Domain 11, 6 controls) | B008 (deployment environment); AML-M0014 (no AIUC-1 mapping) | EAGCF governs training data lineage, fine-tuning integrity, tamper-evidence; AIUC-1 does not |
| Cross-border jurisdiction (Domain 12) | E011 (processing location record) | EAGCF covers adequacy mechanisms, routing constraints, output jurisdiction; AIUC-1 records location only |
| Developer workflow integration (Part XIII) | Not present | EAGCF embeds governance in CI/CD and pre-commit hooks |
| Control implementation architecture (Part XI, 9 enforcement points) | Not present | EAGCF specifies WHERE each control lives in the stack |
| Control validation pipeline (Part XII) | C010–C012 (third-party testing) | EAGCF defines continuous automated red-team pipeline; AIUC-1 requires testing without specifying how |
| Governance cost model and SLAs (Part XIV) | Not present | EAGCF makes governance economics explicit and governable |
| Multi-model fallback architecture (Part XIV) | Not present | EAGCF covers vendor dependency resilience |
| Governance operating model variants (centralized/federated/hybrid) | Not present | EAGCF is operating-model-aware |
| RACI matrix (Part VI) | E004 assigns accountability (single control) | EAGCF provides full decision-rights and accountability matrix |
| Sector-specific overlays (Part VIII) | References sector legislation; no delta requirements | EAGCF provides delta requirements for financial services, healthcare, and safety-critical infrastructure |
| Governance misallocation diagnostic (Part VIII) | Not present | EAGCF explicitly diagnoses over-governance of low-risk and under-governance of high-risk |
| Board/committee structure (Part VI) | Not present | EAGCF defines Board, Executive AI Council, AI Risk Committee, Model Validation Function |

---

## 6. Summary Gap Table — EAGCF vs AIUC-1

The following 13 targeted additions would close the gaps surfaced by this recon.

| Gap ID | Gap description | Source framework | AIUC-1 control | Priority | Recommended EAGCF addition |
|---|---|---|---|---|---|
| GAP-01 | Technical disclosure limits — no control preventing public release of AI architecture, model details, or training information | MITRE ATLAS AML-M0001; AIUC-1 B003 | B003 | High | Add new control: SEC-01 (Technical AI Disclosure Limits) to Domain 8 or new Domain 16 |
| GAP-02 | Cloud vs on-prem AI processing decision record — no explicit standalone artifact | AIUC-1 E005 | E005 | Medium | Add CBJ-05 (AI Processing Location Decision Record) to Domain 12 |
| GAP-03 | AI-generated vulnerable code prevention — content policy filter does not name code security explicitly | AIUC-1 C006; OWASP LLM05 | C006 | High | Add OUT-07 (AI-Generated Code Security Control) to Domain 7 |
| GAP-04 | Cyber misuse prevention as a named preventive design control | AIUC-1 F001; Cisco AITech-18.1/18.2 | F001 | High | Add new Domain 16 Section: Societal Harm Controls (SOC-01: Cyber Misuse Prevention) |
| GAP-05 | Catastrophic misuse prevention — CBRN, WMD uplift explicitly named | AIUC-1 F002; IBM 60/65 | F002 | Critical | Extend Tier 0 prohibited list + add SOC-02 (Catastrophic Misuse Prevention) to Domain 16 |
| GAP-06 | Cryptographic artifact verification for ALL models (not only open-weight) | MITRE ATLAS AML-M0014 | None | Medium | Extend MSC-03 scope to cover all production models, not open-weight only |
| GAP-07 | Training data poisoning detection — active detection, not only lineage documentation | MITRE ATLAS AML-M0007; IBM 29 | None | High | Add MSC-07 (Training Data Poisoning Detection) to Domain 11 |
| GAP-08 | Backdoor trigger testing as explicit validation step | MITRE ATLAS AML-M0008 | None | High | Add to Part XII Section 12.3 control validation matrix: MDL validation — backdoor test |
| GAP-09 | Token/resource consumption limits as a preventive control (rate limiting, query quota, token budget) | OWASP LLM10; Cisco AITech-13.1 | B004 (partial) | Medium | Add TOL-08 (Resource Consumption Limits) to Domain 6 |
| GAP-10 | Multi-modal injection — image/audio/document injection surface | Cisco AITech-1.4; OWASP LLM04 | None | Medium | Add PRM-09 (Multi-Modal Input Injection Controls) to Domain 4 for applicable archetypes |
| GAP-11 | Agent identity verification — cryptographic identity assertion for agents in multi-agent systems | OWASP AIVSS Agent Identity Impersonation | B006/B007 (partial) | High | Add AGT-10 (Agent Identity Verification) to Domain 10 |
| GAP-12 | Cross-session memory poisoning detection — explicit monitoring signal | OWASP AIVSS Agent Memory Manipulation | None | Medium | Add MON-19 (Cross-Session Memory Integrity Signal) to Deliverable E |
| GAP-13 | Training data quality assessment — representativeness, contamination, bias at procurement or pre-training stage | IBM 23–28; AIUC-1 E013 partial | None | Medium | Add MSC-08 (Training Data Quality Assessment) to Domain 11 |

---

## 7. AIUC-1 Cross-Framework Coverage Compared to EAGCF

This table shows, per AIUC-1 crosswalk, how well EAGCF covers the same ground.

| AIUC-1 Crosswalk | Key coverage in AIUC-1 | EAGCF coverage | EAGCF advantage | EAGCF gap |
|---|---|---|---|---|
| **NIST AI RMF** | Govern/Map/Measure/Manage functions → 30 AIUC-1 controls | EAGCF uses NIST AI RMF as backbone; equivalent or deeper on all four functions | Lifecycle gate wiring; risk tiering bound to MANAGE | Diverse evaluation teams (GOVERN 3.1); human subject evaluations (MEASURE 2.2) — edge cases |
| **ISO 42001** | Management system clauses → E controls + QMS | EAGCF references ISO 42001 as management shell; Deliverable G provides equivalent document artifacts | Full evidence pack; lifecycle governance; assurance design | EAGCF does not prescribe management review meeting cadence explicitly (ISO Clause 9.3) |
| **EU AI Act** | Article 9–73 obligations → A/B/C/E controls | Section 4.5 regulatory mapping; EU AI Act obligations covered by tier 1 controls | Sector overlay depth; tiered treatment by risk class | EAGCF does not explicitly address GPAI model transparency obligations (Article 53) beyond GEN-03 |
| **OWASP LLM Top 10** | LLM01–LLM10 threats → B/C/D controls | Domains 4, 5, 6, 7 cover LLM01-LLM09 well | Prompt governance depth; RAG corpus controls; agentic tool controls | LLM10 (unbounded consumption) — no explicit preventive token budget control (GAP-09) |
| **MITRE ATLAS** | 26 adversarial ML mitigations → B/C/E controls | Part XII red-team pipeline; Domains 4, 9, 11 | Continuous automated red-team; model supply chain provenance | AML-M0006 (ensemble), M0007 (poisoning detection), M0008 (backdoor), M0014 (all-model checksum), M0022 (alignment) |
| **OWASP AIVSS** | 10 agentic vulnerability categories → B/C/E controls | Domain 10 (9 AGT controls) | Reversibility classification; action chain audit; HITL thresholds; scope inheritance | Agent identity verification (GAP-11); cross-session memory poisoning signal (GAP-12) |
| **IBM AI Risk Atlas** | 99 risks across agentic/training/inference/output/non-technical | EAGCF covers ~70% of IBM risks explicitly | Governance operating model; archetype-specific controls | IBM 17–22 societal; IBM 23–28 training data quality; IBM 75–78 explainability (non-decision-support systems) |
| **Cisco AI Security Framework** | 19 attacker objectives, 150+ subtechniques → B/D/E controls | Security domain (IAM, injection, output, vendor) covers ~80% | Control implementation architecture specifies enforcement points per attack surface | Multi-modal injection (GAP-10); corpus poisoning detection (partial GAP); AI endpoint availability |
| **CSA AI Controls Matrix** | 200+ controls → A/B/C/D/E domains | EAGCF covers ~50 CSA controls directly; infrastructure-layer gaps intentional | AI-specific depth exceeds CSA in all AI-native domains | BCR/DCS/HRS/I&S (infrastructure) — intentionally out of scope; ethics committee not explicitly named |

---

## 8. Recommended AIUC-1 Alignment Statement

If the enterprise pursues AIUC-1 certification, the following mapping statement applies:

> **EAGCF v1.1 addresses 42 of 49 AIUC-1 controls directly and 5 partially. The 7 partial/gap controls
> require 13 targeted control additions (GAP-01 through GAP-13) to achieve full AIUC-1 alignment.
> EAGCF substantively exceeds AIUC-1 in governance operating model, lifecycle governance depth,
> prompt governance, agentic controls, model supply chain, developer workflow integration, and
> governance economics — none of which are in scope for AIUC-1 certification.**

AIUC-1 certification and EAGCF are **complementary**, not competing:

- **AIUC-1** provides the certifiable external signal (customer-facing, procurement-relevant, insurer-relevant)
- **EAGCF** provides the internal governance operating system that makes AIUC-1 controls operational, evidenced, and lifecycle-integrated

---

## 9. Recommended Next Action

**Immediate:** Incorporate GAP-01, GAP-03, GAP-04, GAP-05, GAP-07, GAP-08, GAP-11 into EAGCF as Part XV (Supplementary Controls) — these are high-priority and have no current EAGCF equivalent.

**Near-term:** Incorporate GAP-02, GAP-06, GAP-09, GAP-10, GAP-12, GAP-13 as control extensions within existing domains.

**Strategic:** Initiate AIUC-1 certification scoping using the EAGCF evidence pack as the primary compliance artifact. The 13 gap controls, once added, should bring EAGCF to full AIUC-1 certification readiness.

---

*Prepared by: AI Governance Office | April 2026*
*Framework version: EAGCF v1.1 | AIUC-1 version: Current as of April 2026*
