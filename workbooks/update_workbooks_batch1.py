import nbformat as nbf
import os

base_path = "/Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks"

def update_nb(fname, cells):
    path = os.path.join(base_path, fname)
    if not os.path.exists(path):
        nb = nbf.v4.new_notebook()
        print(f"Creating new notebook: {path}")
    else:
        with open(path, 'r') as f:
            nb = nbf.read(f, as_version=4)
    nb['cells'] = cells
    with open(path, 'w') as f:
        nbf.write(nb, f)
    print(f"Updated {path}")

# --- MODULE 00: THE HOOK ---
m00_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 0: The Hook - The Era of 'Unpriced AI Liability'"),
    nbf.v4.new_code_cell("""
inventory = aigrc_utils.load_inventory('ai_inventory_master.csv')
inventory['liability'] = inventory['business_value'] * (inventory['risk_score'] / 100) * 10000
high_risk = inventory[inventory['risk_tier'].str.contains('High|Tier 1')]
aigrc_utils.display_liability_card(inventory['liability'].sum(), len(high_risk), len(inventory))
aigrc_utils.display_interactive_risk_map(inventory)
"""),
    nbf.v4.new_code_cell("aigrc_utils.display_liability_scatter(inventory)")
]

# --- MODULE 01: GOVERNANCE SPEED ---
m01_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 1: Governance Proportionality and Speed"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('B', 'Enterprise AI Risk-Tiering Model')"),
    nbf.v4.new_code_cell("""
inventory = aigrc_utils.load_inventory('ai_inventory_master.csv')
def assign_gate(row):
    if row['risk_tier'] == "Tier 0: Prohibited": return "REJECTED: Prohibited Use Case"
    if row['risk_tier'] in ["Tier 3: Standard", "Tier 4: Low"]: return "PASSED: Fast-Lane Approval"
    return "PENDING: Full Governance Review Required"
inventory['gate_decision'] = inventory.apply(assign_gate, axis=1)
aigrc_utils.display_velocity_stats(inventory)
aigrc_utils.display_intake_sankey(inventory)
""")
]

# --- MODULE 02: ACCOUNTABILITY ---
m02_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 2: Accountability without Ambiguity"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('F', 'Governance Forums & Roles')"),
    nbf.v4.new_code_cell("""
inventory = aigrc_utils.load_inventory('ai_inventory_master.csv')
aigrc_utils.display_ownership_heatmap(inventory)
aigrc_utils.display_accountability_sankey(inventory)
""")
]

# --- MODULE 03: INVENTORY & CLASSIFICATION ---
m03_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 3: Inventory, Classification, and the Vetted Catalog"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('A/D', 'Standardized Asset Catalog & Lifecycle Map')"),
    nbf.v4.new_code_cell("""
catalog = aigrc_utils.generate_app_store_catalog(n=200)
aigrc_utils.display_app_catalog_sunburst(catalog)
aigrc_utils.display_capability_risk_matrix(catalog)
""")
]

# --- MODULE 04: RISK TAXONOMY ---
m04_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 4: The Enterprise AI Risk Taxonomy"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('C', 'Detailed Enterprise AI Risk Taxonomy')"),
    nbf.v4.new_code_cell("""
risk_lib = aigrc_utils.generate_risk_taxonomy()
aigrc_utils.display_risk_taxonomy_sunburst(risk_lib)
profiles = [
    {'name': 'Agentic', 'Security': 90, 'Privacy': 40, 'Fairness': 30, 'Safety': 95, 'Compliance': 80, 'Operational': 95},
    {'name': 'RAG', 'Security': 40, 'Privacy': 95, 'Fairness': 50, 'Safety': 40, 'Compliance': 60, 'Operational': 50}
]
aigrc_utils.display_risk_radar(profiles)
aigrc_utils.display_residual_risk_heatmap(risk_lib)
""")
]

# --- MODULE 05: THE PAVED ROAD ---
m05_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 5: The 'Paved Road' to Production"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('B/D', 'Automated Risk-Tiering & Lifecycle Paved Road')"),
    nbf.v4.new_code_cell("""
inventory = aigrc_utils.load_inventory('ai_inventory_master.csv')
aigrc_utils.display_governance_paved_road(inventory)
metrics = aigrc_utils.calculate_velocity_metrics(inventory)
aigrc_utils.display_velocity_gauges(metrics)
""")
]

# --- MODULE 06: DATA LINEAGE - DEPTH OVERHAUL ---
m06_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 6: Data Sovereignty & Training Lineage Analysis"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('E', 'High-Fidelity Training Lineage Depth Analysis')"),
    nbf.v4.new_markdown_cell("""
## 1. Concrete Proof of Data Minimization (§5.2 DAT-03)
The framework mandates that only necessary data is collected. The **Transformation Waterfall** below provides volumetric proof of active 'PII Scrubbing' and 'Toxicity Filtering' before model ingress.
"""),
    nbf.v4.new_code_cell("""
lineage = aigrc_utils.generate_training_lineage(n=50)
aigrc_utils.display_transformation_waterfall(lineage)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Chain-of-Custody Depth (§5.2 DAT-04)
Explore the deep provenance of training assets. This 4-tier visual traces the flow from **Raw Source** → **Sensitivity** → **Labeling Method (HITL/Synthetic)** → **Final Model Weight**.
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_lineage_depth_sunburst(lineage)
"""),
    nbf.v4.new_markdown_cell("""
## 3. Strategic Quality vs. Risk Matrix (§5.2 DAT-09)
We triage training data based on its **Quality** vs. its **Inherent Toxicity Risk**. This identifies 'Toxic Gold' assets that require the highest differential privacy protections.
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_quality_vs_risk_scatter(lineage)
"""),
    nbf.v4.new_markdown_cell("""
## 4. Global Sovereignty: Jurisdictional Flight Paths
Finally, we maintain the veracious map of cross-border transfers to ensure **DAT-08** compliance.
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_sovereignty_map(lineage)
""")
]

update_nb("module_00_hook.ipynb", m00_cells)
update_nb("module_01_governance_speed.ipynb", m01_cells)
update_nb("module_02_accountability.ipynb", m02_cells)
update_nb("module_03_inventory_classification.ipynb", m03_cells)
update_nb("module_04_risk_taxonomy.ipynb", m04_cells)
update_nb("module_05_paved_road.ipynb", m05_cells)
update_nb("module_06_data_lineage.ipynb", m06_cells)

# --- MODULE 07: SECURING THE WEIGHTS ---
m07_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\nimport importlib\nimportlib.reload(aigrc_utils)\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 7: Securing the Weights - Depth Overhaul"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('G', 'Active Strategy & Red-Team Evidence')"),
    nbf.v4.new_markdown_cell("""
## 1. Security Attrition Depth (Domain 3 Model Controls)
Basic encryption is state-of-the-norm, but **Operational Security** requires proof of defense-in-depth effectiveness. This waterfall visualizes the volumetric reduction of risk across the mandated gatekeepers.
"""),
    nbf.v4.new_code_cell("""
revocation_df = aigrc_utils.generate_vulnerability_lifecycle_data()
aigrc_utils.display_security_vulnerability_waterfall(revocation_df)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Adversarial Resilience Matrix (§12.1 Red-Teaming)
We cross-reference attack vectors against deployment archetypes (SaaS vs Self-Hosted) to identify structural weaknesses in model access patterns.
"""),
    nbf.v4.new_code_cell("""
red_team_logs = aigrc_utils.generate_detailed_red_team_logs()
aigrc_utils.display_resilience_heatmap(red_team_logs)
"""),
    nbf.v4.new_markdown_cell("""
## 3. Active Defense Velocity (Deliverable E Velocity)
Proof of real-time monitoring. We track **Detection Latency** (target < 100ms) and **Automated Revocation Success** to prove compliance with MSC-03.
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_defense_velocity_dashboard(revocation_df)
"""),
    nbf.v4.new_markdown_cell("""
## 4. Traditional Posture Dashboard
Summary of static controls (Encryption, Tamper Evidence, Weight Protection).
"""),
    nbf.v4.new_code_cell("""
sec_df = aigrc_utils.generate_security_posture_data()
aigrc_utils.display_security_vault_dashboard(sec_df)
""")
]
update_nb("module_07_weight_security.ipynb", m07_cells)
