<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=SCRPM%20Framework&fontSize=38&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Safeguarding-Centric%20Risk%20Priority%20Matrix%20for%20UK%20Education&descAlignY=55&descAlign=50" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-15%20Passing-00C48C?style=for-the-badge&logo=pytest&logoColor=white)](#testing)
[![NCSC](https://img.shields.io/badge/NCSC-Aligned-1E3A5F?style=for-the-badge)](https://ncsc.gov.uk)
[![DSR](https://img.shields.io/badge/Design%20Science-Research-E91E63?style=for-the-badge)](https://doi.org/10.2307/25148625)
[![UWE](https://img.shields.io/badge/UWE%20Bristol-Dissertation%202026-FF6B35?style=for-the-badge)](https://uwe.ac.uk)
[![License](https://img.shields.io/badge/License-MIT-00C48C?style=for-the-badge)](LICENSE)

> **"A risk-scoring algorithm that integrates threat severity, resilience capability, and safeguarding impact into a prioritisation decision-support tool — addressing the absence of structured IS mechanisms for translating cross-sector vulnerability analysis into actionable risk management in education."**
>
> — SCRPM Dissertation Abstract, UWE Bristol 2026

**[⚡ Quick Start](#quick-start) · [📊 The Algorithm](#the-algorithm) · [🔬 Research Basis](#research-basis) · [📋 Key Findings](#key-findings) · [🧪 Tests](#testing)**

</div>

---

## 🎯 What Is SCRPM?

The **Safeguarding-Centric Risk Priority Matrix (SCRPM)** is a cybersecurity risk-scoring framework designed specifically for **UK educational institutions** — schools, FE colleges, and universities.

It emerged from a critical research finding: **existing risk frameworks (NIST CSF, ISO 27001) are designed for enterprise environments and do not account for safeguarding risk**, leaving education institutions with an ill-fitting security posture.

SCRPM addresses this by placing **safeguarding** — the statutory duty to protect students and children — at the centre of risk prioritisation.

---

## 📊 The Algorithm

**Formula (Dissertation Chapter 7.3):**

```
SCRPM Score = (Threat Severity × 0.30)
            + (Resilience Deficit × 0.35)
            + (Safeguarding Impact × 0.35)
```

| Dimension | Weight | Rationale |
|---|---|---|
| ⚔️ **Threat Severity** | **30%** | How severe is the attack? |
| 🛡️ **Resilience Deficit** | **35%** | How weak is the institution's cyber capability? |
| 👶 **Safeguarding Impact** | **35%** | What is the risk to student/child welfare? |

**Scale:** All dimensions rated **1–5** → Composite score **1.0–5.0**

### Why These Weights?

The weighting structure encodes the dissertation's central empirical finding:

> *"Per-incident harm in UK education is determined primarily by capability deficits and statutory obligation, NOT attack frequency alone."*
> *(Dissertation Chapter 7.3)*

Resilience Deficit and Safeguarding Impact are weighted **above** Threat Severity (0.35 vs 0.30) because the cross-sector evidence demonstrates that a **moderate threat against a vulnerable, safeguarding-intensive institution** generates substantially greater risk than a **severe threat against a resilient institution with low safeguarding exposure**.

### Risk Classification (Table 5)

| SCRPM Score | Band | Action Required |
|---|---|---|
| **4.0 – 5.0** | 🔴 **CRITICAL** | Immediate escalation to SLT · Invoke incident response plan · Notify DPO |
| **3.0 – 3.9** | 🟠 **HIGH** | Action within 24–48 hours · Document in risk register |
| **2.0 – 2.9** | 🟡 **MODERATE** | Planned remediation within 30 days |
| **1.0 – 1.9** | 🟢 **LOW** | Monitor quarterly · Accept with documentation |

---

## 🔬 Research Basis

### Methodology
- **Type:** BSc (Hons) Information Systems Dissertation — UFCFM5-30-3
- **University:** University of the West of England (UWE) Bristol · 2025/2026
- **Author:** Md Onik Mia
- **Supervisor:** Mark Rhodes
- **Word Count:** 11,992 words
- **Framework:** Design Science Research — Hevner et al. (2004)
- **Artefact Type:** Model (March & Smith, 1995)

### Epistemological Position
**Pragmatic** philosophy + **Critical Realist** ontology, enabling cross-sector comparison of quantitative DSIT survey data with qualitative NCSC/DfE policy analysis.

### Data Sources (6 Source Types Triangulated)

| Source | Type | Key Contribution |
|---|---|---|
| **DSIT (2024)** | Quantitative survey | Breach prevalence across all sectors |
| **NCSC Guidance** | Policy prescription | Cyber controls and standards |
| **DfE (2024) KCSIE** | Statutory guidance | Safeguarding legal obligations |
| **Jisc (2022)** | Sector report | Resilience capability indicators |
| **ICO (2023)** | Enforcement cases | 215 education enforcement actions 2020-2023 |
| **Academic literature** | Theoretical | Hevner, Hollnagel, Teece et al. |

### Research Questions Addressed

| RQ | Question | Key Finding |
|---|---|---|
| **RQ1** | How do cyber incident rates differ across sectors? | Clear gradient: Primary 52% → HE 97% (DSIT, 2024) |
| **RQ2** | Which resilience capabilities vary by sector? | Governance integration is the critical differentiator |
| **RQ3** | How do incidents translate to stability harms? | Four mechanisms: containment, continuity, governance, recovery-learning |
| **RQ4** | Where do policy expectations diverge from practice? | Persistent compliance-capability gap across all sectors |

---

## 📋 Key Findings

### Finding 1: Cyber Breach Prevalence (DSIT, 2024)

```
Primary Schools     ████████████░░░░░░░░  52%
Secondary Schools   ██████████████░░░░░░  71%
FE Colleges         █████████████████░░░  86%
Universities        ████████████████████  97%
```

*Higher prevalence does NOT equal higher institutional risk.*

### Finding 2: The School Vulnerability Inversion (Chapter 6.7)

> Schools face **lower measured breach exposure** (52%) but **higher per-incident vulnerability** than universities, because:
> - Highest safeguarding obligations (KCSIE statutory duties)
> - Weakest cyber resilience capabilities
> - Only **58% conduct formal risk assessments** (vs 90% HE)
> - Only **47% deploy monitoring tools** (vs 87% HE)

```python
# SCRPM demonstrates the inversion:
primary_school = Risk(threat_severity=3, resilience_deficit=5, safeguarding_impact=5)
university     = Risk(threat_severity=5, resilience_deficit=2, safeguarding_impact=1)

# Same threat environment, vastly different SCRPM scores:
engine.score_risk(primary_school)["score"]  # → 4.50 (CRITICAL)
engine.score_risk(university)["score"]       # → 2.25 (MODERATE)
```

### Finding 3: The Compliance-Capability Gap (Chapter 5.2)

Institutions **meet formal policy requirements** without achieving **operational resilience**:

| Policy Expectation | Reported Practice |
|---|---|
| Formal risk assessments | 58% primary / 90% HE |
| Dedicated cyber staff | 37% FE / 92% HE (Jisc, 2022) |
| Incident response plans | Variable, rarely tested |
| Post-incident learning | Weakest dimension across ALL sectors |

### Finding 4: Governance as Critical Enabler (Chapter 5.6)

> *"Governance determines whether AWRR dimensions function as an integrated resilience system or as disconnected technical measures."*
> *(Kelly, 2023; Dissertation Chapter 5.6)*

---

## 🏗️ AWRR Resilience Framework

SCRPM is grounded in the **AWRR framework** (Hollnagel et al., 2011):

```
ANTICIPATE          WITHSTAND           RESPOND             RECOVER
Risk assessments → Monitoring tools → Incident plans → Post-incident learning
58% primary         47% primary         Low formalised      Weakest dimension
90% HE              87% HE             97% HE              across ALL sectors
(DSIT 2025)         (DSIT 2024)        (Jisc 2022)
```

**Governance Integration** is the critical enabler across all four dimensions.

---

## ⚡ Quick Start

```bash
git clone https://github.com/mdonikmia/scrpm-framework.git
cd scrpm-framework
pip install -r requirements.txt

# Run the sample assessment
python examples/sample_assessment.py
```

**Example output:**

```
SCRPM PRIORITY RANKING
═══════════════════════════════════════════════════════════════

  #1 🔴 [CRITICAL]  Score: 5.00/5.0
     Sector: Primary School
     Risk:   Ransomware encrypting pastoral and safeguarding databases
     Breakdown: Threat=5/5 | Resilience Deficit=5/5 | Safeguarding=5/5

  #2 🔴 [CRITICAL]  Score: 4.40/5.0
     Sector: Secondary School
     Risk:   Unauthorised access to student SEND and medical records
     Breakdown: Threat=3/5 | Resilience Deficit=5/5 | Safeguarding=5/5

  ...

  #6 🟡 [MODERATE]  Score: 2.55/5.0
     Sector: University
     Risk:   Research data breach — commercially sensitive IP
     Breakdown: Threat=5/5 | Resilience Deficit=2/5 | Safeguarding=1/5
```

*The same threat severity (5/5) scores CRITICAL for a primary school and MODERATE for a university — demonstrating SCRPM's institutional sensitivity.*

---

## 💻 API Usage

```python
from framework.scrpm_engine import SCRPMEngine, Risk

engine = SCRPMEngine()

# Score a single risk
risk = Risk(
    id="RISK-001",
    description="Ransomware encrypting safeguarding records",
    threat_severity=5,
    resilience_deficit=5,
    safeguarding_impact=5,
    sector="Primary School",
    category="Ransomware",
    affected_systems=["Pastoral database", "DSL referral system"]
)

result = engine.score_risk(risk)
print(f"Score: {result['score']}/5.0")
print(f"Band:  {result['classification']}")
print(f"Action: {result['recommended_action']}")
# → Score: 5.0/5.0 | Band: CRITICAL | Immediate escalation...

# Score and rank multiple risks
risks = engine.load_risk_register("data/sample_risks.json")
ranked = engine.score_and_rank(risks)

# Generate report
print(engine.generate_report(ranked, institution="Example Primary School"))
```

### Custom Weights (Sensitivity Analysis)

```python
# Emphasise safeguarding (e.g., schools)
school_engine = SCRPMEngine(weights={
    "threat_severity":    0.20,
    "resilience_deficit": 0.35,
    "safeguarding_impact": 0.45,
})

# Emphasise resilience (e.g., FE colleges)
fe_engine = SCRPMEngine(weights={
    "threat_severity":    0.30,
    "resilience_deficit": 0.45,
    "safeguarding_impact": 0.25,
})
```

---

## 🧪 Testing

```bash
pytest tests/ -v
```

**15 tests across 4 test classes:**

| Class | Tests | Coverage |
|---|---|---|
| `TestWeights` | 4 | Weight validation, dissertation constraints |
| `TestScoring` | 5 | Formula accuracy, boundary conditions |
| `TestClassification` | 3 | Band thresholds (Table 5) |
| `TestDissertationInsight` | 3 | School vulnerability inversion, compliance gap |

The `TestDissertationInsight` class encodes the dissertation's empirical findings as executable assertions — ensuring the algorithm mathematically reflects the research conclusions.

---

## 📁 Repository Structure

```
scrpm-framework/
├── README.md                    # This file
├── requirements.txt
├── LICENSE
│
├── framework/
│   └── scrpm_engine.py          # Core SCRPM algorithm (Chapter 7.3 formula)
│
├── data/
│   └── sample_risks.json        # 7 risk scenarios from real DSIT/ICO/NCSC data
│
├── examples/
│   └── sample_assessment.py     # Demonstration with sector context
│
└── tests/
    └── test_scoring.py          # 15 unit tests encoding dissertation findings
```

---

## 🎓 Academic Context

### Contributions (Chapter 7.6)

1. **Cross-sectoral framework** — integrates fragmented cyber security, resilience, and governance literatures across UK education
2. **FE blind spot exposure** — identifies significant research and policy gap for further education colleges
3. **SCRPM artefact** — novel IS decision-support tool with safeguarding-sensitive algorithm
4. **Safeguarding as IS problem** — repositions child welfare from regulatory compliance to information systems resilience

### DSR Evaluation (Against Hevner et al., 2004 — Table 6)

| DSR Guideline | SCRPM Response |
|---|---|
| Design as Artefact | Risk-scoring model (March & Smith, 1995 typology) |
| Problem Relevance | Cross-sector vulnerability analysis gap identified |
| Design Evaluation | Scenario testing against DSIT/NCSC evidence base |
| Research Contribution | Novel safeguarding-weighted algorithm |
| Research Rigour | Triangulation across 6 source types |
| Design as Search Process | Iterative weight calibration via scenario testing |
| Communication | Dissertation + open-source repository |

### Limitations

- SCRPM weighting validated through scenario testing; requires stakeholder validation before operational deployment
- Secondary data methodology limits causal inference
- FE evidence base remains sparse (identified as future research priority)
- Operational demonstration and iterative refinement remain as future work

---

## 📚 Key References

```bibtex
@article{hevner2004design,
  author  = {Hevner, A. R. and March, S. T. and Park, J. and Ram, S.},
  title   = {Design Science in Information Systems Research},
  journal = {MIS Quarterly},
  year    = {2004}, volume = {28}, number = {1}, pages = {75--105}
}

@book{hollnagel2011resilience,
  author    = {Hollnagel, E. and Woods, D. D. and Leveson, N.},
  title     = {Resilience Engineering: Concepts and Precepts},
  publisher = {Ashgate}, year = {2011}
}
```

**Additional sources:** DSIT (2022, 2023, 2024, 2025), NCSC (2020, 2021, 2022), DfE (2023, 2024 KCSIE), Jisc (2022), ICO (2023), Kelly (2023), Lallie et al. (2023)

---

## 🤝 Author

**Md Onik Mia** · BSc Information Technology (Hons) · UWE Bristol · 2026

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/md-onik-mia-643322385/)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=flat&logo=gmail)](mailto:mdonikmia88@gmail.com)
[![VoltSight BI](https://img.shields.io/badge/VoltSight%20BI-Live%20Demo-00C48C?style=flat&logo=streamlit)](https://voltsight-bi.streamlit.app)

---

## 📄 Citation

```bibtex
@misc{mia2026scrpm,
  author    = {Mia, Md Onik},
  title     = {SCRPM: Safeguarding-Centric Risk Priority Matrix for UK Education Institutions},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/mdonikmia/scrpm-framework},
  note      = {BSc Information Systems Dissertation, UWE Bristol, UFCFM5-30-3}
}
```

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>
</div>
