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

# --- MODULE 05: PAVED ROAD ---
m05_cells = [
    nbf.v4.new_markdown_cell("# Module 5: The 'Paved Road' to Production - Risk-Tiering & Automated Intake"),
    nbf.v4.new_markdown_cell("""
## 1. Context: Proportional Scrutiny
Uniformity causes adoption tax. **Part VIII** mandates that high-risk systems face "proportionate scrutiny."

**Goal**: Implement the binding risk-tiering logic from Deliverable B.
"""),
    nbf.v4.new_code_cell("""
import grc_utils
inventory = grc_utils.load_inventory('ai_inventory_master.csv')

def determine_gate_path(risk_tier):
    \"\"\"Determines the governance path based on the framework's tiering model.\"\"\"
    paths = {
        "Tier 0: Prohibited": "BLOCK: Immediate Escalation to Legal",
        "Tier 1: High": "GATE: Independent Validation + Red Team Required",
        "Tier 2: Elevated": "GATE: Security & Privacy Sign-off Required",
        "Tier 3: Standard": "FAST-LANE: Automated Intake Review",
        "Tier 4: Low": "SELF-CERT: Business Owner Certification"
    }
    return paths.get(risk_tier, "UNKNOWN")

# Test on our inventory
tier_summary = inventory.groupby('risk_tier').size()
display(tier_summary)

print(f"Path for AI-1001: {determine_gate_path(inventory.iloc[0]['risk_tier'])}")
"""),
    nbf.v4.new_markdown_cell("""
## 2. Evidence: Threshold Enforcement
We implement a "Wait-State" for any Tier 1 system missing a Red-Team report.
"""),
    nbf.v4.new_code_cell("""
is_compliant = False # Simulated check
if inventory.iloc[0]['risk_tier'] == 'Tier 1: High' and not is_compliant:
    print("WARNING: Deployment Blocked. Required Evidence (INT-01) Missing.")
""")
]

# --- MODULE 06: DATA SOVEREIGNTY ---
m06_cells = [
    nbf.v4.new_markdown_cell("# Module 6: Data Sovereignty & Training Lineage - The Chain-of-Custody"),
    nbf.v4.new_markdown_cell("""
## 1. Context: Provenance is Control
**Part V Domain 2 (DAT-04)** mandates training data documentation (source, lineage, consent).

**Goal**: Trace the training data chain-of-custody for a model.
"""),
    nbf.v4.new_code_cell("""
import json

# Example Chain-of-Custody Metadata (JSON)
provenance_record = {
    "dataset_id": "DS-2024-ALPHA",
    "sources": [
        {"name": "Internal CRM", "last_update": "2024-01-10", "consent_basis": "Contractual"},
        {"name": "Public-Web-2023", "license": "CC-BY-4.0", "curation_date": "2023-12-05"}
    ],
    "processing": [
        {"step": "Anonymization", "tool": "Presidio", "operator": "DataOps_Engine"},
        {"step": "Filtering", "threshold": "Quality > 0.8"}
    ],
    "hash": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}

print("--- AI Software Bill of Materials (AI-SBOM) ---")
print(json.dumps(provenance_record, indent=2))
"""),
    nbf.v4.new_markdown_cell("""
## 2. Implementation: Detecting PII in Training Ingestion
Preventing data leakage begins before the model is even trained.
"""),
    nbf.v4.new_code_cell("""
# Simple PII redactor simulation
def check_pii(text):
    sensitive_patterns = ["EMAIL:", "SSN:", "PHONE:"]
    found = [p for p in sensitive_patterns if p in text]
    return found

corpus_sample = "User report from EMAIL: test@corp.com"
print(f"Ingestion Check: {check_pii(corpus_sample)}")
""")
]

# --- MODULE 07: SECURING THE WEIGHTS ---
m07_cells = [
    nbf.v4.new_markdown_cell("# Module 7: Securing the Weights - Protecting Dual-Use Foundations"),
    nbf.v4.new_markdown_cell("""
## 1. Context: The NIST Priority
Dual-use foundation models carry catastrophic risk if weights are stolen. **Part XV (SOC-01)** mandates explicit constraints against malware generation and weight theft.

**Goal**: Implement a simulation of model weight security (Encryption + Integrity).
"""),
    nbf.v4.new_code_cell("""
import hashlib
import os

# Simulated Model Weight Buffer
model_weights = b"highly_sensitive_transformer_parameters_v1.0"

# 1. Integrity Control: SHA-256 Hashing (MSC-03)
def generate_tamper_signature(weights):
    return hashlib.sha256(weights).hexdigest()

signature = generate_tamper_signature(model_weights)
print(f"Model Weight Signature (SHA-256): {signature}")

# 2. Access Control: Simulated Key Management (Identity-Based)
user_permissions = {"admin_user": "READ/WRITE", "data_scientist": "READ", "external_app": "NONE"}

def load_model(user):
    scope = user_permissions.get(user, "NONE")
    if "READ" in scope:
        print(f"ACCESS GRANTED for {user}. Decrypting weights...")
        return model_weights
    else:
        print(f"ACCESS DENIED for {user}. Unauthorized weight extraction attempt (SOC-01).")
        return None

weights = load_model("external_app")
"""),
    nbf.v4.new_markdown_cell("""
## 2. Incident Simulation: Tamper Detection
What happens if a quantization process or a malicious actor alters the weights?
"""),
    nbf.v4.new_code_cell("""
# Malicious Alteration
tampered_weights = model_weights + b"_malware_payload"

new_sig = generate_tamper_signature(tampered_weights)
if new_sig != signature:
    print("!!! CRITICAL ALERT: Model Weight Integrity Violation Detected !!!")
    print(f"Expected: {signature}")
    print(f"Actual:   {new_sig}")
    # Trigger Corrective Control: OUT-06 (Rollback)
""")
]

update_nb("module_05_paved_road.ipynb", m05_cells)
update_nb("module_06_data_lineage.ipynb", m06_cells)
update_nb("module_07_weight_security.ipynb", m07_cells)
