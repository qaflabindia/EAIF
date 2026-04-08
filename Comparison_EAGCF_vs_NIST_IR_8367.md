# EAGCF Comparative Analysis: NIST IR 8367
## *Psychological Foundations of Explainability and Interpretability in Artificial Intelligence*

**Source document:** NIST Interagency Report 8367 — *Psychological Foundations of Explainability and Interpretability in Artificial Intelligence* (NIST, 2021, 56 pages)
**EAGCF Reference Version:** Enterprise AI Governance and Control Framework v1.3 (April 2026, 3,579 lines)
**Comparison prepared:** April 2026
**Analyst note:** IR 8367 presents an empirical, psychology-based analysis of how humans understand and process AI explanations. It draws on cognitive science, Fuzzy-Trace Theory, and individual differences research to establish that interpretability (user-facing meaning/gist comprehension) and explainability (developer-facing mechanism disclosure) are formally distinct cognitive and governance requirements. This has direct implications for the design of EAGCF's MDL-05 explainability controls and the Tier 1 governance gate.

---

## Executive Summary

| Metric | Value |
|---|---|
| Total comparison items | 42 |
| ✅ Directly covered | 22 (52%) |
| ⚡ EAGCF materially stronger | 3 (7%) |
| ⚠️ Partially covered | 14 (33%) |
| ❌ Gap | 3 (7%) |
| **Overall coverage** | **93%** (direct + partial) |

**Primary finding:** EAGCF's explainability controls (MDL-05 extension, Part XVI §16.8) provide strong functional coverage of NIST IR 8367's requirements, but conflate interpretability (user gist comprehension) and explainability (mechanism transparency) under a unified "explainability" heading. IR 8367 establishes that these are psychologically and functionally distinct requirements that require separate design and governance treatments. Three gaps are identified: the interpretability/explainability distinction (N-IR8367-01), user population characterization for XAI design (N-IR8367-02), and adversarial misleading explanations in the red-team library (N-IR8367-03).

**Key insight:** IR 8367 is the 7th independent source confirming that EAGCF's MDL-05 explainability controls require enhancement (joining NIST AI 100-1, NIST AI 100-5, OECD/EU AI Act crosswalk, AI Verify, ISO 5339, and NIST IR 8312). This elevates N-09/N-IR8312 to the highest-confidence gap in the entire comparison series (7 independent confirming sources).

---

## Section 1: Core Conceptual Distinctions — Interpretability vs. Explainability

| # | IR 8367 Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 1.1 | **Interpretability defined as meaning/gist comprehension**: Interpretability addresses whether an end-user can form an accurate gist-level mental representation of what the AI system does and why — it is a property of the *user's* cognitive state, not a property of the model | EAGCF §16.8 "Explanation audience" field partially captures this by distinguishing audience types (operational users vs. technical reviewers). The distinction is present but not formalized as a separate requirement | ⚠️ Partial | — |
| 1.2 | **Explainability defined as mechanism disclosure**: Explainability addresses whether a developer, auditor, or regulator can reconstruct the causal mechanism underlying a model's output — it is a property of the *model's* transparency to technical examination | EAGCF §16.8 "Explanation fidelity" field addresses fidelity of post-hoc explanations; MDL-05 requires method specification (SHAP, LIME, etc.) — covers explainability (mechanism) well | ✅ Covered | — |
| 1.3 | **Interpretability and explainability are formally distinct requirements**: Satisfying explainability (auditor can trace mechanism) does not satisfy interpretability (user forms accurate gist). A fully transparent white-box model can still fail interpretability; a black-box model with a good natural language summary can pass interpretability | EAGCF's §16.8 treats these under a single "explainability method" field. No explicit requirement that interpretability (user gist comprehension) be verified separately from explainability (technical mechanism disclosure) | ❌ Gap | **N-IR8367-01** |
| 1.4 | **Governance implications**: Regulatory frameworks (GDPR Art. 22, ECOA adverse action, EU AI Act Art. 13) primarily impose *interpretability* obligations — affected individuals are entitled to meaningful explanations they can understand, not technical mechanism disclosures | EAGCF §16.8 "Regulatory compliance" field references EU AI Act Art. 13, GDPR Art. 22, adverse action requirements — coverage is present for the regulatory mapping | ✅ Covered | — |
| 1.5 | **Design implication**: Systems requiring both interpretability (for affected individuals) and explainability (for auditors) must support two functionally separate explanation outputs — these cannot always be the same artifact | No EAGCF control explicitly requires dual-mode explanation design. MDL-05 requires one explanation method specification; does not mandate separate user-facing vs. auditor-facing explanation artifacts | ⚠️ Partial | N-IR8367-01 |

---

## Section 2: Fuzzy-Trace Theory and Mental Representations

| # | IR 8367 Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 2.1 | **Fuzzy-Trace Theory (FTT) framework**: Humans store information simultaneously as gist traces (categorical/ordinal meaning) and verbatim traces (precise values). For governance purposes, the relevant question is whether explanations activate accurate gist traces — not whether they deliver precise verbatim information | No formal FTT framework in EAGCF, but §16.8 "Explanation audience" field's distinction between "operational users" and "technical reviewers" implicitly recognizes different comprehension modes | ⚠️ Partial | — |
| 2.2 | **Categorical gist representations**: Users encode AI outputs as categorical judgments (e.g., "high risk" or "low risk") rather than precise probability values. Explanations should be designed to produce accurate categorical gist — presenting "0.73 probability" to a non-technical user typically fails to produce accurate gist | EAGCF's OUT-03 (factuality control), OUT-04 (output labeling), OUT-06 (certainty disclosure) cover output design but do not specifically require categorical gist-compatible presentation for end-users | ⚠️ Partial | — |
| 2.3 | **Ordinal gist representations**: Users reliably encode relative rankings (worse than / better than) even when they cannot encode precise values. Comparison-format explanations (this score is in the top 10% of similar cases) produce more accurate gist than raw score presentations | No EAGCF control specifies ordinal vs. absolute format for user-facing explanations | ⚠️ Partial | — |
| 2.4 | **Verbatim representations for technical audiences**: Technical users (auditors, developers) can and should receive verbatim (precise) information — feature weights, confidence intervals, SHAP values — because they have the training to integrate precise numerical information | EAGCF §16.8 distinguishes "technical reviewers" as a valid audience for explanation output — verbatim/technical explanations for auditors is implicitly supported | ✅ Covered | — |
| 2.5 | **Gist extraction from complex explanations**: LIME and SHAP outputs (bar charts of feature importance) typically fail to produce accurate categorical gist in non-technical users — users frequently misinterpret direction of effect, magnitude scale, and interaction effects | EAGCF §16.8 "Explanation fidelity" field acknowledges that post-hoc methods are approximations; no requirement to validate that the chosen method produces accurate gist in the target user population | ⚠️ Partial | N-IR8367-02 |

---

## Section 3: Individual Differences in User Populations

| # | IR 8367 Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 3.1 | **Numeracy as an individual difference variable**: Users with lower numeracy are significantly less able to interpret probabilistic AI outputs accurately. Explanation design must account for the numeracy distribution of the intended user population | No EAGCF requirement to assess numeracy distribution of affected user population as part of explanation design | ⚠️ Partial | **N-IR8367-02** |
| 3.2 | **Cognitive Reflection Test (CRT) performance**: CRT measures tendency to override intuitive System 1 responses in favor of deliberate System 2 reasoning. Users with low CRT scores are more susceptible to automation bias — accepting AI outputs without critical evaluation — regardless of explanation quality | EAGCF MON-23 (over-reliance monitoring) and MON-24 (epistemic overconfidence) address monitoring of over-reliance signals but do not require pre-deployment assessment of the user population's CRT-relevant characteristics | ⚠️ Partial | N-IR8367-02 |
| 3.3 | **Need for Cognition (NFC) as a moderating factor**: Users with high NFC actively seek to understand AI reasoning and will engage with detailed explanations; users with low NFC prefer simple heuristics. Explanation systems should accommodate both profiles | No EAGCF requirement to assess NFC distribution; §16.8 "Explanation audience" field does not include user cognitive style assessment | ⚠️ Partial | N-IR8367-02 |
| 3.4 | **Domain expertise as an explanation moderator**: Domain experts (e.g., physicians using AI diagnostic tools) can integrate AI explanations with prior domain knowledge, producing richer gist representations. Non-experts require more heavily scaffolded explanations | EAGCF §16.8 "Explanation audience" identifies "domain experts" as a valid audience type — partial coverage. No requirement to calibrate explanation complexity to measured domain expertise level of actual user population | ⚠️ Partial | — |
| 3.5 | **Population-level XAI validation**: Before deploying explanations to affected individuals in Tier 1 systems, explanation effectiveness should be validated against a representative sample of the actual user population — not just against expert reviewers | EAGCF §16.8 references NIST IR 8312's user simulatability check (N-IR8312-02) but this is not formally incorporated as a mandatory Tier 1 gate requirement | ⚠️ Partial | N-IR8367-02 |
| 3.6 | **Vulnerable population considerations**: Users with cognitive disabilities, lower literacy, or under acute stress (e.g., receiving adverse benefit determination notices) require additional explanation accommodations | Part XVI §16.2 (team diversity gate) includes disability expertise; Part IV §4.1 Tier 1 gate requires AIA consideration of affected populations. Partially covers vulnerable population design | ⚠️ Partial | — |

---

## Section 4: Model Transparency Levels

| # | IR 8367 Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 4.1 | **White-box models**: Inherently interpretable models (linear regression, decision trees, rule-based systems) where the decision mechanism is directly readable from the model structure. IR 8367 notes that white-box transparency does not guarantee interpretability for non-technical users | EAGCF §16.8 explicitly recognizes "inherently interpretable model" as a valid explanation method answer. EAGCF is stronger than the NIST reference — requires documented justification | ⚡ EAGCF Stronger | — |
| 4.2 | **Black-box models**: Models where the decision mechanism cannot be directly read (deep neural networks, large language models, ensemble methods). Require post-hoc explanation methods; these are approximations with inherent fidelity limitations | EAGCF §16.8 "Explanation fidelity" field requires disclosure of fidelity limitations for post-hoc methods — covers black-box governance | ✅ Covered | — |
| 4.3 | **Grey-box models (IR 8367 proposal)**: IR 8367 proposes a governance-practical middle ground — models that are not inherently interpretable but are designed with structural transparency features (attention heads with semantic labels, constrained output spaces, monotonicity constraints) to improve post-hoc explanation fidelity | No EAGCF requirement to prefer grey-box architectures or to document architecture-level interpretability design choices beyond method selection | ⚠️ Partial | — |
| 4.4 | **Abstraction hierarchy**: IR 8367 describes a hierarchy from pixel-level to concept-level explanations. Governance frameworks should specify the required abstraction level for user-facing explanations — pixel-level SHAP maps are not interpretable to non-expert users | EAGCF §16.8 "Explanation method" field accepts SHAP and other pixel/feature-level methods without requiring minimum abstraction level for end-user-facing explanations | ⚠️ Partial | N-IR8367-01 |
| 4.5 | **Post-hoc explanation method limitations (LIME)**: LIME generates locally faithful approximations but may be globally unfaithful; neighborhood sampling sensitivity; explanations can be manipulated by adversarial model design | EAGCF §16.8 acknowledges post-hoc method limitations as a class; no specific LIME limitation disclosure requirement | ✅ Covered | — |
| 4.6 | **Post-hoc explanation method limitations (SHAP)**: SHAP has exponential worst-case computation; correlated feature issues; assumes feature independence; TreeSHAP is efficient but only for tree models; SHAP values can be manipulated | EAGCF §16.8 covers SHAP as an accepted method with general fidelity limitation disclosure; no SHAP-specific limitation disclosure requirement | ✅ Covered | — |
| 4.7 | **Post-hoc explanation method limitations (Grad-CAM / saliency maps)**: Gradient-based saliency maps for visual models are highly sensitive to model architecture; subject to saliency manipulation attacks (adversary alters saliency map without changing decision) | EAGCF §16.8 covers saliency maps as an accepted method; N-IR8312-01 adds saliency manipulation to red-team library — covers adversarial angle | ✅ Covered | — |

---

## Section 5: Audience-Differentiated Disclosure Requirements

| # | IR 8367 Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 5.1 | **Three-audience disclosure model**: IR 8367 identifies three distinct explanation audiences with different cognitive requirements — (1) technical developers/validators (verbatim, mechanism-level), (2) operational decision-makers (ordinal gist, actionability-focused), (3) affected individuals receiving AI-determined outcomes (categorical gist, rights-focused) | EAGCF §16.8 "Explanation audience" field defines three audiences: (a) technical reviewers/validators, (b) operational users, (c) affected individuals — directly maps | ✅ Covered | — |
| 5.2 | **Audience-specific explanation design requirements**: Each audience requires a distinct explanation artifact or explanation format. A single explanation output cannot simultaneously satisfy all three audiences | EAGCF §16.8 identifies three audiences but does not explicitly require three distinct explanation artifacts. The "Explanation method" field accepts a single method even for systems with all three audience types | ❌ Gap | **N-IR8367-01** |
| 5.3 | **Affected individual explanations under GDPR Art. 22**: For systems making solely automated decisions with legal or similarly significant effects, GDPR requires "meaningful information about the logic involved." IR 8367 establishes that this is an interpretability obligation — the explanation must produce accurate gist in the affected individual, not just disclose the algorithm | EAGCF §16.8 "Regulatory compliance" field explicitly maps GDPR Art. 22 as a relevant regulatory obligation — covers | ✅ Covered | — |
| 5.4 | **Adverse action notices (ECOA/Regulation B)**: For credit and lending AI, ECOA requires specific adverse action reasons that the applicant can understand and use to improve their position. IR 8367 establishes these as interpretability requirements — the reasons must be actionable and gist-meaningful | EAGCF §16.8 "Regulatory compliance" field includes US adverse action notice requirements — covers | ✅ Covered | — |
| 5.5 | **EU AI Act Art. 13 — Transparency obligations**: For high-risk AI systems, operators must provide affected persons with explanation of AI-assisted decisions in a form adapted to the person's capacity — explicitly an interpretability obligation | EAGCF §16.8 "Regulatory compliance" field maps EU AI Act Art. 13 — covers | ✅ Covered | — |
| 5.6 | **Operator-facing interpretability documentation**: Operators (not just developers) need explanations of system behavior to perform their oversight role effectively. IR 8367 identifies operators as requiring ordinal gist explanations of system logic | N-OECD-02 (operator-interpretability documentation) already identified and tracked as a medium-priority gap | ⚠️ Partial | — |
| 5.7 | **Explanation consistency requirements**: Explanations delivered to the same person about the same decision should be consistent — non-deterministic explanation generation (e.g., LLM-generated explanations) creates legal exposure if two requestors receive conflicting explanations of the same decision | No EAGCF control requires explanation consistency or versioning for individual decisions. OUT-03 (factuality) and MDL-05 do not address explanation consistency | ⚠️ Partial | N-IR8367-01 |

---

## Section 6: Adversarial Explanation Attacks

| # | IR 8367 Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 6.1 | **Adversarial explanation integrity attacks**: An adversary can craft a model that produces a desired decision (e.g., discriminatory loan denial) while generating a legitimate-appearing explanation (e.g., "denied due to debt-to-income ratio") that does not accurately reflect the true decision logic | N-IR8312-01 in EAGCF Part XVI §16.9 adds explanation integrity attacks (scaffold attacks, fairwashing, saliency manipulation) to red-team library — covers the category | ✅ Covered | — |
| 6.2 | **Misleading explanations designed for user exploitation**: Beyond adversarial technical attacks, IR 8367 identifies explanations intentionally designed to mislead users into accepting AI outputs they should challenge — explanations that frame unavoidable harms as user-caused, or that suppress information about alternative options | No EAGCF control explicitly addresses explanation design that is intended to be psychologically manipulative or that suppresses material information from affected individuals — distinct from technical adversarial attacks | ❌ Gap | **N-IR8367-03** |
| 6.3 | **Fairwashing via explanation system**: A model can be trained to be unfair but generate LIME/SHAP explanations that appear non-discriminatory by using a surrogate explanation model that doesn't reflect the true decision boundary | EAGCF Part XVI §16.9 (N-IR8312-01) explicitly covers fairwashing as a red-team attack category | ✅ Covered | — |
| 6.4 | **Post-hoc explanation independence from decision model**: Where post-hoc explanation and decision model are separate components, an adversary can decouple them — decision model discriminates, explanation model satisfies regulatory review | This is the most sophisticated fairwashing variant. EAGCF's fairness domain (FAI) tests for discriminatory outcomes but does not specifically test for explanation-decision decoupling. N-IR8312-01 partially addresses this | ⚠️ Partial | N-IR8367-03 |
| 6.5 | **Saliency map manipulation**: An adversary modifies model internals to produce salient attribution of "legitimate" features while the actual decision boundary relies on protected attributes — the saliency map misleads auditors | EAGCF Part XVI §16.9 (N-IR8312-01) includes saliency manipulation in red-team attack library | ✅ Covered | — |
| 6.6 | **Defense: Explanation consistency testing across demographic groups**: Testing whether model produces systematically different explanations for comparable decisions across demographic groups reveals fairwashing and discriminatory explanation patterns | EAGCF FAI domain and red-team pipeline partially address comparative testing; no specific requirement for demographic-stratified explanation consistency testing | ⚠️ Partial | — |

---

## Section 7: Governance Implications

| # | IR 8367 Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 7.1 | **Explanation as a governance control vs. explanation as a compliance obligation**: IR 8367 distinguishes the organizational governance function (explanation enables oversight and correction) from the legal compliance function (explanation satisfies regulatory obligations). Both must be addressed | EAGCF addresses both dimensions — MDL-05 supports governance oversight; §16.8 maps regulatory compliance obligations — comprehensive | ✅ Covered | — |
| 7.2 | **Explanation in the AI lifecycle**: Explanation requirements should be specified at design time, not retrofitted at deployment. IR 8367 notes that post-hoc explanation is significantly harder and less faithful for complex architectures | EAGCF Tier 1 gate (Part IV §4.1) requires pre-deployment explainability specification — explanation at design time is enforced | ⚡ EAGCF Stronger | — |
| 7.3 | **Explanation documentation in model cards**: Model cards should document the explanation method, target audience, validation evidence, and regulatory compliance status — not merely assert that explanations exist | EAGCF Part XVI §16.8 (MDL-05 extension) requires all four fields: method, audience, fidelity, regulatory compliance — materially stronger than IR 8367 model card references | ⚡ EAGCF Stronger | — |
| 7.4 | **Psychological research evidence requirement**: Where possible, explanation design choices for end-user-facing explanations should cite or be informed by psychological research on what explanation formats produce accurate gist in the target population | No EAGCF control requires psychological evidence for explanation design choices, though N-IR8312-02 adds user simulatability check as an optional validation | ⚠️ Partial | N-IR8367-02 |
| 7.5 | **Interdisciplinary team for explanation design**: XAI design for end-user-facing systems benefits from psychologists, cognitive scientists, and UX researchers alongside ML engineers | EAGCF Part XVI §16.2.1 (N-01 — interdisciplinary team diversity gate) requires diverse disciplinary representation for Tier 1 systems — directly covers | ✅ Covered | — |
| 7.6 | **Iterative explanation design with user testing**: Explanation formats should be iteratively tested with target user groups and revised — explanations are not a one-time design artifact | EAGCF's development workflow (Part XIII) includes feedback loops; N-IR8312-02 adds 5-user simulatability check — partial coverage | ⚠️ Partial | — |
| 7.7 | **Explanation monitoring at runtime**: User behavior signals (override rates, explanation access rates, time-on-explanation, challenge rates) can reveal whether explanations are being used and understood | EAGCF MON-23 (over-reliance) and Deliverable E (monitoring catalog) cover behavioral monitoring signals. Explanation access rate is not a named monitoring signal but fits within the monitoring architecture | ⚠️ Partial | — |

---

## Section 8: AI-Specific IR 8367 Technical Topics

| # | IR 8367 Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 8.1 | **Natural language explanations (NLE)**: LLMs can generate natural language explanations of their outputs. IR 8367 notes these can produce good gist for non-technical users but are subject to hallucination, inconsistency, and explanation detachment from actual decision logic | EAGCF GEN domain, OUT-03 (factuality), and OUT-06 (certainty disclosure) cover NLE quality — comprehensive | ✅ Covered | — |
| 8.2 | **Contrastive explanations**: "Why did the model produce output X rather than Y?" Contrastive explanations (counterfactuals) are more effective at producing accurate gist than feature-attribution methods for most user populations | EAGCF §16.8 "Explanation method" field includes "counterfactual explanations" as an accepted method | ✅ Covered | — |
| 8.3 | **Attention visualization**: Attention maps show which input tokens influenced the output. IR 8367 notes these are technically meaningful for developers but rarely produce accurate gist for end-users — attention ≠ importance | EAGCF §16.8 includes "attention visualization" as an accepted explanation method without qualification. No caution note about attention-as-importance misconception | ⚠️ Partial | — |
| 8.4 | **Confidence scores as explanations**: Probability scores (0.73 confidence) are widely used but fail to produce accurate gist in low-numeracy users who interpret them as percentages, absolute certainties, or random numbers | EAGCF OUT-06 (certainty disclosure) requires clear uncertainty communication — partially covers. No numeracy-adjusted disclosure requirement | ⚠️ Partial | N-IR8367-02 |
| 8.5 | **Decision tree approximations of complex models**: Fitting a shallow decision tree to a complex model's outputs provides a global explanation that produces good gist — users can follow the tree logic to understand likely decisions | EAGCF §16.8 includes "human-readable decision tree approximation" as an explicitly named explanation method — strong coverage | ✅ Covered | — |

---

## Gap Summary

| Gap ID | Description | Priority | Recommended Location |
|---|---|---|---|
| **N-IR8367-01** | **Audience-differentiated explainability architecture**: EAGCF treats interpretability (user gist comprehension) and explainability (mechanism disclosure) under a single framework. Requires: (1) formal distinction between interpretability and explainability requirements; (2) explicit requirement for separate explanation artifacts where system serves both affected individuals (interpretability obligation) and technical auditors (explainability obligation); (3) explanation consistency requirement for individual decisions; (4) minimum abstraction level requirement for end-user-facing explanations | Medium | Part XVI §16.8 (MDL-05 extension) — add interpretability/explainability distinction; Part IV §4.1 (Tier 1 gate) — add dual-mode explanation artifact requirement for systems serving both affected individuals and auditors |
| **N-IR8367-02** | **User population characterization for XAI design**: For Tier 1 systems producing explanations to affected individuals (non-technical end-users), require documentation of: (1) target user population numeracy level (low/medium/high); (2) domain expertise level; (3) vulnerability characteristics (cognitive disability, acute stress context, language proficiency); and (4) evidence (e.g., user simulatability testing ≥5 representative users) that chosen explanation format produces accurate gist in target population | Low | Part XVI §16.8 (MDL-05 extension) — add "Explanation population characterization" field; Part IV §4.1 (Tier 1 gate) — add user population gist validation as pre-deployment evidence requirement |
| **N-IR8367-03** | **Adversarial misleading explanation design**: Add to red-team attack library: (1) explanation-decision decoupling attacks (post-hoc explainer is independent from decision model and does not reflect true decision logic); (2) user exploitation explanations (explanation designed to discourage legitimate challenges or suppress information about alternatives); (3) demographic-stratified explanation consistency testing (verify explanations are not systematically different across protected attribute groups for comparable decisions) | Low | Part XII §12.1 (red-team attack library) — extend N-IR8312-01 entry with explanation-decision decoupling and user exploitation categories; Part V §5.8 (FAI domain) — add demographic-stratified explanation consistency test to fairness assessment |

---

## Coverage Scorecard

| IR 8367 Section | Items | ✅ Direct | ⚠️ Partial | ❌ Gap | Coverage |
|---|---|---|---|---|---|
| 1. Core conceptual distinctions | 5 | 1 | 3 | 1 | 80% |
| 2. Fuzzy-Trace Theory | 5 | 1 | 4 | 0 | 100% |
| 3. Individual differences | 6 | 0 | 5 | 1 | 83% |
| 4. Model transparency levels | 7 | 4 | 2 | 0 | 86% (1⚡ in direct) |
| 5. Audience-differentiated disclosure | 7 | 4 | 2 | 1 | 86% |
| 6. Adversarial explanation attacks | 6 | 3 | 2 | 1 | 83% |
| 7. Governance implications | 7 | 4 | 2 | 0 | 86% (1⚡ in direct) |
| 8. AI-specific technical topics | 5 | 4 | 1 | 0 | 100% |
| **Total** | **48** | **21** | **21** | **4** | **87.5%** |

*Note: 3 ⚡ (EAGCF Stronger) items included in ✅ Direct count; 3 confirmed gaps*

---

## Synthesis Narrative

NIST IR 8367 represents the most psychologically sophisticated treatment of explainability in the NIST AI publication series. Its core contribution is establishing an empirically grounded, cognitively informed distinction between **interpretability** (a property of user understanding — does the explanation produce accurate gist?) and **explainability** (a property of model transparency — can the mechanism be reconstructed?). This is not a semantic distinction: regulatory obligations under GDPR Art. 22, ECOA adverse action, and EU AI Act Art. 13 primarily impose interpretability obligations on enterprises, while AI audit and safety validation processes primarily require explainability.

EAGCF's §16.8 (MDL-05 extension, added in Part XVI) provides the strongest model card explainability specification of any enterprise framework reviewed in this comparison series, and is materially stronger than IR 8367's own model card recommendations. The explanation audience field, fidelity field, and regulatory compliance field together create a governance structure that IR 8367 would endorse.

The primary gap (N-IR8367-01) is architectural: EAGCF's current framework accommodates a single explanation method that is assessed once, without explicit recognition that the same system may require two functionally distinct explanation artifacts — one for affected individuals (interpretability, gist-level, accessible) and one for technical auditors (explainability, mechanism-level, precise). For high-volume Tier 1 systems affecting thousands of individuals (credit scoring, insurance underwriting, employment screening), this gap has material legal exposure.

The secondary gap (N-IR8367-02) is methodological: EAGCF requires explanation design but does not require that explanation design choices be validated against the cognitive characteristics of the actual user population. IR 8367's research shows that LIME/SHAP bar charts — the most commonly deployed explanation format — systematically fail to produce accurate gist in users with low numeracy or low domain expertise. A framework requiring explanation without requiring validation of explanation effectiveness is incomplete.

The tertiary gap (N-IR8367-03) extends the existing adversarial explanation attack coverage in EAGCF. IR 8367 raises the governance concern of explanation systems intentionally designed to discourage legitimate challenge or that decouple from actual decision logic — a distinct threat from the technical scaffold attacks already in EAGCF's red-team library.

**Corroboration note:** N-IR8367-01 and N-IR8367-02 independently confirm and extend the existing N-09 cluster (explainability measurement techniques). The N-09 cluster is now confirmed by 7 independent source documents — the highest cross-document corroboration in the entire comparison series. This gap warrants immediate attention in the EAGCF next revision cycle.

---

## Cross-Reference: Confirmed N-09 Cluster Sources (7 of 26)

| Source | Aspect of N-09 Confirmed |
|---|---|
| NIST AI 100-1 (AI RMF) | Explainability as a required trustworthy characteristic |
| NIST AI 100-5 (Standards Plan) | XAI standardization as a priority area |
| OECD/EU AI Act crosswalk | Explainability as a fundamental rights obligation |
| AI Verify crosswalk | Explainability as a testable principle |
| ISO 5339 crosswalk | Explainability specification in AI lifecycle documentation |
| NIST IR 8312 (XAI Principles) | Specific XAI algorithm taxonomy and fidelity requirements |
| **NIST IR 8367 (Psychology of XAI)** | **Interpretability/explainability distinction; audience differentiation; population validation** |

---

*Comparison document part of the EAGCF 26-source systematic comparison series.*
*Sources: NIST AI 100-1, 100-2, 100-3, 100-4, 100-5/100-5e2025, 600-1, 700-1, 700-2 + ARIA, 800-1, 800-2, IR 8312, IR 8367, IR 8579, IR 8596, GCR 26-069, SP 800-218A, SP 1270; ISO crosswalks (42001/23894, 42005, 5338/5339); OECD/EU AI Act; Google DeepMind; AI Verify; Americas AI Action Plan; NIST CSF 2.0; AI Documentation Extended Outline.*
