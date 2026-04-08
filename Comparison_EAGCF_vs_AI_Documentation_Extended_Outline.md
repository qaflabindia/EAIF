# Side-by-Side Comparison: EAGCF vs. NIST Extended Outline — AI Dataset and Model Documentation Standard
## *Proposed Zero Draft for a Standard on Documentation of AI Datasets and AI Models*

**Source Document:** `Extended Outline - Proposed Zero Draft for a Standard on Documentation of AI datasets and AI models_September 2025.pdf` (NIST, September 2025)
**Issuing Body:** NIST (AI Standards Zero Drafts pilot project, launched March 2025)
**Intended path:** INCITS/AI → ISO/IEC JTC 1/SC 42 international standard
**Comment deadline:** October 17, 2025
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.3, 2026)
**Comparison Date:** April 2026
**Analyst Note:** This NIST pre-standard outline proposes structured documentation templates for AI datasets and AI models — the next-generation successor to current model cards, data cards, and dataset documentation practices. It is not yet a finalized standard (it is a "zero draft" solicitation) but represents the direction NIST intends to take international AI documentation standards via ISO/IEC JTC 1/SC 42. For EAGCF, the critical comparison is against MDL-05 (model card), the AI-SBOM (MSC-09), the AI Use Case Registration (Deliverable G §G.5), and the DPIA template (Deliverable G §G.8). This document is the most detailed AI documentation specification available and will likely become a normative ISO/IEC standard within 3–5 years.

---

## 1. Document Scope Alignment

| Dimension | AI Documentation Extended Outline | EAGCF |
|---|---|---|
| **Document type** | Pre-standard outline for public-facing AI dataset and model documentation templates | Enterprise governance and control operating model |
| **Primary purpose** | Provide standardized templates for documenting AI datasets and models; enable comparability, reuse, and trust | Enable enterprises to govern, control, and assure AI use |
| **Documentation scope** | Public-facing documentation of datasets and models (not AI systems) | Internal and external documentation across full governance lifecycle |
| **Governance integration** | Clause 8 (Governance): framework compliance disclosure field | Part V §5.3 (MDL-05 model card); Part XVI §16.7.1 (AI-SBOM); Deliverable G templates |
| **Standard status** | Pre-standard — all fields are "should" (guidance); community input sought on which become "shall" | Voluntary enterprise standard; ISO 42001 certification-aligned |
| **Key design goal** | Comprehensibility, informativeness, correctness, judiciousness, freshness, interoperability, findability, maintainability | Governance depth, proportionality, audit defensibility, adoption acceleration |

---

## 2. AI Dataset Documentation Template vs. EAGCF

### Field 1: Dataset Identifying Descriptors

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Formal identifier, human-readable description, URL | Part V §5.2 (DAT-01: dataset registry — unique identifier and description required) | ✅ Covered |
| Authors/creators, contact details | Part V §5.2 (DAT-01: dataset owner and custodian documented) | ✅ Covered |
| Version, digital signature (cryptographic hash manifest), release date, decommissioning date | Part V §5.2 (DAT-07: dataset versioning); Part V §5.11 (MSC-09: AI-SBOM includes hash manifest for training data) | ✅ Covered |
| Citation, attributions | Part V §5.2 (DAT-01: data provenance documentation) | ✅ Covered |
| **Documentation author(s)** (separate from dataset creators) | Not specified — EAGCF requires data owner/custodian but not a separate documentation author role | ⚠️ Partial |

### Field 2: Dataset Intended Use

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Task(s) supported, limitations, anticipated use, out-of-scope use, motivation | Part V §5.1 (STR-01: use-case registration — intended use, limitations, and out-of-scope use required); Part V §5.3 (MDL-05: model card — same fields apply to training dataset) | ✅ Covered |

### Field 3: Usage Rights and Limitations

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| License (human- and machine-readable), payments, data rightsholders | Part V §5.2 (DAT-08: dataset license and rights documentation); Part V §5.9 (VND-05: contractual rights for licensed datasets) | ✅ Covered |
| **Degree of openness** (proprietary vs. open access, specified separately for weights/code/data) | Part XVI §16.7.1 (MSC-09 AI-SBOM: model openness indicator included for base model) | ⚠️ Partial — base model openness captured; dataset-level openness classification not specifically required |

### Field 4: Dataset Composition and Provenance

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Data characteristics (size, modality, splits, attributes, structure, types/formats) | Part V §5.2 (DAT-01: dataset metadata — size, modality, format documented) | ✅ Covered |
| Funding disclosure | Not specified — EAGCF does not require funding source disclosure for training datasets | ⚠️ Partial |
| PII/confidential data identification | Part V §5.2 (DAT-02: PII classification and handling); Deliverable G §G.8 (DPIA: personal data identification) | ✅ Covered |
| Data sources, sampling procedure | Part V §5.2 (DAT-01: data provenance — source, acquisition method, and sampling) | ✅ Covered |
| Consent procedures for human-generated data | Deliverable G §G.8 (DPIA: consent documentation); Part V §5.2 (DAT-03: data collection legal basis) | ✅ Covered |
| **Data flows / chain of custody** | Not specified at this level of detail — EAGCF's DAT domain covers provenance but not a formal chain-of-custody specification for training data | ⚠️ Partial — N-AIDOC-01 below |
| **Synthetic data generation description** (algorithms, software, proportion of dataset) | Part V §5.11 (MSC-09 AI-SBOM: training data sources include synthetic data flag); Part V §5.15 (GEN domain: synthetic content controls) | ⚠️ Partial — synthetic data flag present; algorithm and proportion not specifically required in dataset documentation |
| Preprocessing description | Part V §5.2 (DAT-03: preprocessing steps documented) | ✅ Covered |
| Annotation (annotators, quality control, inter-annotator methodology) | Part V §5.2 (DAT-04: annotation governance — annotator qualifications and QC documented) | ✅ Covered |

### Field 5: Dataset Evaluation

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Risk and impact analyses | Deliverable G §G.3 (AI Impact Assessment: dataset risk included); Deliverable G §G.8 (DPIA: privacy risk for data) | ✅ Covered |
| Data analysis, data validation (TEVV) | Part V §5.2 (DAT-05: data quality validation); Part XII §12.2 (control validation: data quality gate) | ✅ Covered |

### Field 6: Maintenance and Monitoring

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Distribution, maintainer, data storage, deprecation plan, versioning policy | Part V §5.2 (DAT-07: dataset versioning and lifecycle management); Part V §5.2 (DAT-06: data retention and deprecation) | ✅ Covered |

---

## 3. AI Model Documentation Template vs. EAGCF

This is the most governance-critical section — comparing the proposed international model documentation standard against EAGCF's MDL-05 model card requirement.

### Field 1: Model Identifying Descriptors

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Model/series identifier, description, version ID | Part V §5.3 (MDL-05: model card — identifier, version, description required) | ✅ Covered |
| Release date, release methods | Part V §5.3 (MDL-05: deployment date); Deliverable D (lifecycle stage 7: deployment gate) | ✅ Covered |
| Points of contact, model developer, model owner | Part V §5.3 (MDL-05: owner, developer, and contact fields); Part VI §6.4 (RACI: model owner role) | ✅ Covered |
| Digital signature (hash) | Part V §5.11 (MSC-09: AI-SBOM includes model hash/digital signature) | ✅ Covered |
| **Model lineage** (prior models, fine-tuning mechanisms, distillation) | Part XVI §16.7.1 (MSC-09 AI-SBOM: base model ID and fine-tuning lineage included) | ✅ Covered |

### Field 2: Model Intended Use

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Intended applications, stakeholders, entities using the model | Part V §5.1 (STR-01: use-case registration — intended application and user population) | ✅ Covered |
| Capabilities offered, known limitations, out-of-scope use | Part V §5.3 (MDL-05: model card — capabilities, limitations, out-of-scope use — required fields) | ✅ Covered |

### Field 3: Usage Rights and Limitations

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| License with degree of openness (weights/code/data separately specified) | Part XVI §16.7.1 (MSC-09 AI-SBOM: model license and openness type); Part V §5.9 (VND-05: contractual license requirements) | ✅ Covered |

### Field 4: Model Design

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Algorithm type(s), model architecture | Part V §5.3 (MDL-05: model card — architecture documented) | ✅ Covered |
| Performance metrics targeted | Part V §5.3 (MDL-01: benchmark control — performance metrics and thresholds) | ✅ Covered |
| Input/output formats (size and modality constraints) | Part V §5.3 (MDL-05: model card — input/output format and constraints); Part XI §11.1 (EP-2: input scope enforcement) | ✅ Covered |

### Field 5: Model Training

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Referenced datasets (with links to dataset documentation) | Part XVI §16.7.1 (MSC-09 AI-SBOM: training data sources field) | ✅ Covered |
| Preprocessing steps, training data role, limitations | Part V §5.3 (MDL-05: training data section); Part V §5.2 (DAT-03: preprocessing documentation) | ✅ Covered |
| **Training protocols** | Not specified in detail — EAGCF requires training data documentation but not a formal training protocol document | ⚠️ Partial — N-AIDOC-02 below |

### Field 6: Model Evaluation

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Referenced evaluation datasets, evaluation data role | Part V §5.3 (MDL-01: benchmark control — evaluation dataset and methodology documented) | ✅ Covered |
| Quantitative analyses (aggregate and disaggregated) | Part XII §12.2 (control validation: disaggregated evaluation by demographic segment for Tier 1) | ✅ Covered |
| **Robustness metrics** (distributional shifts, adversarial conditions) | Part V §5.3 (MDL-04: drift detection thresholds); Part XII §12.1 (red-team: adversarial robustness testing) | ⚠️ Partial — robustness tested; formal robustness metrics not required in model card |
| Evaluation metrics with uncertainty estimates / confidence intervals | Part XII §12.2 (control validation: performance thresholds); Part XVI gap N800-08 (statistical uncertainty for benchmark scores — confirmed gap) | ⚠️ Partial — N800-08 applies here: confidence intervals not required in validation reports |
| Risk and impact analyses | Deliverable G §G.3 (AI Impact Assessment) | ✅ Covered |

### Field 7: Model Maintenance

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| Monitoring mechanisms (logs, classifiers, drift detection) | Deliverable E (MON-01 through MON-24: full monitoring signal catalog); Part XIV §14.1 (logging) | ✅ Covered |
| Update mechanisms (retraining procedures) | Part XIII §13.1 (change management: retraining triggers and procedures) | ✅ Covered |
| Change log | Part V §5.3 (MDL-07: model versioning — change log required) | ✅ Covered |
| **Post-deployment reports** | Not required as a separate model card section — EAGCF's post-deployment monitoring generates KRI reports but these are not linked back to the model card | ⚠️ Partial — N-AIDOC-03 below |
| **Incident reports and resolutions** (field 7.5) | Part VII §7.4 (corrective action: incident documentation); Part XVI §16.4 (external incident reporting) | ⚠️ Partial — incidents documented separately; not linked to/referenced in model card |

### Field 8: Governance

| AI Doc Outline Field | EAGCF Coverage | Status |
|---|---|---|
| **Framework adherence/compliance** (e.g., G7 Hiroshima Code of Conduct, ISO 42001) + governance report links | Part V §5.3 (MDL-05: model card — governance framework references); Part IV §4.2 (normative references: ISO 42001 certification) | ⚠️ Partial — framework references present; structured compliance disclosure field and governance report link not explicitly required in model card |
| **Interpretability description** (efforts to ensure interpretable outputs) | Part XVI §16.8 (MDL-05 extension: explainability method, audience, fidelity, regulatory compliance — 4-field specification) | ✅ Covered — EAGCF's MDL-05 extension directly implements Field 8.2 |
| **Documentation practices and terminology** (SOPs, normative background) | Part VI §6.6 (annual review cadence); Part II §2.2 (definitions) | ⚠️ Partial — documentation governance present; formal documentation SOPs not required |

---

## 4. Documentation Quality Principles vs. EAGCF

The AI Documentation outline specifies 8 desired qualities for documentation artifacts.

| Quality Principle | EAGCF Implementation | Status |
|---|---|---|
| **Comprehensibility** — clear, accessible, plain language | Part V §5.3 (MDL-05: model card — audience-specific fields); Part XVI §16.8 (audience field required) | ✅ Covered |
| **Informativeness** — extensive and detailed; includes contact/redress | Part V §5.3 (MDL-05: comprehensive required fields); Part XVI §16.2.2 (feedback channel as redress mechanism) | ✅ Covered |
| **Correctness** — factual, precise, evidence-based | Part XII §12.2 (control validation: evidence-based documentation requirement) | ✅ Covered |
| **Judiciousness** — include only publicly appropriate information | Part IV §4.3 (transparency and disclosure: balance between transparency and IP/security protection); Part V §5.11 (MSC-03: model weight protection — IP sensitivity applies) | ✅ Covered |
| **Freshness** — up to date; version management | Part V §5.3 (MDL-07: model versioning); Part VI §6.6 (annual review: documentation currency check) | ✅ Covered |
| **Interoperability** — machine-readable + human-readable; indexed metadata | Part XVI §16.7.1 (MSC-09 AI-SBOM: machine-readable format specified); Part V §5.3 (MDL-05: structured fields enable machine processing) | ⚠️ Partial — SBOM is machine-readable; MDL-05 model card format not required to be machine-readable |
| **Findability and availability** — easy to locate; minimal access barriers | Part V §5.9 (VND domain: vendor documentation access requirements); Part IV §4.3 (transparency: documentation accessible to stakeholders) | ⚠️ Partial — documentation accessibility requirements present; formal findability standard not specified |
| **Maintainability** — easy to update; modular; lifecycle-spanning | Part V §5.3 (MDL-07: versioning enables updates); Deliverable D (lifecycle gate: documentation updated at each stage) | ✅ Covered |

---

## 5. Governance Process Requirements vs. EAGCF

| AI Doc Outline Process Requirement | EAGCF Coverage | Status |
|---|---|---|
| **Organizational leadership support**: resources, budget, KPIs for documentation | Part VI §6.2 (governance office: budget and headcount for governance functions including documentation); Part VI §6.6 (annual review: documentation currency assessed) | ✅ Covered |
| **Defined documentation objectives** | Part V §5.3 (MDL-05: required fields define documentation objectives) | ✅ Covered |
| **Continuous lifecycle documentation** (begin at design, not at release) | Deliverable D (11-stage lifecycle: documentation requirements at each stage gate) | ✅ Covered |
| **Distributed responsibility** (SME technical accounts + documentarian oversight) | Part VI §6.4 (RACI: model owner provides technical content; governance office oversees documentation quality) | ✅ Covered |
| **Audience input incorporated** | Part XVI §16.2.2 (external stakeholder feedback at pre-deployment gate) | ✅ Covered |
| **Framework compliance disclosure** (field 8.1) | Part V §5.3 (MDL-05: governance framework section); not a fully structured disclosure field | ⚠️ Partial — see N-AIDOC-04 below |
| **Incident reporting integration** (field 7.5) | Part VII §7.4 (incident documentation separate from model card) | ⚠️ Partial — see N-AIDOC-03 |
| **Machine-readable format** for both dataset and model documentation | Part XVI §16.7.1 (SBOM machine-readable); model card format not machine-readable by requirement | ⚠️ Partial — see N-AIDOC-05 |

---

## 6. Scoring Summary

| Area | Items | ✅ Covered | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|
| Dataset template (Fields 1–6) | 18 | 13 | 5 | 0 |
| Model template (Fields 1–8) | 22 | 15 | 7 | 0 |
| Documentation quality principles | 8 | 6 | 2 | 0 |
| Governance process requirements | 7 | 5 | 2 | 0 |
| **TOTALS** | **55 items** | **39 (71%)** | **16 (29%)** | **0 (0%)** |

**Coverage interpretation:** 100% of items at least partially covered; 71% fully addressed. The 29% partial rate reflects that this pre-standard document proposes more rigorous documentation structure than EAGCF currently requires — particularly around: chain-of-custody for training data, machine-readable model card format, governance compliance disclosure as a structured field, incident linkage to model card, and post-deployment report linkage. These are documentation depth enhancements, not control gaps.

---

## 7. Gap Items: Recommended EAGCF Additions

| Gap ID | Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N-AIDOC-01** | Outline Field 4.6 | **Training data chain-of-custody**: Extend DAT-01 (data provenance) to require a brief chain-of-custody statement for training data — identifying each major transformation step from source data to final training set, including any consent transfer, anonymization, or synthetic augmentation steps | Low | Part V §5.2 (DAT-01: data provenance — add chain-of-custody sub-field) |
| **N-AIDOC-02** | Outline Field 5.2 | **Training protocol documentation**: For Tier 1 systems, require a training protocol summary in the model card (MDL-05) — including: training framework, hyperparameters, number of training runs, hardware, and retraining schedule. This enables reproducibility and supports model lineage tracing | Low | Part V §5.3 (MDL-05: model card — add training protocol summary as a required Tier 1 field) |
| **N-AIDOC-03** | Outline Field 7.5 | **Incident linkage in model card**: Add a model card field (MDL-05) pointing to the AI incident register for the specific system — enabling external parties to identify known incidents and resolutions without requiring access to the full incident governance system | Low | Part V §5.3 (MDL-05: model card — add "incident register reference" field; may be internal URL or summary of public incidents) |
| **N-AIDOC-04** | Outline Field 8.1 | **Structured governance framework compliance field**: Add a structured governance compliance disclosure field to MDL-05 — listing each governance framework the system claims conformance with and providing a reference link to the relevant conformance evidence or certification. At minimum: ISO 42001 certification status; NIST AI RMF self-assessment checklist reference | Low | Part V §5.3 (MDL-05: model card — add structured governance compliance section; link to Deliverable G §G.14 self-assessment checklist) |
| **N-AIDOC-05** | Outline Clause 5.2 | **Machine-readable model card format**: When NIST/ISO finalize a machine-readable model documentation schema, add a requirement that EAGCF's MDL-05 model card be available in both human-readable and machine-readable formats. Track INCITS/AI and ISO/IEC JTC 1/SC 42 progress on this standard | Low (pending standard) | Part XVI §16.1 (standards watch register: add AI Documentation Standard as pending normative reference); Part V §5.3 (MDL-05) — update when standard finalized |

---

## 8. Most Significant Future EAGCF Impact

When this pre-standard becomes a finalized ISO/IEC standard (projected 2027–2028), EAGCF's MDL-05 model card requirement will need to be updated to align with the international template. The most material changes:

1. **Dataset documentation template**: EAGCF's DAT domain will need to reference the ISO template structure for dataset documentation artifacts delivered as part of vendor due diligence (VND-03/VND-06)
2. **Model card interoperability**: MDL-05 will need to produce a machine-readable artifact conforming to the ISO schema to enable automated procurement validation and regulatory submission
3. **Governance compliance field (8.1)**: ISO 42001 certification status + NIST AI RMF self-assessment reference in every model card becomes the de facto procurement standard for AI systems

These changes are anticipated by N-AIDOC-04 and N-AIDOC-05 above.

---

## 9. Synthesis

The NIST Extended Outline for AI Dataset and Model Documentation is the best available preview of where international AI documentation standards are heading. EAGCF's coverage is strong (100% at least partial) because its existing documentation architecture (MDL-05 model card, MSC-09 AI-SBOM, DAT domain, Deliverable G templates) was designed with the same underlying objectives — comparability, accountability, and auditability.

The 5 low-priority gap items (N-AIDOC-01 through N-AIDOC-05) are primarily documentation depth enhancements that will become more pressing once the ISO/IEC standard is finalized. The most actionable near-term addition is N-AIDOC-04 (structured governance compliance field in MDL-05), which requires no external standard to finalize and directly improves EAGCF's audit defensibility.

**Governance relevance rating:** Medium-High — this is a pre-standard that will become a material normative reference within 3–5 years. Early EAGCF alignment positions adopting enterprises for straightforward transition when the standard is finalized. EAGCF's documentation architecture already satisfies ~71% of the proposed requirements directly.

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Comparisons completed (26 sources): NIST AI 100-1, 100-2, 100-3, 100-4, 100-5/100-5e2025, 600-1, 700-1, 700-2 + ARIA Companion, 800-1, 800-2, IR 8312, IR 8596, GCR 26-069, SP 800-218A, SP 1270; ISO crosswalks (42001/23894, 42005, 5338/5339); OECD/EU AI Act crosswalk; Google DeepMind Gap Analysis; AI Verify crosswalks; Americas AI Action Plan; NIST CSF 2.0; AI Documentation Extended Outline*
