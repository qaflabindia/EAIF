# Side-by-Side Comparison: EAGCF vs. ARIA Program Companion Document
## *Assessing Risks and Impacts of AI — NIST Evaluation Program Design*

**Source Document:** `ARIA_Program_Companion_Document_Dec20.pdf` (NIST, December 20, 2024)
**Authors:** Reva Schwartz et al., NIST / NIST Associates
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** The ARIA Companion Document is the detailed methodology specification for NIST's ARIA (Assessing Risks and Impacts of AI) evaluation program — companion to the reported results published in NIST AI 700-2. While the 700-2 comparison covered ARIA's outputs and CoRIx scores, this document covers the *design* of ARIA: the three-level testbed architecture, the annotation schema with five categories, CoRIx's tree-level measurement model, the proxy scenario methodology, and the governance rationale for ARIA's design choices. This provides deeper implementation detail for EAGCF's evaluation architecture than what was available from 700-2 alone.

---

## 1. Document Scope Alignment

| Dimension | ARIA Companion | EAGCF |
|---|---|---|
| **Primary purpose** | Design specification for a NIST evaluation program measuring real-world AI risk materialization | Enterprise governance and control operating model |
| **Risk definition** | NIST AI RMF definition: probability × magnitude of consequences | Tier-based risk model (5 tiers): probability × severity × reversibility |
| **Lifecycle alignment** | NIST AI RMF lifecycle; AI 600-1 risk taxonomy | 11-stage lifecycle wired to Deliverable D gate intensity |
| **Measurement philosophy** | Contextual robustness: performance under real-world variation, not just controlled test conditions | KPI/KRI/KCI framework + SLA thresholds (controlled conditions) |
| **Key output** | CoRIx hierarchical risk scores from human-AI interaction data | Pass/fail control validation + tier-based risk acceptance |

---

## 2. ARIA Three-Level Testbed vs. EAGCF

### Level 1: Model Testing (Automated)

| ARIA Level 1 Component | EAGCF Coverage | Status |
|---|---|---|
| **Pre-defined automated scripts** confirm capabilities and guardrail adherence before human testing | Part XII §12.2 (control validation matrix: pre-deployment testing with pass/fail thresholds) | ✅ Covered |
| **Guardrail definition**: violated when prohibited content released OR permitted content withheld | Part XI §11.1 (EP-1 through EP-9: enforcement points define prohibited/permitted content boundaries) | ✅ Covered |
| **Capability confirmation** against claimed performance before deployment | Part XII §12.2 (benchmark validation: MDL-01 benchmark against declared specifications) | ✅ Covered |

### Level 2: Red Teaming (Adversarial Users)

| ARIA Level 2 Component | EAGCF Coverage | Status |
|---|---|---|
| **Adversarial human red teamers** attempt guardrail violations via structured prompting | Part XII §12.1 (red-team pipeline: attack library → generator → runner → classifier; external red team requirement) | ✅ Covered |
| **Attack strategy logging** (what adversarial strategies were attempted) | Part XII §12.1 (red-team pipeline output: structured attack report) | ✅ Covered |
| **Post-session questionnaires** for red teamers | Not required | ⚠️ Partial — EAGCF requires red-team structured output but not post-session questionnaire methodology |
| **Guardrail violation classification**: user-induced vs. system failure | Part XII §12.1 (red-team classifier: violation type attribution) | ✅ Covered |

### Level 3: Field Testing (Everyday Users)

| ARIA Level 3 Component | EAGCF Coverage | Status |
|---|---|---|
| **Non-adversarial everyday users** in realistic scenario conditions | Not formally required | ❌ Gap — N700-01 (confirmed from 700-2 comparison): structured field testing with real end-users not required for Tier 1 systems |
| **Free-play interaction mode** (unstructured natural use) | Not addressed | ❌ Gap — EAGCF red-team is adversarial/structured; natural unstructured usage testing not required |
| **Post-session questionnaires for users** (perception of risk exposure, utility) | Not addressed | ❌ Gap — N700-03 (confirmed): user perception surveys not required |
| **Proxy scenario design** (controlled scenario representing real-world risk conditions) | Deliverable G §G.3 (AI Impact Assessment includes use-case risk scenarios); Part IV §4.1 (use-case risk tiering) | ⚠️ Partial — risk scenario analysis present; structured proxy scenario testbed not required |

---

## 3. ARIA Annotation Schema vs. EAGCF

ARIA's annotation schema has five categories applied to every AI interaction. This provides a structured quality model for AI outputs that EAGCF can reference.

### Annotation Category 1: Risk Assessment (Was a guardrail violated?)

| ARIA Annotation Item | EAGCF Coverage | Status |
|---|---|---|
| **Was prohibited content released?** | Part XI (EP-5: output classifier); GEN-02 (content safety) — automated detection | ✅ Covered |
| **Was permitted content withheld?** (over-refusal = guardrail violation) | Part V §5.7 (OUT-01/02: response relevance; over-restriction as an output quality signal) | ⚠️ Partial — under-response/over-refusal is a monitoring signal but not formally classified as a guardrail violation type |
| **Was the violation user-induced or system-initiated?** | Part XII §12.1 (red-team: attack attribution to input vs. model) | ✅ Covered |

### Annotation Category 2: Content Characterization

| ARIA Annotation Item | EAGCF Coverage | Status |
|---|---|---|
| **Quality and relevance of AI-generated content per turn** | Part V §5.7 (OUT-01: response quality; OUT-03: factuality) | ✅ Covered |
| **Accuracy and groundedness of factual claims** | Part V §5.7 (OUT-03: output factuality — hallucination detection) | ✅ Covered |
| **Potential for harm in content** | Part XI §11.1 (EP-5: output classifier with harm taxonomy) | ✅ Covered |

### Annotation Category 3: Dialogue Dynamics

| ARIA Annotation Item | EAGCF Coverage | Status |
|---|---|---|
| **Over-reliance patterns** (user deferring to AI without critical evaluation) | Part V §5.7 (OUT-06: human override requirement); Part VI §6.3 (HITL governance) | ⚠️ Partial — mechanisms to enforce human review present; monitoring for over-reliance behavioral patterns not specified |
| **User trust calibration** (appropriate vs. excessive trust in AI) | Not specified | ⚠️ Partial — HITL and override mechanisms present; user trust calibration as a monitoring signal not required |
| **Interplay between user prompting and AI response escalation** | Part V §5.4 (PRM domain: multi-turn memory boundary controls) | ⚠️ Partial — multi-turn context controls present; escalation pattern detection not formalized |

### Annotation Category 4: Interaction Style

| ARIA Annotation Item | EAGCF Coverage | Status |
|---|---|---|
| **Persuasive or confidently stated tone** (epistemic overconfidence) | Part V §5.7 (OUT-03: factuality — confidence calibration requirement) | ⚠️ Partial — factuality monitored; rhetorical persuasiveness as a distinct risk signal not specified |
| **Authoritative framing of uncertain information** | Part V §5.7 (OUT-03: hallucination detection) | ⚠️ Partial — hallucination detected; confident framing of correct but misleading information not separately monitored |

### Annotation Category 5: Dialogue Utility

| ARIA Annotation Item | EAGCF Coverage | Status |
|---|---|---|
| **Utility of output for user's intended purpose** | Part V §5.7 (OUT-01: response relevance and utility) | ✅ Covered |
| **Tradeoff analysis: utility vs. risk** (high utility + low risk = optimal; low utility + high risk = worst) | Part IV §4.8 (assurance model: control effectiveness vs. adoption friction); Part VIII (adoption acceleration) | ⚠️ Partial — governance misallocation diagnostic addresses over-governing low-risk; utility-risk tradeoff per-interaction not measured |

---

## 4. CoRIx Measurement Instrument — Extended Analysis

Building on the NIST AI 700-2 comparison, the Companion Document provides more detail on CoRIx design:

| CoRIx Design Attribute | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Multidimensional output** (4 initial dimensions; expanding to 10 including all 7 AI RMF characteristics) | Part XII §12.2 (control validation: multi-domain assessment) | ⚠️ Partial — multiple dimensions assessed but not aggregated into a hierarchical score tree |
| **Tree-structure output** (6 levels from raw labels to top-level dimensions) | Not addressed | ❌ Gap — EAGCF uses categorical tier-based assessment; no hierarchical measurement aggregation |
| **Interdependency analytics** (tradeoffs between trustworthy characteristics mapped) | Not addressed | ❌ Gap — EAGCF assesses each domain independently; inter-domain tradeoff analysis not required |
| **Across-dimension weighting** (configurable relative importance of each dimension) | Deliverable B (risk tiering: severity and probability weighting) | ⚠️ Partial — risk weighting at tier level; per-characteristic weighting within an evaluation not configurable |
| **Mixed methods integration** (quantitative AI outputs + qualitative human judgments) | Part XII §12.1 (red-team: human + automated); Part VI §6.3 (HITL) | ✅ Covered |
| **Annotator disagreement preserved** (not resolved to majority; surfaced as uncertainty) | Not addressed | ❌ Gap — EAGCF does not specify annotation quality methodology for human evaluation |
| **Proxy scenario design** (reproducible, comparable, controlled) | Deliverable G §G.3 (impact assessment scenarios) | ⚠️ Partial — risk scenarios defined; standardized proxy scenario protocol not formalized |

---

## 5. Why Current Testing Approaches Are Insufficient — ARIA's Governance Critique vs. EAGCF Position

ARIA explicitly identifies limitations of current AI testing paradigms. EAGCF's position on each:

| ARIA Critique | Implication | EAGCF Response |
|---|---|---|
| **Performance-based metrics don't correlate with real-world risk** | Accuracy/F1 scores don't predict whether harm occurs in deployment | ✅ EAGCF's KRI framework focuses on behavioral signals (drift, guardrail violations, escalations) not just performance metrics |
| **Static benchmark datasets are retrospective and model-centric** | Can't capture socio-technical dynamics of deployment | ⚠️ Partial — EAGCF's monitoring signals are runtime-focused but don't require human-in-the-loop scenario testing |
| **RLHF and keyword filtering are reductionist** | Not generalizable; can introduce unintended harms | ✅ EAGCF's defense-in-depth posture (9 enforcement points) goes beyond RLHF/filtering |
| **Controlled testing ≠ real-world deployment behavior** | Gap between lab and deployment is a fundamental governance risk | ⚠️ Partial — N700-01 gap: field testing with real users not required |

---

## 6. Scoring Summary

| ARIA Companion Area | Items | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| Level 1: Model testing | 3 | 3 | 0 | 0 | 0 |
| Level 2: Red teaming | 4 | 3 | 0 | 1 | 0 |
| Level 3: Field testing | 4 | 0 | 0 | 1 | 3 |
| Annotation schema (5 categories) | 12 | 5 | 0 | 6 | 1 |
| CoRIx design attributes | 7 | 1 | 0 | 3 | 3 |
| ARIA governance critique | 4 | 2 | 0 | 2 | 0 |
| **TOTALS** | **34 items** | **14 (41%)** | **0 (0%)** | **13 (38%)** | **7 (21%)** |

**Coverage interpretation:** 79% total coverage (41% direct + 38% partial). EAGCF covers automated and adversarial testing comprehensively. The gaps (21%) are concentrated in: (1) real-world field testing (confirmed N700-01), (2) CoRIx hierarchical measurement (specialized research measurement, not an enterprise governance requirement), and (3) interaction style and over-reliance monitoring (emerging best practice). The partial rate reflects ARIA's depth as a specialized evaluation methodology versus EAGCF's governance framework scope.

---

## 7. Gap Items: Recommended EAGCF Additions from ARIA Companion

| Gap ID | Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N-ARIA-01** | Level 3 field testing | **Structured field testing for Tier 1 systems**: Extend N700-01 recommendation — require structured field testing with representative (non-adversarial) users for Tier 1 high-risk AI systems using realistic proxy scenarios based on the AI Use Case Registration's intended use cases | High | Part VII §7.5 (assurance evidence pack): add field testing as required Tier 1 evidence activity |
| **N-ARIA-02** | Annotation Category 3 | **Over-reliance monitoring signal**: Add a runtime monitoring signal for AI over-reliance patterns: frequency of users accepting AI output without explicit review, override rate decline trends, and escalation-suppression patterns | Medium | Deliverable E (monitoring signal catalog) — add MON-24: Over-reliance signal |
| **N-ARIA-03** | Annotation Category 4 | **Epistemic overconfidence monitoring**: Add factuality confidence calibration as a monitoring requirement — AI outputs expressing high confidence on contested or uncertain facts should be flagged as a separate risk category from factual errors | Medium | Part V §5.7 (OUT-03: factuality) — extend to distinguish calibration errors from hallucinations |
| **N-ARIA-04** | CoRIx interdependency | **Trustworthiness tradeoff documentation**: For Tier 1 systems, require documentation of known tradeoffs between trustworthy characteristics (e.g., safety vs. utility, explainability vs. performance) in the AI Impact Assessment | Low | Deliverable G §G.3 (AI Impact Assessment) — add trustworthiness tradeoff section |

---

## 8. Key ARIA Governance Insights for EAGCF

**Most actionable insight for EAGCF:**

The ARIA Companion Document's proxy scenario methodology is directly applicable to EAGCF's AI Use Case Registration process. Each Tier 1 AI system registered in Deliverable G §G.5 has a defined intended use, risk profile, and user population — exactly the inputs needed to design ARIA-style proxy scenarios. EAGCF could add a guidance note to the Impact Assessment template (§G.3) recommending that Tier 1 impact assessments include at least one standardized proxy scenario test derived from the intended use case.

**Contextual robustness as an enterprise governance standard:**

ARIA defines contextual robustness as "an AI system's ability to maintain trustworthy functionality across varying real-world deployment contexts." This is a governance standard that enterprises can adopt operationally: every Tier 1 system should be evaluated not just for performance in controlled test conditions, but for performance under representative variation in user behavior, input distribution, and deployment context. EAGCF's SLA table (Part XIV §14.2) already sets thresholds — extending these to contextual robustness conditions (user population variation, input domain shift) would bring EAGCF's measurement framework closer to ARIA's standard.

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Comparisons completed (18 sources): NIST AI 100-1, 100-2, 100-4, 100-5, 600-1, 700-1, 700-2 + ARIA Companion, 800-1, 800-2, IR 8596; ISO crosswalks (42001/23894, 42005, 5338/5339); OECD/EU AI Act crosswalk; Google DeepMind Gap Analysis; AI Verify crosswalks; Americas AI Action Plan*
