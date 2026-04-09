import aigrc_utils
import importlib
importlib.reload(aigrc_utils)
aigrc_utils.inject_framework_style()
aigrc_utils.display_deliverable_anchor('MSC-09', 'AI-SBOM & Lineage Audit Artifact')

sankey_data, sbom_df, vex_df = aigrc_utils.generate_expert_supply_chain_audit_data()
aigrc_utils.display_ai_sbom_lineage_sankey(sankey_data)


aigrc_utils.display_audit_provenance_registry(sbom_df)


aigrc_utils.display_vulnerability_vex_auditor(vex_df)


_ , sunburst_df = aigrc_utils.generate_vulnerability_vex_registry()
aigrc_utils.display_supply_chain_risk_sunburst(sunburst_df)

