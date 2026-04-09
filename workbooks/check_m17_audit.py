import grc_utils
import importlib
importlib.reload(grc_utils)
grc_utils.inject_framework_style()
grc_utils.display_deliverable_anchor('MSC-09', 'AI-SBOM & Lineage Audit Artifact')

sankey_data, sbom_df, vex_df = grc_utils.generate_expert_supply_chain_audit_data()
grc_utils.display_ai_sbom_lineage_sankey(sankey_data)


grc_utils.display_audit_provenance_registry(sbom_df)


grc_utils.display_vulnerability_vex_auditor(vex_df)


_ , sunburst_df = grc_utils.generate_vulnerability_vex_registry()
grc_utils.display_supply_chain_risk_sunburst(sunburst_df)

