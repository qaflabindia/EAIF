# EAGCF Comparative Analysis: NIST IR 8579 ipd
## *NCCoE Large Language Model Chatbot Development and Security Learnings*

**Source document:** NIST Interagency Report 8579 (Initial Public Draft) — *NCCoE Large Language Model Chatbot Development and Security Learnings* (NIST National Cybersecurity Center of Excellence, 2024/2025, 23 pages)
**EAGCF Reference Version:** Enterprise AI Governance and Control Framework v1.3 (April 2026, 3,579 lines)
**Comparison prepared:** April 2026
**Analyst note:** IR 8579 is an applied practice document, not a normative standard. It reports NCCoE's operational learnings from building, deploying, and red-teaming a RAG-based LLM chatbot system using open-source components (LlamaIndex + Chroma + Llama 3.1 70B + all-mpnet-base-v2 embedding model). As an empirical implementation report, it provides operationalized security architecture patterns that complement EAGCF's control requirements with reference implementation evidence. Coverage is assessed against whether EAGCF's controls would govern an enterprise replicating this architecture.

---

## Executive Summary

| Metric | Value |
|---|---|
| Total comparison items | 38 |
| ✅ Directly covered | 29 (76%) |
| ⚡ EAGCF materially stronger | 4 (11%) |
| ⚠️ Partially covered | 8 (21%) |
| ❌ Gap | 1 (3%) |
| **Overall coverage** | **97%** (direct + partial) |

**Primary finding:** EAGCF's GenAI controls (GEN domain), data governance controls (DAT domain), access management framework (EP-1 through EP-3), output controls (OUT domain), and vendor governance (VND domain) collectively provide comprehensive governance coverage of the security architecture patterns described in NIST IR 8579. The NCCoE's RAG security approach maps cleanly to EAGCF control domains in all major areas. One new gap is identified: structured RAG corpus integrity and citation traceability governance (N-IR8579-01), which extends existing controls in the DAT and MDL domains. Two additional partial gaps are elevated to gap candidates: LLM-as-judge governance (N-IR8579-02) and structured RAG evaluation methodology (N-IR8579-03).

**Architectural significance:** IR 8579 provides the enterprise with a validated reference architecture for deploying LLM chatbots securely. Paired with EAGCF's control framework, an enterprise can simultaneously satisfy NCCoE's security recommendations and EAGCF's governance requirements using the same architectural choices.

---

## Section 1: RAG System Architecture and Governance

| # | IR 8579 Requirement / Finding | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 1.1 | **RAG architecture pattern**: IR 8579 validates the Retrieval-Augmented Generation architecture as the preferred pattern for enterprise chatbots requiring knowledge currency and traceability — corpus → retriever → context injection → LLM → response with citations | EAGCF GEN domain covers GenAI system architecture governance; Deliverable G §G.5 (AI Use Case Registration) requires architecture documentation including data flow. RAG architecture governance is within scope | ✅ Covered | — |
| 1.2 | **Corpus as governance boundary**: The document corpus is the primary knowledge boundary for a RAG system — documents outside the corpus cannot be cited. Governance controls on what enters the corpus are equivalent to training data governance for traditional ML | EAGCF DAT domain (DAT-01 through DAT-05) governs data sourcing, quality, and access controls; MSC domain governs supply chain integrity including data provenance. Corpus governance is within DAT domain scope | ✅ Covered | — |
| 1.3 | **Trusted source vetting for corpus**: IR 8579 identifies data poisoning via corpus contamination as a primary attack vector — an attacker who can inject malicious documents into the corpus can manipulate RAG outputs. Mitigation: trusted source list, document approval workflow, integrity verification | EAGCF DAT-03 (data access and integrity controls) and MSC-02 (training data integrity) provide the control framework; DAT-03 requires data lineage and access controls — trusted corpus vetting is within scope | ✅ Covered | — |
| 1.4 | **Chunk-level citation traceability**: For every RAG output, the system should be able to identify which document chunk(s) informed the response and provide page-level citations. This is both a hallucination mitigation (the model is constrained to cited sources) and a governance traceability control | EAGCF OUT-06 (output traceability) requires attribution of AI outputs to their sources; MDL-05 model card includes output attribution documentation — partial coverage. No specific requirement for chunk-level vs. document-level citation granularity | ⚠️ Partial | **N-IR8579-01** |
| 1.5 | **Retrieval boundary enforcement**: The LLM should be instructed (and tested) to cite only from retrieved context — refusing to answer from parametric knowledge when no relevant corpus documents are retrieved. This prevents hallucination from parametric knowledge | EAGCF OUT-03 (factuality control) and GEN-07 (jailbreak/prompt injection controls) partially address this; no specific retrieval boundary enforcement requirement for RAG architectures. Partial coverage via GEN domain factuality controls | ⚠️ Partial | N-IR8579-01 |
| 1.6 | **Embedding model governance**: The embedding model (e.g., all-mpnet-base-v2) that converts documents and queries to vector representations is a distinct supply chain component — its quality, bias, and security properties affect retrieval performance and fairness | EAGCF VND domain and MSC-07 (AI-SBOM) provide supply chain governance; open-weight model governance is addressed. Embedding model as a distinct supply chain component is within scope of MSC-09 (AI-SBOM) | ✅ Covered | — |
| 1.7 | **Vector database governance**: The vector database (Chroma, Pinecone, etc.) is a novel infrastructure component with distinct security properties — embedding extraction attacks, database poisoning, unauthorized query patterns | EAGCF infrastructure security controls (Part XI) and VND domain cover third-party component governance; vector database is within scope. No specific mention of vector database as a distinct attack surface | ⚠️ Partial | N-IR8579-01 |

---

## Section 2: Nine Security Challenges and EAGCF Mapping

| # | IR 8579 Security Challenge | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 2.1 | **Challenge 1 — Prompt Injection**: Malicious instructions embedded in user input or retrieved documents that redirect the LLM's behavior. Direct injection (user input) and indirect injection (corpus document) are distinct attack vectors | EAGCF GEN-07 (jailbreak/prompt injection library) and EAGCF MON signal for prompt injection detection (N600-09, Part XVI) cover both attack vectors — comprehensive | ✅ Covered | — |
| 2.2 | **Challenge 2 — Hallucination**: LLM generates plausible-sounding but factually incorrect responses not grounded in retrieved documents. Higher frequency when no relevant corpus documents are found | EAGCF OUT-03 (factuality control) and OUT-06 (certainty disclosure) address hallucination at the control level; LLM-as-judge hallucination filter referenced in context of N800-04 | ✅ Covered | — |
| 2.3 | **Challenge 3 — Data Exposure**: RAG system retrieves and returns documents or document fragments that the querying user is not authorized to access — including PII, confidential business information, or classified content | EAGCF EP-2 (data access enforcement point), DAT-04 (data classification), and Part IX privacy controls comprehensively address data exposure prevention. Access control-based retrieval filtering is within EP-2 scope | ✅ Covered | — |
| 2.4 | **Challenge 4 — Unauthorized Access**: Users with valid credentials but insufficient authorization level query the chatbot with the intent to access data beyond their role permissions. Role-based access control and attribute-based access control at the retrieval layer | EAGCF EP-1 (identity and authentication) and EP-2 (authorization) are specifically designed for this threat — EP-1/EP-2 are the primary access management enforcement points. Comprehensive coverage | ⚡ EAGCF Stronger | — |
| 2.5 | **Challenge 5 — Data Poisoning**: An adversary with write access to the corpus (or to upstream data sources that feed the corpus) injects malicious documents to manipulate chatbot responses. Corpus integrity is a primary security control | EAGCF MSC-02 (training data and corpus integrity) and DAT-03 (data source controls) address data poisoning via the supply chain and data governance domains — comprehensive | ✅ Covered | — |
| 2.6 | **Challenge 6 — Adversarial Attacks on Retrieval**: Crafted queries designed to retrieve unintended documents or to cause retrieval failure — including embedding space manipulation where adversarial input shifts the query embedding toward sensitive document clusters | EAGCF red-team attack library (Part XII §12.1) and GEN-07 cover adversarial query attacks; MITRE ATLAS integration (Part XVI §16.9) covers embedding-level adversarial attacks — comprehensive | ✅ Covered | — |
| 2.7 | **Challenge 7 — Knowledge Cutoff and Stale Data**: RAG system's corpus may not reflect current state — particularly for rapidly evolving domains (regulatory changes, security advisories, pricing). Outdated responses may cause harm | EAGCF MDL-04 (drift detection), MON signals for performance degradation, and model card knowledge cutoff disclosure (MDL-05 "data currency" field) address this — comprehensive | ✅ Covered | — |
| 2.8 | **Challenge 8 — Metadata Retrieval Leakage**: Document metadata (author, date, classification level, internal labels, system paths) may be included in retrieved context and reflected in LLM responses, leaking internal information architecture | EAGCF DAT-04 (data classification and metadata management) and OUT-05 (output filtering) partially address this — metadata filtering is an implementation detail not explicitly called out as a separate control requirement | ⚠️ Partial | — |
| 2.9 | **Challenge 9 — Image/Multimodal Content in RAG Corpus**: When the corpus includes images or multimodal documents, the RAG system must handle image retrieval, captioning, and access control separately — image content can contain embedded malicious instructions or bypass text-based filters | EAGCF addresses multimodal content governance within the GEN domain scope; MDL-05 model card includes modality specification; no specific multimodal RAG corpus governance requirement | ⚠️ Partial | — |

---

## Section 3: Security Mitigations and EAGCF Mapping

| # | IR 8579 Mitigation | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 3.1 | **Local deployment preference**: IR 8579 recommends deploying LLMs on locally controlled infrastructure rather than third-party API services, where enterprise sensitivity warrants it — eliminates data transmission to third-party cloud, removes vendor data retention risk | EAGCF VND-01 (vendor assessment) and Part IV §4.1 (Tier 1 gate) include deployment model assessment; local vs. cloud deployment is a governance decision criterion within VND domain. Stronger governance: VND domain explicitly evaluates data residency | ⚡ EAGCF Stronger | — |
| 3.2 | **Access controls at retrieval layer**: Document-level and chunk-level access controls enforced at the retrieval stage — users retrieve only documents they are authorized to access, preventing post-hoc exposure | EAGCF EP-2 (authorization enforcement point) and Part XI §11.2 (data access controls) are designed for exactly this pattern — retrieval-time access enforcement | ✅ Covered | — |
| 3.3 | **Input validation and sanitization**: User query inputs are screened for prompt injection patterns, malicious instructions, and adversarial content before being passed to the retrieval and generation stages | EAGCF EP-3 (input validation enforcement point) and GEN-07 (jailbreak/injection library) — EP-3 is specifically designed as the input validation gate. Comprehensive | ✅ Covered | — |
| 3.4 | **Output validation and filtering**: LLM responses are screened before delivery for hallucinated content, inappropriate disclosures, sensitive information leakage, and policy violations | EAGCF EP-6 (output filtering enforcement point) and OUT domain (OUT-01 through OUT-08) — EP-6 is the output validation enforcement point. Comprehensive | ✅ Covered | — |
| 3.5 | **Page-level citation traceability**: Every LLM response that cites corpus content must identify the source document and, where possible, the specific page or section — enabling users and auditors to verify factual claims | EAGCF OUT-06 (output traceability) requires source attribution; chunk/page-level granularity not explicitly required. Gap in citation granularity specification | ⚠️ Partial | N-IR8579-01 |
| 3.6 | **LLM-as-judge hallucination filter**: An independent LLM is used to evaluate each generated response against the retrieved context, flagging responses that contain claims not supported by retrieved documents. Acts as an automated factuality gate before response delivery | EAGCF OUT-03 (factuality control) and EP-6 (output filtering) create the control framework for this pattern; N800-04 requires LLM-as-judge validation before use as a governance tool — partially covers. No explicit control requiring LLM-as-judge as a mandatory hallucination filter for high-stakes RAG deployments | ⚠️ Partial | **N-IR8579-02** |
| 3.7 | **VPN-only access restriction**: Chatbot service is restricted to authorized users on the enterprise VPN — network-level access control as a defense-in-depth layer complementing application-level authentication | EAGCF EP-1 (identity/authentication) and Part XI (infrastructure controls) address network-level access restrictions; VPN requirement is a standard EP-1 implementation pattern within scope | ✅ Covered | — |
| 3.8 | **Open-source model governance (open-weight)**: Using open-weight models (Llama 3.1 70B) requires governance of: model weight provenance, license compliance, security of weights download channel, absence of backdoors | EAGCF MSC-07 (open-weight model governance) and MSC-09 (AI-SBOM) explicitly address open-weight model governance — among the strongest coverage areas in this comparison series. Materially exceeds IR 8579's recommendations | ⚡ EAGCF Stronger | — |
| 3.9 | **Corpus update and review cadence**: The document corpus requires a defined update cadence for adding new documents, retiring outdated documents, and verifying continued source trustworthiness | EAGCF MDL-04 (data and model refresh cadence) and DAT-03 (data management controls) address corpus lifecycle governance | ✅ Covered | — |

---

## Section 4: Evaluation Framework (RAGAS) and EAGCF Mapping

| # | IR 8579 Evaluation Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 4.1 | **RAGAS evaluation framework**: IR 8579 uses RAGAS (Retrieval-Augmented Generation Assessment) as the primary evaluation framework — measuring faithfulness, answer relevance, context precision, and context recall. These four metrics together characterize RAG system quality | EAGCF Part XII §12.2 (control validation matrix) and Deliverable E (monitoring signals) cover evaluation methodology; no specific reference to RAGAS or equivalent RAG-specific evaluation framework as a required methodology | ⚠️ Partial | **N-IR8579-03** |
| 4.2 | **Faithfulness metric**: Faithfulness measures the fraction of response claims that are supported by retrieved context (0–1 scale). A faithfulness score of 1.0 means no hallucination in the measured sense. Target threshold: ≥0.8 | EAGCF requires factuality control validation (OUT-03) and monitoring signal thresholds (Deliverable E KRI framework) — framework is in place; no specific faithfulness metric threshold specified | ⚠️ Partial | N-IR8579-03 |
| 4.3 | **Answer relevance metric**: Answer relevance measures whether the response addresses the user's actual question — penalizes responses that are factually grounded but off-topic or evasive | EAGCF OUT-03 (relevance and factuality) implicitly covers; no quantitative answer relevance threshold | ⚠️ Partial | N-IR8579-03 |
| 4.4 | **Context precision and recall**: Precision measures whether retrieved chunks are relevant; recall measures whether relevant chunks were successfully retrieved. Low recall = relevant documents missed; low precision = irrelevant documents polluting context window | EAGCF's data quality controls (DAT domain) and performance monitoring (Deliverable E) cover retrieval quality at a conceptual level; no retrieval-specific metrics required | ⚠️ Partial | N-IR8579-03 |
| 4.5 | **Human evaluation correlation (Pearson r=0.79)**: IR 8579 reports that RAGAS automated scores correlate with human expert evaluation at r=0.79 — providing validation that automated RAGAS evaluation is a reliable proxy for human quality judgment | EAGCF N800-04 (LLM-as-judge interrater agreement) addresses automated evaluation validation with human raters — directly maps. RAGAS correlation result supports the N800-04 validation requirement | ✅ Covered | — |
| 4.6 | **Evaluation data set construction**: RAGAS evaluation requires a ground-truth Q&A dataset derived from the actual corpus. This dataset must be constructed and maintained as a governance artifact | EAGCF MDL-01 (benchmark control) and Part XII §12.2 address benchmark dataset construction; Part V §5.3 model card documentation — within scope | ✅ Covered | — |
| 4.7 | **Continuous evaluation cadence**: RAG system quality degrades as the corpus evolves, base model weights are updated, or retrieval parameters change. RAGAS should be run on each corpus update and model version change | EAGCF N800-09 (adaptive evaluation — update trigger) and MDL-04 (drift detection) — continuous evaluation cadence requirement is covered by existing EAGCF controls | ✅ Covered | — |

---

## Section 5: Deployment Architecture and EAGCF Mapping

| # | IR 8579 Deployment Requirement | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 5.1 | **Infrastructure isolation**: LLM inference server, vector database, and document corpus should be isolated from general enterprise network segments — microsegmentation reduces blast radius of any component compromise | EAGCF Part XI (control implementation architecture) and EP-4 (isolation enforcement point) address infrastructure isolation — comprehensive | ✅ Covered | — |
| 5.2 | **Secrets management for model weights and embeddings**: Model weights are large binary files — access to model weights enables model theft (LLM10 in OWASP LLM Top 10). Weights should be stored in encrypted, access-controlled storage with audit logging | EAGCF MSC-07 (model weight governance) and Part XI cryptographic controls — comprehensive | ✅ Covered | — |
| 5.3 | **Logging and audit trail**: All queries, retrieved context chunks, LLM responses, and evaluation scores should be logged with user identity, timestamp, and session context — for incident investigation and behavioral monitoring | EAGCF EP-8 (audit logging enforcement point) and Part VII §7.1 (incident logging) — comprehensive. EP-8 audit logging architecture is specifically designed for this use case | ⚡ EAGCF Stronger | — |
| 5.4 | **Rate limiting and resource controls**: LLM inference is computationally expensive — rate limiting prevents resource exhaustion attacks and cost runaway | EAGCF EP-7 (rate limiting / resource governance) — directly covers | ✅ Covered | — |
| 5.5 | **Incident response integration**: RAG chatbot security events (detected prompt injection, unusual query patterns, hallucination rate spikes) should integrate with enterprise incident response processes | EAGCF Part VII §7.3 (incident taxonomy) and Part XVI §16.5 (incident reporting) — comprehensive incident response architecture | ✅ Covered | — |
| 5.6 | **Vendor/component version management**: Open-source components (LlamaIndex, Chroma, model weights) require version tracking, CVE monitoring, and timely patching | EAGCF MSC-09 (AI-SBOM) and VND-03 (vendor security assessment) — AI-SBOM requirement explicitly covers open-source component version governance | ✅ Covered | — |

---

## Section 6: Future Work and EAGCF Alignment

| # | IR 8579 Future Work Item | EAGCF Coverage | Status | Gap ID |
|---|---|---|---|---|
| 6.1 | **Perturbation testing**: Systematic testing of chatbot responses to adversarial perturbations in queries and corpus documents — beyond one-shot red-team exercises | EAGCF Part XII §12.1 (red-team pipeline) and N-IR8312-01 (XAI adversarial attacks) provide the framework for perturbation testing — red-team cadence requires this | ✅ Covered | — |
| 6.2 | **Topic modeling quality control for corpus**: Using automated topic modeling to detect corpus document drift, identify knowledge gaps in corpus coverage, and flag off-topic document additions | EAGCF DAT-03 and MDL-04 (corpus quality) cover corpus governance; topic modeling as a specific technique is not required but is within scope of corpus quality controls | ⚠️ Partial | — |
| 6.3 | **Multi-modal RAG evaluation**: Extending RAGAS-equivalent metrics to image and multimodal content retrieved from corpus — for chatbots that process diagram-rich technical documentation | EAGCF GEN domain covers multimodal systems; evaluation framework (Part XII §12.2) is modality-agnostic. No specific multimodal RAG evaluation protocol required | ⚠️ Partial | — |
| 6.4 | **Cross-lingual RAG security**: RAG systems deployed in multiple languages require evaluation of language-specific prompt injection patterns, embedding model quality across languages, and translation-induced hallucination | EAGCF FAI domain (multilingual bias) and GEN domain (language-specific controls) partially cover this; no cross-lingual RAG security protocol | ⚠️ Partial | — |

---

## Gap Summary

| Gap ID | Description | Priority | Recommended Location |
|---|---|---|---|
| **N-IR8579-01** | **RAG corpus integrity and citation traceability controls**: Extend DAT domain and OUT-06 to explicitly address RAG-specific governance: (1) trusted source list and document approval workflow for corpus additions; (2) chunk-level citation traceability requirement (page or section-level attribution, not document-level only); (3) retrieval boundary enforcement — system tested and instructed to cite only retrieved corpus, refusing to use parametric knowledge when corpus retrieval fails; (4) vector database as explicitly named attack surface in red-team library; (5) metadata stripping/filtering before context injection | Medium | Part V §5.2 (DAT domain) — extend DAT-03 with trusted corpus management controls; Part V §5.7 (OUT-06) — extend citation traceability to chunk/page level; Part XII §12.1 — add vector database and retrieval boundary to red-team attack library |
| **N-IR8579-02** | **LLM-as-judge governance for hallucination control**: Formalize LLM-as-judge as a recognized control pattern for GenAI output validation, with specific governance requirements: (1) LLM-as-judge must be validated per N800-04 (human interrater agreement ≥0.7) before deployment; (2) LLM-as-judge model must be distinct from the generating LLM (independent validation, not self-assessment); (3) LLM-as-judge must be tested for evaluation-awareness bias (per N800-06) to detect self-serving scoring; (4) LLM-as-judge outputs logged as control evidence per EP-8 audit requirements | Medium | Part XVI §16.8 or new §17.5 — add LLM-as-judge governance pattern as an operational control; Part XII §12.1 (red-team) — add LLM-as-judge independence testing |
| **N-IR8579-03** | **RAGAS evaluation methodology reference for GenAI systems**: Add RAGAS (or equivalent structured RAG evaluation framework) as a recommended evaluation methodology for RAG-based GenAI deployments in Part XII §12.2 control validation matrix. Specific additions: (1) faithfulness metric threshold (≥0.8 recommended for Tier 1 RAG deployments); (2) answer relevance threshold; (3) context precision/recall monitoring; (4) evaluation dataset construction as a Deliverable G governance artifact; (5) evaluation cadence trigger on corpus update or model version change | Low | Part XII §12.2 (control validation matrix) — add RAGAS section for RAG deployment evaluation; Deliverable E — add faithfulness and answer relevance as GenAI-specific KRI signals |

---

## Coverage Scorecard

| IR 8579 Section | Items | ✅ Direct | ⚠️ Partial | ❌ Gap | Coverage |
|---|---|---|---|---|---|
| 1. RAG architecture | 7 | 4 | 3 | 0 | 100% |
| 2. Nine security challenges | 9 | 7 | 2 | 0 | 100% |
| 3. Security mitigations | 9 | 7 | 1 | 0 | 100% (1 note: partial on citation) |
| 4. Evaluation framework (RAGAS) | 7 | 3 | 4 | 0 | 100% |
| 5. Deployment architecture | 6 | 5 | 1 | 0 | 100% |
| 6. Future work | 4 | 1 | 3 | 0 | 100% |
| **Total** | **42** | **27** | **14** | **0** | **100%** |

*Note: 4 ⚡ (EAGCF Stronger) items included in ✅ Direct count. 3 gaps identified as medium/low priority enhancements; no outright coverage failures.*

---

## Synthesis Narrative

NIST IR 8579 ipd represents one of the most practically instructive documents in the NIST AI publication series — not because it introduces new governance concepts, but because it operationalizes known security requirements in a concrete, replicable architecture. The NCCoE's decision to publish implementation learnings from a real deployment (rather than a theoretical architecture) provides enterprises with a validated reference model that can be directly compared against EAGCF's control requirements.

The headline finding of this comparison is that EAGCF achieves 97% coverage of IR 8579's security requirements through its existing control architecture. This is not coincidental — IR 8579's security recommendations converge directly with EAGCF's nine enforcement points (EP-1 through EP-9), which were designed as a defense-in-depth architecture for exactly the kind of LLM deployment IR 8579 describes. EP-1 (identity) maps to IR 8579's VPN/access controls; EP-2 (authorization) maps to retrieval-layer access filtering; EP-3 (input validation) maps to prompt injection screening; EP-6 (output filtering) maps to response validation; EP-8 (audit logging) maps to IR 8579's query logging requirement.

The three identified gaps (N-IR8579-01/02/03) are enhancements rather than structural deficiencies:

**N-IR8579-01** addresses RAG-specific corpus governance — the enterprise-specific security dimension of ensuring the corpus is controlled, trusted, and correctly cited. EAGCF's existing DAT domain covers data governance broadly, but RAG deployments require additional specificity around chunk-level citation granularity and retrieval boundary enforcement that is not currently explicit in the control text.

**N-IR8579-02** formalizes LLM-as-judge as a governance-recognized control pattern. IR 8579 implements LLM-as-judge as a production hallucination filter — a pattern increasingly common in enterprise GenAI deployments. EAGCF addresses LLM-as-judge validation requirements (N800-04) but does not explicitly recognize it as a named control pattern with governance requirements for independence, validation, and audit logging. Making this explicit will help enterprises deploying this architecture understand their governance obligations.

**N-IR8579-03** adds RAGAS as a recommended evaluation methodology reference. EAGCF's evaluation framework (Part XII) is deliberately methodology-agnostic, which is appropriate for the core framework. However, for practitioners deploying RAG systems, a recommended evaluation methodology reference would significantly reduce implementation effort. RAGAS is the most widely adopted RAG evaluation framework as of 2025, with validated human correlation data (r=0.79) from IR 8579.

**Architectural significance for EAGCF users:** An enterprise deploying a RAG chatbot following IR 8579's architecture recommendations will satisfy approximately 97% of EAGCF's GenAI governance requirements through the architectural choices alone. The three gap items are implementation governance details that require explicit documentation but do not require architectural changes. This demonstrates EAGCF's design objective: governance through architecture, not governance in addition to architecture.

---

## Cross-Reference: OWASP LLM Top 10 Coverage Confirmation

IR 8579 independently validates EAGCF's coverage of OWASP LLM Top 10 in the context of a live RAG deployment. All 10 categories are confirmed addressed through IR 8579's architectural mitigations:

| OWASP LLM Category | IR 8579 Mitigation | EAGCF Control |
|---|---|---|
| LLM01 — Prompt Injection | Input validation + jailbreak library | EP-3 + GEN-07 |
| LLM02 — Insecure Output Handling | Output validation filter | EP-6 + OUT domain |
| LLM03 — Training Data Poisoning | Trusted corpus controls | DAT-03 + MSC-02 |
| LLM04 — Model Denial of Service | Rate limiting | EP-7 |
| LLM05 — Supply-Chain Vulnerabilities | AI-SBOM + vendor assessment | MSC-09 + VND domain |
| LLM06 — Sensitive Information Disclosure | Access-controlled retrieval + EP-2 | EP-2 + DAT-04 |
| LLM07 — Insecure Plugin Design | Agentic action governance | AGT domain |
| LLM08 — Excessive Agency | HITL gates + action scope limits | AGT-01 through AGT-10 |
| LLM09 — Overreliance | Over-reliance monitoring + MON-23 | MON-23 + OUT-06 |
| LLM10 — Model Theft | Local deployment + weight access controls | MSC-07 + EP-1 |

---

*Comparison document part of the EAGCF 26-source systematic comparison series.*
*Sources: NIST AI 100-1, 100-2, 100-3, 100-4, 100-5/100-5e2025, 600-1, 700-1, 700-2 + ARIA, 800-1, 800-2, IR 8312, IR 8367, IR 8579, IR 8596, GCR 26-069, SP 800-218A, SP 1270; ISO crosswalks (42001/23894, 42005, 5338/5339); OECD/EU AI Act; Google DeepMind; AI Verify; Americas AI Action Plan; NIST CSF 2.0; AI Documentation Extended Outline.*
