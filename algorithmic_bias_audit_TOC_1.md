# Algorithmic Bias Audit — Table of Contents
### Version 4.0 | 12 Phases | 130 Topics & Deliverables

---

## PHASE 0 — Problem Formulation, Causal Thinking, and Legal Framing
12 Topics | Foundation Layer

    0.1   Correlation vs Causation: DAGs and the Data Generating Process
    0.2   Confounders, Proxies, Mediators, and Colliders
    0.3   Observational vs Intervention Thinking (Pearl's Causal Ladder)
    0.4   Simpson's Paradox and Aggregation Traps
    0.5   Measurement Validity: Does Your Outcome Measure What You Think?
    0.6   Problem Formulation Bias: Target Definition and Framing Effects
    0.7   Label vs Outcome Mismatch and Proxy Target Selection
    0.8   Counterfactual Fairness
    0.9   Structural Causal Models (SCMs) and Path-Specific Effects
    0.10  Mediation Analysis for Bias
    0.11  Legal Scaffolding: Disparate Treatment vs Disparate Impact
    0.12  Translating Legal Concepts into Audit Hypotheses and Evidentiary Thresholds

---

## PHASE 1 — System Anatomy: Where Bias Can Appear
7 Topics | Orientation Layer

    1.1   The Full Pipeline: Problem → Data → Model → Decision → Product
    1.2   Human-in-the-Loop and Governance Insertion Points
    1.3   Scope of Systems: Classifiers, Rankers, Recommenders, Moderation, LLMs, Search
    1.4   Feedback Loops: Conceptual Introduction
    1.5   Distribution Shift and Concept Drift: Definitions
    1.6   Sociotechnical Context: Organizational and Procurement Factors
    1.7   Operational Constraints That Shape Audit Feasibility

---

## PHASE 2 — Failure Mode Taxonomy: Mechanisms
16 Topics | Diagnostic Layer

    2.1   Sampling Bias and Coverage Gaps
    2.2   Historical and Structural Bias Encoded in Labels
    2.3   Measurement Error and Systematic Annotation Bias
    2.4   Annotation Systems: Instruction Bias, Disagreement, and Aggregation
    2.5   Proxy Variable Leakage
    2.6   Objective Function Misspecification
    2.7   Shortcut Learning and Spurious Correlations
    2.8   Representation Collapse and Underfitting Minority Patterns
    2.9   Aggregation Bias
    2.10  Evaluation Bias
    2.11  Deployment-Induced Bias: Feedback Loop Mechanisms (Formal)
    2.12  Interaction Bias
    2.13  Temporal Bias and Cohort Effects
    2.14  Delayed Feedback Bias and Policy Lag
    2.15  Long-Run Harm Accumulation
    2.16  Economic and Incentive Structures as Bias Mechanisms

---

## PHASE 3 — Detection: Designing Experiments That Reveal Bias
14 Topics | Empirical Toolkit

    3.1   Subgroup Performance Slicing
    3.2   Intersectional Analysis
    3.3   Counterfactual Testing and Controlled Attribute Perturbation
    3.4   The 4/5ths Rule (Adverse Impact Analysis)
    3.5   Propensity Score and Reweighting Diagnostics
    3.6   Distribution Shift and Drift Detection by Subgroup
    3.7   A/B Testing and Randomized Controlled Fairness Experiments
    3.8   Adversarial and Stress Testing
    3.9   Interaction and Behavioral Analytics for Rankers and Recommenders
    3.10  Logging Design and Privacy-Aware Telemetry
    3.11  Evaluation Dataset and Benchmark Bias
    3.12  Test Set Leakage and Hidden Subgroup Failures
    3.13  Confidence Intervals and Hypothesis Testing for Fairness Metrics
    3.14  Power Analysis and Small Sample Problems in Bias Detection

---

## PHASE 4 — Assessment: Metrics, Trade-offs, and Decision Rules
8 Topics | Quantification Layer

    4.1   Demographic Parity
    4.2   Equalized Odds
    4.3   Predictive Parity and Calibration
    4.4   Error Rate Decompositions by Subgroup
    4.5   Ranking and Recommender-Specific Metrics
    4.6   Individual Fairness
    4.7   The Impossibility Theorems: Named and Precise
    4.8   Metric Selection Rules: Tying Metrics to Legal and Business Objectives

---

## PHASE 5 — Mitigation: Fixing Bias at the Right Layer
9 Topics | Intervention Layer

    5.1   Preprocessing: Reweighting and Resampling
    5.2   Preprocessing: Label Repair and Synthetic Augmentation
    5.3   Representation Fixes: Debiasing Embeddings and Feature Transforms
    5.4   In-Processing: Constrained Optimization and Fairness Regularizers
    5.5   In-Processing: Adversarial Debiasing
    5.6   Post-Processing: Threshold Adjustment and Calibrated Re-ranking
    5.7   Causal Debiasing: Intervening on the Causal Graph
    5.8   System-Level and Interface-Level Fixes
    5.9   The Fairness-Accuracy Pareto Frontier and Mitigation Side-Effects

---

## PHASE 6 — LLMs and Generative Systems
8 Topics | Non-Deterministic Layer

    6.1   Pretraining Data Signals and Representational Harm
    6.2   Tokenization Bias
    6.3   Prompt Engineering and Prompt Sensitivity Tests
    6.4   RLHF Bias: Reward Model Bias and Labeler Composition Effects
    6.5   Safety Filters, Guardrails, and Asymmetric Application
    6.6   RAG-Based Bias: Retrieval Layer as an Audit Target
    6.7   Measurement for Stochastic Systems: Sampling and Harm Scoring
    6.8   LLM-Specific Mitigation: RLHF Design, Prompt Templates, Output Filtering

---

## PHASE 7 — Production Reality: Monitoring, Drift, and Structural Forces
12 Topics | Operational Layer

    7.1   Monitoring Architecture: Metrics, Dashboards, and Per-Group Baselines
    7.2   Population Drift vs Concept Drift: Distinct Monitoring Strategies
    7.3   Causal Feedback Loops: Formal Models and Long-Run Effects
    7.4   Remediation Playbooks: Rollback, Throttling, and Targeted Retraining
    7.5   Human-in-the-Loop Corrections and Escalation Rules
    7.6   Privacy and Logging Trade-offs in Production
    7.7   Post-Deployment Continuous Audit Design
    7.8   Revenue Optimization vs Fairness: The Incentive Structure Problem
    7.9   Marketplace Dynamics and Strategic Bias
    7.10  Data Poisoning and Adversarial Manipulation of Fairness
    7.11  Prompt Injection and Adversarial LLM Manipulation
    7.12  Attack Surface Mapping for Deployed Systems

---

## PHASE 8 — Systems Beyond Classifiers: Ranking, Recommendation, Moderation, Search
10 Topics | Scope Expansion Layer

    8.1   Exposure and Fairness in Ranking
    8.2   Long-Tail Access and Discovery Fairness in Recommenders
    8.3   Content Moderation: Automation and Human Escalation Trade-offs
    8.4   Amplification Risk and Virality Mechanics
    8.5   Multi-Stakeholder Fairness: Creators vs Consumers
    8.6   Measurement Approaches Unique to These Systems
    8.7   Search Systems: Query Bias and Intent Misinterpretation
    8.8   Embedding Bias in Retrieval Systems
    8.9   Semantic Retrieval Distortion and Knowledge Gaps
    8.10  RAG Pipeline Bias as an End-to-End Audit Problem

---

## PHASE 9 — Business, Legal, and Regulatory Framing
7 Topics | Consequence Layer

    9.1   Legal Risk Mapping: Disparate Treatment, Disparate Impact, Documentation
    9.2   Regulatory Landscape: Named Frameworks and Obligations
          — EU AI Act, NIST RMF, ISO 42001, IEEE 7010, EEOC, CFPB
    9.3   Algorithmic Impact Assessments
    9.4   Quantifying Business Impact: Revenue, Churn, and Brand Risk
    9.5   Stakeholder Communication: Executive, Legal, Engineering, Public
    9.6   ROI on Mitigation: Cost vs Risk Reduction
    9.7   Vendor and Third-Party Model Risk

---

## PHASE 10 — Governance, Audit Process, and Tooling
12 Topics | Institutional Layer

    10.1  The Audit Lifecycle: Scope, Evidence, Analysis, Remediation, Verification
    10.2  Documentation Standards: Datasheets, Model Cards, Decision Logs
    10.3  Roles and Responsibilities: Audit Teams, Ethics Boards, Champions
    10.4  Community Participation in Audit Design
    10.5  Fairlearn: Capabilities, Limitations, and Appropriate Use
    10.6  Aequitas: Bias Auditing for Decision Systems
    10.7  What-If Tool: Exploratory Fairness Analysis
    10.8  LLM Evaluation Frameworks: HELM and Model-Level Evaluation
    10.9  Dataset Auditing Tools and Annotation Quality Assessment
          — Cleanlab, Perspective API, Slicefinder, Manifold
    10.10 Experiment Tracking for Fairness: Versioning and Reproducibility
          — MLflow, Weights and Biases
    10.11 Third-Party Audits and Red-Team Engagements
    10.12 Integrating Fairness into the Development Lifecycle

---

## PHASE 11 — Case Studies: Documented Systems and Documented Failures
5 Cases | Grounding Layer

    11.1  Amazon Hiring Algorithm
          Mechanism: Historical label bias + proxy variable leakage
    11.2  COMPAS Recidivism Tool
          Mechanism: Objective misspecification + measurement validity
          + Chouldechova impossibility theorem in practice
    11.3  Obermeyer et al. Healthcare Algorithm (Science, 2019)
          Mechanism: Aggregation bias + cost as proxy for need
    11.4  Apple Card Gender Discrimination
          Mechanism: Proxy variable leakage + disparate impact without intent
    11.5  Facial Recognition: NIST FRVT
          Mechanism: Sampling and coverage gaps + representation collapse

---

## PHASE 12 — Capstone: End-to-End Audit
6 Deliverables | Full Delivery Track

    12.1  Audit Scoping Document
    12.2  Bias Detection Report
    12.3  Metric Assessment
    12.4  Mitigation Strategy
    12.5  Post-Mitigation Verification Plan
    12.6  Stakeholder Communication Package
          — Executive Summary / Legal Memo / Technical Appendix

---

## PHASE COUNT SUMMARY

    Phase  0    Problem Formulation, Causal Thinking, Legal Framing    12 topics
    Phase  1    System Anatomy                                           7 topics
    Phase  2    Failure Mode Taxonomy                                   16 topics
    Phase  3    Detection Methods                                       14 topics
    Phase  4    Assessment and Metrics                                   8 topics
    Phase  5    Mitigation Techniques                                    9 topics
    Phase  6    LLMs and Generative Systems                              8 topics
    Phase  7    Production Monitoring and Structural Forces             12 topics
    Phase  8    Ranking, Recommenders, Moderation, Search               10 topics
    Phase  9    Business, Legal, Regulatory                              7 topics
    Phase 10    Governance, Audit Process, Tooling                      12 topics
    Phase 11    Case Studies                                             5 cases
    Phase 12    Capstone Deliverables                                    6 deliverables
                                                               ─────────────────────
                TOTAL                                                  130 items

---

*Algorithmic Bias Audit — Master Lesson Plan v4.0*
*Full lesson content in: algorithmic_bias_audit_v4_master_plan.md*
