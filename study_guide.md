# Study Guide: Enterprise AI Governance, Risk & Control

This guide summarizes the core pillars of AI GRC through the lens of the **Enterprise AI Governance and Control Framework (EAGCF)**.

## Phase 1: Foundations & Strategy

### Chapter 0: The Hook & Risk Exposure
- **Theoretical Pillar**: AI failure is an "unpriced liability"—a business decision that looks like a bug (Part I).
- **Practical Implementation**: `RiskExposureStatement` Pydantic schema and liability quantification.
- **Workbook**: [Module 0](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_00_hook.ipynb)

### Chapter 1: Governance as Permission to Scale
- **Theoretical Pillar**: Speed is achieved through standardized "Paved Roads" and fast-lane approvals (Part VIII).
- **Practical Implementation**: Policy-as-Code intake gate (`compliance_gate`).
- **Workbook**: [Module 1](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_01_governance_speed.ipynb)

### Chapter 2: Accountability Without Ownership
- **Theoretical Pillar**: Named owners for Business, Model, and System are mandatory (Part VI).
- **Practical Implementation**: RACI Matrix generation and MLflow artifact tagging.
- **Workbook**: [Module 2](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_02_accountability.ipynb)

### Chapter 3: AI Risk vs Software Risk
- **Theoretical Pillar**: Deterministic failures vs. Probabilistic "plausible" failures (Part III).
- **Practical Implementation**: Model drift simulation and risk threshold visualization.
- **Workbook**: [Module 3](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_03_ai_risk_v_software.ipynb)

### Chapter 4: Enterprise AI Risk Taxonomy
- **Theoretical Pillar**: The 15 Control Domains (Part V).
- **Practical Implementation**: Risk concentration analysis and Master Incident Register.
- **Workbook**: [Module 4](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_04_risk_taxonomy.ipynb)

## Phase 2: Technical Controls & Dual-Use Safety

### Chapter 5: The "Paved Road" to Production
- **Theoretical Pillar**: Proportionate scrutiny gates based on risk tiers (Part VIII).
- **Practical Implementation**: Risk-proportionate gate routing (`determine_gate_path`).
- **Workbook**: [Module 5](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_05_paved_road.ipynb)

### Chapter 6: Data Sovereignty & Lineage
- **Theoretical Pillar**: Training Data Chain-of-Custody (DAT-04, Part XVII).
- **Practical Implementation**: AI-SBOM provenance record and PII ingestion scanning.
- **Workbook**: [Module 6](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_06_data_lineage.ipynb)

### Chapter 7: Securing Dual-Use Weights
- **Theoretical Pillar**: Protecting weights against theft and CBRN misuse (Part XV).
- **Practical Implementation**: SHA-256 integrity signatures and identity-based access simulation.
- **Workbook**: [Module 7](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_07_weight_security.ipynb)

### Chapter 8: Prompt Engineering Discipline
- **Theoretical Pillar**: System Prompt versioning and defense-in-depth (PRM-01).
- **Practical Implementation**: Prompt versions registry and injection sanitation logic.
- **Workbook**: [Module 8](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_08_prompt_ops.ipynb)

### Chapter 9: RAG Integrity
- **Theoretical Pillar**: Corpus poisoning and chunk-level traceability (Part XVII).
- **Practical Implementation**: RAGAS Faithfulness verification and citation tracking.
- **Workbook**: [Module 9](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_09_rag_integrity.ipynb)

### Chapter 10: Agentic Kill-Switches
- **Theoretical Pillar**: Autonomy limits and reversible action gates (Domain 10).
- **Practical Implementation**: Agentic HITL trigger and Kill-Switch handler.
- **Workbook**: [Module 10](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_10_agentic_killswitch.ipynb)

## Phase 3: Validation & Response

### Chapter 11: Machine-Readable Accountability
- **Theoretical Pillar**: Model and System Cards as primary disclosure artifacts (Deliverable C).
- **Practical Implementation**: Automated System Card generation from metadata.
- **Workbook**: [Module 11](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_11_documentation.ipynb)

### Chapter 12: Independent Validation
- **Theoretical Pillar**: MV function and Challenger Model protocols (Part VI).
- **Practical Implementation**: Cross-model consistency auditing.
- **Workbook**: [Module 12](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_12_validation.ipynb)

### Chapter 13: Red-Teaming (MITRE ATLAS)
- **Theoretical Pillar**: Attack Library and adversarial resilience (Part XII).
- **Practical Implementation**: Evasion attack simulation targeting classifiers.
- **Workbook**: [Module 13](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_13_red_teaming.ipynb)

### Chapter 14: Incident Response
- **Theoretical Pillar**: S1-S4 Severity models and response SLAs (Part VII).
- **Practical Implementation**: Incident triage bot and Rollback/Safe-Mode command.
- **Workbook**: [Module 14](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_14_incident_response.ipynb)

### Chapter 15: AI Fairness
- **Theoretical Pillar**: Impossibility constraints and FAI domain (Part XVII).
- **Practical Implementation**: Disparate Impact calculation (80% Rule).
- **Workbook**: [Module 15](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_15_fairness.ipynb)

## Phase 4: Strategy & Alignment

### Chapter 16: XAI Architecture
- **Theoretical Pillar**: Gist (Interpretability) vs Mechanism (Explainability) (Part XVII).
- **Practical Implementation**: Audience-differentiated explanation generation.
- **Workbook**: [Module 16](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_16_xai_architecture.ipynb)

### Chapter 17: Supply Chain & Vendor Risk
- **Theoretical Pillar**: Trusted vendors and AI-SBOM validation (Part XVI).
- **Practical Implementation**: Vendor SBOM audit and safety filter check.
- **Workbook**: [Module 17](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_17_supply_chain.ipynb)

### Chapter 18: Regulatory Convergence
- **Theoretical Pillar**: NIST AI RMF to EU AI Act mapping (Part IV).
- **Practical Implementation**: EU AI Act Annex III High-Risk categorizer.
- **Workbook**: [Module 18](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_18_regulatory_mapping.ipynb)

### Chapter 19: The Board Report
- **Theoretical Pillar**: Board reporting cadences and Residual Risk pricing (Part VI).
- **Practical Implementation**: Executive AI Governance Scorecard generation.
- **Workbook**: [Module 19](file:///Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks/module_19_board_report.ipynb)
