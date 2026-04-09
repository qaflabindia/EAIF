import nbformat as nbf
import os

def update_nb(nb_path, cells):
    if not os.path.exists(nb_path):
        nb = nbf.v4.new_notebook()
        nb['cells'] = cells
    else:
        with open(nb_path, 'r') as f:
            nb = nbf.read(f, as_version=4)
        nb['cells'] = cells
    
    with open(nb_path, 'w') as f:
        nbf.write(nb, f)
    print(f"Updated {nb_path}")

# --- MODULE 17: SUPPLY CHAIN SECURITY (AUDIT-GRADE) ---
m17_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\nimport importlib\nimportlib.reload(aigrc_utils)\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 17: AI Supply Chain & Provenance Audit"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('MSC-09', 'AI-SBOM & Lineage Audit Artifact')"),
    nbf.v4.new_markdown_cell("""
## 1. Model Provenance: Chain of Custody Audit (Domain 11.2)
Specifically implementing **Control MSC-01/03/06**. This Sankey Flow documents the technical lineage from original weights to production artifacts, flagging cryptographic verification milestones.
"""),
    nbf.v4.new_code_cell("""
sankey_data, sbom_df, vex_df = aigrc_utils.generate_expert_supply_chain_audit_data()
aigrc_utils.display_ai_sbom_lineage_sankey(sankey_data)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Interactive AI-SBOM Registry (MSC-09)
Transitive dependency audit covering **Model**, **Dataset**, and **Infrastructure components**. This artifact provides the SHA-256 evidence required for regulatory defensibility under MSC-09.
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_audit_provenance_registry(sbom_df)
"""),
    nbf.v4.new_markdown_cell("""
## 3. VEX Vulnerability Governance (NIST 10.5 Alignment)
Mapping identified vulnerabilities to their **Exploitability Status** (VEX). This allows auditors to prioritize 'Open' high-CVSS risks over 'Not Affected' isolated components.
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_vulnerability_vex_auditor(vex_df)
"""),
    nbf.v4.new_markdown_cell("""
## 4. Supply Chain 'Blast Radius' — Tiered Hierarchy
Visualizing risk depth across the full AI stack: **Infrastructure**, **Library**, **Model**, and **Data**. 
"""),
    nbf.v4.new_code_cell("""
_ , sunburst_df = aigrc_utils.generate_vulnerability_vex_registry()
aigrc_utils.display_supply_chain_risk_sunburst(sunburst_df)
""")
]

# --- MODULE 18: REGULATORY MAPPING (EXPERT LAB) ---
m18_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\nimport importlib\nimportlib.reload(aigrc_utils)\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 18: Regulatory Mapping & Compliance Registry"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('REG-01', 'Harmonized Compliance Framework')"),
    nbf.v4.new_markdown_cell("""
## 1. Harmonized Compliance Maturity (Domain 16)
Benchmarking the enterprise's current governance posture against four global anchors: **NIST AI RMF**, **EU AI Act**, **GDPR**, and **ISO/IEC 42001**. The radar/spider chart identifies compliance gaps across jurisdictions.
"""),
    nbf.v4.new_code_cell("""
risk_df, maturity_df = aigrc_utils.generate_expert_regulatory_register_data()
aigrc_utils.display_compliance_maturity_radar(maturity_df)
"""),
    nbf.v4.new_markdown_cell("""
## 2. The Enterprise AI Risk Register
Establishing the "System of Record" for AI risks. This registry maps risk tiers (0-4) to primary risk categories (Bias, Privacy, Hallucination) and provides real-time mitigation status as required by the framework's **Domain 1 & 3**.
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_enterprise_risk_register_table(risk_df)
"""),
    nbf.v4.new_markdown_cell("""
## 3. EU AI Act Delta — FRIA Tracking (Art. 27)
Specifically tracking the status of **Fundamental Rights Impact Assessments (FRIA)** for High-Risk systems (Annex III), as defined in the framework extension section 16.2.4.
"""),
    nbf.v4.new_code_cell("""
# Filter for EU AI Act Annex III systems
eu_high_risk = risk_df[risk_df['Regulation'].str.contains('EU AI Act')]
aigrc_utils.display_enterprise_risk_register_table(eu_high_risk)
""")
]

# --- MODULE 19: BOARD REPORTING (EXPERT LAB) ---
m19_cells = [
    nbf.v4.new_code_cell("import aigrc_utils\nimport importlib\nimportlib.reload(aigrc_utils)\naigrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 19: Executive Board Reporting & KPIs"),
    nbf.v4.new_code_cell("aigrc_utils.display_deliverable_anchor('BRD-01', 'Executive Governance KPI Dashboard')"),
    nbf.v4.new_markdown_cell("""
## 1. Global Governance Scorecard (Part VII §7.1)
High-impact indicator row providing the Board with an immediate sanity check on the enterprise AI health. Tracks **Overall Compliance**, **Safety Index** (as defined in §7.2), and **Risk Mitigation** success rates.
"""),
    nbf.v4.new_code_cell("""
scorecard, treemap_df, incident_df, progress_df = aigrc_utils.generate_expert_board_kpi_data()
aigrc_utils.display_executive_governance_scorecard(scorecard)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Multinational Risk Portfolio (Regional Concentration)
Multinational view of the AI estate, sized by **Cumulative Usage** and colored by **Risk Tier (0-4)**. This treemap allows for the identification of risk concentration within specific Business Units (e.g., AMER Finance vs APAC Tech).
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_global_risk_portfolio_treemap(treemap_df)
"""),
    nbf.v4.new_markdown_cell("""
## 3. Red-Flag Command Center: Incident Severity (S1-S4)
Tracking critical security and safety events over the reporting period. This visualization identifies the volume of **S1 (Critical)** and **S2 (High)** incidents which require immediate Board notification (within 24 hours per §7.2).
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_red_flag_incident_command(incident_df)
"""),
    nbf.v4.new_markdown_cell("""
## 4. Control Domain Implementation Maturity
Visualizing implementation progress across all **15 Governance Domains**. This radar map identifies maturity gaps in 'Agentic' or 'Supply Chain' controls relative to foundational strategy.
"""),
    nbf.v4.new_code_cell("""
aigrc_utils.display_domain_progress_radar(progress_df)
""")
]

update_nb("module_17_supply_chain.ipynb", m17_cells)
update_nb("module_18_regulatory_mapping.ipynb", m18_cells)
update_nb("module_19_board_report.ipynb", m19_cells)
