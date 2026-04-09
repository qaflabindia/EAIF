import grc_utils
import importlib
importlib.reload(grc_utils)
grc_utils.inject_framework_style()
grc_utils.display_deliverable_anchor('MSC-09', 'AI-SBOM Multi-Modal Lineage Audit')

portfolio_df = grc_utils.generate_expert_multimodal_portfolio_data()
grc_utils.display_foundation_model_ecosystem_sunburst(portfolio_df)


grc_utils.display_msc_09_sbom_registry(portfolio_df)


_ , sunburst_df = grc_utils.generate_vulnerability_vex_registry()
grc_utils.display_supply_chain_risk_sunburst(sunburst_df)

