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

# --- MODULE 02: ACCOUNTABILITY ---
m02_cells = [
    nbf.v4.new_markdown_cell("# Module 2: Accountability Without Ownership - The RACI Reality"),
    nbf.v4.new_markdown_cell("""
## 1. Context: Named Accountability
Shared accountability is unaccountability. **Part VI** of the framework mandates 3 primary owners for every AI system:
1. **Business Owner**: Accountable for benefits/harms.
2. **Model Owner**: Accountable for artifact performance.
3. **System Owner**: Accountable for the full deployment stack.

**Goal**: Assign and verify ownership for the inventory.
"""),
    nbf.v4.new_code_cell("""
import grc_utils
import pandas as pd

inventory = grc_utils.load_inventory('ai_inventory_master.csv')

# Simulate a RACI Matrix for a specific high-risk use case
case_id = inventory[inventory['risk_tier'].str.contains('High')].iloc[0]['id']
case_name = inventory[inventory['id'] == case_id]['name'].values[0]

raci_matrix = {
    "Task": ["Approve Strategy", "Model Evaluation", "Prompt Versioning", "Incident Response"],
    "Business_Owner": ["AR", "I", "I", "A"],
    "Model_Owner": ["C", "AR", "I", "C"],
    "System_Owner": ["C", "C", "AR", "R"]
}

print(f"--- RACI Matrix for {case_name} ({case_id}) ---")
print(pd.DataFrame(raci_matrix))
"""),
    nbf.v4.new_markdown_cell("""
## 2. Implementation: MLflow Model Tags
In a practical MLOps environment, ownership should be tagged directly on the model artifact.
"""),
    nbf.v4.new_code_cell("""
# Mock MLflow tagging logic
model_tags = {
    "model_owner": "j.doe@enterprise.com",
    "business_owner": "s.risk@enterprise.com",
    "risk_tier": "Tier 1: High",
    "approved_by": "AI_Risk_Committee_v1"
}

print("MLflow Registry Tags Applied:")
for k, v in model_tags.items():
    print(f"Tag: {k} -> {v}")
""")
]

# --- MODULE 03: PROBABILISTIC FAILURE ---
m03_cells = [
    nbf.v4.new_markdown_cell("# Module 3: Why AI Risk Is Not Software Risk - Probabilistic Failures"),
    nbf.v4.new_markdown_cell("""
## 1. Context: "Looks Right" is Dangerous
AI fails plausibly. **Part III** of the framework notes that deterministic systems fail cleanly, while AI fails by producing incorrect but convincing outputs.

**Practical Goal**: Simulate model drift and its impact on the risk distribution.
"""),
    nbf.v4.new_code_cell("""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate a distribution of model confidence scores
np.random.seed(42)
baseline_scores = np.random.normal(0.85, 0.05, 1000) # Pre-drift
drifted_scores = np.random.normal(0.70, 0.15, 1000)  # Post-drift

plt.figure(figsize=(10, 6))
plt.hist(baseline_scores, bins=30, alpha=0.5, label='Baseline (Pre-deployment)')
plt.hist(drifted_scores, bins=30, alpha=0.5, label='Drifted (Post-deployment)')
plt.axvline(0.75, color='red', linestyle='--', label='Risk Threshold')
plt.title("Model Confidence Score Drift Simulation")
plt.legend()
plt.show()

print(f"Samples below threshold (Baseline): {sum(baseline_scores < 0.75)}")
print(f"Samples below threshold (Drifted): {sum(drifted_scores < 0.75)}")
"""),
    nbf.v4.new_markdown_cell("""
## 2. Detection: Evidently / Monitoring
Monitoring drift isn't just a performance task—it's a control task.
"""),
    nbf.v4.new_code_cell("""
# Concept: If drift detected > threshold, trigger 'Post-change Monitoring Period' (Part VII Stage 9)
def trigger_governance_alert(drift_score):
    if drift_score > 0.1:
        return "ALERT: Material Change Detected. Suspend Auto-Approval."
    return "STATUS: Normal"

print(trigger_governance_alert(0.15))
""")
]

# --- MODULE 04: RISK TAXONOMY ---
m04_cells = [
    nbf.v4.new_markdown_cell("# Module 4: The Enterprise AI Risk Taxonomy - A Master Register"),
    nbf.v4.new_markdown_cell("""
## 1. Context: The Governance Operating Model
A risk register must survive front-page scrutiny. **Part V** provides the 15 control domains.

**Goal**: Map the inventory to the risk taxonomy (Strategic, Operational, Legal, Financial).
"""),
    nbf.v4.new_code_cell("""
import grc_utils
inventory = grc_utils.load_inventory('ai_inventory_master.csv')

# Grouping by risk themes
taxonomy_mapping = {
    "Strategic": ["National Security", "HR"],
    "Operational": ["Customer Service", "Supply Chain"],
    "Legal/Privacy": ["PII_Exposure == True"],
    "Financial": ["Finance"]
}

print("Inventory Risk Concentration by Taxonomy:")
for theme, criteria in taxonomy_mapping.items():
    if theme == "Legal/Privacy":
        count = len(inventory[inventory['pii_exposure'] == True])
    else:
        count = len(inventory[inventory['domain'].isin(criteria)])
    print(f"- {theme}: {count} systems")
"""),
    nbf.v4.new_markdown_cell("""
## 2. Implementation: The Master AI Incident Register (Mock)
A preventive control is only as good as the incident register that informs it.
"""),
    nbf.v4.new_code_cell("""
incident_log = pd.DataFrame({
    "incident_id": ["INC-001", "INC-002"],
    "type": ["Prompt Injection", "Data Leakage"],
    "severity": ["S2 - High", "S1 - Critical"],
    "affected_system": ["AI-1005", "AI-1021"],
    "remediation": ["System Prompt Hardened", "PII Filter Applied"]
})
incident_log
""")
]

update_nb("module_02_accountability.ipynb", m02_cells)
update_nb("module_03_ai_risk_v_software.ipynb", m03_cells)
update_nb("module_04_risk_taxonomy.ipynb", m04_cells)
