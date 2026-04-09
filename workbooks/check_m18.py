import aigrc_utils
import importlib
importlib.reload(aigrc_utils)
aigrc_utils.inject_framework_style()
aigrc_utils.display_deliverable_anchor('REG-01', 'Harmonized Compliance Framework')

risk_df, maturity_df = aigrc_utils.generate_expert_regulatory_register_data()
aigrc_utils.display_compliance_maturity_radar(maturity_df)


aigrc_utils.display_enterprise_risk_register_table(risk_df)


# Filter for EU AI Act Annex III systems
eu_high_risk = risk_df[risk_df['Regulation'].str.contains('EU AI Act')]
aigrc_utils.display_enterprise_risk_register_table(eu_high_risk)

