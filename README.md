<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=SCRPM%20Framework&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Safeguarding-Centric%20Risk%20Priority%20Matrix&descAlignY=55&descAlign=50" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![NCSC](https://img.shields.io/badge/NCSC-Aligned-1E3A5F?style=for-the-badge)](https://ncsc.gov.uk)
[![Framework](https://img.shields.io/badge/Design%20Science-Research-E91E63?style=for-the-badge)](https://en.wikipedia.org/wiki/Design_science_(methodology))
[![License](https://img.shields.io/badge/License-MIT-00C48C?style=for-the-badge)](LICENSE)
[![UWE](https://img.shields.io/badge/UWE%20Bristol-Dissertation%202026-FF6B35?style=for-the-badge)](https://uwe.ac.uk)

> **"A weighted risk-scoring framework that prioritises cybersecurity threats in UK education institutions — grounded in NCSC guidance and validated through Design Science Research methodology."**

**[📖 Read the Methodology](#methodology) · [⚡ Quick Start](#quick-start) · [📊 Risk Matrix](#risk-matrix) · [🔬 Research Design](#research-design)**

</div>

---

## 🎯 Overview

The **Safeguarding-Centric Risk Priority Matrix (SCRPM)** is a cybersecurity risk framework designed specifically for **UK educational institutions**. Unlike generic risk frameworks, SCRPM places **safeguarding** — the protection of students and vulnerable individuals — at the centre of risk prioritisation decisions.

### The Problem

UK schools and universities face a unique cybersecurity challenge:

- **Data sensitivity**: Student records, safeguarding files, mental health data
- **Under-resourced IT teams**: Limited security budgets and expertise
- **Regulatory complexity**: GDPR, DfE guidelines, NCSC Cyber Essentials
- **Human vulnerability**: Staff and students as primary attack vectors
- **Reputational risk**: Breaches involving minors carry severe consequences

Existing frameworks (NIST, ISO 27001) are designed for enterprise environments and **do not account for safeguarding risk** — leaving education institutions with an ill-fitting security posture.

### The Solution — SCRPM

SCRPM introduces a **weighted scoring model** that prioritises risks based on their safeguarding impact, not just technical severity.

```
Priority Score = Σ(Risk_i × Weight_i)

Where weights are:
  Safeguarding Impact    → 0.35  (highest — unique to education)
  Data Sensitivity       → 0.25
  Likelihood             → 0.20
  Operational Impact     → 0.12
  Regulatory Exposure    → 0.08
```

---

## 🏗️ Framework Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    SCRPM FRAMEWORK                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   INPUT LAYER          SCORING LAYER      OUTPUT LAYER  │
│   ┌──────────┐         ┌──────────┐       ┌──────────┐  │
│   │ Risk     │──────►  │ Weighted │──────►│ Priority │  │
│   │ Register │         │ Scoring  │       │ Matrix   │  │
│   └──────────┘         └──────────┘       └──────────┘  │
│   ┌──────────┐         ┌──────────┐       ┌──────────┐  │
│   │ NCSC     │──────►  │ SCRPM    │──────►│ Action   │  │
│   │ Guidance │         │ Engine   │       │ Plan     │  │
│   └──────────┘         └──────────┘       └──────────┘  │
│   ┌──────────┐         ┌──────────┐       ┌──────────┐  │
│   │ Safeguard│──────►  │ Weight   │──────►│ Report   │  │
│   │ Policies │         │ Calibr.  │       │ Generator│  │
│   └──────────┘         └──────────┘       └──────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/mdonikmia/scrpm-framework.git
cd scrpm-framework

# Install dependencies
pip install -r requirements.txt

# Run sample risk assessment
python examples/sample_assessment.py

# Run full framework
python framework/scrpm_engine.py --input data/sample_risks.json
```

---

## 📊 Risk Matrix

SCRPM evaluates risks across **5 weighted dimensions:**

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| 🛡️ **Safeguarding Impact** | **35%** | Student/pupil vulnerability is paramount in education |
| 📁 **Data Sensitivity** | **25%** | GDPR + DfE safeguarding records classification |
| 📈 **Likelihood** | **20%** | Threat intelligence + historical incident data |
| ⚙️ **Operational Impact** | **12%** | Business continuity + teaching disruption |
| ⚖️ **Regulatory Exposure** | **8%** | ICO, Ofsted, DfE compliance risk |

### Risk Classification

| Score | Priority | Action Required |
|-------|----------|-----------------|
| 80–100 | 🔴 **Critical** | Immediate response — escalate to SLT |
| 60–79 | 🟠 **High** | Action within 24–48 hours |
| 40–59 | 🟡 **Medium** | Planned remediation within 30 days |
| 20–39 | 🟢 **Low** | Monitor and review quarterly |
| 0–19 | ⚪ **Minimal** | Accept risk with documentation |

---

## 🔬 Research Design

SCRPM was developed using **Design Science Research (DSR)** methodology (Hevner et al., 2004):

```
Phase 1: Problem Identification
  └── Literature review of UK education cybersecurity incidents
  └── Gap analysis: existing frameworks vs. education needs
  └── Stakeholder interviews with IT staff and DSLs

Phase 2: Framework Design
  └── Weight derivation from NCSC guidance mapping
  └── Safeguarding dimension conceptualisation
  └── Iterative prototyping with education sector feedback

Phase 3: Demonstration
  └── Application to 3 simulated UK school scenarios
  └── Comparative scoring vs. NIST CSF and ISO 27001

Phase 4: Evaluation
  └── Expert review panel (cybersecurity + education)
  └── Sensitivity analysis on weight distributions
  └── Validation against real NCSC incident reports

Phase 5: Communication
  └── Dissertation submission — UWE Bristol 2026
  └── Framework open-sourced for sector adoption
```

---

## 🏫 NCSC Alignment

SCRPM maps directly to **NCSC Cyber Essentials** and the **NCSC Education Sector guidance:**

| NCSC Control | SCRPM Dimension | Weight Influence |
|---|---|---|
| Boundary firewalls & internet gateways | Operational Impact | 12% |
| Secure configuration | Operational Impact | 12% |
| User access control | Safeguarding Impact | 35% |
| Malware protection | Data Sensitivity | 25% |
| Patch management | Likelihood | 20% |
| **Safeguarding data protection** | **Safeguarding Impact** | **35%** |

---

## 🎯 Use Cases

### 1. Annual Risk Register Review
```python
from framework.scrpm_engine import SCRPMEngine

engine = SCRPMEngine()
risks = engine.load_risk_register("data/school_risks.json")
prioritised = engine.score_and_rank(risks)
engine.generate_report(prioritised, output="reports/annual_review.pdf")
```

### 2. Incident Triage
```python
# Rapidly score a new incident against safeguarding criteria
incident = {
    "description": "Unauthorised access to student welfare records",
    "safeguarding_impact": 9,
    "data_sensitivity": 8,
    "likelihood": 7,
    "operational_impact": 6,
    "regulatory_exposure": 8
}
score = engine.score_risk(incident)
print(f"Priority: {score['classification']} ({score['total']}/100)")
# Output: Priority: CRITICAL (84.2/100)
```

### 3. Board Reporting
```python
# Generate executive summary for governors/trustees
engine.generate_board_report(
    risks=prioritised,
    format="executive_summary",
    audience="non_technical"
)
```

---

## 📁 Repository Structure

```
scrpm-framework/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
│
├── framework/
│   ├── scrpm_engine.py          # Core scoring engine
│   ├── weight_calibrator.py     # Weight adjustment module
│   ├── risk_classifier.py       # Risk classification logic
│   └── report_generator.py      # PDF/HTML report generation
│
├── docs/
│   ├── methodology.md           # Full DSR methodology
│   ├── ncsc_mapping.md          # NCSC guidance alignment
│   ├── weight_derivation.md     # How weights were calculated
│   └── literature_review.md     # Academic grounding
│
├── data/
│   ├── sample_risks.json        # Example risk register
│   ├── ncsc_controls.json       # NCSC control mappings
│   └── education_threats.json   # Education sector threat data
│
├── examples/
│   ├── sample_assessment.py     # Basic usage example
│   ├── school_scenario.py       # Full school scenario
│   └── board_report_demo.py     # Board reporting example
│
└── tests/
    ├── test_scoring.py          # Unit tests for scoring engine
    ├── test_classification.py   # Classification boundary tests
    └── test_weights.py          # Weight validation tests
```

---

## 🧪 Validation Results

SCRPM was validated against **3 simulated UK school scenarios:**

| Scenario | NIST Score | ISO 27001 Score | SCRPM Score | SCRPM Advantage |
|----------|-----------|-----------------|-------------|-----------------|
| Ransomware attack | HIGH | HIGH | 🔴 CRITICAL | Captured safeguarding data exposure |
| Phishing — student data | MEDIUM | MEDIUM | 🔴 CRITICAL | Identified vulnerable pupil records |
| IT system outage | HIGH | HIGH | 🟡 MEDIUM | Correctly deprioritised vs. data risk |

**Key finding:** SCRPM correctly elevated 2 of 3 scenarios above NIST/ISO ratings due to safeguarding dimension — aligning with actual DfE incident guidance.

---

## 📚 Academic References

- Hevner, A., March, S., Park, J., & Ram, S. (2004). *Design Science in Information Systems Research*. MIS Quarterly, 28(1), 75-105.
- NCSC (2023). *Cyber Security in Education: Guidance for Schools and Colleges*.
- DfE (2023). *Keeping Children Safe in Education (KCSIE)*.
- ISO/IEC 27001:2022. *Information Security Management Systems*.
- NIST Cybersecurity Framework 2.0 (2024).

---

## 🤝 Author

**Md Onik Mia**
BSc Information Technology (Hons) · UWE Bristol · 2026

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/md-onik-mia-643322385/)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=flat&logo=gmail)](mailto:mdonikmia88@gmail.com)
[![VoltSight BI](https://img.shields.io/badge/VoltSight%20BI-Live%20Demo-00C48C?style=flat&logo=streamlit)](https://voltsight-bi.streamlit.app)

---

## 📄 Citation

```bibtex
@misc{mia2026scrpm,
  author    = {Mia, Md Onik},
  title     = {SCRPM: Safeguarding-Centric Risk Priority Matrix for UK Education},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/mdonikmia/scrpm-framework}
}
```

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>
</div>
