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

# --- MODULE 08: PROMPT OPS ---
m08_cells = [
    nbf.v4.new_code_cell("import grc_utils\nimport importlib\nimportlib.reload(grc_utils)\ngrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 8: Prompt Engineering Depth Overhaul - PRM & MSC-04"),
    nbf.v4.new_code_cell("grc_utils.display_deliverable_anchor('PRM', 'Adversarial Prompting & Version Control')"),
    nbf.v4.new_markdown_cell("""
## 1. Prompt Defense Attrition (PRM-04)
Adversarial prompts (Jailbreaks, Injections) must be blocked by layered controls. This waterfall visualizes the effectiveness of System Prompts vs Guardrail APIs vs Semantic filters.
"""),
    nbf.v4.new_code_cell("""
adv_data = grc_utils.generate_adversarial_prompt_data()
grc_utils.display_prompt_safety_attrition_waterfall(adv_data)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Prompt Engineering Drift (PRM-01)
As prompts are hardened for safety, their "Utility" (performance on core tasks) and "Latency" might shift. Governance mandates tracking this trade-off across versions.
"""),
    nbf.v4.new_code_cell("""
drift_df = grc_utils.generate_prompt_version_safety_scores()
grc_utils.display_prompt_drift_analysis(drift_df)
"""),
    nbf.v4.new_markdown_cell("""
## 3. Adversarial Vector Matrix (MSC-04)
Mapping injection techniques against deployment archetypes. Hardened SaaS endpoints should show lower success rates compared to base models.
"""),
    nbf.v4.new_code_cell("""
heatmap_df = grc_utils.generate_injection_vector_data(adv_data)
grc_utils.display_injection_vector_heatmap(heatmap_df)
""")
]

# --- MODULE 09: RAG INTEGRITY ---
m09_cells = [
    nbf.v4.new_code_cell("import grc_utils\nimport importlib\nimportlib.reload(grc_utils)\ngrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 9: RAG Integrity - Depth Overhaul & Hallucination Mitigation"),
    nbf.v4.new_code_cell("grc_utils.display_deliverable_anchor('RAG', 'Knowledge Base Integrity & Claim Verification')"),
    nbf.v4.new_markdown_cell("""
## 1. RAG Integrity Radar (Part V Domain 9)
Beyond simple PASS/FAIL, we track the multi-dimensional quality of retrieval. This radar monitors the complete **RAGAS suite**: **Faithfulness**, **Answer Relevancy**, **Context Precision**, **Context Recall**, **Entity Recall**, **Semantic Similarity**, and **Factual Correctness**.
"""),
    nbf.v4.new_code_cell("""
rag_perf_df = grc_utils.generate_rag_performance_data()
grc_utils.display_rag_faithfulness_radar(rag_perf_df)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Hallucination Drift Monitoring (Signal G.9)
Hallucinations are often a trailing indicator of retrieval quality degradation. We monitor this relationship longitudinally to trigger re-indexing or corpus cleaning.
"""),
    nbf.v4.new_code_cell("""
grc_utils.display_hallucination_trend_dashboard(rag_perf_df)
"""),
    nbf.v4.new_markdown_cell("""
## 3. Corpus Integrity Matrix (§17.5)
The Knowledge Base is a supply chain of facts. We monitor for **Corpus Poisoning** (unauthorized chunk modifications) and ensure successful detection by automated integrity gates.
"""),
    nbf.v4.new_code_cell("""
integrity_df = grc_utils.generate_retrieval_integrity_logs()
grc_utils.display_retrieval_integrity_matrix(integrity_df)
""")
]

# --- MODULE 10: AGENTIC KILL-SWITCH ---
m10_cells = [
    nbf.v4.new_code_cell("import grc_utils\nimport importlib\nimportlib.reload(grc_utils)\ngrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 10: Agentic Autonomy - Depth Overhaul & Emergency Stop"),
    nbf.v4.new_code_cell("grc_utils.display_deliverable_anchor('AGT', 'Degrees of Freedom & Kill-switch Protocol')"),
    nbf.v4.new_markdown_cell("""
## 1. Agent Autonomy Profiling (AGT-01/02)
Not all agents are created equal. We monitor the **Degrees of Freedom** across functional clusters. IT Admin agents require higher "Code Execution" freedom, while Customer Support is restricted to "Read-only" and low-value "Transactional" tasks.
"""),
    nbf.v4.new_code_cell("""
agent_gov_df = grc_utils.generate_agentic_governance_data()
grc_utils.display_agent_autonomy_radar(agent_gov_df)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Agent Safety Attrition (AGT-10)
High-depth governance mandates that agentic actions are filtered through multiple safety gates. This waterfall tracks the attrition from raw action requests to authorized autonomy after **Tool-Limit** and **HITL (Human-in-the-Loop)** filtering.
"""),
    nbf.v4.new_code_cell("""
grc_utils.display_tool_limit_attrition_waterfall(agent_gov_df)
"""),
    nbf.v4.new_markdown_cell("""
## 3. Kill-switch Response Velocity (AGT-05)
An autonomous system must have a functional "Emergency Stop". We monitor the latency between detecting a policy violation (e.g., recursive tool calls) and the automated kill-switch activation.
"""),
    nbf.v4.new_code_cell("""
kill_metrics_df = grc_utils.generate_killswitch_metrics()
grc_utils.display_killswitch_velocity_chart(kill_metrics_df)
""")
]

# --- MODULE 11: DOCUMENTATION ---
m11_cells = [
    nbf.v4.new_code_cell("import grc_utils\nimport importlib\nimportlib.reload(grc_utils)\ngrc_utils.inject_framework_style()"),
    nbf.v4.new_markdown_cell("# Module 11: Machine-Readable Accountability - Deep Dive"),
    nbf.v4.new_code_cell("grc_utils.display_deliverable_anchor('C', 'Model & System Cards (§12.1)')"),
    nbf.v4.new_markdown_cell("""
## 1. Accountability Completeness Radar (MDL-01)
Machine-readable accountability requires a balanced documentation profile across 6 pillars. This radar maps our **Goal** vs. **Actual** completeness for System Cards, highlighting gaps in high-risk categories.
"""),
    nbf.v4.new_code_cell("""
acc_df = grc_utils.generate_accountability_profile_data()
grc_utils.display_accountability_radar(acc_df)
"""),
    nbf.v4.new_markdown_cell("""
## 2. Information Lineage Sankey (Deliverable C)
How does a raw data attribute become a compliance signal? This Sankey visualizes the **Metadata Lineage**, showing how inventory data, prompt registries, and security logs aggregate into the final **Deliverable C** disclosure.
"""),
    nbf.v4.new_code_cell("""
lineage_data = grc_utils.generate_metadata_lineage_data()
grc_utils.display_documentation_sankey(lineage_data)
"""),
    nbf.v4.new_markdown_cell("""
## 3. Documentation Gap Waterfall
Starting with a 100% target completeness, this waterfall shows the volumetric "Documentation Debt"—the specific categories (Bias audits, Security logs, IP clearance) that deduct from our target status.
"""),
    nbf.v4.new_code_cell("""
grc_utils.display_compliance_gap_waterfall(acc_df)
"""),
    nbf.v4.new_markdown_cell("""
## 4. Mindblowing 3D Risk Landscape (§12.1)
**Exploded Portfolio Cube**: Navigate the entire model inventory in interactive 3D space. Explore the relationship between **Operational Impact**, **Complexity**, and **Failure Probability** with full "Slice and Dice" interaction.
"""),
    nbf.v4.new_code_cell("""
cube_df = grc_utils.generate_3d_risk_cube_data()
grc_utils.display_3d_risk_landscape(cube_df)
""")
]

update_nb("module_08_prompt_ops.ipynb", m08_cells)
update_nb("module_09_rag_integrity.ipynb", m09_cells)
update_nb("module_10_agentic_killswitch.ipynb", m10_cells)
update_nb("module_11_documentation.ipynb", m11_cells)
