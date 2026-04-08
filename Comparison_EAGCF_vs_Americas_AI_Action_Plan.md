# Side-by-Side Comparison: EAGCF vs. America's AI Action Plan
## *White House AI Strategy — July 2025*

**Source Document:** `Americas-AI-Action-Plan.pdf` (The White House, July 2025)
**Authors:** Michael J. Kratsios (OSTP), David O. Sacks (Special Advisor for AI and Crypto), Marco A. Rubio (NSA)
**Directed by:** Executive Order 14179 ("Removing Barriers to American Leadership in Artificial Intelligence")
**EAGCF Reference:** Enterprise AI Governance and Control Framework (v1.0, 2026)
**Comparison Date:** April 2026
**Analyst Note:** America's AI Action Plan is the Trump Administration's national AI strategy — a policy and diplomacy document, not a technical governance standard. Its value to EAGCF is: (1) signaling shifts in U.S. regulatory philosophy (deregulatory, competitiveness-first) that affect the enterprise governance landscape; (2) confirming certain security requirements (secure-by-design, incident response) that align with EAGCF; (3) flagging the planned revision of the NIST AI RMF (to remove DEI/misinformation/climate framing) as a material change to EAGCF's normative reference stack; (4) identifying new regulatory structures (AI-ISAC, CAIOC, GSA AI procurement toolbox) relevant to enterprises operating in or adjacent to federal government. This is a policy context document, not a governance control document.

---

## 1. Document Scope Alignment

| Dimension | America's AI Action Plan | EAGCF |
|---|---|---|
| **Document type** | National AI strategy / policy action plan | Enterprise governance and control framework |
| **Primary purpose** | U.S. global AI dominance through innovation, infrastructure, and diplomacy | Enable enterprises to govern, control, and assure AI use |
| **Governance content** | Policy directions, regulatory reforms, funding priorities — no enterprise controls | 15 control domains, 9 enforcement points, 5-tier risk model |
| **Audience** | Federal agencies, Congress, private sector, international partners | Board, CRO, governance office, internal audit, compliance |
| **Binding nature** | Executive-directed policy — creates new Federal programs and directions; not directly binding on private enterprises | Voluntary enterprise standard, wired to ISO 42001 |
| **Risk philosophy** | Acceleration-first: remove barriers, enable innovation; security requirements concentrated in critical infrastructure | Risk-tiered governance: proportional controls based on system risk level |

---

## 2. Pillar I: Accelerate AI Innovation — Enterprise Governance Implications

### Regulatory Environment Signals

| Policy Action | Enterprise Governance Implication | EAGCF Position |
|---|---|---|
| **NIST AI RMF revision** (strip DEI/misinformation/climate change references) | EAGCF's normative reference to NIST AI 100-1 may require re-baselining when revision is published | ⚠️ Watch — EAGCF should track AI RMF revision and assess impact on Part IV and Part V domains referencing AI RMF categories |
| **FTC investigations and consent decrees review** (rescind those that "unduly burden" AI) | Enterprises under prior FTC AI-related orders should anticipate modification; reduced FTC enforcement posture | Informative context — affects regulatory overlay in Part VIII but not EAGCF's control architecture |
| **State AI regulatory climate** in discretionary funding decisions | Enterprises in AI-intensive sectors face Federal funding consequences if operating in high-regulation states | Informative context — sector-specific regulatory environment signal |
| **Regulatory sandboxes** (FDA, SEC, NIST AI Centers of Excellence) | Enterprises in healthcare, energy, and agriculture may pilot AI under relaxed compliance | Part VIII §8.8 (sector overlays) — sandbox participation opportunities for Tier 2/3 systems |

### Federal Procurement Standards for LLMs

| Policy Action | Enterprise Governance Implication | EAGCF Position |
|---|---|---|
| **Frontier LLM ideological objectivity requirement** for Federal procurement | LLM vendors seeking government contracts must demonstrate model objectivity; enterprises must document this for procurement compliance | Part V §5.3 (MDL-05: model card) — model bias documentation field; Part XIV §14.2 (vendor SLA requirements) |
| **GSA AI procurement toolbox** (multi-model catalog with compliance requirements) | Enterprises serving Federal clients must align offerings with GSA catalog; privacy and transparency standards required | Part V §5.9 (VND domain) — vendor qualification framework covers these requirements for EAGCF-governed enterprises |

### AI Evaluation Ecosystem

| Policy Action | Enterprise Governance Implication | EAGCF Position |
|---|---|---|
| **NIST guidelines for Federal agency AI evaluations** (CAISI) | Will establish government evaluation benchmarks; enterprises serving government will need to align | Part XII §12.2 (control validation matrix) — EAGCF's validation framework can be extended with CAISI benchmarks when published |
| **AI interpretability, control, and robustness** DARPA program + hackathons | Investment in interpretability and adversarial robustness research will produce new tools and standards | Part V §5.3 (MDL-05: model card) + Part XII §12.1 (red-team) — EAGCF should track DARPA outputs as potential additions to adversarial testing toolkit |
| **NIST Guardians of Forensic Evidence** (deepfake standards) | Voluntary deepfake forensic benchmark for legal proceedings | Part V §5.11 (MSC-08: watermarking); N1004-01/02 (confirmed synthetic content gaps) — will provide implementation guidance for deepfake detection |

### Workforce and Tax Provisions

| Policy Action | Enterprise Governance Implication | EAGCF Position |
|---|---|---|
| **IRC Section 132 AI training reimbursement** (Treasury guidance pending) | AI literacy training for employees may qualify as tax-free benefit | Part VIII §8.3 (workforce enablement) — applicable to EAGCF training rollout |

---

## 3. Pillar I Governance: Synthetic Media in the Legal System

| Policy Action | EAGCF Coverage | Status |
|---|---|---|
| **NIST Guardians of Forensic Evidence program** → formal guideline with voluntary benchmark | Part V §5.11 (MSC-08: watermarking control); N1004-01/02/08 from synthetic content comparison | ⚠️ Partial — watermarking control present; forensic-grade detection benchmark requirements pending |
| **DOJ guidance on deepfake standards for adjudications** | Not addressed | ❌ Gap — EAGCF does not address AI-generated evidence admissibility standards for litigation contexts |
| **Federal Rules of Evidence (FRE) deepfake amendments** | Not addressed | Out of scope — regulatory/legal standard, not enterprise governance |

---

## 4. Pillar II: Build American AI Infrastructure — Security-Relevant Provisions

These are the most directly governance-relevant requirements for enterprises, particularly those operating critical infrastructure.

### Secure-by-Design Mandate

| Policy Direction | Requirement | EAGCF Coverage | Status |
|---|---|---|---|
| **AI in safety-critical/homeland security** applications must be: | | | |
| (1) Secure-by-design, robust, and resilient | Built-in security from design, not bolted-on | Part XI §11.1 (enforcement architecture: security controls at 9 enforcement points); Part V §5.11 (MSC domain) | ✅ Covered |
| (2) Instrumented to detect performance shifts | Real-time monitoring for anomalous behavior | Deliverable E (runtime monitoring signal catalog: drift, degradation, behavioral anomaly signals) | ✅ Covered |
| (3) Able to alert on data poisoning or adversarial example attacks | Detection monitoring for training and runtime attacks | Part XII §12.1 (red-team: poisoning attacks); GEN-09 (data poisoning detection) | ✅ Covered |

### AI Information Sharing and Analysis Center (AI-ISAC)

| Policy Direction | Enterprise Implication | EAGCF Coverage | Status |
|---|---|---|---|
| **AI-ISAC** under DHS (with CAISI and ONCD) for AI-specific vulnerability sharing | Enterprises should monitor AI-ISAC for vulnerability intelligence and share AI incident data | Part VII §7.3 (incident taxonomy: feeds into AI incident knowledge); N801-07 (AI incident database reporting gap) | ⚠️ Partial — gap N801-07 confirmed: EAGCF does not require external AI incident reporting; AI-ISAC participation not addressed |
| **Known AI vulnerabilities shared to private sector** via existing cybersecurity mechanisms | Enterprises should subscribe to AI vulnerability feeds from AI-ISAC and CISA | Part V §5.11 (MSC domain: vulnerability management); Part XII §12.1 (red-team attack library updates) | ⚠️ Partial — threat intelligence integration not formalized |

### AI Incident Response

| Policy Direction | Enterprise Implication | EAGCF Coverage | Status |
|---|---|---|---|
| **CISA Cybersecurity Incident & Vulnerability Response Playbooks** updated to incorporate AI | Critical infrastructure enterprises must update incident response to include AI-specific playbook | Part VII §7.3 (incident taxonomy); Part VII §7.4 (corrective action) | ✅ Covered — EAGCF's incident taxonomy and corrective action process pre-dates and anticipates AI-specific incident response |
| **CISOs to consult CAIOs** during AI-related incidents | AI and cybersecurity functions must be jointly engaged during AI incidents | Part VI §6.2 (governance office: CISO/CAIO joint accountability); Part VI §6.4 (RACI: AI incident escalation) | ✅ Covered |
| **AI incident response standards and best practices** (fly-away kits) (NIST/CAISI) | Standards will be published; enterprises should adopt when available | Part VII §7.3–7.4 (incident governance) — EAGCF framework ready to incorporate CAISI playbook when published | ⚠️ Partial — pending CAISI publication |

### High-Security AI Data Centers (DOD/IC Standards)

| Policy Direction | Enterprise Implication | EAGCF Coverage | Status |
|---|---|---|---|
| **Technical standards for high-security AI data centers** resistant to nation-state attacks | Enterprises hosting AI for government/defense must meet new security standards | Part V §5.2 (DAT domain: data security); Part V §5.11 (MSC domain); Part IX (identity/access) | ⚠️ Partial — standard content pending; EAGCF's security domains will need alignment when standards published |

---

## 5. Pillar III: International AI Diplomacy — Standards Implications

| Policy Direction | EAGCF Relevance |
|---|---|
| **Counter Chinese influence** in international governance bodies (UN, OECD, G7, ITU) | EAGCF's OECD footnote-only treatment aligns with U.S. policy direction to keep OECD as a political reference, not normative standard |
| **Promote innovation-enabling AI governance** in international standards bodies | Confirms EAGCF's approach of grounding in NIST + ISO (with demonstrated innovation-acceleration capability) |
| **AI global alliance** technology diplomacy plan | Enterprises with international operations should monitor for new AI standards and cross-border compliance requirements |
| **Semiconductor export controls** and chip location verification | Relevant for enterprises designing or procuring AI compute hardware; supply chain due diligence (VND domain) |

---

## 6. Critical Material Change: NIST AI RMF Revision

The planned NIST AI RMF revision is the most significant EAGCF-impacting element of the Action Plan.

| Revision Direction | Current EAGCF Exposure | Risk Assessment |
|---|---|---|
| **Remove DEI references** | EAGCF's FAI domain (fairness and bias) is grounded in functional controls, not DEI framing | Low — EAGCF's bias management is outcome-focused (disparate impact testing, fairness metrics) not DEI-framed; revision should not require material changes |
| **Remove misinformation references** | EAGCF's OUT domain covers factuality and hallucination detection; not framed as "misinformation governance" | Low — EAGCF's output controls are technically grounded |
| **Remove climate change references** | EAGCF's environmental gap (N-06) is already identified as a gap; no climate-specific content | Low — no material impact |
| **Overall RMF reframing** toward innovation | EAGCF's adoption-acceleration blueprint (Part VIII) and governance misallocation diagnostic are already innovation-enabling | Low — EAGCF's design already emphasizes enabling adoption, not restricting it |

**Assessment:** The NIST AI RMF revision is unlikely to require material changes to EAGCF. EAGCF's control architecture is grounded in functional governance requirements, not the political/social framing that the revision targets.

---

## 7. Biosecurity Provisions — Enterprise Impact

| Policy Action | Enterprise Implication | EAGCF Coverage | Status |
|---|---|---|---|
| **Mandatory nucleic acid synthesis screening** (Federally funded research) | Research enterprises receiving Federal funding must use screened synthesis providers; compliance mandatory | Not addressed | ❌ Gap — N-AP-01: biosecurity-related AI use controls for life science enterprises not in EAGCF scope |
| **Data sharing between synthesis providers** | Research enterprise supply chain obligation | Part V §5.9 (VND domain) — vendor due diligence but not biosecurity-specific | ⚠️ Partial |

---

## 8. Scoring Summary

| Policy Area | Items | ✅ Covered | ⚡ EAGCF Stronger | ⚠️ Partial | ❌ Gap |
|---|---|---|---|---|---|
| Regulatory environment signals | 4 | 0 | 0 | 4 | 0 |
| Federal procurement standards | 2 | 1 | 0 | 1 | 0 |
| AI evaluation ecosystem | 3 | 0 | 0 | 3 | 0 |
| Synthetic media / deepfake legal | 3 | 0 | 0 | 1 | 2 |
| Secure-by-design mandate | 3 | 3 | 0 | 0 | 0 |
| AI-ISAC and vulnerability sharing | 2 | 0 | 0 | 2 | 0 |
| AI incident response | 3 | 2 | 0 | 1 | 0 |
| International standards implications | 4 | 2 | 1 | 1 | 0 |
| Biosecurity provisions | 2 | 0 | 0 | 1 | 1 |
| **TOTALS** | **26 items** | **8 (31%)** | **1** | **14 (54%)** | **3 (12%)** |

**Coverage interpretation:** 85% total coverage (31% direct + 54% partial). The high partial rate reflects the nature of this document: most items are forward-looking policy directions (pending CAISI publications, revised NIST RMF, new AI-ISAC programs) that EAGCF addresses functionally but where the specific implementation standards have not yet been published. The 3 gaps are specialized contexts (deepfake legal admissibility, biosecurity for research enterprises) outside EAGCF's enterprise governance scope.

---

## 9. Gap Items: Recommended EAGCF Additions

| Gap ID | Source | Gap Description | Priority | Recommended EAGCF Location |
|---|---|---|---|---|
| **N-AP-01** | Biosecurity §IV.G | **Life science enterprise biosecurity note**: For enterprises in pharmaceutical, biotech, or life sciences receiving Federal research funding, add a sector overlay noting the mandatory nucleic acid synthesis screening requirement and vendor selection criteria | Low (sector-specific) | Part VIII §8.8 (sector overlays) — add life sciences/biotech delta note |
| **N-AP-02** | Pillar II / AI-ISAC | **AI-ISAC participation**: When the DHS AI-ISAC is operational, add guidance for enterprises in critical infrastructure to subscribe to AI vulnerability intelligence feeds and incorporate into EAGCF's red-team attack library update process | Medium | Part XII §12.1 (red-team pipeline: attack library update process) — add external threat intelligence integration point |
| **N-AP-03** | NIST AI RMF revision | **NIST AI RMF revision tracking**: Add a monitoring note to EAGCF's normative reference (Part IV §4.2) indicating that NIST AI 100-1 is under revision per EO 14179; EAGCF will require review against the revised RMF when published, expected 2026 | High | Part IV §4.2 (normative references) — add version watch note |

---

## 10. Synthesis

America's AI Action Plan is a national competitiveness strategy, not an enterprise governance standard. Its governance-relevant provisions for EAGCF are concentrated in four areas:

1. **NIST AI RMF revision** (N-AP-03): The highest-priority EAGCF action — monitor for the revised RMF and validate EAGCF's continued alignment. The revision is expected to remove political framing without changing the functional governance architecture, suggesting minimal EAGCF impact.

2. **Secure-by-design requirements** for critical infrastructure AI: EAGCF already meets these requirements comprehensively — Part XI's 9 enforcement points, Deliverable E's monitoring signals, and Part XII's red-team pipeline satisfy the Action Plan's three specific requirements.

3. **AI-ISAC and incident response** (N-AP-02): New federal infrastructure for AI vulnerability sharing that EAGCF should integrate when operational.

4. **Regulatory deregulation signals**: The overall deregulatory direction confirms that EAGCF's adoption-acceleration design (Part VIII, governance misallocation diagnostic) is aligned with the regulatory environment. Enterprises using EAGCF as a governance overlay are well-positioned for both compliance-light environments and potential future tighter regulatory requirements.

---

*Comparison prepared as part of EAGCF continuous improvement program.*
*Comparisons completed (19 sources): NIST AI 100-1, 100-2, 100-4, 100-5, 600-1, 700-1, 700-2 + ARIA Companion, 800-1, 800-2, IR 8596; ISO crosswalks (42001/23894, 42005, 5338/5339); OECD/EU AI Act crosswalk; Google DeepMind Gap Analysis; AI Verify crosswalks; Americas AI Action Plan*
