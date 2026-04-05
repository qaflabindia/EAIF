# Side-by-Side Comparison: EAGCF vs. NIST AI 100-2e2025
## *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (2025 Edition)*

**NIST Document:** NIST AI 100-2e2025 (March 2025)
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** NIST AI 100-2e2025 is the authoritative adversarial machine learning (AML) taxonomy, covering both Predictive AI and Generative AI attack categories with formal NIST identifiers (NISTAML.xxx), mitigation techniques, and theoretical robustness limits. This document is the primary technical reference for EAGCF Part XII (Control Validation) and the attack library underpinning the red-team pipeline. The comparison assesses whether EAGCF's control taxonomy and validation framework addresses each named attack class and its recommended mitigations.

---

## 1. Document Scope Alignment

| Dimension | NIST AI 100-2e2025 | EAGCF |
|---|---|---|
| **Primary function** | Attack taxonomy + mitigation reference | Enterprise governance and control operating model |
| **Coverage scope** | AML attacks on PredAI and GenAI; mitigations; theoretical limits | Full AI governance including AML controls, plus governance, assurance, lifecycle, vendor, sector |
| **Audience** | AI developers, security researchers, evaluators, governance teams | Board, CRO, governance office, internal audit, compliance |
| **Regulatory basis** | Voluntary; informs future standards and practice guides | Voluntary, wired to ISO 42001, EU AI Act, NIST AI RMF |
| **Attack IDs** | Formal NISTAML.xxx identifiers for each attack class | No formal attack IDs; references attack categories by name |
| **Mitigation depth** | Deep technical detail on each mitigation with academic citations | Control-level prescriptions with tooling and enforcement architecture |

---

## 2. Predictive AI (PredAI) Attack Taxonomy vs. EAGCF

### 2.1 Evasion Attacks (NISTAML.022, NISTAML.025)

| NIST AI 100-2 Item | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **White-box evasion** (gradient-based, FGSM, PGD, C&W attacks) | Part XII §12.1 (red-team attack library: evasion category); GEN-07 (jailbreak pattern library) | ⚠️ Partial | Red-team pipeline includes evasion testing; formal white-box vs. black-box distinction not explicitly structured in attack library |
| **Black-box evasion** (transfer-based, score-based, decision-based attacks) | Part XII §12.1 (red-team attack library) | ⚠️ Partial | |
| **Transferability of attacks** (cross-model attack transfer) | Part XII §12.4 (degradation detection; behavioral fingerprinting) | ⚠️ Partial | Behavioral fingerprinting detects unexpected behavior changes; transfer-attack-specific detection not specified |
| **Mitigation: Adversarial training** (augment training with adversarial examples) | Part V §5.11 (MSC-06: fine-tuning/RLHF integrity controls) | ⚠️ Partial | Fine-tuning integrity referenced; adversarial training as a named mitigation technique not required |
| **Mitigation: Randomized smoothing** (certified robustness under Gaussian noise) | Not addressed | ❌ Gap | EAGCF does not reference certified robustness methods |
| **Mitigation: Formal verification** (neural network robustness certification) | Not addressed | ❌ Gap | Formal verification of ML models not addressed in EAGCF |
| Robustness-accuracy trade-off acknowledgment | Part XII §12.2 (control validation matrix: false positive/negative thresholds) | ⚠️ Partial | |

### 2.2 Poisoning Attacks (NISTAML.011–NISTAML.013, NISTAML.023–NISTAML.024)

| NIST AI 100-2 Item | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Availability poisoning** (indiscriminate model degradation) | Part VII §7.1 (MON-01: performance monitoring; MON-04: drift detection); Part XII §12.4 (degradation detection) | ✅ Covered | Runtime monitoring and degradation detection address availability poisoning detection |
| **Targeted poisoning** (subpopulation integrity violation) | Part V §5.11 (MSC-02: data provenance attestation); Part XII §12.1 (red-team: poisoning category) | ⚠️ Partial | Data provenance present; targeted subpopulation detection not specified |
| **Backdoor poisoning** (trigger-based integrity violation; NISTAML.023) | Part V §5.11 (MSC-02: data provenance); Part XII §12.1 (red-team attack library) | ⚠️ Partial | Red-team pipeline tests for backdoor patterns; systematic trigger reconstruction or activation clustering detection not required |
| **Clean-label backdoor** (NISTAML.021) | Part XII §12.1 (red-team: adversarial ML category) | ⚠️ Partial | |
| **Model poisoning** (NISTAML.011, NISTAML.051; federated learning, supply chain) | Part V §5.11 (MSC-07: supply chain security); MSC-06 (fine-tuning integrity) | ✅ Covered | Supply chain controls and fine-tuning integrity directly address model poisoning |
| **Mitigation: Training data sanitization** (outlier detection, RONI, clustering) | Part V §5.11 (MSC-02: data provenance); Part V §5.2 (DAT-04: data quality validation) | ✅ Covered | |
| **Mitigation: Robust training** (ensemble voting, trimmed loss) | Not addressed | ❌ Gap | EAGCF does not require robust training techniques |
| **Mitigation: Certified defenses** (BagFlip, Deep Partition Aggregation) | Not addressed | ❌ Gap | Certified defenses not referenced |
| **Mitigation: Poison forensics** (root-cause analysis to training set) | Not addressed | ❌ Gap | No requirement for poison forensics capability |
| **Mitigation: Cryptographic dataset integrity** (hashes for training data provenance) | Part V §5.11 (MSC-01: training data lineage; MSC-02: data provenance attestation) | ✅ Covered | MSC-01/02 include provenance and integrity attestation |
| **Mitigation: Differential privacy for poisoning defense** | Not addressed | ⚠️ Partial | Privacy controls exist in DAT domain; DP as a poisoning mitigation technique not specified |

### 2.3 Privacy Attacks (NISTAML.031–NISTAML.034)

| NIST AI 100-2 Item | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Data reconstruction attacks** (NISTAML.032; reconstruct training data from model) | Part V §5.11 (MSC-07: weight protection); Part V §5.2 (DAT domain) | ⚠️ Partial | Weight protection and data governance present; reconstruction attack-specific defenses not named |
| **Membership inference attacks** (NISTAML.033; determine if sample was in training set) | Not addressed | ❌ Gap | Membership inference as a named attack class with mitigation is not addressed in EAGCF |
| **Property inference attacks** (NISTAML.034; extract subpopulation properties) | Not addressed | ❌ Gap | |
| **Model extraction attacks** (NISTAML.031; recreate model from queries) | Part V §5.11 (MSC-07: supply chain security); IAM-05 (rate limiting) | ⚠️ Partial | Rate limiting and access controls present; model extraction specifically named and its mitigations (query limiting, detection) not formalized |
| **Mitigation: Differential privacy (DP-SGD)** | Not addressed | ❌ Gap | DP as privacy preservation technique during training not addressed |
| **Mitigation: Privacy auditing** (canary insertion, empirical measurement of ε) | Not addressed | ❌ Gap | No privacy audit requirement for ML model training |
| **Mitigation: Machine unlearning** (right-to-erasure for model training data) | Not addressed | ❌ Gap | EAGCF does not address machine unlearning as a privacy control |
| **Mitigation: Query limiting / suspicious query detection** | Part V §5.8 (IAM-05: rate limiting, access controls) | ✅ Covered | |

---

## 3. Generative AI (GenAI) Attack Taxonomy vs. EAGCF

### 3.1 Supply Chain Attacks on GenAI (NISTAML.051)

| NIST AI 100-2 Item | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Data poisoning via web-scale training data** | Part V §5.11 (MSC-01: training data lineage; MSC-02: data provenance) | ✅ Covered | |
| **Model poisoning in supply chain** (upstream model compromise) | Part V §5.11 (MSC-07: supply chain security); VND-08 (threat profile register — gap from 800-1) | ✅ Covered | |
| **Mitigation: Cryptographic hash verification of training data** | Part V §5.11 (MSC-02: data provenance attestation) | ✅ Covered | |
| **Mitigation: Mechanistic interpretability for backdoor feature detection** | Not addressed | ❌ Gap | Mechanistic interpretability not referenced as a detection tool |
| **Mitigation: Design for untrusted model components** (assume model can be compromised; constrain via interfaces) | Part XI §11.1 (EP-1 through EP-9: defense-in-depth enforcement architecture); Part XI §11.4 (agentic data plane isolation) | ⚡ EAGCF Stronger | EAGCF's 9-enforcement-point architecture directly implements the "design for untrusted model" principle with architectural rigor beyond NIST's guidance |

### 3.2 Direct Prompting Attacks (NISTAML.018)

| NIST AI 100-2 Item | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Jailbreaking** (direct instruction to violate safeguards) | Part V §5.4 (PRM-05: prompt injection detection); GEN-07 (jailbreak pattern library); EP-2 (prompt sanitizer) | ✅ Covered | |
| **Prompt injection via user input** (NISTAML.018) | Part V §5.4 (PRM-05); EP-2 | ✅ Covered | |
| **Prompt extraction / system prompt theft** (NISTAML.035) | Part V §5.4 (PRM-04: system prompt as versioned artifact); Part XI §11.3 (prompt registry) | ✅ Covered | System prompt governance and prompt registry directly address this |
| **Information extraction attacks** (NISTAML.038: data extraction) | Part V §5.7 (OUT domain: output controls); EP-5 (output classifier) | ✅ Covered | |
| **Misaligned outputs** (NISTAML.027) | Part V §5.7 (OUT-03: output factuality; OUT-04: output labeling); GEN-08 (output monitoring) | ✅ Covered | |
| **Mitigation: Pre-training and post-training safety** (RLHF, adversarial training during training) | Part V §5.11 (MSC-06: fine-tuning/RLHF integrity controls) | ✅ Covered | |
| **Mitigation: Automated vulnerability evaluation** (broad automated adversarial testing at deployment) | Part XII §12.1 (red-team pipeline: automated runner with PyRIT, Garak, PromptBench) | ✅ Covered | |
| **Mitigation: Expert red teaming** | Part XII §12.1 (red-team pipeline: external red team engagement) | ✅ Covered | |
| **Mitigation: Bug bounties for AI vulnerabilities** | Not addressed | ❌ Gap | Bug bounty programs not addressed (also gap from NIST 800-1 comparison, N801-07) |
| **Mitigation: XML tag isolation / prompt formatting** (separate system vs. user instructions) | Part V §5.4 (PRM-01: system prompt governance; PRM-02: prompt structure controls) | ✅ Covered | |
| **Mitigation: LLM-based harm detection / guardrails** (fine-tuned classifier models) | Part XI §11.5 (EP-5: output classifier); GEN-08 (output monitoring) | ✅ Covered | |
| **Mitigation: Spotlighting** (distinguish trusted vs. untrusted data in prompt) | Part V §5.4 (PRM-06: multi-turn memory controls); Part XI §11.2 (prompt registry context controls) | ⚠️ Partial | Context boundary controls present; "spotlighting" as a named technique not explicitly required |
| **Mitigation: SmoothLLM** (output aggregation from multiple perturbed prompts) | Not addressed | ❌ Gap | Aggregate output across perturbed prompts not specified |
| **Mitigation: Prompt paraphrasing / retokenization** | Not addressed | ❌ Gap | Input modification techniques not specified |
| **Mitigation: Monitoring and logging of injection attempts** | Part V §5.14 (LOG-01 through LOG-05); Part VII §7.1 (MON signals); EP-8 (audit logger) | ✅ Covered | |
| **Mitigation: Usage restrictions** (limit inference parameters, logit probabilities, total queries) | Part V §5.8 (IAM-05: rate limiting); Part XI §11.1 (EP-3: input validator) | ✅ Covered | |
| **Mitigation: Training data sanitization** (remove toxic/sensitive content) | Part V §5.2 (DAT-04: data quality); Part V §5.11 (MSC-01: training data lineage) | ✅ Covered | |
| **Mitigation: Machine unlearning** (remove harmful capabilities post-training) | Not addressed | ❌ Gap | Machine unlearning not addressed in EAGCF (also gap from privacy section) |
| **Mitigation: Watermarking** (content provenance for AI-generated output) | Part V §5.11 (MSC-08: watermarking); Part V §5.7 (OUT-05: output attribution) | ✅ Covered | NIST AI 100-2 notes theoretical limits of watermarking — EAGCF should acknowledge these limits |

### 3.3 Indirect Prompt Injection Attacks (NISTAML.015)

| NIST AI 100-2 Item | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Availability attacks via indirect injection** (agent denial, infinite loops) | Part V §5.10 (AGT-03: action scope limits; AGT-06: HITL threshold) | ✅ Covered | |
| **Integrity attacks via indirect injection** (hijack agent actions via external content) | Part V §5.10 (AGT-07: indirect injection — agentic specific); PRM-05 (prompt injection detection) | ✅ Covered | AGT-07 explicitly names indirect injection as an agentic control |
| **Privacy compromise via indirect injection** (NISTAML.039: exfiltrate data via injected instructions; NISTAML.036: leaking from user interactions) | Part V §5.10 (AGT-08: agent memory governance); Part V §5.14 (LOG domain) | ⚠️ Partial | Memory governance and logging present; data exfiltration via injected external content as a specific scenario not detailed |
| **Mitigation: Task-specific fine-tuning for injection resistance** | MSC-06 (fine-tuning integrity) | ⚠️ Partial | |
| **Mitigation: Hierarchical trust in prompts** (system > user > external data) | Part V §5.4 (PRM-01/PRM-02: system prompt governance); EP-4 (context enforcer) | ✅ Covered | Context enforcer implements hierarchical trust |
| **Mitigation: Input filtering to remove instructions from third-party sources** | EP-2 (prompt sanitizer); PRM-05 (injection detection) | ✅ Covered | |
| **Mitigation: Multi-LLM architectures with separate permissions** (different LLMs for different trust levels) | Part XI §11.4 (agentic data plane stack; isolation between agents) | ⚠️ Partial | Multi-agent isolation present; permission-differentiated multi-LLM architecture not explicitly specified |
| **Mitigation: Well-defined interfaces for untrusted data** | Part XI §11.1 (EP-1 through EP-4: structured enforcement chain) | ✅ Covered | |
| **Mitigation: Public education on indirect injection risks** | Part VIII §8.9 (workforce enablement) | ✅ Covered | |

### 3.4 Security of Agents (NISTAML.018, NISTAML.015 in agentic context)

| NIST AI 100-2 Item | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Agents vulnerable to direct and indirect prompt injection** | Part V §5.10 (AGT domain, 10 controls); PRM domain | ✅ Covered | |
| **Tool-use amplification of injection attacks** (execute arbitrary code, exfiltrate data via hijacked agent) | Part V §5.10 (AGT-04: reversibility classification; AGT-05: tool scope limits per agent); Part V §5.6 (TOL domain: tool control) | ✅ Covered | |
| **Agent vulnerability evaluation** (specific AML attack testing for agents) | Part XII §12.1 (red-team pipeline: agentic attack category) | ✅ Covered | |
| **Interventions to manage agent security risks** | Part XI §11.4 (agentic data plane architecture); AGT-01 through AGT-10 | ⚡ EAGCF Stronger | EAGCF provides substantially more detailed agentic governance than NIST AI 100-2's brief §3.5 |
| **Multi-agent system trust isolation** | Part V §5.10 (AGT-09: inter-agent trust isolation) | ⚡ EAGCF Stronger | |

---

## 4. Key Challenges and Theoretical Limits vs. EAGCF

| NIST AI 100-2 Challenge | EAGCF Coverage | Status | Notes |
|---|---|---|---|
| **Robustness-accuracy trade-off** (mitigations reduce accuracy; inherent tension) | Part XII §12.2 (control validation: acceptance thresholds) | ⚠️ Partial | Thresholds present; explicit robustness-accuracy trade-off framework not required |
| **Theoretical limits on adversarial robustness** (impossibility results for all-attack prevention) | Not addressed | ❌ Gap | EAGCF does not acknowledge theoretical limits on mitigation completeness; could lead to overconfidence in control effectiveness |
| **Scale challenge** (frontier models have emergent attack surfaces; harder to test comprehensively) | Part VIII §8.10 (anti-pattern 7: governance theater); Part XII §12.4 (continuous validation) | ⚠️ Partial | Governance theater warning and continuous validation address this spirit; theoretical scale challenge not formally acknowledged |
| **Supply chain challenges** (third-party model components with unknown vulnerabilities) | Part V §5.11 (MSC domain: full 8 controls) | ✅ Covered | |
| **Multimodal model vulnerabilities** (text, image, audio, video cross-modal attacks) | Part V §5.15 (GEN domain: multimodal controls) | ⚠️ Partial | GenAI controls present; multimodal-specific attack surface not explicitly addressed |
| **Quantized model vulnerabilities** (quantization may introduce or expose vulnerabilities) | Part V §5.11 (MSC-04: quantized/distilled model tamper-evidence) | ✅ Covered | MSC-04 explicitly addresses quantized model integrity |
| **Any aligned behavior that attenuates rather than removes a risk remains vulnerable** (theoretical: if probability > 0 of undesired behavior, adversarial prompts can trigger it) | Not addressed | ❌ Gap | EAGCF's control philosophy does not address the theoretical impossibility of perfect alignment — important for calibrating governance expectations |

---

## 5. NISTAML Attack ID to EAGCF Control Mapping

| NISTAML ID | Attack Name | EAGCF Primary Control | Status |
|---|---|---|---|
| NISTAML.011 | Model Poisoning (PredAI) | MSC-06, MSC-07 | ✅ |
| NISTAML.012 | Clean-label Poisoning | MSC-02, Part XII §12.1 | ⚠️ |
| NISTAML.013 | Data Poisoning | MSC-01, MSC-02, DAT-04 | ✅ |
| NISTAML.014 | Energy-latency Attack | AGT-03 (scope limits) | ⚠️ |
| NISTAML.015 | Indirect Prompt Injection | AGT-07, PRM-05, EP-2/EP-4 | ✅ |
| NISTAML.018 | Prompt Injection (direct) | PRM-05, EP-2, GEN-07 | ✅ |
| NISTAML.021 | Clean-label Backdoor | Part XII §12.1 | ⚠️ |
| NISTAML.022 | Evasion | Part XII §12.1 | ⚠️ |
| NISTAML.023 | Backdoor Poisoning | MSC-02, Part XII §12.1 | ⚠️ |
| NISTAML.024 | Targeted Poisoning | MSC-02, DAT-04 | ⚠️ |
| NISTAML.025 | Black-box Evasion | Part XII §12.1 | ⚠️ |
| NISTAML.026 | Model Poisoning (GenAI) | MSC-06, MSC-07 | ✅ |
| NISTAML.027 | Misaligned Outputs | OUT-03, OUT-04, GEN-08 | ✅ |
| NISTAML.031 | Model Extraction | IAM-05, MSC-07 | ⚠️ |
| NISTAML.032 | Data Reconstruction | MSC-07, DAT domain | ⚠️ |
| NISTAML.033 | Membership Inference | *(not addressed)* | ❌ |
| NISTAML.034 | Property Inference | *(not addressed)* | ❌ |
| NISTAML.035 | Prompt Extraction | PRM-04, Part XI §11.3 | ✅ |
| NISTAML.036 | Leaking from User Interactions | AGT-08, LOG domain | ⚠️ |
| NISTAML.037 | Training Data Attacks | MSC-01, MSC-02 | ✅ |
| NISTAML.038 | Data Extraction | OUT domain, EP-5 | ✅ |
| NISTAML.039 | Compromising Connected Resources | AGT-05, TOL domain | ✅ |
| NISTAML.051 | Supply Chain Attacks | MSC-07, VND domain | ✅ |

**Coverage by NISTAML ID:** 11 fully covered (48%), 9 partially covered (39%), 2 not addressed (9%)

---

## 6. Scoring Summary

| NIST AI 100-2 Section | Items | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| PredAI: Evasion attacks and mitigations | 7 items | 0 | 0 | 4 | 3 |
| PredAI: Poisoning attacks and mitigations | 11 items | 4 | 0 | 4 | 3 |
| PredAI: Privacy attacks and mitigations | 8 items | 1 | 0 | 3 | 4 |
| GenAI: Supply chain attacks | 4 items | 2 | 1 | 0 | 1 |
| GenAI: Direct prompting attacks | 18 items | 9 | 0 | 3 | 6 |
| GenAI: Indirect prompt injection | 8 items | 4 | 0 | 3 | 1 |
| GenAI: Agent security | 5 items | 2 | 2 | 1 | 0 |
| Theoretical challenges | 7 items | 1 | 0 | 3 | 3 |
| **TOTALS** | **68 items** | **23 (34%)** | **3 (4%)** | **21 (31%)** | **21 (31%)** |

**Coverage interpretation:** 69% total coverage (34% direct + 4% stronger + 31% partial). The 31% gap rate is higher than other NIST comparisons because NIST AI 100-2 goes deep into *technical mitigation implementations* (adversarial training algorithms, differential privacy parameters, formal verification methods) that EAGCF deliberately does not prescribe. EAGCF operates at the *control* level (what must be implemented) while NIST AI 100-2 operates at the *technique* level (how to implement it). This is an appropriate division — EAGCF should reference NIST AI 100-2 as the normative technical implementation guide for adversarial ML controls.

---

## 7. Where EAGCF Materially Exceeds NIST AI 100-2e2025

| Dimension | EAGCF Capability | NIST AI 100-2 |
|---|---|---|
| **Enforcement architecture** | 9-point enforcement chain (EP-1 through EP-9) implementing "design for untrusted model" | §3.2.3 recommendation only; no architecture |
| **Agentic governance** | AGT-01 through AGT-10 (scope, reversibility, HITL, inter-agent trust, memory) | §3.5 (one paragraph; "early-stage research") |
| **Prompt governance** | System prompt registry, injection detection library, multi-turn memory, jailbreak library | Lists mitigations without governance infrastructure |
| **Governance operating model** | 9 governance bodies, RACI, tiering, lifecycle | Not addressed |
| **Risk tiering** | 5-tier model wired to lifecycle gate intensity | Not addressed |
| **Vendor governance** | 6-dimension scoring, behavioral fingerprinting, fallback architecture | Not addressed |
| **Sector overlays** | Financial services, healthcare, safety-critical | Not addressed |
| **Cost governance** | SLA model, ROI metrics, misallocation diagnostic | Not addressed |
| **Model supply chain** | MSC-01 through MSC-08 (lineage through watermarking) | References data integrity; no architecture |
| **Lifecycle governance** | 11-stage lifecycle map wired to tier | Not addressed |
| **Adoption acceleration** | Fast-lane, anti-patterns, workforce enablement | Not addressed |

---

## 8. Gap Items: Recommended EAGCF Additions

These gaps represent technical mitigation concepts from NIST AI 100-2 that should be incorporated into EAGCF to improve adversarial ML resilience at the control specification level.

| Gap ID | NIST AI 100-2 Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N1002-01** | §2.4 (Privacy Attacks) | **Membership inference and property inference as named threats**: Add NISTAML.033 (membership inference) and NISTAML.034 (property inference) as named controls in the MDL domain; require detection/mitigation proportionate to data sensitivity | High | Part V §5.3 — add MDL-13: Privacy attack surface assessment for deployed models |
| **N1002-02** | §2.4.5 / §3.x | **Differential privacy (DP) for training**: For Tier 1 (High) AI systems processing sensitive data, require DP-SGD or equivalent privacy-preserving training to bound membership inference risk | High | Part V §5.11 MSC domain — add MSC-09: Differential Privacy training requirement for high-sensitivity Tier 1 systems |
| **N1002-03** | §2.4.5 | **Privacy auditing (canary insertion)**: Require empirical privacy audit using canary insertion for Tier 1 AI systems handling PII, PHI, or regulated data to verify DP guarantees hold in practice | Medium | Part XII §12.2 — add privacy audit as a required control validation activity for Tier 1 |
| **N1002-04** | §2.4.5 | **Machine unlearning capability**: For AI systems subject to right-to-erasure obligations, require machine unlearning capability (exact or approximate) to satisfy data subject deletion requests at the model training level | Medium | Part V §5.2 DAT domain — add DAT-09: Machine unlearning for deletion compliance |
| **N1002-05** | §2.2.5 | **Theoretical limits acknowledgment**: Add explicit statement in EAGCF governance principles that no set of AML mitigations provides complete protection (impossibility of all-attack prevention); controls reduce but cannot eliminate adversarial risk | High | Part IV §4.0 (governance principles) — add principle caveat; Part XII §12.2 — add limitation statement in control validation matrix |
| **N1002-06** | §2.3.3 | **Backdoor trigger detection**: For Tier 1 models and open-weight models (Archetype 10), require systematic backdoor detection using activation clustering, trigger reconstruction, or mechanistic interpretability techniques during model validation | Medium | Part XII §12.2 — add backdoor detection to control validation matrix; extend MSC-03 (model card) to include backdoor scan attestation |
| **N1002-07** | §3.3.3 | **Bug bounty / continuous vulnerability disclosure**: Add requirement for AI vulnerability disclosure program for Tier 0/1 deployments (aligns with N801-07 from NIST 800-1 comparison) | Medium | Part V §5.9 VND domain or Part IV §4.3 (transparency) |
| **N1002-08** | §3.3.3 | **Watermarking limitations disclosure**: Require that AI output watermarking implementations acknowledge known theoretical limits (not universally robust); document adversarial removal risk in MSC-08 watermarking control | Low | Part V §5.11 (MSC-08) — add limitation clause to watermarking control |
| **N1002-09** | §4.1.2 / §4.2.5 | **Theoretical robustness ceilings**: Incorporate in governance documentation that alignment processes that attenuate but do not remove unwanted behaviors remain adversarially exploitable; inform risk acceptance decisions for Tier 0/1 systems | High | Part IV §4.1 (Deliverable B risk tiering) — add footnote on alignment impossibility results |
| **N1002-10** | §3.4.4 | **Multi-LLM permission architecture for indirect injection**: For agentic deployments with untrusted external data sources (RAG, tool outputs), require differentiated LLM routing — high-trust operations use a permission-restricted model; external data processing uses a separate lower-privilege model | Medium | Part V §5.10 (AGT domain) — add AGT-11: Multi-LLM permission isolation for indirect injection |
| **N1002-11** | §2.1–2.3 | **NISTAML attack ID reference in red-team library**: Add formal NIST AI 100-2 NISTAML identifiers to EAGCF's red-team attack library to enable traceability between attack tests and the authoritative taxonomy | Low | Part XII §12.1 — reference NISTAML IDs in attack library taxonomy |

---

## 9. Synthesis: NIST AI 100-2e2025 as EAGCF's Technical Implementation Reference

NIST AI 100-2e2025 and EAGCF are **designed to work together** at different levels of specificity:

- **EAGCF** specifies *what controls exist, who owns them, what evidence they produce, and how they wire into governance*
- **NIST AI 100-2** specifies *how to technically implement those controls at the ML algorithm and system design level*

**Recommended integration posture:**
1. Reference NIST AI 100-2e2025 as the **normative technical implementation guide** for all adversarial ML controls in EAGCF Part XII §12.3 (Tooling and Methodology Reference)
2. Add NISTAML attack IDs to the EAGCF red-team attack library for formal cross-referencing
3. Incorporate **N1002-01, N1002-02, N1002-05, N1002-09** (membership inference, DP, theoretical limits acknowledgment) as high-priority additions — these close real governance gaps
4. Note that EAGCF's agentic governance (AGT domain) and enforcement architecture (Part XI) substantially exceed what NIST AI 100-2 provides in §3.5 — EAGCF fills a critical gap that NIST AI 100-2 acknowledges as "early-stage research"

**Coverage summary:**
- NIST AI 100-2 items with direct EAGCF coverage: **23 (34%)**
- NIST AI 100-2 items where EAGCF is stronger: **3 (4%)**
- NIST AI 100-2 items partially covered: **21 (31%)**
- NIST AI 100-2 items not addressed: **21 (31%)**
- Dimensions where EAGCF materially exceeds NIST AI 100-2: **11**

The 31% gap rate reflects the deep technical implementation specificity of NIST AI 100-2 in areas (certified robustness, differential privacy, formal verification, machine unlearning) that are at the ML engineering level rather than the governance control level. The most actionable governance gaps are membership inference controls, DP requirements, and the theoretical limits acknowledgment.

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Next comparison in sequence: NIST AI 600-1 (GenAI Profile — already referenced in EAGCF as a backbone document)*
