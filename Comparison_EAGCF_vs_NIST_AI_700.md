# Side-by-Side Comparison: EAGCF vs. NIST AI 700-1 and NIST AI 700-2
## *NIST GenAI Pilot (Text-to-Text Evaluation) and ARIA (Assessing Risks and Impacts of AI)*

**NIST Documents:** NIST AI 700-1 (June 2025) + NIST AI 700-2 (November 2025)
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** The NIST AI 700 series documents report on NIST's own AI evaluation programs — AI 700-1 on measuring text-to-text generation quality and detection accuracy, and AI 700-2 on a sociotechnical risk evaluation framework (ARIA). These are empirical research reports, not governance frameworks. Their value to EAGCF is primarily as *evaluation methodology references* (augmenting the NIST AI 800-2 comparison) and as *evidence of real-world AI capabilities and risks*. The most governance-relevant content is ARIA's CoRIx measurement instrument and the three-layer evaluation architecture.

---

## 1. Document Scope Alignment

| Dimension | NIST AI 700-1 | NIST AI 700-2 | EAGCF |
|---|---|---|---|
| **Primary function** | Empirical evaluation: AI text generation vs. detection (adversarial competition) | Empirical evaluation: sociotechnical AI risk measurement (ARIA program) | Enterprise governance and control operating model |
| **Method** | Generator vs. discriminator adversarial competition; AUC/Brier scores | Three-layer evaluation (testing, assessment, measurement via CoRIx) | 15 control domains, 9 enforcement points, lifecycle governance |
| **RMF alignment** | Implicit (measurement science) | Explicit: Measure function of NIST AI RMF (AI 100-1) | Full AI RMF + ISO 42001 + COBIT + COSO |
| **Certification path** | No | No | ISO 42001 via EAGCF |
| **Output** | Benchmark scores (AUC, Brier) per generator/discriminator pair | CoRIx validity scores (0–10) per application/testing level | Controls, evidence, monitoring signals, governance artifacts |

---

## 2. NIST AI 700-1: GenAI Text Detection Evaluation vs. EAGCF

NIST AI 700-1 introduces a rigorous adversarial benchmark evaluation framework for AI-generated text detection. Its relevance to EAGCF is primarily in the areas of evaluation methodology (augmenting NIST AI 800-2 recommendations) and AI-generated text detection capabilities.

| NIST AI 700-1 Concept | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Adversarial generator vs. discriminator paradigm** (iterative rounds where generators try to fool discriminators) | Part XII §12.1 (red-team pipeline: attack-defense cycle) | ⚠️ Partial | Red-team pipeline includes adversarial testing; does not formalize an iterative generator-discriminator competition structure for ongoing capability measurement |
| **Multi-round evaluation cadence** (D-Round 1, 2, 3 — discriminators improve over time) | Part XII §12.2 (continuous control validation); Part VII §7.1 (monitoring signal refresh cadence) | ⚠️ Partial | Ongoing validation present; formalized multi-round adversarial competition structure not specified |
| **Discriminator metrics: AUC, BrierT, BrierN, EER** | Part XII §12.2 (control validation matrix: accuracy thresholds); N800-08 (statistical uncertainty gap) | ⚠️ Partial | Performance thresholds defined; formal probabilistic calibration metrics (Brier scores) not specified for AI detection systems |
| **Binary vs. calibrated confidence scoring** for AI content detection | Not specified | ❌ Gap | EAGCF does not distinguish binary classification outputs from well-calibrated probability scores for AI-generated content detection |
| **Generator metrics: statistical indistinguishability from human content** | Not addressed | ❌ Gap | EAGCF does not include metrics for measuring how closely AI-generated content resembles human-generated content at population level |
| **Key finding: some generators can defeat most discriminators** (AUC ≤ 0.5) | Part XIV §14.5 (behavioral fingerprinting); Part XII §12.4 (degradation detection) | ⚠️ Partial | Behavioral monitoring present; implication that some content will evade detection not formally acknowledged as a residual risk |
| **Evaluation findings: discriminator accuracy varies 50%–100% across generators** | N1004-08 (synthetic content detection benchmarks gap) | ⚠️ Partial | Benchmark accuracy ranges not formally incorporated |
| **Continuous benchmarking recommendation** | Part XII §12.2 (validation cadence); Part XIV §14.4 (vendor benchmark requirements) | ✅ Covered | |
| **Explainability in detection models** (XAI for why text is classified as AI-generated) | Part V §5.7 (OUT-03: output factuality); Part XII §12.2 | ⚠️ Partial | |
| **Domain expansion beyond summarization** (creative writing, legal texts, conversational AI) | Part II §2.2 (10 AI archetypes); Part V §5.15 (GEN domain) | ✅ Covered | EAGCF's archetype framework covers multiple use case domains |
| **Multimodal benchmark datasets** (text + image + audio + video) | Part V §5.15 (GEN domain: multi-modal controls) | ⚠️ Partial | Multi-modal AI addressed in GEN domain; multi-modal benchmark evaluation framework not specified |

---

## 3. NIST AI 700-2: ARIA Evaluation Framework vs. EAGCF

NIST AI 700-2 introduces ARIA (Assessing Risks and Impacts of AI), a structured three-layer sociotechnical evaluation framework aligned with the NIST AI RMF Measure function. CoRIx (Contextual Robustness Index) is its primary measurement instrument.

### Layer 1: Testing (Model Testing, Red Teaming, Field Testing)

| NIST AI 700-2 Testing Level | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Model testing** (pre-defined prompts; confirm capabilities and guardrail adherence) | Part XII §12.2 (control validation matrix: pre-deployment testing) | ✅ Covered | |
| **Red teaming** (adversarial prompting to elicit prohibited behaviors; structured goal) | Part XII §12.1 (red-team pipeline: attack library → generator → runner → classifier) | ✅ Covered | |
| **Field testing** (realistic human-AI interaction; simulating real-world usage with free play mode) | Part XII §12.1 (red-team: external red team engagement); Part VII §7.1 (post-deployment monitoring) | ⚠️ Partial | Real-world field testing with structured human sessions not formally required in EAGCF |
| **Scenario-based evaluation** (TV Spoilers, Meal Planner, Pathfinder — proxies for NIST 600-1 risks) | Part IV §4.1 (risk tiering: use-case based); Deliverable G §G.3 (AI Impact Assessment template) | ⚠️ Partial | Impact assessment present; scenario-based human testing program not formalized |
| **Guardrail-based evaluation** (permitted vs. prohibited information per scenario) | Part XI §11.1 (EP-1 through EP-9: enforcement architecture); Part V §5.4 (PRM domain) | ✅ Covered | EAGCF's enforcement architecture implements guardrail logic at production scale |

### Layer 2: Assessment (Dialogue Annotation and Post-Task Questionnaires)

| NIST AI 700-2 Assessment Approach | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Structured dialogue annotation** (risk assessment, content characterization, dialogue dynamics, utility) | Part VII §7.1 (monitoring signals); Part XII §12.2 (control validation) | ⚠️ Partial | EAGCF monitoring captures signals but does not require structured dialogue annotation |
| **Human annotator inter-rater reliability** (adjudication process; disagreement measurement) | N800-04 (LLM-as-judge interrater agreement gap) | ⚠️ Partial | LLM-as-judge governance gap confirmed; human annotator IRA not required |
| **Post-task questionnaires for user perception** (user perception of AI content quality, guardrail violations) | Not addressed | ❌ Gap | EAGCF does not require user perception surveys as a formal evaluation mechanism |
| **Annotation independence** (annotators not involved in system development) | Part XII §12.1 (external red team: independence requirement) | ✅ Covered | |

### Layer 3: CoRIx Measurement Instrument

| NIST AI 700-2 CoRIx Component | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Contextual robustness definition** (system maintaining performance under real-world circumstances and user expectations) | Part VII §7.2 (KPI/KRI/KCI framework); Part XIV §14.2 (performance SLA table) | ⚠️ Partial | Performance monitoring present; formal "contextual robustness" construct with tree-structured measurement not specified |
| **Hierarchical measurement tree** (6-level aggregation from raw annotations to RMF trustworthy characteristics) | Not addressed | ❌ Gap | EAGCF does not use a hierarchical measurement aggregation framework; risk scores are tier-based, not signal-aggregated |
| **Crosswalk: assessment items → target construct** (validity — did system meet permitted/prohibited requirements?) | Part XII §12.2 (control validation matrix: pass/fail thresholds) | ⚠️ Partial | Binary pass/fail present; nuanced construct validity measurement not formalized |
| **CoRIx scores: 0–10 validity risk scale** | Not addressed | ❌ Gap | EAGCF uses categorical (Tier 0–4) and binary (pass/fail) assessment; continuous risk score per interaction not used |
| **Attribution transparency** (CoRIx traces score to specific testing type and annotation source) | Part XIV §14.2 (SLA by tier); Part VII §7.4 (incident attribution) | ⚠️ Partial | |
| **Real-world vs. controlled performance gap** (controlled testing ≠ real-world behavior) | Part XII §12.1 (field testing via external red team); N800-06 (evaluation awareness gap) | ⚠️ Partial | External testing addresses real-world gap; structured field testing protocol not required |

---

## 4. Scoring Summary

| NIST AI 700 Section | Items | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| 700-1: Text detection evaluation framework | 11 | 2 | 0 | 7 | 2 |
| 700-2: Testing layer (3 levels) | 5 | 2 | 0 | 3 | 0 |
| 700-2: Assessment layer | 4 | 1 | 0 | 2 | 1 |
| 700-2: CoRIx measurement | 6 | 0 | 0 | 3 | 3 |
| **TOTALS** | **26 items** | **5 (19%)** | **0 (0%)** | **15 (58%)** | **6 (23%)** |

**Coverage interpretation:** 77% total coverage (19% direct + 58% partial). The high partial rate and low direct coverage reflect the nature of these documents as empirical research reports with specialized measurement methods (CoRIx, adversarial competition scoring) rather than governance requirements. EAGCF covers the *activities* (red teaming, monitoring, validation) but not the rigorous *measurement methodology* these programs establish.

The 23% gap rate covers specialized evaluation measurement items (post-task questionnaires, CoRIx hierarchical scoring, generator indistinguishability metrics) that are at the evaluation research level rather than the governance control level.

---

## 5. Where EAGCF Materially Exceeds NIST AI 700-1 and 700-2

| Dimension | EAGCF Capability | NIST AI 700 Series |
|---|---|---|
| **Production enforcement architecture** | 9 enforcement points (EP-1 through EP-9) | Not addressed (research evaluation context) |
| **Governance operating model** | 9 bodies, RACI, decision rights, review cadences | Administrative requirements for study conduct only |
| **Risk tiering with lifecycle gates** | 5-tier model wired to 11-stage lifecycle | Not addressed |
| **Agentic governance** | AGT-01 through AGT-10 | Not addressed |
| **Vendor governance** | 6-dimension scoring, behavioral fingerprinting, fallback | Not addressed |
| **Sector overlays** | Financial services, healthcare, safety-critical | Not addressed |
| **Control taxonomy** | 15 domains, 97+ controls | Not addressed |
| **Adoption acceleration** | Fast-lane, anti-patterns, misallocation diagnostic | Not addressed |

---

## 6. Gap Items: Recommended EAGCF Additions from NIST AI 700 Series

| Gap ID | Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N700-01** | AI 700-2 / ARIA | **Human field testing requirement**: For Tier 1 (High) AI systems, require structured field testing with real end-users under realistic conditions (not just controlled red-team testing) before deployment, to identify real-world gaps not surfaced in laboratory conditions | High | Part VII §7.5 (assurance evidence pack) — add field testing as a required assurance activity for Tier 1 systems |
| **N700-02** | AI 700-1 | **Probabilistic calibration metrics for detection systems**: When deploying AI-generated content detection systems (watermark detectors, classifier outputs), require well-calibrated probability outputs (Brier score) rather than binary classification only | Medium | Part XII §12.2 (control validation matrix) — add calibration requirements for detection system outputs |
| **N700-03** | AI 700-2 / CoRIx | **Contextual robustness measurement**: For Tier 1 systems with significant user interaction volume, require measurement of contextual robustness (performance under real-world variation) using structured human evaluation sessions with post-task questionnaires | Medium | Part XII §12.2 — add contextual robustness as a validation activity for Tier 1 interactive systems |
| **N700-04** | AI 700-1 | **Residual detection evasion risk acknowledgment**: Formally document residual risk that state-of-the-art AI content detectors can be evaded by sophisticated generators; include this in risk acceptance documentation for systems relying on AI-generated content detection as a control | Low | Part IV §4.1 (risk tiering) — add residual evasion risk to risk acceptance criteria for detection-dependent controls |

---

## 7. Key ARIA Scenario Risk Mappings (Informative for EAGCF Use Case Registration)

The three ARIA scenarios serve as templates for risk-based AI evaluation. The mapping to NIST 600-1 risk categories provides a useful template for EAGCF use case risk profiling:

| ARIA Scenario | Risk Proxy | NIST 600-1 Risk | EAGCF Tier Mapping |
|---|---|---|---|
| **TV Spoilers** | Withhold privileged/nefarious information (private data, IP, dangerous materials) | CBRN / Data Privacy / Information Security | Tier 0 (if CBRN) / Tier 1 (if PII) |
| **Meal Planner** | Withhold unsafe information (endangering life, health, property) | Dangerous/Violent Content / Confabulation | Tier 1 (health/safety risk) |
| **Pathfinder** | Produce factual content (no hallucination) | Confabulation | Tier 2 (Elevated — reputational/operational risk) |

This scenario → risk → tier mapping aligns well with EAGCF's Deliverable B risk tiering and can inform the AI Use Case Registration template (Deliverable G §G.5).

---

## 8. Synthesis

NIST AI 700-1 and 700-2 are **empirical research reports** that validate the *effectiveness* of various AI evaluation approaches and reveal important real-world findings:

**From AI 700-1 (detection capability):**
- AI-generated text is increasingly difficult to distinguish from human text — some generators can defeat most detectors
- Best discriminators achieve near-perfect accuracy (AUC ~1.0) but this requires specialized systems
- Detection accuracy varies dramatically across different content types and compression levels
- This validates EAGCF's defense-in-depth posture (don't rely on detection alone)

**From AI 700-2 (sociotechnical risk):**
- Controlled red-team evaluation consistently shows different (higher) risk profiles than user perception surveys
- All tested applications showed guardrail violation risks; open-source applications performed worse than highly-resourced ones
- CoRIx successfully attributes risk contributions to specific testing levels — important for governance accountability

**Primary integration points for EAGCF:**
1. **Field testing** (N700-01) — the most actionable gap, requiring structured real-user testing for Tier 1 systems
2. **ARIA's three-scenario approach** — informative template for EAGCF's AI Use Case Registration and impact assessment templates
3. **Residual detection evasion** (N700-04) — important caveat for any control relying on AI-generated content detection

**Coverage summary:**
- NIST AI 700 items with direct EAGCF coverage: **5 (19%)**
- NIST AI 700 items partially covered: **15 (58%)**
- NIST AI 700 items not addressed: **6 (23%)**
- Items where EAGCF materially exceeds NIST AI 700 series: **8 dimensions**

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Comparisons completed: NIST AI 100-1, 100-2, 100-4, 600-1, 700-1, 700-2, 800-1, 800-2, IR 8596 (9 documents)*
*Remaining high-priority: NIST AI 100-5 (AI in Cybersecurity), NIST AI 100-3 (AI Talent), crosswalk PDFs*
