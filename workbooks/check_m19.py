import aigrc_utils
import importlib
importlib.reload(aigrc_utils)
aigrc_utils.inject_framework_style()
aigrc_utils.display_deliverable_anchor('BRD-01', 'Executive Governance KPI Dashboard')

scorecard, treemap_df, incident_df, progress_df = aigrc_utils.generate_expert_board_kpi_data()
aigrc_utils.display_executive_governance_scorecard(scorecard)


aigrc_utils.display_global_risk_portfolio_treemap(treemap_df)


aigrc_utils.display_red_flag_incident_command(incident_df)


aigrc_utils.display_domain_progress_radar(progress_df)

