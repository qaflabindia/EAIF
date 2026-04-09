import grc_utils
import importlib
importlib.reload(grc_utils)
grc_utils.inject_framework_style()
grc_utils.display_deliverable_anchor('REG-01', 'Harmonized Compliance Framework')

risk_df, maturity_df = grc_utils.generate_expert_regulatory_register_data()
grc_utils.display_compliance_maturity_radar(maturity_df)


grc_utils.display_enterprise_risk_register_table(risk_df)


# Filter for EU AI Act Annex III systems
eu_high_risk = risk_df[risk_df['Regulation'].str.contains('EU AI Act')]
grc_utils.display_enterprise_risk_register_table(eu_high_risk)

