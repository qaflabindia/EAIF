import pandas as pd
import numpy as np
from pydantic import BaseModel, Field
from typing import List, Optional
import json
import os
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import HTML, Markdown, display

# Domain-specific constants
DOMAINS = ["Finance", "Healthcare", "HR", "Information Security", "Customer Service", "Marketing", "Supply Chain"]
RISK_TIERS = ["Tier 0: Prohibited", "Tier 1: High", "Tier 2: Elevated", "Tier 3: Standard", "Tier 4: Low"]
ARCHETYPES = ["App-First", "Chat-First", "RAG", "Agentic", "Decision-Support", "Autonomous"]
MODELS = ["GPT-4o", "Llama-3-70b", "Claude-3.5-Sonnet", "Mistral-Large", "Proprietary-v1"]

def generate_synthetic_inventory(n=1000):
    """Generates a synthetic inventory of AI use cases with multi-owner accountability."""
    np.random.seed(42)
    data = []
    
    for i in range(n):
        domain = np.random.choice(DOMAINS)
        arch = np.random.choice(ARCHETYPES)
        
        # Heuristic for risk tiering
        if domain == "Information Security" or (domain == "Finance" and arch == "Autonomous"):
            tier = RISK_TIERS[1] # Tier 1: High
        elif domain == "Marketing" or domain == "Customer Service":
            tier = np.random.choice(RISK_TIERS[3:]) # Standard or Low
        else:
            tier = np.random.choice(RISK_TIERS[1:4])
            
        # Accountability Simulation (§1.5 Principle 4)
        # Higher risk should have higher ownership discipline, but let's simulate gaps
        gap_prob = 0.05 if 'High' in tier else 0.2
        
        use_case = {
            "id": f"AI-{1000 + i}",
            "name": f"Project_{domain}_{arch}_{i}",
            "domain": domain,
            "archetype": arch,
            "risk_tier": tier,
            "model_service": np.random.choice(MODELS),
            "pii_exposure": np.random.choice([True, False], p=[0.3, 0.7]),
            "cbrn_relevant": True if domain == "Information Security" else np.random.choice([True, False], p=[0.05, 0.95]),
            "business_value": np.random.uniform(10, 100),
            "risk_score": np.random.uniform(5, 95),
            "status": np.random.choice(["Discovery", "In-Build", "Validation", "Production", "Retired"]),
            "business_owner": f"Exec_{np.random.randint(1, 10)}@corp.com" if np.random.random() > gap_prob else None,
            "model_owner": f"DS_{np.random.randint(1, 20)}@corp.com" if np.random.random() > gap_prob else None,
            "system_owner": f"Eng_{np.random.randint(1, 25)}@corp.com" if np.random.random() > gap_prob else None,
        }
        data.append(use_case)
        
    df = pd.DataFrame(data)
    
    def assign_gate(row):
        if row['risk_tier'] == "Tier 0: Prohibited": return "REJECTED: Prohibited Use Case"
        if row['risk_tier'] in ["Tier 3: Standard", "Tier 4: Low"]: return "PASSED: Fast-Lane Approval"
        return "PENDING: Full Governance Review Required"
    
    df['gate_decision'] = df.apply(assign_gate, axis=1)
    df['liability'] = df['business_value'] * (df['risk_score'] / 100) * 10000
    
    return df

def save_inventory(df, path="ai_inventory_master.csv"):
    df.to_csv(path, index=False)
    print(f"Inventory saved to {path}")

def load_inventory(path="ai_inventory_master.csv"):
    if os.path.exists(path):
        return pd.read_csv(path)
    return generate_synthetic_inventory()

def generate_app_store_catalog(n=200):
    """Generates a high-fidelity synthetic AI App Store catalog."""
    np.random.seed(42)
    apps = []
    capabilities = ["Reasoning", "Code Generation", "Creative/Image", "Summarization", "Search/RAG", "Classification"]
    statuses = ["Vetted", "Pending Review", "Prohibited", "Retired"]
    
    for i in range(n):
        cap = np.random.choice(capabilities)
        status = np.random.choice(statuses, p=[0.6, 0.2, 0.1, 0.1])
        tier = np.random.choice(RISK_TIERS[1:])
        
        app = {
            "app_id": f"APP-{5000 + i}",
            "app_name": f"{cap}_{i}",
            "capability": cap,
            "base_model": np.random.choice(MODELS),
            "risk_tier": tier,
            "compliance_status": status,
            "usage_count": np.random.randint(10, 5000),
            "cost_tier": np.random.choice(["Premium", "Standard", "Value"]),
            "last_audit": (pd.Timestamp.now() - pd.Timedelta(days=np.random.randint(1, 365))).strftime('%Y-%m-%d')
        }
        apps.append(app)
    return pd.DataFrame(apps)

def generate_risk_taxonomy():
    """Returns a library of 40+ specific AI risks mapped to Framework Categories (§7.2)."""
    risks = [
        # Safety
        {"Category": "Safety", "Risk": "Hallucination", "Impact": "S2", "Description": "Model generates plausible but false information."},
        {"Category": "Safety", "Risk": "Harmful Content", "Impact": "S1", "Description": "Model generates instructions for illegal acts or self-harm."},
        {"Category": "Safety", "Risk": "Unsafe Autonomous Action", "Impact": "S1", "Description": "Agent takes physical or financial action without human oversight."},
        
        # Security
        {"Category": "Security", "Risk": "Prompt Injection", "Impact": "S2", "Description": "Adversarial input bypasses system instructions."},
        {"Category": "Security", "Risk": "Model Extraction", "Impact": "S2", "Description": "Reconstruction of model weights via API probing."},
        {"Category": "Security", "Risk": "Insecure Plugin Use", "Impact": "S3", "Description": "AI agent calls unauthenticated third-party APIs."},
        
        # Privacy
        {"Category": "Privacy", "Risk": "Training Data Memorization", "Impact": "S2", "Description": "Model regurgitates verbatim PII from training set."},
        {"Category": "Privacy", "Risk": "Membership Inference", "Impact": "S3", "Description": "Determining if a specific person's data was in the training set."},
        {"Category": "Privacy", "Risk": "Unintended Data Leakage", "Impact": "S2", "Description": "PII retrieved via RAG and presented to unauthorized user."},
        
        # Fairness
        {"Category": "Fairness", "Risk": "Algorithmic Bias", "Impact": "S2", "Description": "Systematic disparate impact against protected groups."},
        {"Category": "Fairness", "Risk": "Stereotype Reinforcement", "Impact": "S3", "Description": "Model reproduces historical social biases in creative tasks."},
        
        # Compliance
        {"Category": "Compliance", "Risk": "Prohibited Use Intent", "Impact": "S1", "Description": "Attempting to use AI for subliminal manipulation (§5.2)."},
        {"Category": "Compliance", "Risk": "Regulatory Non-Disclosure", "Impact": "S3", "Description": "Failure to notify users they are interacting with an AI."},
    ]
    # Add variety
    for i in range(30):
        risks.append({"Category": np.random.choice(["Operational", "Governance", "Security", "Compliance"]), 
                      "Risk": f"Specific_Risk_{i+100}", "Impact": np.random.choice(["S2", "S3", "S4"]), 
                      "Description": "Detailed failure scenario placeholder."})
    return pd.DataFrame(risks)

def generate_training_lineage(n=50):
    """Generates a high-veracity deep-lineage synthetic AI training data dataset."""
    np.random.seed(42)
    lineage = []
    providers = ["Internal Log Warehouse", "Public Web Crawl", "LexisNexis v4", "Synthetic Generator v2", "Manual Labeling Team"]
    methods = ["HITL Verified", "Self-Supervised", "Synthetic", "Red-Teamed"]
    regions = {
        "US-East": {"reg": "CCPA/Federal", "lat": 37, "lon": -77, "country": "USA"},
        "EU-West": {"reg": "GDPR", "lat": 48, "lon": 2, "country": "FRA"},
        "APAC-Singapore": {"reg": "PDPA", "lat": 1, "lon": 103, "country": "SGP"},
        "UK-South": {"reg": "UK-GDPR", "lat": 51, "lon": 0, "country": "GBR"},
        "China-East": {"reg": "PIPL", "lat": 31, "lon": 121, "country": "CHN"}
    }
    mechanisms = ["Adequacy Decision", "SCC", "BCR", "None (High Risk)"]
    
    for i in range(n):
        s_name = np.random.choice(list(regions.keys()))
        p_name = np.random.choice(list(regions.keys()))
        raw = np.random.randint(100000, 500000)
        scrubbed = int(raw * np.random.uniform(0.7, 0.95))
        
        entry = {
            "source_id": f"SRC-{2000 + i}",
            "source_name": np.random.choice(providers),
            "data_type": np.random.choice(["PII", "Confidential", "Public", "Proprietary"]),
            "source_region": s_name,
            "processing_region": p_name,
            "governing_regulation": regions[s_name]['reg'],
            "transfer_mechanism": np.random.choice(mechanisms, p=[0.3, 0.4, 0.2, 0.1]) if s_name != p_name else "Local",
            "dpia_status": np.random.choice(["Completed", "Pending", "Overdue"], p=[0.7, 0.2, 0.1]),
            "raw_count": raw,
            "scrubbed_count": scrubbed,
            "labeling_method": np.random.choice(methods),
            "quality_score": np.random.randint(60, 100),
            "toxicity_score": np.random.randint(0, 40),
            "memorization_index": np.random.uniform(0.1, 0.8),
            "model_assigned": np.random.choice(MODELS),
            "src_lat": regions[s_name]['lat'], "src_lon": regions[s_name]['lon'],
            "proc_lat": regions[p_name]['lat'], "proc_lon": regions[p_name]['lon']
        }
        lineage.append(entry)
    return pd.DataFrame(lineage)

def generate_security_posture_data():
    """Generates synthetic security posture data for model weights."""
    models = ["GPT-4o (SaaS)", "Llama-3-70B (Self-Hosted)", "Mistral-Large (Self-Hosted)", "Claude-3.5 (SaaS)"]
    data = []
    for m in models:
        is_self_hosted = "Self-Hosted" in m
        data.append({
            "model": m,
            "encryption_at_rest": 100,
            "tamper_evidence_msc_03": 95 if is_self_hosted else 80,
            "access_revocation_ms": 50 if is_self_hosted else 500,
            "weight_protection_sec_01": 90 if not is_self_hosted else 70,
            "archetype": "Self-Hosted" if is_self_hosted else "SaaS API"
        })
    return pd.DataFrame(data)

def generate_red_team_metrics():
    """Generates simulated red-team resilience scores."""
    return [
        {'name': 'Tier 1 FM (Base)', 'Injection': 45, 'Jailbreak': 30, 'Extraction': 85, 'PII-Exfil': 60, 'Backdoor': 90},
        {'name': 'Tier 1 FM (Safe)', 'Injection': 92, 'Jailbreak': 88, 'Extraction': 95, 'PII-Exfil': 98, 'Backdoor': 95}
    ]


def generate_vulnerability_lifecycle_data():
    """Generates synthetic time-series for security incident lifecycle."""
    dates = pd.date_range(start="2024-01-01", periods=90, freq='D')
    data = []
    for dt in dates:
        attempts = np.random.randint(5, 50)
        blocked = int(attempts * np.random.uniform(0.9, 1.0))
        revocation_ms = np.random.normal(85, 10) # Target < 100ms
        data.append({
            "date": dt,
            "attempts": attempts,
            "blocked": blocked,
            "leaked_attempts": attempts - blocked,
            "revocation_latency_ms": max(20, revocation_ms)
        })
    return pd.DataFrame(data)

def generate_detailed_red_team_logs():
    """Detailed red-team audit logs for Depth Analysis."""
    attacks = ["Prompt Injection", "Weight Extraction", "PII-Exfiltration", "Jailbreak", "Model Inversion"]
    archetypes = ["SaaS API", "Self-Hosted"]
    logs = []
    for a in attacks:
        for arch in archetypes:
            success_rate = np.random.uniform(0.01, 0.15) if arch == "SaaS API" else np.random.uniform(0.1, 0.3)
            logs.append({
                "attack_vector": a,
                "archetype": arch,
                "success_rate": success_rate,
                "detected_rate": np.random.uniform(0.8, 0.99),
                "business_impact": "Critical" if "Extraction" in a else "Medium"
            })
    return pd.DataFrame(logs)

def calculate_velocity_metrics(df):
    """Calculates governance efficiency metrics for display."""
    total = len(df)
    fast_lane = len(df[df['gate_decision'].str.contains('PASSED')])
    full_review = total - fast_lane
    
    # Simulating days-to-production (DTP)
    # Fast-lane: 5-15 days, Full-review: 45-90 days
    df['dtp'] = df.apply(lambda r: np.random.randint(5, 15) if 'PASSED' in r['gate_decision'] else np.random.randint(45, 90), axis=1)
    
    metrics = {
        "fast_lane_pct": (fast_lane / total) * 100,
        "avg_dtp_fast": df[df['gate_decision'].str.contains('PASSED')]['dtp'].mean(),
        "avg_dtp_full": df[~df['gate_decision'].str.contains('PASSED')]['dtp'].mean(),
        "fte_days_saved": fast_lane * 40 # Assuming 40 days saved per fast-lane auto-approval
    }
    return metrics

def generate_adversarial_prompt_data():
    """Generates synthetic time-series of adversarial prompt attacks."""
    dates = pd.date_range(start="2024-01-01", periods=60, freq='D')
    attack_types = ['Jailbreak (Direct)', 'Indirect Injection', 'Obfuscation', 'Translation Bypass']
    data = []
    
    for dt in dates:
        for atype in attack_types:
            attempts = np.random.randint(10, 100)
            # Higher success rate for Obfuscation/Translation in baseline
            base_success = 0.2 if atype in ['Obfuscation', 'Translation Bypass'] else 0.05
            successes = int(attempts * np.random.uniform(base_success * 0.5, base_success * 1.5))
            data.append({
                "date": dt,
                "attack_type": atype,
                "attempts": attempts,
                "successes": successes,
                "blocked": attempts - successes
            })
    return pd.DataFrame(data)

def generate_prompt_version_safety_scores():
    """Tracks safety vs utility across prompt iterations."""
    versions = [f"v{i}.0" for i in range(1, 6)]
    data = []
    for i, v in enumerate(versions):
        # Trade-off: As we harden the prompt, utility might drop slightly while safety rises
        utility = 95 - (i * 3) + np.random.uniform(-2, 2)
        safety = 40 + (i * 12) + np.random.uniform(-3, 3)
        latency = 150 + (i * 50) # Complex prompts take longer
        data.append({
            "version": v,
            "utility_score": utility,
            "safety_score": min(safety, 99.5),
            "latency_ms": latency,
            "tokens": 500 + (i * 200)
        })
    return pd.DataFrame(data)

def generate_rag_performance_data():
    """Generates synthetic time-series of RAG performance metrics (Faithfulness, Relevancy)."""
    dates = pd.date_range(start="2024-01-01", periods=60, freq='D')
    data = []
    for dt in dates:
        # Realistic fluctuations (weekend dips, random spikes)
        base_faith = 0.85 + 0.1 * np.sin(dt.dayofyear / 5)
        faithfulness = np.clip(base_faith + np.random.normal(0, 0.05), 0, 1)
        
        relevancy = np.clip(0.8 + 0.1 * np.cos(dt.dayofyear / 7) + np.random.normal(0, 0.05), 0, 1)
        
        # Context metrics
        context_precision = np.random.uniform(0.75, 0.98)
        context_recall = np.random.uniform(0.70, 0.96)
        
        # Spikes in hallucination when faithfulness drops
        hallucination_rate = max(0, (1 - faithfulness) * 0.8 + np.random.uniform(0, 0.1))
        
        data.append({
            "date": dt,
            "faithfulness": faithfulness,
            "answer_relevancy": relevancy,
            "context_precision": context_precision,
            "context_recall": context_recall,
            "context_entities_recall": np.random.uniform(0.6, 0.9),
            "answer_similarity": np.random.uniform(0.8, 0.98),
            "answer_correctness": np.random.uniform(0.75, 0.97),
            "hallucination_rate": hallucination_rate * 100 # Convert to %
        })
    return pd.DataFrame(data)

def generate_retrieval_integrity_logs():
    """Generates synthetic logs for corpus integrity monitoring."""
    corpora = ['HR Documents', 'Financial Reports', 'Product Specs', 'Customer Wiki']
    data = []
    for corp in corpora:
        total_chunks = np.random.randint(1000, 5000)
        poisoned_attempts = np.random.randint(0, 50)
        detected_poison = int(poisoned_attempts * np.random.uniform(0.8, 1.0))
        data.append({
            "corpus": corp,
            "total_chunks": total_chunks,
            "poisoned_attempts": poisoned_attempts,
            "detected_poison": detected_poison,
            "integrity_score": (1 - (poisoned_attempts - detected_poison) / total_chunks) * 100
        })
    return pd.DataFrame(data)

def generate_agentic_governance_data():
    """Generates synthetic logs for agentic autonomy and HITL triggers."""
    clusters = ['Internal Finance', 'Customer Support', 'IT Admin', 'HR Policy']
    data = []
    for c in clusters:
        total_actions = np.random.randint(500, 2000)
        # Blocked by tool limits (read-only vs transactional)
        blocked_tool = int(total_actions * np.random.uniform(0.1, 0.2))
        # Triggered HITL for high-value transactions
        hitl_triggered = int((total_actions - blocked_tool) * np.random.uniform(0.05, 0.15))
        # Autonomy Score: High value means more read/write freedom
        autonomy_read = np.random.uniform(0.8, 1.0)
        autonomy_transact = 0.9 if 'Finance' in c else 0.4
        autonomy_exec = 0.8 if 'IT' in c else 0.1
        
        data.append({
            "cluster": c,
            "total_actions": total_actions,
            "blocked_tool": blocked_tool,
            "hitl_triggered": hitl_triggered,
            "read_freedom": autonomy_read,
            "transaction_freedom": autonomy_transact,
            "exec_freedom": autonomy_exec
        })
    return pd.DataFrame(data)

def generate_killswitch_metrics():
    """Generates time-series of kill-switch activation velocity."""
    dates = pd.date_range(start="2024-01-01", periods=30, freq='D')
    data = []
    for dt in dates:
        anomalies = np.random.randint(1, 5)
        # Latency in seconds between detection and halt
        latency = np.random.uniform(0.5, 5.0) # Aiming for sub-5s response
        data.append({
            "date": dt,
            "anomalies_detected": anomalies,
            "halt_latency_sec": latency,
            "auto_halt_success": 100 if np.random.random() > 0.05 else 0
        })
    return pd.DataFrame(data)

def generate_accountability_profile_data():
    """Scores documentation completeness across 6 pillars (Deliverable C)."""
    categories = ['Performance', 'Ethics/Bias', 'Data Transparency', 'Security', 'Legal/IP', 'Archetype Logic']
    data = []
    # Comparing 2 different model risk tiers
    for tier in ['High Risk (T1)', 'Medium Risk (T2)']:
        for cat in categories:
            target = 95 if 'High' in tier else 80
            # Skewing: 'Ethics' and 'Security' are harder to document (higher gap)
            skew = 15 if cat in ['Ethics/Bias', 'Security'] else 5
            actual = target - np.random.uniform(skew, skew + 10)
            data.append({
                "Tier": tier,
                "Category": cat,
                "Target": target,
                "Actual": actual,
                "Gap": target - actual
            })
    return pd.DataFrame(data)

def generate_metadata_lineage_data():
    """Tracks the flow of model metadata into various audit artifacts."""
    # Nodes for Sankey: Inventory -> System Prompt -> Security Logs -> Audit Report -> Deliverable C
    nodes = ["Model Inventory", "Prompt Registry", "Security Logs", "System Card", "Audit Report", "Deliverable C"]
    sources = [0, 1, 2, 3, 3, 4] # Inventory -> System Card, Prompt -> System Card, etc.
    targets = [3, 3, 3, 4, 5, 5]
    values = [40, 30, 30, 60, 40, 100]
    return {"nodes": nodes, "sources": sources, "targets": targets, "values": values}

def generate_3d_risk_cube_data():
    """Multi-variate data for 3D risk portfolio navigation."""
    archetypes = ['SaaS', 'On-Prem', 'Hybrid', 'Edge']
    data = []
    for i in range(150):
        arch = np.random.choice(archetypes)
        # Create clusters: SaaS models are high complexity, Edge are low impact
        if arch == 'SaaS':
            impact = np.random.uniform(60, 100)
            complexity = np.random.uniform(70, 100)
        elif arch == 'Edge':
            impact = np.random.uniform(10, 40)
            complexity = np.random.uniform(20, 60)
        else:
            impact = np.random.uniform(30, 80)
            complexity = np.random.uniform(40, 90)
            
        prob = np.random.uniform(5, 50)
        risk_score = (impact * prob) / 100
        data.append({
            "model_id": f"AI-{1000+i}",
            "archetype": arch,
            "impact": impact,
            "complexity": complexity,
            "probability": prob,
            "risk_score": risk_score,
            "tier": "Tier 1: High" if risk_score > 25 else "Tier 2: Medium"
        })
    return pd.DataFrame(data)

def generate_validation_drift_data():
    """Simulates Primary vs Challenger model drift across 1000 test cases (§6.4)."""
    data = []
    # Primary model accuracy slowly drifting down, Challenger model stable
    for i in range(100):
        # Case ID
        cid = f"TEST-{2000+i}"
        # Primary response score (0.0 to 1.0)
        # Inducing some 'high risk' cases where Primary fails
        primary = np.random.uniform(0.6, 0.98)
        if i % 10 == 0: primary -= 0.3 # Simulated outlier/failure
        
        # Challenger response score (Independent Validation)
        challenger = np.random.uniform(0.8, 0.99)
        
        data.append({
            "test_id": cid,
            "primary_score": primary,
            "challenger_score": challenger,
            "variance": abs(primary - challenger),
            "status": "PASS" if abs(primary - challenger) < 0.15 else "FAIL (CONSISTENCY)"
        })
    return pd.DataFrame(data)

def generate_redteam_atlas_data():
    """Maps attack success rates to MITRE ATLAS Tactics."""
    tactics = ['Reconnaissance', 'Resource Development', 'Initial Access', 
               'ML Model Access', 'Execution', 'Persistence', 'Evasion', 
               'ML Model Inversion', 'Data Poisoning', 'Exfiltration']
    data = []
    for t in tactics:
        # Success probability varies by tactic
        base_success = np.random.uniform(5, 40)
        # ML-specific tactics are often higher risk in early stages
        if 'ML' in t or 'Data' in t: base_success += 20
        
        data.append({
            "Tactic": t,
            "Attack Volume": np.random.randint(100, 1000),
            "Success Rate": base_success,
            "Risk Level": "High" if base_success > 40 else "Medium"
        })
    return pd.DataFrame(data)

def generate_incident_timeline_data():
    """Generates time-series IR metrics for MTTD/MTTR analysis."""
    dates = pd.date_range(start="2024-01-01", periods=12, freq='M')
    data = []
    for dt in dates:
        # Improvements over time (efficiency gain)
        month_idx = (dt.year - 2024) * 12 + dt.month
        mttd = max(10, 120 - month_idx * 5 + np.random.uniform(0, 20)) # Minutes to detection
        mttr = max(60, 480 - month_idx * 15 + np.random.uniform(0, 50)) # Minutes to resolve
        
        data.append({
            "Month": dt.strftime('%b %Y'),
            "MTTD (Min)": mttd,
            "MTTR (Min)": mttr,
            "Severity_S1": np.random.randint(0, 3),
            "Severity_S2": np.random.randint(2, 8)
        })
    return pd.DataFrame(data)

def generate_fairness_bias_data():
    """Simulates Disparate Impact across protected classes (§17.11)."""
    groups = ['Gender (F)', 'Gender (M)', 'Age (Over 50)', 'Age (Under 50)', 
              'Minority (Group A)', 'Majority (Group B)']
    data = []
    for g in groups:
        # Target Parity is 1.0 (Fair)
        # Inducing some bias into specific groups
        parity = 1.0
        if 'F' in g or 'Over 50' in g or 'Minority' in g:
            parity -= np.random.uniform(0.1, 0.25) # Simulated Bias
        
        data.append({
            "Protected Class": g,
            "Selection Rate (%)": parity * 80, # Base rate 80%
            "Impact Ratio": parity,
            "Status": "Fair" if parity > 0.8 else "Bias Threshold Triggered"
        })
    return pd.DataFrame(data)

def generate_adversarial_surface_data():
    """Models Accuracy vs Perturbation Level (ε) across model versions."""
    noise_levels = np.linspace(0.0, 0.5, 20)
    versions = ['v1.0 (Base)', 'v1.1 (Hardened)', 'v2.0 (Adversarial Trained)']
    data = []
    for v in versions:
        for eps in noise_levels:
            # Base model falls off fast, Ad-Trained is robust
            if 'Base' in v:
                acc = max(0.1, 0.95 * np.exp(-10 * eps))
            elif 'Hardened' in v:
                acc = max(0.1, 0.95 * np.exp(-5 * eps))
            else: # Ad-Trained
                acc = max(0.5, 0.95 * np.exp(-2 * eps))
            
            data.append({
                "Noise Level (ε)": eps,
                "Model Version": v,
                "Accuracy": acc
            })
    return pd.DataFrame(data)

def generate_redteam_findings_history():
    """Generates remediation timelines for red-team vulnerabilities (§16.5)."""
    dates = pd.date_range(start="2024-01-01", periods=12, freq='M')
    data = []
    for dt in dates:
        open_vuls = np.random.randint(5, 20)
        closed_vuls = int(open_vuls * np.random.uniform(0.6, 1.2))
        avg_mttr = max(2, 30 - (dt.month * 2) + np.random.randint(-5, 5)) # Improving speed
        
        data.append({
            "Month": dt.strftime('%b %Y'),
            "Open Findings": open_vuls,
            "Resolved Findings": closed_vuls,
            "MTTR (Days)": avg_mttr,
            "SLA Compliance": 100 if avg_mttr <= 15 else 80
        })
    return pd.DataFrame(data)

def generate_attacker_capability_data():
    """Models Success Rate% by Attacker Strategy and MITRE ATLAS Tactic."""
    strategies = ['Script Kiddie', 'Professional', 'Advanced Persist (APT)']
    tactics = ['Reconnaissance', 'Initial Access', 'Execution', 'Evasion', 'Poisoning', 'Exfiltration']
    data = []
    for s in strategies:
        for t in tactics:
            # Capability multipliers
            mult = 1.0 if 'Script' in s else (2.5 if 'Prof' in s else 6.0)
            base_success = np.random.uniform(2, 8)
            success = min(100, base_success * mult)
            
            data.append({
                "Archetype": s,
                "Tactic": t,
                "Success Rate (%)": success,
                "Risk Index": success * 1.5
            })
    return pd.DataFrame(data)

def generate_incident_lineage_data():
    """Maps Causes -> Symptoms -> Business Impacts for RCA Sankey."""
    nodes = ['Prompt Injection', 'Training Data Poisoning', 'Model Drift', 'Insecure API', 
             'Hallucination', 'Privacy Leak', 'Toxicity Outbreak', 'Denial of Service',
             'Financial Loss', 'Brand Damage', 'Regulatory Fine', 'Operational Downtime']
    
    sources = [0, 0, 1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 7] # Mappings
    targets = [4, 5, 5, 6, 4, 6, 7, 8, 9, 9, 10, 10, 11]
    values = [40, 60, 30, 70, 50, 50, 80, 45, 55, 65, 35, 40, 60]
    
    return {"nodes": nodes, "sources": sources, "targets": targets, "values": values}

def generate_blast_radius_simulation():
    """Models user impact progression vs. Kill-Switch response time."""
    time_steps = np.linspace(0, 60, 20) # 60 minutes
    data = []
    for t in time_steps:
        # S-Curve of infection (Logistic growth)
        impacted_users = 1000 / (1 + 15 * np.exp(-0.15 * t))
        # Intervention at T=25
        curative_effect = 0
        if t > 25:
            curative_effect = 800 * (1 - np.exp(-0.2 * (t-25)))
        
        data.append({
            "Minutes Elapsed": t,
            "Total Impacted Users": max(0, impacted_users - curative_effect),
            "Protocol Status": "Detection" if t < 10 else ("Escalation" if t < 25 else "Recovery")
        })
    return pd.DataFrame(data)

def generate_german_credit_data():
    """Simulates the UCI German Credit dataset for fairness benchmarking."""
    n_samples = 1000
    # Features: Checking Account, Duration, Credit History, Credit Amount...
    # Sensitive Features: Sex (Male: 1, Female: 0), Age (Young: <25, Old: >=25)
    data = {
        'Sex': np.random.choice([0, 1], n_samples, p=[0.4, 0.6]),
        'Age_Under_25': np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),
        'Duration': np.random.randint(6, 48, n_samples),
        'Credit_Amount': np.random.randint(500, 15000, n_samples),
        'Savings': np.random.randint(0, 5, n_samples),
    }
    
    # Target: Credit Risk (1: Good, 0: Bad)
    # Bias injection: Approval rate higher for Men and Older applicants
    linear_comb = (
        0.5 * data['Sex'] + 
        0.3 * (1 - data['Age_Under_25']) + 
        0.1 * (data['Savings'] / 5) - 
        0.05 * (data['Duration'] / 12) + 
        np.random.normal(0, 0.1, n_samples)
    )
    data['Approved'] = (linear_comb > 0.4).astype(int)
    
    return pd.DataFrame(data)

def generate_fairness_bias_data():
    """Mock metrics for the bias assessment treemap/radar."""
    groups = ['Male', 'Female', 'Youth (<25)', 'Senior (>60)', 'Disability']
    data = []
    for g in groups:
        base_rate = 0.5 if 'F' in g or 'Y' in g else 0.8
        data.append({
            "Protected Class": g,
            "Selection Rate": base_rate + np.random.uniform(-0.05, 0.05),
            "Impact Ratio": (base_rate / 0.8),
            "Outcome Parity": "Violation" if (base_rate/0.8) < 0.8 else "Compliance"
        })
    return pd.DataFrame(data)

def run_fairness_mitigation_stages():
    """Simulation of Pre/In/Post Mitigation impact on Pareto Frontier."""
    stages = [
        {"Stage": "Baseline (Unmitigated)", "Accuracy": 0.85, "Fairness (DP Diff)": 0.25},
        {"Stage": "Pre-processing (CorrRemover)", "Accuracy": 0.83, "Fairness (DP Diff)": 0.15},
        {"Stage": "In-processing (ExpGradient)", "Accuracy": 0.79, "Fairness (DP Diff)": 0.05},
        {"Stage": "Post-processing (ThreshOpt)", "Accuracy": 0.81, "Fairness (DP Diff)": 0.08}
    ]
    return pd.DataFrame(stages)

def generate_exhaustive_fairness_metrics():
    """Simulates the full Fairlearn metric registry disaggregated by group."""
    groups = ['Male', 'Female', 'Youth (<25)', 'Senior (>60)']
    metrics = [
        'Selection Rate', 'Accuracy', 'Precision', 'Recall', 
        'False Positive Rate', 'False Negative Rate'
    ]
    data = []
    for g in groups:
        for m in metrics:
            base = 0.8 if 'M' in g or 'S' in g else 0.6
            val = base + np.random.uniform(-0.1, 0.1)
            data.append({"Group": g, "Metric": m, "Value": val})
    return pd.DataFrame(data)

def generate_mitigation_lifecycle_registry():
    """Comparative registry of all fairness metrics across the 4 stages of mitigation."""
    stages = ['Baseline', 'Pre-processed (CorrRemover)', 'In-processed (ExpGrad)', 'Post-processed (ThreshOpt)']
    metrics = [
        'Demographic Parity Diff', 'Demographic Parity Ratio', 
        'Equalized Odds Diff', 'Equalized Odds Ratio',
        'FPR Difference', 'FNR Difference'
    ]
    
    data = []
    for s in stages:
        # Success logic: mitigation reduces diffs (gets closer to 0) and increases ratios (closer to 1)
        success_factor = 1.0 if s == 'Baseline' else (0.5 if 'Pre' in s else (0.2 if 'In' in s else 0.3))
        for m in metrics:
            if 'Diff' in m:
                val = 0.25 * success_factor + np.random.uniform(0, 0.05)
            else: # Ratio
                val = min(1.0, 0.7 + (0.3 * (1-success_factor)) + np.random.uniform(-0.05, 0.05))
            
            data.append({
                "Mitigation Stage": s,
                "Fairness Metric": m,
                "Value": val,
                "Accuracy (%)": (0.85 - (1-success_factor)*0.08) * 100
            })
    return pd.DataFrame(data)

def generate_ragas_metrics():
    """Simulates the exhaustive 9-metric RAGAS suite for deep diagnostic auditing."""
    metrics = [
        'Faithfulness', 'Answer Relevancy', 'Context Precision', 'Context Recall',
        'Context Entities Recall', 'Answer Correctness', 'Answer Semantic Similarity',
        'Noise Sensitivity', 'Context Utilization'
    ]
    data = []
    for m in metrics:
        # Simulate a specific 'High-Recall/Low-Faithfulness' failure pattern
        data.append({
            "Metric": m,
            "Baseline Score": np.random.uniform(0.60, 0.70) if m != 'Noise Sensitivity' else 0.45,
            "Optimized Score": np.random.uniform(0.85, 0.95),
            "SLA Threshold": 0.85 if m in ['Faithfulness', 'Context Recall'] else 0.80
        })
    return pd.DataFrame(data)

def generate_rag_failure_trace():
    """Worked-out case study: Kill-switch protocol hallucination analysis."""
    audit_data = [
        {"Claim": "Tier 3 requires AIRC notification", "Source": "Policy Doc §10.4", "Faithfulness": 0.98, "Relevance": 0.95},
        {"Claim": "Mandatory kill-switch within 15 min", "Source": "MISSING in Context", "Faithfulness": 0.05, "Relevance": 0.90},
        {"Claim": "Immediate quarantine of model weights", "Source": "Policy Doc §12.1", "Faithfulness": 0.92, "Relevance": 0.85}
    ]
    return pd.DataFrame(audit_data)


def generate_retrieval_graph_data():
    """Node/Link structure for a RAG Knowledge Graph retrieval path."""
    nodes = [
        {"id": "Query", "type": "input", "label": "How is risk managed?"},
        {"id": "Doc_1", "type": "document", "label": "ISO 31000 Context"},
        {"id": "Doc_2", "type": "document", "label": "NIST AI RMF"},
        {"id": "Concept_A", "type": "concept", "label": "Likelihood"},
        {"id": "Concept_B", "type": "concept", "label": "Impact"},
        {"id": "Concept_C", "type": "concept", "label": "Mitigation"},
        {"id": "Answer", "type": "output", "label": "Risk is Likelihood x Impact"}
    ]
    links = [
        {"source": "Query", "target": "Doc_1", "weight": 0.8},
        {"source": "Query", "target": "Doc_2", "weight": 0.9},
        {"source": "Doc_1", "target": "Concept_A", "weight": 0.7},
        {"source": "Doc_2", "target": "Concept_B", "weight": 0.85},
        {"source": "Concept_A", "target": "Answer", "weight": 0.9},
        {"source": "Concept_B", "target": "Answer", "weight": 0.9},
        {"source": "Concept_C", "target": "Answer", "weight": 0.6}
    ]
    return {"nodes": nodes, "links": links}

def generate_ai_sbom_graph_data():
    """Generates multi-tier AI-SBOM lineage for a foundation model supply chain (Expert Edition)."""
    nodes = [
        "Meta (Llama-3-70B)", "Internal Curation §A", "Hugging Face (Repo)", 
        "LoRA Adapter (Safetensors)", "LoRA Adapter (Pickle)", "8-bit Quantization", "Inference Endpoint"
    ]
    # Flow: Meta -> HF -> Curation -> Adapters -> Quant -> Prod
    sources = [0, 2, 1, 1, 3, 4, 5]
    targets = [2, 1, 3, 4, 5, 5, 6]
    values = [1.0, 1.0, 0.7, 0.3, 0.7, 0.2, 0.9]
    return {"nodes": nodes, "sources": sources, "targets": targets, "values": values}

def generate_vulnerability_vex_registry():
    """Expert AI-specific CVE registry with VEX justifications."""
    data = [
        {"Component": "PyTorch v2.1", "CVE": "CVE-2024-1234", "Severity": 9.8, "VEX_Status": "Fixed", "Justification": "Patched in CI/CD build #442"},
        {"Component": "Transformers", "CVE": "CVE-2023-6730", "Severity": 8.5, "VEX_Status": "Remediated", "Justification": "Migrated to v4.36.2 (Safe)"},
        {"Component": "LangChain", "CVE": "CVE-2024-5678", "Severity": 7.2, "VEX_Status": "Not Affected", "Justification": "Vulnerable RAG module disabled §10.2"},
        {"Component": "Internal Adapter", "Type": "Pickle", "Severity": 9.0, "VEX_Status": "Action Required", "Justification": "Insecure serialization detected"}
    ]
    # Synthetic explode for Sunburst
    sun_data = [
        {"Layer": "Infrastructure", "Comp": "Azure GPU Cluster", "Severity": 2.0},
        {"Layer": "Infrastructure", "Comp": "Docker Registry", "Severity": 4.5},
        {"Layer": "Library", "Comp": "PyTorch", "Severity": 9.8},
        {"Layer": "Library", "Comp": "Transformers", "Severity": 7.5},
        {"Layer": "Model", "Comp": "Llama-3 Weights", "Severity": 1.0},
        {"Layer": "Model", "Comp": "Pickle Adapter", "Severity": 9.0},
        {"Layer": "Data", "Comp": "Training Corra", "Severity": 3.2}
    ]
    return pd.DataFrame(data), pd.DataFrame(sun_data)

def generate_provenance_audit_trail():
    """Chain of custody SHA-256 verification history."""
    data = [
        {"Environment": "Development", "Timestamp": "2024-01-10", "SHA-256": "8f3a...b12", "VerifiedBy": "CI/CD Pipeline", "Status": "Valid"},
        {"Environment": "Staging", "Timestamp": "2024-01-15", "SHA-256": "8f3a...b12", "VerifiedBy": "App-Sec SecOps", "Status": "Valid"},
        {"Environment": "Production", "Timestamp": "2024-01-20", "SHA-256": "8f3a...b12", "VerifiedBy": "Hardware Enclave (TPM)", "Status": "Valid"}
    ]
    return pd.DataFrame(data)

def generate_expert_multimodal_portfolio_data():
    """Generates a high-fidelity audit of the enterprise's multi-modal foundation portfolio."""
    data = [
        # Vision
        {"Modality": "Vision", "Model": "SAM (Segment Anything)", "Provider": "Meta", "License": "Apache 2.0", 
         "Lineage": "SA-1B Dataset (1B masks)", "Integrity_SHA": "8f3...a", "MSC_Status": "Validated"},
        {"Modality": "Vision", "Model": "ViT (Base)", "Provider": "Google", "License": "Apache 2.0", 
         "Lineage": "ImageNet-21k", "Integrity_SHA": "bc1...d", "MSC_Status": "Monitored"},
        # Audio
        {"Modality": "Audio", "Model": "Whisper v3", "Provider": "OpenAI", "License": "MIT", 
         "Lineage": "680k hrs Multi-lingual", "Integrity_SHA": "ff2...1", "MSC_Status": "Validated"},
        # Language
        {"Modality": "Language", "Model": "Llama-3-70B", "Provider": "Meta", "License": "Llama-3 Community", 
         "Lineage": "15T tokens (C4/CommonCrawl)", "Integrity_SHA": "ab4...e", "MSC_Status": "Audit Required"},
        {"Modality": "Language", "Model": "Mistral-7B", "Provider": "Mistral AI", "License": "Apache 2.0", 
         "Lineage": "Curation v2 (Internal)", "Integrity_SHA": "d98...2", "MSC_Status": "Validated"},
        # Embedding
        {"Modality": "Embedding", "Model": "BGE-v1.5", "Provider": "BAAI", "License": "MIT", 
         "Lineage": "Multi-vector retrieval corp.", "Integrity_SHA": "e77...f", "MSC_Status": "Secure"}
    ]
    return pd.DataFrame(data)

def generate_expert_regulatory_register_data():
    """Generates a high-fidelity mapping of enterprise AI systems to global regulations."""
    # Data for the Risk Register
    risk_data = [
        {"System": "HR-Genie (Recruitment)", "Tier": "1 (High)", "Regulation": "EU AI Act (Annex III)", "Primary_Risk": "Bias / Discrimination", "Status": "Mitigated", "FRIA_Status": "Complete"},
        {"System": "Finance-Bot (Trading)", "Tier": "1 (Critical)", "Regulation": "SEC / SR 11-7", "Primary_Risk": "Market Stability", "Status": "Monitored", "FRIA_Status": "N/A"},
        {"System": "Customer-Support (RAG)", "Tier": "2 (Medium)", "Regulation": "GDPR (Art 22)", "Primary_Risk": "Hallucination", "Status": "In-Progress", "FRIA_Status": "N/A"},
        {"System": "Legal-Researcher", "Tier": "3 (Low)", "Regulation": "NIST AI RMF", "Primary_Risk": "Privacy Leakage", "Status": "Validated", "FRIA_Status": "N/A"}
    ]
    
    # Data for the Maturity Radar
    maturity_data = {
        "Framework": ["NIST AI RMF", "EU AI Act", "GDPR", "ISO 42001", "Audit Ready"],
        "Current": [0.8, 0.4, 0.9, 0.3, 0.6],
        "Target": [1.0, 0.9, 1.0, 0.8, 1.0]
    }
    
    return pd.DataFrame(risk_data), pd.DataFrame(maturity_data)

def generate_expert_board_kpi_data():
    """Generates a high-fidelity executive dataset for the Multinational Corporate Dashboard."""
    # Scorecard Indicators
    scorecard_data = {"Overall_Compliance": 84, "Safety_Score": 92, "Inventory_Complete": 100, "Risk_Mitigated": 78}
    
    # Regional Treemap Data
    treemap_data = [
        {"Region": "AMER", "BU": "Finance", "System": "Trading-Bot", "Usage": 5000, "Tier": "1 (Critical)"},
        {"Region": "AMER", "BU": "Retail", "System": "Recommender", "Usage": 8000, "Tier": "2 (Medium)"},
        {"Region": "EMEA", "BU": "HR", "System": "Recruiter-AI", "Usage": 2000, "Tier": "1 (High)"},
        {"Region": "EMEA", "BU": "Legal", "System": "Doc-Review", "Usage": 3000, "Tier": "2 (Medium)"},
        {"Region": "APAC", "BU": "Ops", "System": "Supply-Chain-AI", "Usage": 6000, "Tier": "1 (High)"},
        {"Region": "APAC", "BU": "Tech", "System": "Code-Copilot", "Usage": 9000, "Tier": "3 (Low)"}
    ]
    
    # Incident Timeline (Red Flags)
    incident_data = [
        {"Month": "Jan", "S1": 0, "S2": 2, "S3": 5, "S4": 12},
        {"Month": "Feb", "S1": 1, "S2": 1, "S3": 8, "S4": 15},
        {"Month": "Mar", "S1": 0, "S2": 3, "S3": 4, "S4": 10}
    ]
    
    # Domain Progress
    domain_data = {
        "Domain": ["Strategy", "Data", "Model", "Prompt", "RAG", "Agentic", "Supply Chain", "Monitoring"],
        "Progress": [95, 88, 82, 75, 70, 65, 80, 90]
    }
    
    return scorecard_data, pd.DataFrame(treemap_data), pd.DataFrame(incident_data), pd.DataFrame(domain_data)





# --- VISUAL STYLING ENGINE ---

def inject_framework_style():
    """Injects global CSS for an executive framework aesthetic."""
    style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        .grc-markdown h1 { color: #0f172a; font-family: 'Inter', sans-serif; font-weight: 700; border-bottom: 2px solid #2dd4bf; padding-bottom: 10px; }
        .grc-markdown h2 { color: #1e293b; font-family: 'Inter', sans-serif; font-weight: 600; margin-top: 30px; }
        .grc-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; margin: 15px 0; font-family: 'Inter', sans-serif; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .grc-table { width: 100%; border-collapse: collapse; margin: 20px 0; font-family: 'Inter', sans-serif; }
        .grc-table th { background: #0f172a; color: white; padding: 12px; text-align: left; font-size: 0.9em; }
        .grc-table td { border-bottom: 1px solid #e2e8f0; padding: 12px; color: #334155; font-size: 0.85em; }
    </style>
    """
    display(HTML(style))

def display_deliverable_anchor(letter, title):
    """Renders a deliverable marker for framework alignment."""
    html = f"""
    <div style="background: #0f172a; color: white; padding: 15px 25px; border-radius: 12px; display: inline-flex; align-items: center; gap: 20px; font-family: 'Inter', sans-serif; margin: 20px 0; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">
        <div style="background: #2dd4bf; color: #0f172a; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: 800; font-size: 1.4em;">{letter}</div>
        <div>
            <div style="font-size: 0.75em; color: #94a3b8; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 600;">Core Deliverable</div>
            <div style="font-size: 1.2em; font-weight: 700; color: #f8fafc;">{title}</div>
        </div>
    </div>
    """
    display(HTML(html))

# --- DASHBOARDS & CHARTS ---

def display_ownership_heatmap(df):
    """Visualizes ownership coverage across domains to highlight unassigned roles."""
    roles = ['business_owner', 'model_owner', 'system_owner']
    coverage = []
    
    for domain in DOMAINS:
        domain_df = df[df['domain'] == domain]
        for role in roles:
            # Check for non-null assignments
            count = domain_df[role].notna().sum()
            total = len(domain_df)
            pct = (count / total) * 100 if total > 0 else 0
            coverage.append({'Domain': domain, 'Accountability Role': role.replace('_', ' ').title(), 'Coverage %': pct})
    
    coverage_df = pd.DataFrame(coverage)
    fig = px.density_heatmap(
        coverage_df, x="Accountability Role", y="Domain", z="Coverage %",
        color_continuous_scale="RdYlGn",
        title="Enterprise Accountability Matrix: Ownership Coverage by Domain",
        labels={"Coverage %": "Coverage (%)"}
    )
    fig.update_layout(template="plotly_white", font_family="Inter")
    fig.show()

def display_accountability_sankey(df):
    """Maps the flow of accountability from Business Units -> Owners -> Committees."""
    # Simulation logic for flow
    bu_to_role = df.groupby(['domain']).size().reset_index(name='count')
    # Filter for high/elevated risk to show the Risk Committee flow
    high_risk = df[df['risk_tier'].isin(['Tier 1: High', 'Tier 2: Elevated'])]
    
    # 1. Define nodes
    nodes = DOMAINS + ["Business Owners", "Model Owners", "System Owners"] + ["AI Gov Office", "AI Risk Committee", "Exec AI Council"]
    node_map = {n: i for i, n in enumerate(nodes)}
    
    links = []
    # Flow BU -> Business Owners
    for domain in DOMAINS:
        count = len(df[df['domain'] == domain])
        links.append({'source': node_map[domain], 'target': node_map["Business Owners"], 'value': count, 'color': 'rgba(148, 163, 184, 0.2)'})
    
    # Flow BU -> Technical Owners (Model/System)
    for domain in DOMAINS:
        count = len(df[df['domain'] == domain])
        links.append({'source': node_map[domain], 'target': node_map["Model Owners"], 'value': count/2, 'color': 'rgba(148, 163, 184, 0.2)'})
        links.append({'source': node_map[domain], 'target': node_map["System Owners"], 'value': count/2, 'color': 'rgba(148, 163, 184, 0.2)'})
        
    # Flow Owners -> Committees based on Risk Tier
    t34_count = len(df[df['risk_tier'].isin(['Tier 3: Standard', 'Tier 4: Low'])])
    t12_count = len(df[df['risk_tier'].isin(['Tier 1: High', 'Tier 2: Elevated'])])
    
    links.append({'source': node_map["Business Owners"], 'target': node_map["AI Gov Office"], 'value': t34_count, 'color': 'rgba(34, 197, 94, 0.4)'})
    links.append({'source': node_map["Business Owners"], 'target': node_map["AI Risk Committee"], 'value': t12_count, 'color': 'rgba(239, 68, 68, 0.4)'})
    links.append({'source': node_map["AI Risk Committee"], 'target': node_map["Exec AI Council"], 'value': t12_count/4, 'color': 'rgba(15, 23, 42, 0.4)'})

    fig = go.Figure(go.Sankey(node=dict(label=nodes, color="#0f172a"), link=dict(source=[l['source'] for l in links], target=[l['target'] for l in links], value=[l['value'] for l in links], color=[l['color'] for l in links])))
    fig.update_layout(title_text="Chain of Responsibility: Business Unit → Defined Roles → Reporting Committees", template="plotly_white", font_family="Inter")
    fig.show()

def display_liability_card(total_liability, high_risk_count, total_use_cases):
    html = f"""<div class="grc-card" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white; border: none;"><h2 style="color: #2dd4bf; margin-top: 0; font-family: 'Inter';">Executive Risk Exposure Statement</h2><div style="display: flex; justify-content: space-between;"><div><p style="color: #94a3b8; margin-bottom: 5px;">Total Unpriced Liability</p><h1 style="font-size: 3em; margin: 0; color: #fbbf24;">${total_liability:,.0f}</h1></div><div style="text-align: right;"><p style="color: #94a3b8; margin-bottom: 5px;">High Risk Concentration</p><h2 style="font-size: 2em; margin: 0;">{high_risk_count} / {total_use_cases}</h2><p style="font-size: 0.8em; color: #2dd4bf;">{ (high_risk_count/total_use_cases)*100:.1f}% of Estate</p></div></div></div>"""
    display(HTML(html))

def display_velocity_stats(df):
    total = len(df); fast_lane = len(df[df['gate_decision'].str.contains('PASSED')]); rejected = len(df[df['gate_decision'].str.contains('REJECTED')]); days_saved = (fast_lane * 45) + (rejected * 10)
    html = f"""<div style="background: #0f172a; padding: 25px; border-radius: 12px; font-family: 'Inter'; color: white; margin: 20px 0;"><div style="color: #2dd4bf; font-weight: 700; margin-bottom: 15px; font-size: 1.1em;">GOVERNANCE VELOCITY (Part VIII §8.3)</div><div style="display: flex; gap: 50px;"><div><div style="color: #94a3b8; font-size: 0.8em;">AUTO-APPROVALS</div><div style="font-size: 2em; font-weight: 700;">{fast_lane}</div></div><div><div style="color: #94a3b8; font-size: 0.8em;">FTE DAYS SAVED</div><div style="font-size: 2em; font-weight: 700; color: #2dd4bf;">{days_saved:,}</div></div><div><div style="color: #94a3b8; font-size: 0.8em;">EFFICIENCY GAIN</div><div style="font-size: 2em; font-weight: 700;">{ (fast_lane/total)*100:.1f}%</div></div></div></div>"""
    display(HTML(html))

def display_diagnostic_checklist(diagnostic_data):
    rows = "".join([f"<tr><td><b>{item['question']}</b></td><td style='color: #991b1b; background: #fef2f2;'>{item['over']}</td><td style='color: #166534; background: #f0fdf4;'>{item['under']}</td><td style='background: #f8fafc; font-style: italic;'>{item['action']}</td></tr>" for item in diagnostic_data])
    display(HTML(f'<table class="grc-table"><thead><tr><th>DIAGNOSTIC QUESTION</th><th>OVER-GOVERNANCE INDICATOR</th><th>UNDER-GOVERNANCE INDICATOR</th><th>CORRECTIVE ACTION</th></tr></thead><tbody>{rows}</tbody></table>'))

def display_violation_gallery(violations):
    cards = "".join([f"<div style='flex: 1; min-width: 300px; background: white; border: 1px solid #e2e8f0; border-top: 5px solid {'#ef4444' if 'Tier 0' in v['tier'] else '#f59e0b'}; padding: 15px; border-radius: 8px; margin: 10px; font-family: 'Inter';'><div style='color: {'#ef4444' if 'Tier 0' in v['tier'] else '#f59e0b'}; font-weight: 700; font-size: 0.9em; margin-bottom: 10px;'>{v['tier']}</div><h4 style='margin: 0;'>{v['name']}</h4><div style='font-size: 0.8em; color: #64748b; margin: 10px 0;'>{v['scenario']}</div><div style='background: #f1f5f9; padding: 10px; border-radius: 4px; font-size: 0.8em;'><b>Gap:</b> {v['gap']}</div><div style='margin-top: 10px; font-size: 0.8em; font-weight: 600; color: #059669;'>Path: {v['path']}</div></div>" for v in violations])
    display(HTML(f'<div style="display: flex; flex-wrap: wrap;">{cards}</div>'))

def display_intake_sankey(df):
    nodes = sorted(df['domain'].unique().tolist()) + sorted(df['risk_tier'].unique().tolist()) + sorted(df['gate_decision'].unique().tolist()); node_map = {n: i for i, n in enumerate(nodes)}; links = []
    for (s, t), v in df.groupby(['domain', 'risk_tier']).size().items(): links.append({'source': node_map[s], 'target': node_map[t], 'value': v, 'color': 'rgba(148, 163, 184, 0.2)'})
    for (s, t), v in df.groupby(['risk_tier', 'gate_decision']).size().items(): links.append({'source': node_map[s], 'target': node_map[t], 'value': v, 'color': 'rgba(239, 68, 68, 0.5)' if 'REJECTED' in t else 'rgba(34, 197, 94, 0.5)'})
    fig = go.Figure(go.Sankey(node=dict(label=[n.split(':')[-1].strip() for n in nodes], color="#0f172a"), link=dict(source=[l['source'] for l in links], target=[l['target'] for l in links], value=[l['value'] for l in links], color=[l['color'] for l in links])))
    fig.update_layout(title_text="Intake Flow", template="plotly_white", font_family="Inter"); fig.show()

def display_app_catalog_sunburst(df):
    """Hierarchy of Capability -> Model -> App for the Internal App Store."""
    fig = px.sunburst(
        df, path=['compliance_status', 'capability', 'base_model'], 
        values='usage_count',
        color='compliance_status',
        color_discrete_map={
            "Vetted": "#22c55e",
            "Pending Review": "#f59e0b",
            "Prohibited": "#ef4444",
            "Retired": "#64748b"
        },
        title="Enterprise AI App Store: Capability & Model Distribution"
    )
    fig.update_layout(template="plotly_white", font_family="Inter")
    fig.show()

def display_capability_risk_matrix(df):
    """Strategic view of the App Catalog Risk Profile."""
    fig = px.scatter(
        df, x="capability", y="risk_tier",
        size="usage_count", color="compliance_status",
        hover_name="app_name",
        title="Strategic Catalog Alignment: Risk Tier vs. Capability Grouping",
        color_discrete_map={
            "Vetted": "#22c55e",
            "Pending Review": "#f59e0b",
            "Prohibited": "#ef4444",
            "Retired": "#64748b"
        }
    )
    fig.update_layout(template="plotly_white", font_family="Inter")
    fig.show()

def display_risk_taxonomy_sunburst(df):
    """Visualizes the hierarchy of Risk Categories and specific failures."""
    fig = px.sunburst(
        df, path=['Category', 'Impact', 'Risk'],
        color='Category',
        title="Master Risk Taxonomy (Part IV §4.2)",
    )
    fig.update_layout(template="plotly_white", font_family="Inter")
    fig.show()

def display_risk_radar(archetype_profiles):
    """Compares risk profiles (Security, Privacy, etc.) across different AI Archetypes."""
    fig = go.Figure()
    categories = ['Security', 'Privacy', 'Fairness', 'Safety', 'Compliance', 'Operational']
    for profile in archetype_profiles:
        fig.add_trace(go.Scatterpolar(
            r=[profile[c] for c in categories] + [profile[categories[0]]],
            theta=categories + [categories[0]],
            fill='toself',
            name=profile['name']
        ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title="Risk Archetype DNA Comparison",
        template="plotly_white", font_family="Inter"
    )
    fig.show()

def display_residual_risk_heatmap(df):
    """5x5 Matrix of Inherent vs. Residual risk."""
    z = [[1, 2, 4, 8, 10], [2, 4, 6, 8, 12], [4, 6, 8, 10, 15], [8, 10, 12, 15, 20], [10, 12, 15, 20, 25]]
    fig = px.imshow(
        z, x=['S4', 'S3', 'S2', 'S1', 'Critical'], 
        y=['Rare', 'Unlikely', 'Possible', 'Likely', 'Frequent'],
        labels=dict(x="Impact Severity", y="Likelihood", color="Risk Events"),
        color_continuous_scale='YlOrRd',
        title="Executive Heatmap: Inherent vs. Residual Portfolio Risk"
    )
    fig.update_layout(template="plotly_white", font_family="Inter")
    fig.show()

def display_governance_paved_road(df):
    """High-impact Parallel Categories visual for interactive lifecycle exploration."""
    plot_df = df[['domain', 'archetype', 'risk_tier', 'gate_decision']].copy()
    plot_df['gate_decision'] = plot_df['gate_decision'].apply(lambda x: "Fast-Lane" if "PASSED" in x else ("Rejected" if "REJECTED" in x else "Full-Review"))
    
    fig = px.parallel_categories(
        plot_df, 
        dimensions=['domain', 'archetype', 'risk_tier', 'gate_decision'],
        labels={'domain': 'Domain', 'archetype': 'Architecture', 'risk_tier': 'Risk Tier', 'gate_decision': 'Gate Path'},
        title="The Paved Road: Lifecycle Flow & Automated Triage"
    )
    fig.update_layout(template="plotly_white", font_family="Inter")
    fig.show()

def display_velocity_gauges(metrics):
    """Interactive Gauges for governance efficiency."""
    from plotly.subplots import make_subplots
    fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]])
    
    fig.add_trace(go.Indicator(
        mode="gauge+number", value=metrics['fast_lane_pct'],
        title={'text': "Fast-Lane Adoption %"},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#2dd4bf"}},
        domain={'x': [0, 0.3], 'y': [0, 1]}
    ), row=1, col=1)
    
    fig.add_trace(go.Indicator(
        mode="number+delta", value=metrics['avg_dtp_fast'],
        delta={'reference': metrics['avg_dtp_full'], 'relative': True, 'position': "bottom", 'increasing': {'color': "#ef4444"}, 'decreasing': {'color': "#22c55e"}},
        title={'text': "Days to Prod (Fast)"},
        domain={'x': [0.35, 0.65], 'y': [0, 1]}
    ), row=1, col=2)
    
    fig.add_trace(go.Indicator(
        mode="number", value=metrics['fte_days_saved'],
        title={'text': "FTE Days Recycled"},
        number={'suffix': "d", 'valueformat': ",.0f"},
        domain={'x': [0.7, 1], 'y': [0, 1]}
    ), row=1, col=3)
    
    fig.update_layout(height=400, template="plotly_white", font_family="Inter")
    fig.show()

def display_transformation_waterfall(df):
    """Waterfall chart showing data shrinkage through cleaning stages (DAT-03)."""
    total_raw = df['raw_count'].sum()
    total_scrubbed = df['scrubbed_count'].sum()
    diff = total_raw - total_scrubbed
    
    fig = go.Figure(go.Waterfall(
        name = "Data Minimization", orientation = "v",
        measure = ["absolute", "relative", "total"],
        x = ["Raw Ingress", "Toxicity/PII Scrubbing", "Training Ready Set"],
        textposition = "outside",
        text = [f"{total_raw/1e6:.1f}M", f"-{diff/1e6:.1f}M", f"{total_scrubbed/1e6:.1f}M"],
        y = [total_raw, -diff, total_scrubbed],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    fig.update_layout(title = "Data Minimization Attrition Depth (Control DAT-03)", template="plotly_white", font_family="Inter")
    fig.show()

def display_security_vault_dashboard(df):
    """High-impact dashboard for Model Security Posture (Deliverable G)."""
    fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]])
    
    avg_enc = df['encryption_at_rest'].mean()
    avg_tamper = df['tamper_evidence_msc_03'].mean()
    avg_weight = df['weight_protection_sec_01'].mean()
    
    fig.add_trace(go.Indicator(
        mode = "gauge+number", value = avg_enc, title = {'text': "Encryption<br>Status", 'font': {'size': 18}},
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#0f172a"}},
        domain = {'x': [0, 0.28], 'y': [0, 1]}
    ), row=1, col=1)
    
    fig.add_trace(go.Indicator(
        mode = "gauge+number", value = avg_tamper, title = {'text': "Tamper Evidence<br>(MSC-03)", 'font': {'size': 18}},
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#2dd4bf"}},
        domain = {'x': [0.36, 0.64], 'y': [0, 1]}
    ), row=1, col=2)
    
    fig.add_trace(go.Indicator(
        mode = "gauge+number", value = avg_weight, title = {'text': "Weight Protection<br>(SEC-01)", 'font': {'size': 18}},
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#38bdf8"}},
        domain = {'x': [0.72, 1], 'y': [0, 1]}
    ), row=1, col=3)
    
    fig.update_layout(height=400, width=1100, template="plotly_white", font_family="Inter")
    fig.show()

def display_adversarial_radar(metrics):
    """Radar chart for Red-Team results (§12.1)."""
    fig = go.Figure()
    categories = ['Injection', 'Jailbreak', 'Extraction', 'PII-Exfil', 'Backdoor']
    
    for m in metrics:
        fig.add_trace(go.Scatterpolar(
            r=[m[c] for c in categories], theta=categories, fill='toself', name=m['name']
        ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        title="Adversarial Robustness Portfolio (SEC-04)",
        template="plotly_white", font_family="Inter"
    )
    fig.show()

def display_security_vulnerability_waterfall(df):
    """Volumetric proof of defense-in-depth security (Audit-Ready)."""
    # Simulate attrition across layers
    total_attempts = df['attempts'].sum()
    network_blocked = int(total_attempts * 0.7) # Simulated 70% network block
    iam_blocked = int((total_attempts - network_blocked) * 0.8) # 80% of remainder
    encryption_blocked = int((total_attempts - network_blocked - iam_blocked) * 0.95)
    
    residual = total_attempts - network_blocked - iam_blocked - encryption_blocked
    
    fig = go.Figure(go.Waterfall(
        name = "Attrition", orientation = "v",
        measure = ["relative", "relative", "relative", "relative", "total"],
        x = ["Brute Force Attempts", "Network Perimeter", "IAM/RBAC Gate", "Weight Encryption", "Residual Risk"],
        textposition = "outside",
        text = [f"{total_attempts}", f"-{network_blocked}", f"-{iam_blocked}", f"-{encryption_blocked}", f"{residual}"],
        y = [total_attempts, -network_blocked, -iam_blocked, -encryption_blocked, residual],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    fig.update_layout(title = "Security Attrition Waterfall: Defense-in-Depth (Domain 3)", template="plotly_white", font_family="Inter")
    fig.show()

def display_resilience_heatmap(df):
    """Strategic mapping of attack success rates across archetypes."""
    # Pivot red-team logs
    pivot_df = df.pivot(index='attack_vector', columns='archetype', values='success_rate')
    fig = px.imshow(pivot_df, 
                    labels=dict(x="Deployment Archetype", y="Attack Vector", color="Success Rate"),
                    color_continuous_scale="Reds",
                    text_auto=".1%")
    fig.update_layout(title="Adversarial Resilience Matrix: Vector x Archetype (Part XII §12.1)", font_family="Inter")
    fig.show()

def display_defense_velocity_dashboard(df):
    """Longitudinal analysis of Revocation Velocity and Detection Latency."""
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Attempt Detection Latency (ms)", "Automated Revocation Success Rate"))
    
    fig.add_trace(go.Scatter(x=df['date'], y=df['revocation_latency_ms'], name="Latency", line=dict(color='#2dd4bf', width=2)), row=1, col=1)
    
    success_rate = (df['blocked'] / df['attempts']) * 100
    fig.add_trace(go.Bar(x=df['date'], y=success_rate, name="Stop Rate", marker_color='#0f172a'), row=1, col=2)
    
    fig.update_layout(title="Active Defense Velocity: Monitoring Signal G.4 (Deliverable E)", template="plotly_white", font_family="Inter")
    fig.show()

def display_prompt_safety_attrition_waterfall(df):
    """Volumetric proof of prompt security gate effectiveness (PRM-04)."""
    # Simulate attrition across prompt layers
    total_attempts = df['attempts'].sum()
    system_prompt_blocked = int(total_attempts * 0.65) # 65% blocked by system instructions
    guardrail_blocked = int((total_attempts - system_prompt_blocked) * 0.85) # 85% of remainder
    semantic_blocked = int((total_attempts - system_prompt_blocked - guardrail_blocked) * 0.9)
    
    residual = total_attempts - system_prompt_blocked - guardrail_blocked - semantic_blocked
    
    fig = go.Figure(go.Waterfall(
        name = "Prompt Defense", orientation = "v",
        measure = ["relative", "relative", "relative", "relative", "total"],
        x = ["Adversarial Attempts", "System Prompt Logic", "Guardrail API", "Semantic Screening", "Residual Risk"],
        textposition = "outside",
        text = [f"{total_attempts}", f"-{system_prompt_blocked}", f"-{guardrail_blocked}", f"-{semantic_blocked}", f"{residual}"],
        y = [total_attempts, -system_prompt_blocked, -guardrail_blocked, -semantic_blocked, residual],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    fig.update_layout(title = "Prompt Defense Attrition: Multi-Gate Security (PRM-04)", template="plotly_white", font_family="Inter")
    fig.show()

def display_prompt_drift_analysis(df):
    """Correlation analysis of Prompt Safety vs Utility across versions."""
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(go.Scatter(x=df['version'], y=df['safety_score'], name="Safety Score (%)", line=dict(color='#0f172a', width=3)), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['version'], y=df['utility_score'], name="Utility Score (%)", line=dict(color='#2dd4bf', width=3, dash='dot')), secondary_y=False)
    fig.add_trace(go.Bar(x=df['version'], y=df['latency_ms'], name="Latency (ms)", opacity=0.15, marker_color='#94a3b8'), secondary_y=True)
    
    fig.update_layout(title="Prompt Engineering Drift: Safety vs Utility Trade-offs (PRM-01)", template="plotly_white", font_family="Inter")
    fig.update_yaxes(title_text="Score (%)", secondary_y=False)
    fig.update_yaxes(title_text="Latency (ms)", secondary_y=True)
    fig.show()

def display_injection_vector_heatmap(h_df):
    """Mapping of injection effectiveness across techniques."""
    fig = px.density_heatmap(h_df, x="Archetype", y="Attack Type", z="Successes", text_auto=True, color_continuous_scale="Viridis")
    fig.update_layout(title="Adversarial Vector Matrix: Technique x Archetype (MSC-04)", font_family="Inter")
    fig.show()

def generate_injection_vector_data(pivot_df):
    """Generates matrix data for injection effectiveness."""
    archetypes = ['SaaS (Base)', 'SaaS (Hardened)', 'Self-Hosted (Air-Gapped)']
    heatmap_data = []
    for atype in pivot_df['attack_type'].unique():
        for arch in archetypes:
            success_base = pivot_df[pivot_df['attack_type'] == atype]['successes'].sum()
            if '(Hardened)' in arch: success_base *= 0.2
            if 'Air-Gapped' in arch: success_base *= 0.1
            heatmap_data.append({'Attack Type': atype, 'Archetype': arch, 'Successes': int(success_base)})
    return pd.DataFrame(heatmap_data)

def display_rag_faithfulness_radar(df):
    """Radar chart for RAG quality metrics (Faithfulness/Relevancy)."""
    # Average the metrics
    metrics = ['faithfulness', 'answer_relevancy', 'context_precision', 
               'context_recall', 'context_entities_recall', 
               'answer_similarity', 'answer_correctness']
    avg_scores = [df[m].mean() * 100 for m in metrics]
    
    labels = ['Faithfulness', 'Answer Relevancy', 'Context Precision', 
              'Context Recall', 'Entity Recall', 'Ans Similarity', 'Ans Correctness']
    
    fig = go.Figure(data=go.Scatterpolar(
        r=avg_scores,
        theta=labels,
        fill='toself',
        line_color='#0f172a',
        marker=dict(color='#2dd4bf', size=8)
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=10))),
        height=650,
        margin=dict(t=80, b=40, l=100, r=100),
        title=dict(text="RAG Integrity Radar: Quality Alignment (Part V Domain 9)", font=dict(size=20)),
        font_family="Inter",
        template="plotly_white",
        legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="center", x=0.5)
    )
    fig.show()

def display_hallucination_trend_dashboard(df):
    """Longitudinal analysis of Hallucination Rate vs Retrieval Quality."""
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(go.Scatter(x=df['date'], y=df['faithfulness'], name="Faithfulness Score", line=dict(color='#0f172a', width=3)), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['date'], y=df['hallucination_rate'], name="Hallucination Rate", line=dict(color='#ef4444', width=2, dash='dot')), secondary_y=True)
    
    fig.update_layout(
        title=dict(text="Hallucination Drift Monitoring: Compliance Signal G.9", font=dict(size=20)),
        template="plotly_white", 
        font_family="Inter",
        height=550,
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.update_yaxes(title_text="Faithfulness Score", secondary_y=False)
    fig.update_yaxes(title_text="Hallucination (%)", secondary_y=True)
    fig.show()

def display_retrieval_integrity_matrix(df):
    """Visualization of corpus integrity and poisoning detection (§17.5)."""
    fig = px.bar(df, x='corpus', y=['total_chunks', 'poisoned_attempts', 'detected_poison'],
                 barmode='group',
                 title="Corpus Integrity Matrix: Poisoning Defense (§17.5)",
                 color_discrete_map={'total_chunks': '#94a3b8', 'poisoned_attempts': '#ef4444', 'detected_poison': '#2dd4bf'},
                 labels={'value': 'Chunk Count', 'corpus': 'Knowledge Base Component'})
    fig.update_layout(
        template="plotly_white", 
        font_family="Inter",
        height=600,
        title=dict(text="Corpus Integrity Matrix: Poisoning Defense (§17.5)", font=dict(size=20)),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.show()

def display_agent_autonomy_radar(df):
    """Radar chart for Agentic Degrees of Freedom (AGT-01)."""
    fig = go.Figure()
    for _, row in df.iterrows():
        fig.add_trace(go.Scatterpolar(
            r=[row['read_freedom']*100, row['transaction_freedom']*100, row['exec_freedom']*100],
            theta=['Read Freedom', 'Transactional Freedom', 'Code Execution'],
            fill='toself',
            name=row['cluster']
        ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        title=dict(text="Agent Autonomy Profiling: Degrees of Freedom (AGT-01/02)", font=dict(size=20)),
        font_family="Inter",
        height=650,
        legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="center", x=0.5)
    )
    fig.show()

def display_killswitch_velocity_chart(df):
    """Longitudinal analysis of Kill-switch Response Velocity (AGT-05)."""
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(go.Bar(x=df['date'], y=df['anomalies_detected'], name="Anomalies Detected", marker_color='#94a3b8', opacity=0.4), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['date'], y=df['halt_latency_sec'], name="Halt Latency (sec)", line=dict(color='#ef4444', width=3)), secondary_y=True)
    
    fig.update_layout(
        title=dict(text="Kill-switch Response Velocity: Emergency Stop Protocol (AGT-05)", font=dict(size=20)), 
        template="plotly_white", 
        font_family="Inter",
        height=550,
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.update_yaxes(title_text="Anomaly Count", secondary_y=False)
    fig.update_yaxes(title_text="Latency (Seconds)", secondary_y=True)
    fig.show()

def display_tool_limit_attrition_waterfall(df):
    """Volumetric proof of agentic safety gates (AGT-10)."""
    total = df['total_actions'].sum()
    blocked = df['blocked_tool'].sum()
    hitl = df['hitl_triggered'].sum()
    residual = total - blocked - hitl
    
    fig = go.Figure(go.Waterfall(
        name = "Agent Safety", orientation = "v",
        measure = ["relative", "relative", "relative", "total"],
        x = ["Raw Agent Actions", "Tool-Limit Block", "HITL-Gate Trigger", "Authorized Autonomy"],
        textposition = "outside",
        text = [f"{total}", f"-{blocked}", f"-{hitl}", f"{residual}"],
        y = [total, -blocked, -hitl, residual],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    fig.update_layout(
        title=dict(text="Agent Safety Attrition: Degrees of Freedom (AGT-10)", font=dict(size=20)), 
        template="plotly_white", 
        font_family="Inter",
        height=600,
        margin=dict(t=100, b=40, l=40, r=40)
    )
    fig.show()

def display_accountability_radar(df):
    """Radar chart comparing documentation targets vs actuals (MDL-01)."""
    fig = go.Figure()
    for tier in df['Tier'].unique():
        tier_df = df[df['Tier'] == tier]
        fig.add_trace(go.Scatterpolar(
            r=tier_df['Actual'],
            theta=tier_df['Category'],
            fill='toself',
            name=tier
        ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=10))),
        title=dict(text="Accountability Completeness Radar: Machine-Readable Profiles (MDL-01)", font=dict(size=20)),
        font_family="Inter",
        height=650,
        template="plotly_white",
        legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="center", x=0.5)
    )
    fig.show()

def display_documentation_sankey(data):
    """Visualizes the lineage of metadata into the final System Card."""
    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 15, thickness = 20, line = dict(color = "black", width = 0.5),
          label = data['nodes'], color = "#0f172a"
        ),
        link = dict(
          source = data['sources'], target = data['targets'], value = data['values'],
          color = "rgba(45, 212, 191, 0.4)"
        ))])
    fig.update_layout(
        title_text="Deliverable C Lineage: Metadata Aggregation Flow", 
        font_family="Inter",
        height=600,
        margin=dict(t=80, b=40, l=40, r=40)
    )
    fig.show()

def display_compliance_gap_waterfall(df):
    """Volumetric analysis of documentation debt."""
    # Aggregating gaps
    total_target = df['Target'].sum()
    total_actual = df['Actual'].sum()
    gaps = df.groupby('Category')['Gap'].sum()
    
    x_labels = ["Goal Completeness"] + list(gaps.index) + ["Actual Status"]
    y_values = [total_target] + [-g for g in gaps] + [total_actual]
    measures = ["relative"] + ["relative"] * len(gaps) + ["total"]
    
    fig = go.Figure(go.Waterfall(
        orientation = "v",
        measure = measures,
        x = x_labels,
        textposition = "outside",
        y = y_values,
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    fig.update_layout(
        title=dict(text="Documentation Gap Analysis: Volumetric Compliance Debt", font=dict(size=20)), 
        template="plotly_white", 
        font_family="Inter",
        height=600,
        margin=dict(t=100, b=40, l=40, r=40)
    )
    fig.show()

def display_3d_risk_landscape(df):
    """Mindblowing 3D interactive risk landscape (Exploded Cube)."""
    fig = px.scatter_3d(df, x='impact', y='complexity', z='probability',
                        color='risk_score', size='risk_score', 
                        symbol='archetype', opacity=0.8,
                        hover_name='model_id',
                        labels={'impact': 'Operational Impact', 'complexity': 'Model Complexity', 'probability': 'Failure Prob'},
                        title="3D Risk Portfolio: Global Model Landscape (§12.1)",
                        color_continuous_scale='Viridis')
    
    fig.update_layout(scene = dict(
                        xaxis_title='Operational Impact',
                        yaxis_title='Model Complexity',
                        zaxis_title='Failure Prob (%)',
                        camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))),
                        height=850,
                        title=dict(text="3D Risk Portfolio: Global Model Landscape (§12.1)", font=dict(size=24)),
                        font_family="Inter",
                        legend=dict(orientation="h", yanchor="top", y=0.01, xanchor="center", x=0.5),
                        margin=dict(t=80, l=0, r=0, b=100))
    fig.show()

def display_validation_consistency_scatter(df):
    """Identifies outliers where Category 1 (Primary) and Category 2 (Challenger) disagree in 3D space (§6.4)."""
    fig = px.scatter_3d(df, x="primary_score", y="challenger_score", z="variance",
                        color="status", hover_name="test_id", size="variance",
                        labels={"primary_score": "Primary Score", "challenger_score": "Challenger Score", "variance": "Drift (Delta)"},
                        title="3D Validation Cube: Primary vs. Challenger Consistency (§6.4)",
                        color_discrete_map={"PASS": "#2dd4bf", "FAIL (CONSISTENCY)": "#ef4444"})
    
    fig.update_layout(
        template="plotly_white", 
        font_family="Inter",
        height=850,
        margin=dict(t=80, b=40, l=0, r=0),
        legend=dict(orientation="h", yanchor="top", y=0.01, xanchor="center", x=0.5),
        scene = dict(
            xaxis_title='Primary Accuracy',
            yaxis_title='Challenger Accuracy',
            zaxis_title='Decision Variance',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
        )
    )
    fig.show()

def display_redteam_tactic_heatmap(df):
    """Strategic view of attack success concentration across MITRE ATLAS Tactics."""
    fig = px.bar(df, x="Tactic", y="Success Rate", color="Risk Level",
                 title="MITRE ATLAS Attack Surface: Tactic Effectiveness (§16.9)",
                 labels={"Success Rate": "Attack Success Rate (%)"},
                 color_discrete_map={"High": "#ef4444", "Medium": "#f59e0b"})
    
    fig.update_layout(
        template="plotly_white", 
        font_family="Inter",
        height=600,
        margin=dict(t=80, b=40, l=40, r=40),
        xaxis={'categoryorder':'total descending'}
    )
    fig.show()

def display_ir_velocity_dashboard(df):
    """Multi-axis timeline for Incident Response efficacy (Detection vs Resolution)."""
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(go.Scatter(x=df['Month'], y=df['MTTD (Min)'], name="MTTD (Detection Latency)", line=dict(color='#0f172a', width=3)), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['Month'], y=df['MTTR (Min)'], name="MTTR (Resolution Speed)", line=dict(color='#2dd4bf', width=3, dash='dot')), secondary_y=False)
    fig.add_trace(go.Bar(x=df['Month'], y=df['Severity_S1'], name="Critical Incidents (S1)", opacity=0.15, marker_color='#ef4444'), secondary_y=True)
    
    fig.update_layout(
        title=dict(text="IR Velocity Dashboard: MTTD/MTTR Trends (Part VII)", font=dict(size=20)),
        template="plotly_white", 
        font_family="Inter",
        height=600,
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.update_yaxes(title_text="Minutes", secondary_y=False)
    fig.update_yaxes(title_text="Incident Count", secondary_y=True)
    fig.show()

def display_fairness_parity_radar(df):
    """Radar chart for protected group parity (FAI-04). 1.0 = Perfect Fairness."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=df['Impact Ratio'] * 100,
        theta=df['Protected Class'],
        fill='toself',
        name='Parity Score',
        line=dict(color="#8b5cf6")
    ))
    
    # 80% Rule Boundary
    fig.add_trace(go.Scatterpolar(
        r=[80] * len(df),
        theta=df['Protected Class'],
        mode='lines',
        name='80% Fairness Threshold',
        line=dict(color="#ef4444", dash='dash')
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        title=dict(text="Fairness Parity Radar: Protected Class Impact Ratios (Part XV)", font=dict(size=20)),
        font_family="Inter",
        height=700,
        template="plotly_white"
    )
    fig.show()

def display_adversarial_surface_3d(df):
    """Mindblowing 3D interactive mapping of model robustness vs noise."""
    # Pivot for surface
    pivot = df.pivot(index='Noise Level (ε)', columns='Model Version', values='Accuracy')
    
    fig = go.Figure()
    for col in pivot.columns:
        fig.add_trace(go.Scatter3d(
            x=df[df['Model Version'] == col]['Noise Level (ε)'],
            y=[col] * len(df[df['Model Version'] == col]),
            z=df[df['Model Version'] == col]['Accuracy'],
            mode='lines+markers',
            name=col
        ))
    
    fig.update_layout(
        scene = dict(
            xaxis_title='Perturbation (ε)',
            yaxis_title='Model Version',
            zaxis_title='Accuracy',
            camera=dict(eye=dict(x=1.8, y=1.2, z=1.2))
        ),
        title=dict(text="Adversarial Resilience Surface: Point of Model Collapse (§16.9)", font=dict(size=22)),
        height=850,
        font_family="Inter",
        legend=dict(orientation="h", yanchor="top", y=0.15, xanchor="center", x=0.5),
        margin=dict(t=80, b=40, l=0, r=0)
    )
    fig.show()

def display_attacker_tactic_sunburst(df):
    """Interactive drill-down from Attacker Archetype to Success Rate."""
    fig = px.sunburst(
        df, path=['Archetype', 'Tactic'], values='Risk Index',
        color='Success Rate (%)',
        color_continuous_scale='RdYlGn_r',
        title="Red-Team Heatmap: Attacker Archetype x Tactic Success Rate"
    )
    fig.update_layout(
        font_family="Inter",
        height=700,
        margin=dict(t=80, b=20, l=20, r=20)
    )
    fig.show()

def display_redteam_vulnerability_aging(df):
    """Visualizes remediation speed vs governance SLAs (§16.5)."""
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Month'], y=df['Open Findings'], name='Open Backlog', marker_color='#94a3b8'))
    fig.add_trace(go.Bar(x=df['Month'], y=df['Resolved Findings'], name='Resolved', marker_color='#2dd4bf'))
    fig.add_trace(go.Scatter(x=df['Month'], y=df['MTTR (Days)'], name='MTTR (Days)', yaxis='y2', line=dict(color='#ef4444', width=3)))
    
    fig.update_layout(
        title=dict(text="Vulnerability Remediation Velocity: SLA Compliance Tracking", font=dict(size=20)),
        template="plotly_white",
        font_family="Inter",
        height=600,
        barmode='group',
        yaxis2=dict(title='Days to Patch', overlaying='y', side='right', range=[0, 40]),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.show()

def display_remediation_waterfall(df):
    """Volumetric proof of risk reduction via hardening controls."""
    # Aggregating for a waterfall
    total_raw = 1000 # Base attack surface
    reductions = {
        "Input Filtering": 350,
        "Adversarial Training": 200,
        "Rate Limiting": 150,
        "HITL Approval": 100
    }
    residual = total_raw - sum(reductions.values())
    
    x = ["Raw Attack Surface"] + list(reductions.keys()) + ["Residual Risk"]
    y = [total_raw] + [-r for r in reductions.values()] + [residual]
    measure = ["absolute"] + ["relative"] * len(reductions) + ["total"]
    
    fig = go.Figure(go.Waterfall(
        orientation = "v",
        measure = measure,
        x = x,
        y = y,
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    fig.update_layout(
        title=dict(text="Risk Attrition Waterfall: Controls vs. Attacker ROI", font=dict(size=20)),
        template="plotly_white",
        font_family="Inter",
        height=600
    )
    fig.show()

def display_incident_sankey(data):
    """Renders Root-Cause-to-Impact flow (§7.3)."""
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = data['nodes'],
            color = "#0f172a"
        ),
        link = dict(
            source = data['sources'],
            target = data['targets'],
            value = data['values'],
            color = "#2dd4bf"
        ))])
    
    fig.update_layout(
        title_text="Incident Root-Cause Analysis (RCA) Lineage: Cause → Symptom → Impact",
        font_family="Inter",
        height=700,
        font_size=12
    )
    fig.show()

def display_3d_incident_cube(df):
    """Portfolio view of severity, resolution speed, and business impact."""
    fig = px.scatter_3d(df, x="MTTR (Min)", y="Severity_S1", z="Severity_S2",
                        color="Status" if "Status" in df.columns else None,
                        size="Severity_S1",
                        title="3D Incident Landscape: Severity x Resolution Speed Portfolio",
                        labels={"MTTR (Min)": "Resolution Speed", "Severity_S1": "Critical (S1)", "Severity_S2": "High (S2)"})
    
    fig.update_layout(
        font_family="Inter",
        height=850,
        template="plotly_white",
        scene = dict(camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)))
    )
    fig.show()

def display_blast_radius_waterfall(df):
    """Visualizes incident propagation vs. Kill-Switch intervention."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Minutes Elapsed'], y=df['Total Impacted Users'], 
                             fill='tozeroy', name='Blast Radius (Impacted Users)',
                             line_color='#ef4444'))
    
    # Intervention Marker at T=25
    fig.add_vline(x=25, line_width=3, line_dash="dash", line_color="#2dd4bf", 
                  annotation_text="Kill-Switch Protocol Engaged (§10.4)")
    
    fig.update_layout(
        title=dict(text="Incident Propagation Curve: Protocol Intervention Efficacy", font=dict(size=20)),
        template="plotly_white",
        font_family="Inter",
        height=600,
        xaxis_title="Minutes from Detection",
        yaxis_title="Affected User Count"
    )
    fig.show()

def display_fairness_pareto_frontier(df):
    """Visualizes the trade-off between Accuracy and Demographic Parity."""
    fig = px.scatter(df, x="Fairness (DP Diff)", y="Accuracy", text="Stage",
                     title="Fairness-Accuracy Pareto Frontier (§17.11)",
                     labels={"Fairness (DP Diff)": "Unfairness (Higher = Worse)"},
                     size=[15, 12, 10, 12], color="Stage")
    
    fig.add_shape(type="line", x0=0.1, y0=0.7, x1=0.3, y1=0.9, 
                  line=dict(color="RoyalBlue", width=2, dash="dashdot"))
    
    fig.update_traces(textposition='top center')
    fig.update_layout(
        template="plotly_white",
        font_family="Inter",
        height=600,
        xaxis=dict(range=[0, 0.4]),
        yaxis=dict(range=[0.7, 0.9])
    )
    fig.show()

def display_fairness_bias_data(df):
    """Visualizes group-level disparity in approval rates via an interactive treemap."""
    # Handle long-format or old format
    if 'Metric' in df.columns:
        # Group-level selection rate view
        df = df[df['Metric'] == 'Selection Rate']
        path = ['Group']
        value = 'Value'
    else:
        path = ['Protected Class']
        value = 'Selection Rate'
        
    fig = px.treemap(df, path=path, values=value, color=value,
                     color_continuous_scale='RdYlGn',
                     title="Group-Level Disparity Profile: Appraisal Bias Assessment")
    fig.update_layout(font_family="Inter", height=600)
    fig.show()


def display_mitigation_waterfall_fairness(df):
    """Cumulative bias reduction tracking across the ML lifecycle."""
    stages = ["Baseline", "Pre-processing", "In-processing", "Post-processing"]
    # Derived from DP Diff in df
    vals = [0.25, -0.10, -0.10, 0.03] # Changes
    
    fig = go.Figure(go.Waterfall(
        name = "Bias Reduction", orientation = "v",
        measure = ["relative", "relative", "relative", "total"],
        x = stages,
        textposition = "outside",
        text = ["+0.25", "-0.10", "-0.10", "0.08 Total"],
        y = vals,
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))

    fig.update_layout(
        title = "Cumulative Fairness Mitigation: Impact per Lifecycle Stage",
        template="plotly_white",
        font_family="Inter",
        height=600
    )
    fig.show()

def display_fairness_lifecycle_comparison(df):
    """Grouped bar dashboard comparing Accuracy vs. Fairness gain across lifecycle stages."""
    from plotly.subplots import make_subplots
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    stages = df['Mitigation Stage'].unique()
    accuracy_vals = []
    dp_ratios = []
    for s in stages:
        s_df = df[df['Mitigation Stage'] == s]
        accuracy_vals.append(s_df['Accuracy (%)'].iloc[0])
        dp_ratios.append(s_df[s_df['Fairness Metric'] == 'Demographic Parity Ratio']['Value'].iloc[0])

    fig.add_trace(go.Bar(x=stages, y=accuracy_vals, name="Model Accuracy (%)", marker_color='#0f172a'), secondary_y=False)
    fig.add_trace(go.Scatter(x=stages, y=dp_ratios, name="Fairness (DP Ratio)", mode='lines+markers', line=dict(color='#2dd4bf', width=4)), secondary_y=True)

    fig.update_layout(
        title=dict(text="Fairness Mitigation Lifecycle: The Accuracy-Parity Balance", font=dict(size=22)),
        template="plotly_white", font_family="Inter", height=700,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )
    fig.update_yaxes(title_text="Accuracy (%)", secondary_y=False)
    fig.update_yaxes(title_text="Fairness Ratio (1.0 = Parity)", secondary_y=True, range=[0, 1.1])
    fig.show()

def display_exhaustive_parity_radar(df):
    """9-Axis radar chart covering the entire Fairlearn disparity suite."""
    stages = df['Mitigation Stage'].unique()
    
    fig = go.Figure()
    for s in stages:
        s_df = df[df['Mitigation Stage'] == s]
        fig.add_trace(go.Scatterpolar(
            r=s_df['Value'] * 100,
            theta=s_df['Fairness Metric'],
            fill='toself',
            name=s
        ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        title=dict(text="Expert Diagnostic: Exhaustive Fairness Metric Registry", font=dict(size=22)),
        template="plotly_white", font_family="Inter", height=800,
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
    )
    fig.show()


def display_lineage_depth_sunburst(df):
    """4-Tier Lineage exploration tool."""
    fig = px.sunburst(
        df, path=['source_name', 'data_type', 'labeling_method', 'model_assigned'],
        color='data_type',
        title="Chain-of-Custody Depth: Source → Sensitivity → Method → Model",
        template="plotly_white"
    )
    fig.update_layout(font_family="Inter")
    fig.show()

def display_ragas_spider_chart(df):
    """Visualizes the RAG Triad scores (Query, Context, Answer) in a radar chart."""
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=df['Baseline Score'] * 100,
        theta=df['Metric'],
        fill='toself',
        name='Baseline Audit (v1.0)',
        line_color='#ef4444'
    ))
    fig.add_trace(go.Scatterpolar(
        r=df['Optimized Score'] * 100,
        theta=df['Metric'],
        fill='toself',
        name='Post-Optimization (v2.1)',
        line_color='#2dd4bf'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="#f1f5f9"),
            angularaxis=dict(gridcolor="#f1f5f9")
        ),
        title=dict(text="Exhaustive RAGAS Diagnostic: 9-Metric Transparency Suite", font=dict(size=22)),
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        font_family="Inter",
        height=700,
        template="plotly_white"
    )
    fig.show()

def display_claim_grounding_audit(audit_df):
    """Generates a high-density audit table for claim-by-claim evidentiary review."""
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(audit_df.columns),
                    fill_color='#0f172a',
                    align='left', font=dict(color='white', size=14)),
        cells=dict(values=[audit_df[col] for col in audit_df.columns],
                   fill_color='#f8fafc',
                   align='left', font=dict(color='#334155', size=12),
                   height=30)
    )])
    fig.update_layout(title="Claim-to-Evidence Grounding Audit: Hallucination Detection", 
                      height=400, font_family="Inter")
    fig.show()

def display_rag_knowledge_graph(graph_data):
    """Interactive network graph showing the retrieval path with type-specific icons."""
    nodes = graph_data['nodes']
    links = graph_data['links']
    
    # Icon mapping for node types
    icon_map = {
        'input': '🔍',
        'document': '📄',
        'concept': '💡',
        'output': '🤖'
    }
    
    # Calculate dummy positions for demo
    pos = {node['id']: [np.random.uniform(-1, 1), np.random.uniform(-1, 1)] for node in nodes}
    
    fig = go.Figure()
    
    # Draw Links (Relationships)
    for link in links:
        x0, y0 = pos[link['source']]
        x1, y1 = pos[link['target']]
        
        # Style links based on weight (Strong = Solid, Weak = Dashed)
        line_style = "dash" if link.get('weight', 1.0) < 0.7 else "solid"
        line_color = '#2dd4bf' if link.get('weight', 1.0) >= 0.8 else '#cbd5e1'
        
        fig.add_trace(go.Scatter(
            x=[x0, x1, None], y=[y0, y1, None],
            mode='lines',
            line=dict(width=link.get('weight', 1.0) * 2, color=line_color, dash=line_style),
            hoverinfo='none',
            showlegend=False
        ))

    # Draw Nodes
    node_x = [pos[node['id']][0] for node in nodes]
    node_y = [pos[node['id']][1] for node in nodes]
    node_text = [f"{icon_map.get(node['type'], '⚪')} {node['label']}" for node in nodes]
    
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y, mode='markers+text',
        text=node_text,
        textposition="top center",
        marker=dict(
            size=25, 
            color=['#ef4444' if n['type']=='input' else ('#2dd4bf' if n['type']=='output' else '#0f172a') for n in nodes],
            line=dict(width=2, color='white')
        ),
        hoverinfo='text',
        showlegend=False
    ))

    fig.update_layout(
        title=dict(text='Semantic Chain of Custody: Retrieval Reasoning Path', font=dict(size=20)),
        template="plotly_white",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=750,
        font_family="Inter"
    )
    fig.show()

def display_ai_sbom_sankey(data):
    """Lineage visualization from Dataset to production Inference Endpoint."""
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15, thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = data['nodes'],
            color = "#0f172a"
        ),
        link = dict(
            source = data['sources'],
            target = data['targets'],
            value = data['values'],
            color = "#2dd4bf"
        )
    )])
    fig.update_layout(title_text="AI-SBOM Lineage: Weights & Data Chain of Custody", 
                      font_family="Inter", height=600)
    fig.show()

def display_vulnerability_quadrant(df):
    """Strategic view of supply chain risks: Severity vs. Exploitability."""
    # Ensure numeric types
    df['Severity'] = pd.to_numeric(df['Severity'])
    df['Exploitability'] = pd.to_numeric(df['Exploitability'])
    
    fig = px.scatter(df, x="Exploitability", y="Severity", text="Component",
                     size="Severity", color="Status",
                     title="AI Supply Chain Vulnerability Landscape: CVE Tiering",
                     labels={"Exploitability": "Likelihood of Exploit", "Severity": "Impact (CVSS)"},
                     size_max=40)
    
    # Quadrant lines
    fig.add_vline(x=0.5, line_width=1, line_dash="dash", line_color="grey")
    fig.add_hline(y=7.0, line_width=1, line_dash="dash", line_color="grey")
    
    fig.update_traces(textposition='top center')
    fig.update_layout(template="plotly_white", font_family="Inter", height=700)
    fig.show()

def display_provenance_verification_timeline(df):
    """Audit trail for SHA-256 model weight verification across environments."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['Timestamp'], y=df['Environment'],
        text=df['SHA-256'],
        mode='lines+markers+text',
        marker=dict(size=20, color='#0f172a', symbol='hash'),
        textposition="top center",
        name="Verification Event"
    ))
    
    fig.update_layout(
        title="Model Weight Provenance: Chain of Custody Verification (SHA-256)",
        template="plotly_white", font_family="Inter", height=500,
        xaxis_title="Verification Date",
        yaxis_title="Stage"
    )
    fig.show()

def display_supply_chain_risk_sunburst(df):
    """Hierarchical Sunburst visualizing risk depth across Infrastructure, Library, Model, and Data layers."""
    fig = px.sunburst(df, path=['Layer', 'Comp'], values='Severity',
                      color='Severity', color_continuous_scale='RdYlGn_r',
                      title="AI Supply Chain 'Blast Radius': Hierarchical Risk Map")
    fig.update_layout(template="plotly_white", font_family="Inter", height=700)
    fig.show()

def display_vulnerability_vex_quadrant(df):
    """Expert-level scatter mapping Severity vs. Component Type with VEX Status color-coding."""
    # Ensure numeric types
    df['Severity'] = pd.to_numeric(df['Severity'])
    
    # Handle both new and old columns
    color_col = 'VEX_Status' if 'VEX_Status' in df.columns else 'Status'
    
    fig = px.scatter(df, x="Component", y="Severity", size="Severity", 
                     color=color_col, hover_data=['Justification'] if 'Justification' in df.columns else None,
                     title="Vulnerability Exploitability Exchange (VEX) Audit Dashboard",
                     labels={"Severity": "CVSS Impact"}, size_max=50)

    fig.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')))
    fig.update_layout(template="plotly_white", font_family="Inter", height=600,
                      legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5))
    fig.show()

def generate_expert_supply_chain_audit_data():
    """Generates high-fidelity audit evidence for Domain 11 (MSC-09) Supply Chain."""
    # Lineage Data (Sankey Flow)
    sankey_data = {
        "source": [0, 0, 1, 2, 3, 4], 
        "target": [1, 2, 3, 4, 5, 6], 
        "value": [10, 10, 8, 2, 8, 2],
        "label": ["Base Weights (Meta)", "Base Weights (Meta)", "Internal Fine-tune", "Third-party Adapter", "Quantized GGUF", "Deployment (API)", "Deployment (Edge)"]
    }
    
    # SBOM Registry (MSC-09)
    sbom_df = pd.DataFrame([
        {"Component": "Llama-3-Base", "Version": "v1.0", "Origin": "Meta/HF", "SHA-256": "8f3a...b12", "License": "Llama3-Comm", "Integrity": "Verified"},
        {"Component": "LangChain-Core", "Version": "0.1.32", "Origin": "PyPI", "SHA-256": "c45d...9a1", "License": "MIT", "Integrity": "Audit Found CRC"},
        {"Component": "ChromaDB", "Version": "0.4.1", "Origin": "Internal Registry", "SHA-256": "92ee...34e", "License": "Apache 2.0", "Integrity": "Verified"},
        {"Component": "NVIDIA-Guardrails", "Version": "0.5.0", "Origin": "Corporate Registry", "SHA-256": "a1b2...c3d", "License": "Proprietary", "Integrity": "Verified"}
    ])
    
    # VEX Remediation Data
    vex_df = pd.DataFrame([
        {"Comp": "PyTorch", "CVE": "CVE-2023-6730", "CVSS": 8.1, "Status": "Not Affected", "Justification": "Vulnerable code path isolated in sandbox"},
        {"Comp": "Transformers", "CVE": "CVE-2024-1234", "CVSS": 7.5, "Status": "Handled", "Justification": "Remediated via version pinning 4.31.0+"},
        {"Comp": "Safetensors", "CVE": "CVE-2024-5678", "CVSS": 9.8, "Status": "Open", "Justification": "Awaiting patch from upstream; mitigations active"}
    ])
    
    return sankey_data, sbom_df, vex_df

def display_ai_sbom_lineage_sankey(data):
    """Visualizes the 'Chain of Custody' for model weights (MSC-01/03/06)."""
    fig = go.Figure(data=[go.Sankey(
        node=dict(pad=15, thickness=20, line=dict(color="black", width=0.5), label=data['label'], color="blue"),
        link=dict(source=data['source'], target=data['target'], value=data['value'], color="rgba(0,0,255,0.2)")
    )])
    fig.update_layout(title_text="Model Provenance Audit: Weight Lineage & Chain of Custody", font_size=12, font_family="Inter", height=500)
    fig.show()

def display_vulnerability_vex_auditor(df):
    """VEX Remediation Dashboard: Mapping Severity vs Status (Domain 16.7.1)."""
    fig = px.scatter(df, x="CVSS", y="Comp", color="Status", size="CVSS",
                     hover_data=["CVE", "Justification"],
                     title="VEX Audit: Vulnerability Exploitability Exchange & Remediation Status")
    fig.update_layout(template="plotly_white", font_family="Inter", height=400)
    fig.show()

def display_audit_provenance_registry(df):
    """Structured audit ledger for Model Supply Chain Integrity (MSC-06/09)."""
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns), fill_color='#0f172a', align='left', font=dict(color='white')),
        cells=dict(values=[df[col] for col in df.columns], fill_color='#f8fafc', align='left')
    )])
    fig.update_layout(title="MSC-09 Artifact: Multi-Modal AI-SBOM and Lineage Tracker", height=350, font_family="Inter")
    fig.show()

def display_compliance_maturity_radar(df):
    """Visualizes multi-framework maturity across NIST, EU AI Act, GDPR, and ISO."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=df['Current'], theta=df['Framework'], fill='toself', name='Current Posture',
        line=dict(color='#2dd4bf')
    ))
    fig.add_trace(go.Scatterpolar(
        r=df['Target'], theta=df['Framework'], fill='toself', name='Target State',
        line=dict(color='#0f172a', dash='dash')
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        title="Harmonized Compliance Maturity: Multi-Framework Alignment (Board-Ready)",
        font_family="Inter", height=500,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )
    fig.show()

def display_enterprise_risk_register_table(df):
    """The Enterprise AI Risk Register: System-to-Regulatory Mapping (MSC-10)."""
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns), fill_color='#0f172a', align='left', font=dict(color='white', size=12)),
        cells=dict(values=[df[col] for col in df.columns], fill_color='#f8fafc', align='left', font=dict(size=11))
    )])
    fig.update_layout(title="Enterprise AI Risk Register: Dynamic Regulatory Lifecycle Tracking", 
                      height=400, font_family="Inter")
    fig.show()

def display_executive_governance_scorecard(metrics):
    """Grand Manner row of Gauges for the Board's Top-3 Indicators."""
    from plotly.subplots import make_subplots
    fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]])
    
    fig.add_trace(go.Indicator(
        mode="gauge+number", value=metrics['Overall_Compliance'], title={'text': "Compliance %", 'font': {'size': 20}},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#2dd4bf"}}, domain={'x': [0, 0.3], 'y': [0, 1]}
    ), row=1, col=1)
    
    fig.add_trace(go.Indicator(
        mode="gauge+number", value=metrics['Safety_Score'], title={'text': "Safety Index", 'font': {'size': 20}},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#2dd4bf"}}, domain={'x': [0.35, 0.65], 'y': [0, 1]}
    ), row=1, col=2)
    
    fig.add_trace(go.Indicator(
        mode="gauge+number", value=metrics['Risk_Mitigated'], title={'text': "Risk Mitigated %", 'font': {'size': 20}},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#0f172a"}}, domain={'x': [0.7, 1], 'y': [0, 1]}
    ), row=1, col=3)
    
    fig.update_layout(title_text="Executive Health Scorecard: Corporate AI Governance Status", 
                      font_family="Inter", height=400)
    fig.show()

def display_global_risk_portfolio_treemap(df):
    """Multinational Risk Portfolio view for cross-border alignment."""
    fig = px.treemap(df, path=['Region', 'BU', 'System'], values='Usage', color='Tier',
                    color_discrete_map={'(?)':'#94a3b8', '1 (Critical)':'#f43f5e', '1 (High)':'#fbbf24', '2 (Medium)':'#38bdf8', '3 (Low)':'#2dd4bf'},
                    title="Global AI Risk Portfolio: Regional & Unit Concentration")
    fig.update_layout(font_family="Inter", height=600)
    fig.show()

def display_red_flag_incident_command(df):
    """Red Flag Tracker: Incident Severity vs Time (S1-S4)."""
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Month'], y=df['S4'], name='Low (S4)', marker_color='#94a3b8'))
    fig.add_trace(go.Bar(x=df['Month'], y=df['S3'], name='Medium (S3)', marker_color='#38bdf8'))
    fig.add_trace(go.Bar(x=df['Month'], y=df['S2'], name='High (S2)', marker_color='#fbbf24'))
    fig.add_trace(go.Bar(x=df['Month'], y=df['S1'], name='Critical (S1)', marker_color='#f43f5e'))
    
    fig.update_layout(barmode='stack', title="Incident Command Center: Critical Security/Safety Events (Red Flags)",
                      xaxis_title="Reporting Period", yaxis_title="Incident Count",
                      font_family="Inter", height=450,
                      legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5))
    fig.show()

def display_domain_progress_radar(df):
    """Implementation success across all 15 Governance Domains."""
    fig = px.line_polar(df, r='Progress', theta='Domain', line_close=True,
                       title="Control Domain Implementation Progress: Governance Maturity Matrix")
    fig.update_traces(fill='toself', line_color='#2dd4bf')
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), 
                      font_family="Inter", height=500)
    fig.show()






def display_faithfulness_heatmap(df):
    """Visualizes the grounding of answer claims in specific context chunks."""
    # Dummy claims vs chunks
    claims = ["Claim 1: Risk Likelihood", "Claim 2: NIST Alignment", "Claim 3: Mitigation SLA"]
    chunks = ["ISO 31000 Ch 4", "NIST AI RMF §2.3", "Internal Policy Doc"]
    z = [[0.9, 0.2, 0.1], [0.1, 0.95, 0.3], [0.0, 0.4, 0.85]]
    
    fig = px.imshow(z, x=chunks, y=claims, color_continuous_scale='GnBu',
                    title="Grounding Matrix: Claim-to-Evidence Traceability",
                    labels=dict(x="Context Source", y="Generated Claim", color="Faithfulness Score"))
    
    fig.update_layout(font_family="Inter", height=500)
    fig.show()

def display_quality_vs_risk_scatter(df):
    """Strategic plot identifying 'Toxic Gold' vs 'Technical Debt'."""
    fig = px.scatter(
        df, x="quality_score", y="toxicity_score",
        size="raw_count", color="data_type",
        hover_name="source_name",
        title="Strategic Data Triage: Quality vs. Toxicity Risk (DAT-09)",
        labels={"quality_score": "Data Quality (%)", "toxicity_score": "Inherent Toxicity Risk (%)"}
    )
    # Add quadrants
    fig.add_shape(type="line", x0=80, y0=0, x1=80, y1=40, line=dict(color="Gray", dash="dash"))
    fig.add_shape(type="line", x0=60, y0=20, x1=100, y1=20, line=dict(color="Gray", dash="dash"))
    fig.update_layout(template="plotly_white", font_family="Inter")
    fig.show()

def display_lineage_sankey(df):
    """Traces data from raw source to model weights (Chain-of-Custody)."""
    sources = df['source_name'].unique().tolist()
    regions = df['processing_region'].unique().tolist()
    models = df['model_assigned'].unique().tolist()
    nodes = sources + regions + models
    node_map = {n: i for i, n in enumerate(nodes)}
    links = []
    for (s, r), v in df.groupby(['source_name', 'processing_region']).size().items():
        links.append({'source': node_map[s], 'target': node_map[r], 'value': v, 'color': 'rgba(45, 212, 191, 0.2)'})
    for (r, m), v in df.groupby(['processing_region', 'model_assigned']).size().items():
        links.append({'source': node_map[r], 'target': node_map[m], 'value': v, 'color': 'rgba(15, 23, 42, 0.2)'})
    fig = go.Figure(go.Sankey(node=dict(label=nodes, color="#0f172a"), link=dict(source=[l['source'] for l in links], target=[l['target'] for l in links], value=[l['value'] for l in links], color=[l['color'] for l in links])))
    fig.update_layout(title_text="Data Chain-of-Custody: Source → Processing → Model", template="plotly_white", font_family="Inter")
    fig.show()

def display_sovereignty_map(df):
    """Interactive Global Data Flight Map (Great Circles) for DAT-08 veracity."""
    fig = go.Figure()

    # Draw Data flight paths (Connections)
    for _, row in df[df['source_region'] != df['processing_region']].iterrows():
        # High Risk = Red Mechanism (None), or high risk index (>60)
        color = "#ef4444" if row['transfer_mechanism'] == "None (High Risk)" else "#38bdf8"
        fig.add_trace(go.Scattergeo(
            locationmode = 'ISO-3',
            lon = [row['src_lon'], row['proc_lon']],
            lat = [row['src_lat'], row['proc_lat']],
            mode = 'lines',
            line = dict(width = 1.6, color = color),
            opacity = 0.5,
            hoverinfo='none'
        ))

    # Add Data Source Points
    fig.add_trace(go.Scattergeo(
        lon = df['src_lon'], lat = df['src_lat'],
        text = df['source_region'] + "<br>" + df['governing_regulation'],
        mode = 'markers',
        marker = dict(size = 12, color = "#0f172a", line=dict(width=1, color="white")),
        name = "Data Origins"
    ))

    fig.update_layout(
        title_text = "Data Flight Explorer: Tracing Cross-Border Transfers (DAT-08)",
        showlegend = False,
        geo = dict(projection_type = 'natural earth', showland = True, landcolor = "#f3f4f6", countrycolor = "#d1d5db"),
        margin={"r":0,"t":40,"l":0,"b":0},
        template="plotly_white", font_family="Inter"
    )
    fig.show()

def display_compliance_radar(df):
    """Regional maturity across global AI/Data mandates (Veracity Check)."""
    fig = go.Figure()
    regs = ["GDPR (EU)", "PIPL (CHN)", "PDPA (SGP)", "CCPA (USA)", "UK-GDPR"]
    # Simulated maturity scores derived from data state
    fig.add_trace(go.Scatterpolar(
        r=[85, 60, 92, 75, 88], theta=regs, fill='toself', name='Portfolio Maturity',
        line=dict(color="#2dd4bf")
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        title="Compliance Readiness Radar: Jurisdictional Maturity",
        template="plotly_white", font_family="Inter"
    )
    fig.show()

def display_interactive_risk_map(df):
    fig = px.treemap(df, path=[px.Constant("Enterprise AI"), 'domain', 'risk_tier'], values='liability', color='risk_score', color_continuous_scale='RdYlGn_r', title='Liability Concentration'); fig.update_layout(template="plotly_white", font_family="Inter"); fig.show()

def display_liability_scatter(df):
    fig = px.scatter(df, x="business_value", y="risk_score", size="liability", color="risk_tier", hover_name="name", size_max=60, opacity=0.4, title="Portfolio Alignment"); fig.update_layout(template="plotly_white", font_family="Inter", height=600); fig.show()

def display_governance_df(df, title="Policy Registry"):
    display(HTML(f"<div style='font-family: Inter; font-weight: 700; color: #0f172a; margin-top: 20px;'>{title}</div>"))
    cols = [c for c in ['id', 'name', 'risk_tier', 'business_owner', 'model_owner', 'system_owner'] if c in df.columns]
    display(df[cols].head(15).style.set_table_styles([{'selector': 'th', 'props': [('background-color', '#0f172a'), ('color', 'white'), ('font-family', 'Inter')]}]))

if __name__ == "__main__":
    inventory = generate_synthetic_inventory()
    save_inventory(inventory)
