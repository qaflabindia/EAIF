import nbformat as nbf
import os

base_path = "/Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks"

def update_nb(fname, cells):
    path = os.path.join(base_path, fname)
    if not os.path.exists(path):
        # Create a new empty notebook if if doesn't exist
        nb = nbf.v4.new_notebook()
        with open(path, 'w') as f:
            nbf.write(nb, f)
            
    with open(path, 'r') as f:
        nb = nbf.read(f, as_version=4)
    nb['cells'] = cells
    with open(path, 'w') as f:
        nbf.write(nb, f)
    print(f"Updated {path}")

# --- MODULE 12: INDEPENDENT VALIDATION ---
m12_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\nimport importlib\nimportlib.reload(aigrc_utils)\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 12: Independent Model Validation (MV) - Challenger Performance"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('VAL-01', 'Independent Validation Report (§6.4)')"),
    nbf.v4.new_markdown_cell("""
## 1. Primary vs. Challenger Consistency Matrix
**Part VI §6.4** mandates that high-risk models undergo independent validation. This matrix compares the **Primary Model** results against a **Challenger Model** (Validation Function). 

Outliers in red indicate significant logical deviations where the Challenger disagrees with the Primary decision engine.
"""),
    nbf.v4.new_code_cell("""
val_df = aigrc_utils.generate_validation_drift_data()
aigrc_utils.display_validation_consistency_scatter(val_df)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Validation Status Distribution
High variance cases are automatically flagged for manual review by the Model Risk Committee (MRC).
"""),
    nbf.v4.new_code_cell("""
display(val_df['status'].value_counts())
""")
]

# --- MODULE 13: RED-TEAMING (MITRE ATLAS) ---
m13_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\nimport importlib\nimportlib.reload(aigrc_utils)\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 13: Adversarial Red-Teaming - MITRE ATLAS Integration"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('MSC-04', 'MITRE ATLAS Vulnerability Matrix (§16.9)')"),
    nbf.v4.new_markdown_cell("""
## 1. MITRE ATLAS Tactic Heatmap (Strategic Drill-Down)
Following **Part XII §12.4**, we map adversarial robustness across the standard MITRE ATLAS tactics. This interactive sunburst allows the Model Risk Committee to drill down from **Attacker Archetype** (e.g., Professional) to specific **Tactics** to identify high-risk success vectors.
"""),
    nbf.v4.new_code_cell("""
attacker_df = aigrc_utils.generate_attacker_capability_data()
aigrc_utils.display_attacker_tactic_sunburst(attacker_df)
"""),
    nbf.v4.new_markdown_cell("""
## 2. 3D Adversarial Robustness Surface
Technical resilience depth is measured by the model's ability to maintain accuracy under increasing adversarial perturbation (ε). This surface plot visualizes the boundary between model utility and **Adversarial Collapse** across different hardening versions.
"""),
    nbf.v4.new_code_cell("""
surface_df = aigrc_utils.generate_adversarial_surface_data()
aigrc_utils.display_adversarial_surface_3d(surface_df)
"""),
    nbf.v4.new_markdown_cell("""
## 3. Risk Attrition: Controls vs. Attacker ROI
Volumetric proof of how specific defensive hardening layers (e.g., Adversarial Training, Rate Limiting) reduced the raw attack surface.
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_remediation_waterfall(None) # Static data inside function for demo
"""),
    nbf.v4.new_markdown_cell("""
## 4. Vulnerability Remediation Velocity (§16.5)
Continuous red-teaming requires rigorous remediation tracking. This dashboard ensures **MTTR (Mean Time to Remediation)** remains within governance SLAs.
"""),
    nbf.v4.new_code_cell("""
aging_df = aigrc_utils.generate_redteam_findings_history()
aigrc_utils.display_redteam_vulnerability_aging(aging_df)
""")
]

# --- MODULE 14: INCIDENT RESPONSE ---
m14_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\nimport importlib\nimportlib.reload(aigrc_utils)\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 14: Incident Response & Emergency Stop Velocity"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('IRT-01', 'Incident Triage & Resolution Velocity (Part VII)')"),
    nbf.v4.new_markdown_cell("""
## 1. IR Velocity Dashboard (MTTD vs MTTR)
Reliable Incident Response (**Part VII §7.2**) relies on minimizing the gap between **Detection** and **Resolution**. This longitudinal dashboard tracks our velocity in handling S1 (Critical) and S2 (High) AI incidents.
"""),
    nbf.v4.new_code_cell("""
ir_df = aigrc_utils.generate_incident_timeline_data()
aigrc_utils.display_ir_velocity_dashboard(ir_df)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Incident Root-Cause Analysis (RCA) Lineage
High-depth traceability from the technical **Root Cause** (e.g., Prompt Injection) through the **Symptom** (e.g., Privacy Leak) to the **Business Impact** (e.g., Regulatory Fine).
"""),
    nbf.v4.new_code_cell("""
sankey_data = aigrc_utils.generate_incident_lineage_data()
aigrc_utils.display_incident_sankey(sankey_data)
"""),
    nbf.v4.new_markdown_cell("""
## 3. 3D Incident Landscape: Resolution vs. Severity Portfolio
Executive view mapping incident severity across two critical dimensions (S1 vs S2) against the resolution speed (MTTR). This cube identifies clusters of **Operational Fragility**.
"""),
    nbf.v4.new_code_cell("""
# ir_df generated in previous cell already contains Severity_S1, Severity_S2, and MTTR (Min)
aigrc_utils.display_3d_incident_cube(ir_df)
"""),
    nbf.v4.new_markdown_cell("""
## 4. Blast Radius Simulation: Kill-Switch Efficacy (§10.4)
Modeling the propagation of an AI toxicity or hallucination outbreak vs. the effectiveness of **Kill-Switch Protocols**. The dashed line indicates the moment of protocol engagement.
"""),
    nbf.v4.new_code_cell("""
blast_df = aigrc_utils.generate_blast_radius_simulation()
aigrc_utils.display_blast_radius_waterfall(blast_df)
""")
]

# --- MODULE 15: AI FAIRNESS (EXPERT LAB) ---
m15_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\nimport importlib\nimportlib.reload(aigrc_utils)\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 15: AI Fairness & Bias Labs (Expert-Level)"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('FAIR-01', 'Algorithmic Fairness Audit & Mitigation')"),
    nbf.v4.new_markdown_cell("""
## 1. Exhaustive Parity Audit: Baseline (German Credit)
Deep-dive disaggregated analysis using the full Fairlearn metric registry. We audit group-specific Selection Rates, FPR/FNR disparities, and misclassification errors to identify systemic bias before any intervention.
"""),
    nbf.v4.new_code_cell("""
# Exhaustive Group-Level Metrics
full_parity_df = aigrc_utils.generate_exhaustive_fairness_metrics()
# Visualizing the disparity profile
aigrc_utils.display_fairness_bias_data(full_parity_df)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Fairness Mitigation Lifecycle: Comparative Audit
Comparative evaluation of model performance across the full mitigation lifecycle:
1. **Baseline**: Unmitigated model.
2. **Pre-processing**: `CorrelationRemover` (Removing biased signals).
3. **In-processing**: `ExponentiatedGradient` (Enforcing Parity Constraints).
4. **Post-processing**: `ThresholdOptimizer` (Calibrating across groups).
"""),
    nbf.v4.new_code_cell("""
lifecycle_registry = aigrc_utils.generate_mitigation_lifecycle_registry()

# Diagnostic 1: Exhaustive Parity Radar
aigrc_utils.display_exhaustive_parity_radar(lifecycle_registry)
"""),
    nbf.v4.new_markdown_cell("""
## 3. The "Fairness Tax": Accuracy vs. Parity Balance
Executive dashboard identifying the Pareto optimal model. This visualization highlights the trade-off (Accuracy cost) associated with moving towards perfect social parity.
"""),
    nbf.v4.new_code_cell("""
# Lifecycle Dashboard: Accuracy vs Fairness Gain
aigrc_utils.display_fairness_lifecycle_comparison(lifecycle_registry)
""")
]

# --- MODULE 16: EXPLAINABLE AI (XAI) ---
m16_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\nimport importlib\nimportlib.reload(aigrc_utils)\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 16: Explainable AI & RAG Transparency"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('XAI-01', 'Reasoning Traceability & Hallucination Audit')"),
    nbf.v4.new_markdown_cell("""
## 1. Diagnostic Case Study: Safety-Protocol Hallucination
**Scenario**: Auditor query on "Kill-Switch Protocols for Tier 3 Anomalies".
**Target Outcome**: Ground-truth requires a 15-min intervention.
**Detection**: RAGAS identifies a "Hallucination by Omission" where the model retrieved the notification duty but ignored the intervention deadline.
"""),
    nbf.v4.new_code_cell("""
# Exhaustive 9-Metric RAGAS Audit
ragas_full_suite = aigrc_utils.generate_ragas_metrics()
aigrc_utils.display_ragas_spider_chart(ragas_full_suite)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Claim-to-Evidence Grounding Audit
Granular breakdown of generated claims vs. retrieved evidence. The **Faithfulness Score** of 0.05 for the 'Kill-switch' claim successfully flags a safety violation.
"""),
    nbf.v4.new_code_cell("""
audit_trace = aigrc_utils.generate_rag_failure_trace()
aigrc_utils.display_claim_grounding_audit(audit_trace)
"""),
    nbf.v4.new_markdown_cell("""
## 3. Retrieval Reasoning path (Knowledge Graph)
Visualizing the semantic disconnect between high-level risk concepts and specific operational mandates.
"""),
    nbf.v4.new_code_cell("""
graph_data = aigrc_utils.generate_retrieval_graph_data()
aigrc_utils.display_rag_knowledge_graph(graph_data)
""")
]

update_nb("module_12_validation.ipynb", m12_cells)
update_nb("module_13_red_teaming.ipynb", m13_cells)
update_nb("module_14_incident_response.ipynb", m14_cells)
update_nb("module_15_fairness.ipynb", m15_cells)
update_nb("module_16_xai.ipynb", m16_cells)
