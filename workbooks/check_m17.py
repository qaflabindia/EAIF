import aigrc_utils
import importlib
importlib.reload(aigrc_utils)
aigrc_utils.inject_framework_style()
aigrc_utils.display_deliverable_anchor('MSC-09', 'AI-SBOM Multi-Modal Lineage Audit')

portfolio_df = aigrc_utils.generate_expert_multimodal_portfolio_data()
aigrc_utils.display_foundation_model_ecosystem_sunburst(portfolio_df)


aigrc_utils.display_msc_09_sbom_registry(portfolio_df)


_ , sunburst_df = aigrc_utils.generate_vulnerability_vex_registry()
aigrc_utils.display_supply_chain_risk_sunburst(sunburst_df)

