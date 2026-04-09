import nbformat as nbf
import os

modules = [
    ("00_hook", "The Hook: The Era of 'Unpriced AI Liability'"),
    ("01_governance_speed", "Governance Isn't Bureaucracy: The License to Scale"),
    ("02_accountability", "Accountability Without Ownership: The RACI Reality"),
    ("03_ai_risk_v_software", "Why AI Risk Is Not Software Risk: Probabilistic Failures"),
    ("04_risk_taxonomy", "The Enterprise AI Risk Taxonomy: A Master Register"),
    ("05_paved_road", "The 'Paved Road' to Production: Risk-Tiering & Automated Intake"),
    ("06_data_lineage", "Data Sovereignty & Training Lineage: The Chain-of-Custody"),
    ("07_weight_security", "Securing the Weights: Protecting Dual-Use Foundations"),
    ("08_prompt_ops", "Prompt Engineering as a Controlled Discipline: Versioning & Defense"),
    ("09_rag_integrity", "RAG Integrity: Beyond Hallucinations"),
    ("10_agentic_killswitch", "Agentic Autonomy: The Kill-Switch & Tool Limits"),
    ("11_documentation", "Machine-Readable Accountability: Model & System Cards"),
    ("12_validation", "Independent Validation: The Challenger Model"),
    ("13_red_teaming", "Red-Teaming & Adversarial Resilience: MITRE ATLAS Integration"),
    ("14_incident_response", "Incident Response: When the Model Refuses to Refuse"),
    ("15_fairness", "AI Fairness: Navigating Impossibility Constraints"),
    ("16_xai_architecture", "Explainability vs. Interpretability: Designing for the Audience"),
    ("17_supply_chain", "Supply Chain & Vendor Risk: Trusting the Hyperscalers"),
    ("18_regulatory_mapping", "Regulatory Convergence: EU AI Act to NIST Alignment"),
    ("19_board_report", "The Board Report: Pricing the Residual AI Risk")
]

base_path = "/Users/lakshminarasimhan.santhanamgigkri.com/AIF/workbooks"

for i, (fname, title) in enumerate(modules):
    nb = nbf.v4.new_notebook()
    
    nb['cells'] = [
        nbf.v4.new_markdown_cell(f"# Module {i}: {title}\n\n*Enterprise AI Governance, Risk & Control Expert Workbook*"),
        nbf.v4.new_markdown_cell("## 1. Introduction & Context\n\n[Theory from EAGCF Framework goes here]"),
        nbf.v4.new_code_cell(f"import pandas as pd\nimport numpy as np\nimport aigrc_utils\n\n# Load the master inventory\ninventory = aigrc_utils.load_inventory('../ai_inventory_master.csv')\ninventory.head()"),
        nbf.v4.new_markdown_cell("## 2. Practical Implementation\n\n[Python Code implementation goes here]"),
        nbf.v4.new_code_cell("# Placeholder for Module Implementation\ndef run_module():\n    print(f'Running Module {i}...')\n\nrun_module()")
    ]
    
    file_path = os.path.join(base_path, f"module_{fname}.ipynb")
    with open(file_path, 'w') as f:
        nbf.write(nb, f)
    print(f"Created {file_path}")
