import grc_utils
import importlib
importlib.reload(grc_utils)
grc_utils.inject_framework_style()
grc_utils.display_deliverable_anchor('BRD-01', 'Executive Governance KPI Dashboard')

scorecard, treemap_df, incident_df, progress_df = grc_utils.generate_expert_board_kpi_data()
grc_utils.display_executive_governance_scorecard(scorecard)


grc_utils.display_global_risk_portfolio_treemap(treemap_df)


grc_utils.display_red_flag_incident_command(incident_df)


grc_utils.display_domain_progress_radar(progress_df)

