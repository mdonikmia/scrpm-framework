"""
SCRPM Sample Assessment — UK Education Sector Scenarios
========================================================
Demonstrates the SCRPM algorithm on real-world inspired scenarios
derived from DSIT (2024), NCSC (2020-2023), and ICO (2023) data.

This script illustrates the dissertation's central finding:
    "Threat frequency alone does not determine institutional risk.
     Schools face lower measured exposure but higher per-incident
     vulnerability due to safeguarding obligations and limited
     cyber capacity." (Chapter 7.4)

Run:
    python examples/sample_assessment.py
"""

import sys
sys.path.insert(0, '.')
from framework.scrpm_engine import SCRPMEngine, Risk, SECTOR_BREACH_RATES, SECTOR_CYBER_STAFF


def print_sector_context():
    """Print real statistics from DSIT (2024) used in the dissertation."""
    print("\n📊 UK EDUCATION SECTOR CYBER BREACH CONTEXT (DSIT, 2024)")
    print("=" * 65)
    print(f"  {'Sector':<25} {'Breach Rate':>12} {'Dedicated Cyber Staff':>22}")
    print(f"  {'-'*25} {'-'*12} {'-'*22}")
    labels = {
        "primary_school":   "Primary Schools",
        "secondary_school": "Secondary Schools",
        "fe_college":       "FE Colleges (Jisc 2022)",
        "university":       "Universities (Jisc 2022)",
    }
    for key, label in labels.items():
        breach = SECTOR_BREACH_RATES.get(key, 0)
        staff  = SECTOR_CYBER_STAFF.get(key, 0)
        print(f"  {label:<25} {breach:>11.0%} {staff:>21.0%}")
    print()
    print("  KEY FINDING (Dissertation Ch.1.5):")
    print("  Jisc (2022): 92% of universities have dedicated cyber staff")
    print("  vs only 37% of FE colleges — uneven capacity across the sector.")
    print("=" * 65)


def print_awrr_framework():
    """Print the AWRR resilience framework used in the dissertation."""
    print("\n🔄 AWRR RESILIENCE FRAMEWORK (Hollnagel et al., 2011)")
    print("=" * 65)
    dimensions = [
        ("Anticipation", "Formal risk assessment rates", "58% primary → 90% HE (DSIT, 2025)"),
        ("Withstanding", "Monitoring tool deployment",  "47% primary → 87% HE (DSIT, 2024)"),
        ("Response",     "Formal incident response plan","~60% schools → 97% HE (Jisc, 2022)"),
        ("Recovery",     "Post-incident learning",       "Weakest dimension across ALL sectors"),
    ]
    for dim, indicator, data in dimensions:
        print(f"\n  {dim.upper()}")
        print(f"    Indicator: {indicator}")
        print(f"    Evidence:  {data}")
    print("\n  GOVERNANCE = Critical enabler (Kelly, 2023; Dissertation Ch.5.6)")
    print("=" * 65)


def main():
    print("=" * 65)
    print("SCRPM FRAMEWORK — RISK ASSESSMENT DEMONSTRATION")
    print("Safeguarding-Centric Risk Priority Matrix")
    print("Md Onik Mia | UWE Bristol | UFCFM5-30-3 | 2026")
    print("=" * 65)

    print_sector_context()
    print_awrr_framework()

    # Initialise engine with dissertation weights
    engine = SCRPMEngine()
    print(f"\n⚖️  SCRPM WEIGHTS (Dissertation Chapter 7.3):")
    print(f"    Threat Severity:     {engine.weights['threat_severity']:.0%}")
    print(f"    Resilience Deficit:  {engine.weights['resilience_deficit']:.0%}")
    print(f"    Safeguarding Impact: {engine.weights['safeguarding_impact']:.0%}")
    print(f"\n    RATIONALE: Resilience deficit and safeguarding impact weighted")
    print(f"    above threat severity — encoding the compliance-capability gap")
    print(f"    and school vulnerability inversion (Chapters 5-6).")

    # Load and score risks
    risks = engine.load_risk_register("data/sample_risks.json")
    print(f"\n✓ Loaded {len(risks)} risks from sample register")

    ranked = engine.score_and_rank(risks)

    print("\n📋 SCRPM PRIORITY RANKING")
    print("=" * 65)
    emojis = {"CRITICAL":"🔴","HIGH":"🟠","MODERATE":"🟡","LOW":"🟢"}
    for i, r in enumerate(ranked, 1):
        e = emojis.get(r["classification"], "⚪")
        bd = r["dimensional_breakdown"]
        print(f"\n  #{i} {e} [{r['classification']:8}]  Score: {r['score']:.2f}/5.0")
        print(f"     Sector: {r['sector']}")
        print(f"     Risk:   {r['description']}")
        print(f"     Score breakdown:")
        print(f"       Threat Severity ×0.30:     {bd['threat_severity']['raw']}/5 → {bd['threat_severity']['weighted']:.3f}")
        print(f"       Resilience Deficit ×0.35:  {bd['resilience_deficit']['raw']}/5 → {bd['resilience_deficit']['weighted']:.3f}")
        print(f"       Safeguarding Impact ×0.35: {bd['safeguarding_impact']['raw']}/5 → {bd['safeguarding_impact']['weighted']:.3f}")
        print(f"     Action: {r['recommended_action'][:80]}...")

    # Key insights
    print("\n\n💡 KEY DISSERTATION INSIGHT DEMONSTRATED:")
    print("=" * 65)
    print("  RISK-006 (University research breach):")
    print("    Threat Severity = 5/5 | BUT Resilience Deficit = 2/5, Safeguarding = 1/5")
    print(f"    SCRPM Score = {(5*0.30 + 2*0.35 + 1*0.35):.2f}/5.0 → HIGH")
    print()
    print("  RISK-001 (Primary school ransomware on safeguarding systems):")
    print("    Threat Severity = 5/5 | Resilience Deficit = 5/5, Safeguarding = 5/5")
    print(f"    SCRPM Score = {(5*0.30 + 5*0.35 + 5*0.35):.2f}/5.0 → CRITICAL")
    print()
    print("  → Same threat severity, vastly different institutional risk.")
    print("    Generic frameworks treat both equally. SCRPM does not.")
    print("    This is the school vulnerability inversion (Chapter 6.7).")
    print("=" * 65)
    print("\n✓ Assessment complete. See full report via engine.generate_report()")

if __name__ == "__main__":
    main()
