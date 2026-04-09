import nbformat as nbf
import os

base_path = "/Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks"

def update_nb(fname, cells):
    path = os.path.join(base_path, fname)
    with open(path, 'r') as f:
        nb = nbf.read(f, as_version=4)
    nb['cells'] = cells
    with open(path, 'w') as f:
        nbf.write(nb, f)
    print(f"Updated {path}")

# --- MODULE 16: XAI ARCHITECTURE ---
m16_cells = [
    nbf.v4.new_markdown_cell("# Module 16: Explainability vs. Interpretability - Designing for the Audience"),
    nbf.v4.new_markdown_cell("""
## 1. Context: Audience-Differentiated XAI
**Part XVII §17.2** distinguishes between *Interpretability* (Gist for users) and *Explainability* (Mechanism for auditors).

**Goal**: Generate different explanation "depths" for the same model decision.
"""),
    nbf.v4.new_code_cell("""
# Decision Logic: Credit Rejection
def get_explanation(audience="User"):
    reason = "Debt-to-Income (DTI) ratio is 45%, exceeding the 40% threshold."
    if audience == "User":
        return f"Your application was declined because your monthly debt payments ({reason.split('is ')[1].split(',')[0]}) are higher than our current limits."
    else:
        return f"Model Feature ID: DTI_01 | Value: 0.45 | Threshold: 0.40 | SHAP_Value: -0.32 | Result: ADVERSE"

print(f"User Gist: {get_explanation('User')}")
print(f"Auditor Mechanism: {get_explanation('Auditor')}")
""")
]

# --- MODULE 17: SUPPLY CHAIN ---
m17_cells = [
    nbf.v4.new_markdown_cell("# Module 17: Supply Chain & Vendor Risk - Trusting the Hyperscalers"),
    nbf.v4.new_markdown_cell("""
## 1. Context: The AI-SBOM
**Part XVI §16.7** mandates an AI Software Bill of Materials (AI-SBOM) for models sourced from third parties.

**Goal**: Parse and validate a vendor AI-SBOM.
"""),
    nbf.v4.new_code_cell("""
# Mock AI-SBOM
vendor_sbom = {
    "model_name": "HyperSmart-v4",
    "base_model": "Llama-3-70b-Base",
    "fine_tuning_data": "Proprietary_Finance_Dataset_v1",
    "safety_filters": ["Llama-Guard-2", "Internal_PII_Layer"],
    "vulnerabilities_disclosed": ["Known hallucination on currency conversion"]
}

def audit_sbom(sbom):
    if "Internal_PII_Layer" not in sbom['safety_filters']:
        return "REJECT: Missing mandatory internal safety layer."
    return "PASS: Vendor AI-SBOM verified."

print(audit_sbom(vendor_sbom))
""")
]

# --- MODULE 18: REGULATORY MAPPING ---
m18_cells = [
    nbf.v4.new_markdown_cell("# Module 18: Regulatory Convergence - EU AI Act to NIST Alignment"),
    nbf.v4.new_markdown_cell("""
## 1. Context: Cross-Framework Mapping
**Part IV §4.5** of the framework provides the translation layer between NIST AI RMF, ISO 42001, and the EU AI Act.

**Goal**: Categorize the inventory into EU AI Act "High Risk" (Annex III) categories.
"""),
    nbf.v4.new_code_cell("""
import aigrc_utils
inventory = aigrc_utils.load_inventory('ai_inventory_master.csv')

# EU AI Act Annex III - High Risk Categories mapping
annex_iii_map = {
    "HR": "Employment, workers management and access to self-employment",
    "Finance": "Access to and enjoyment of essential private services and public services",
    "National Security": "Law enforcement / Migration / Asylum"
}

def get_eu_category(domain):
    return annex_iii_map.get(domain, "Not High-Risk (Annex III)")

inventory['eu_ai_act_category'] = inventory['domain'].apply(get_eu_category)
high_risk_eu = inventory[inventory['eu_ai_act_category'] != "Not High-Risk (Annex III)"]

print(f"Detected {len(high_risk_eu)} use cases likely falling under EU AI Act High-Risk obligations.")
high_risk_eu[['id', 'name', 'domain', 'eu_ai_act_category']].head()
""")
]

# --- MODULE 19: BOARD REPORT ---
m19_cells = [
    nbf.v4.new_markdown_cell("# Module 19: The Board Report - Pricing the Residual AI Risk"),
    nbf.v4.new_markdown_cell("""
## 1. Context: Executive Oversight
The final goal of AI GRC is to provide the Board with a quantitative view of residual risk. **Part VI** defines the Reporting Cadence.

**Goal**: Generate the final AI Governance Scorecard.
"""),
    nbf.v4.new_code_cell("""
import aigrc_utils
inventory = aigrc_utils.load_inventory('ai_inventory_master.csv')

# Pricing Residual Risk (Simple Model)
# Residual Risk = (Risk Score * Business Value) * (1 - Control Effectiveness)
# Mock: Controls are 80% effective
inventory['residual_risk'] = (inventory['risk_score'] / 100) * inventory['business_value'] * 0.20

scorecard = {
    "Portfolio Size": len(inventory),
    "Total Business Value": f"${inventory['business_value'].sum():,.2f}M",
    "Inherent Risk Exposure": f"${(inventory['risk_score']/100 * inventory['business_value']).sum():,.2f}M",
    "Residual Risk (Post-Control)": f"${inventory['residual_risk'].sum():,.2f}M",
    "Critical Incidents (YTD)": 2
}

print("--- BOARD EXECUTIVE AI GOVERNANCE SCORECARD ---")
for k, v in scorecard.items():
    print(f"{k:<30}: {v}")
""")
]

update_nb("module_16_xai_architecture.ipynb", m16_cells)
update_nb("module_17_supply_chain.ipynb", m17_cells)
update_nb("module_18_regulatory_mapping.ipynb", m18_cells)
update_nb("module_19_board_report.ipynb", m19_cells)
