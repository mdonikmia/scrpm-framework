"""
SCRPM Engine — Safeguarding-Centric Risk Priority Matrix
=========================================================
Author:     Md Onik Mia
Module:     UFCFM5-30-3 Information Systems Dissertation
University: University of the West of England, Bristol
Supervisor: Mark Rhodes
Year:       2025/2026

SCRPM Formula (from dissertation Chapter 7.3):
    Score = (Threat Severity × 0.30) + (Resilience Deficit × 0.35)
          + (Safeguarding Impact × 0.35)

Key Design Rationale:
    - Resilience Deficit and Safeguarding Impact are weighted at parity (0.35 each)
      ABOVE Threat Severity (0.30)
    - This reflects the dissertation's central empirical finding: per-incident harm
      in UK education is determined primarily by capability deficits and statutory
      obligation, NOT attack frequency alone
    - The weighting encodes the Chapter 4 distinction between frequency and severity:
      a moderate threat against a vulnerable, safeguarding-intensive institution
      generates substantially greater risk than a severe threat against a resilient
      institution with low safeguarding exposure

Scale: All dimensions rated 1–5
Output: Composite score 1.0–5.0 → mapped to risk band

References:
    Hevner et al. (2004) Design Science in Information Systems Research. MIS Quarterly.
    March & Smith (1995) Design and Natural Science Research on IT. Decision Support Systems.
    Peffers et al. (2007) A Design Science Research Methodology for IS Research.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
import json
from pathlib import Path

# ── SCRPM Weights (dissertation Chapter 7.3) ───────────────────────────────
WEIGHTS = {
    "threat_severity":    0.30,
    "resilience_deficit": 0.35,
    "safeguarding_impact": 0.35,
}

# ── Risk Classification Thresholds (dissertation Table 5) ─────────────────
# Calibrated against the 1.0–5.0 output range through scenario testing
CLASSIFICATION_BANDS = {
    "CRITICAL": 4.0,   # Immediate escalation to SLT
    "HIGH":     3.0,   # Action within 24–48 hours
    "MODERATE": 2.0,   # Planned remediation within 30 days
    "LOW":      1.0,   # Monitor and review quarterly
}

# ── Sector Profiles (from DSIT 2024 data used in dissertation) ────────────
SECTOR_BREACH_RATES = {
    "primary_school":    0.52,  # DSIT (2024): 52% of primary schools breached
    "secondary_school":  0.71,  # DSIT (2024): 71% of secondary schools breached
    "fe_college":        0.86,  # DSIT (2024): 86% of FE colleges breached
    "university":        0.97,  # DSIT (2024): 97% of universities breached
}

SECTOR_CYBER_STAFF = {
    "university":        0.92,  # Jisc (2022): 92% of HE have dedicated cyber staff
    "fe_college":        0.37,  # Jisc (2022): only 37% of FE colleges
    "secondary_school":  0.15,  # Estimated from DSIT data
    "primary_school":    0.05,  # Estimated from DSIT data
}

# ── Recommended Actions (dissertation Table 5) ────────────────────────────
RECOMMENDED_ACTIONS = {
    "CRITICAL": (
        "Immediate escalation to Senior Leadership Team. "
        "Invoke incident response plan. Notify Data Protection Officer immediately. "
        "Assess whether safeguarding systems are affected — engage DSL. "
        "Consider mandatory ICO notification within 72 hours (UK GDPR Article 33)."
    ),
    "HIGH": (
        "Action required within 24–48 hours. "
        "Notify Data Protection Officer. Conduct internal investigation. "
        "Document in risk register. Brief governing body. "
        "Review adequacy of existing controls."
    ),
    "MODERATE": (
        "Planned remediation within 30 days. "
        "Include in next governance cycle. "
        "Update risk register and Business Continuity Plan. "
        "Consider staff awareness training."
    ),
    "LOW": (
        "Monitor and review quarterly. "
        "Document in risk register with review date. "
        "Include in annual cyber security review. "
        "Accept risk with appropriate documentation."
    ),
}


@dataclass
class Risk:
    """
    Represents a single cybersecurity risk for SCRPM scoring.

    Three dimensions (dissertation Chapter 7.3):
        - threat_severity:     How severe is the threat? (1=minimal, 5=catastrophic)
        - resilience_deficit:  How weak is the institution's resilience? (1=strong, 5=none)
        - safeguarding_impact: What is the risk to student welfare? (1=none, 5=severe)
    """
    id: str
    description: str
    threat_severity: float       # 1–5 scale
    resilience_deficit: float    # 1–5 scale (higher = weaker resilience)
    safeguarding_impact: float   # 1–5 scale (higher = greater child welfare risk)
    sector: str = "Unknown"
    category: str = "Uncategorised"
    affected_systems: list = field(default_factory=list)
    notes: str = ""
    score: Optional[float] = field(default=None, init=False)
    classification: Optional[str] = field(default=None, init=False)

    def validate(self) -> bool:
        """Ensure all scores are within 1–5 range."""
        return all(
            1.0 <= val <= 5.0
            for val in [self.threat_severity, self.resilience_deficit, self.safeguarding_impact]
        )


class SCRPMEngine:
    """
    SCRPM scoring engine — implements the dissertation's risk-scoring algorithm.

    Formula (Chapter 7.3):
        Score = (Threat Severity × 0.30) + (Resilience Deficit × 0.35)
              + (Safeguarding Impact × 0.35)

    Design Science Research artefact type: Model (March & Smith, 1995)
    DSR evaluation criteria: Hevner et al. (2004) seven guidelines
    """

    def __init__(self, weights: dict = None):
        self.weights = weights or WEIGHTS
        self._validate_weights()

    def _validate_weights(self) -> None:
        total = sum(self.weights.values())
        if abs(total - 1.0) > 0.001:
            raise ValueError(
                f"Weights must sum to 1.0 (current: {total:.3f}). "
                "Adjust weights proportionally."
            )

    def score_risk(self, risk: Risk) -> dict:
        """
        Score a single risk using the SCRPM algorithm.

        Returns a complete assessment dict including score, classification,
        dimensional breakdown, and recommended action.
        """
        if not risk.validate():
            raise ValueError(
                f"Risk '{risk.id}': all dimensions must be between 1.0 and 5.0. "
                f"Got: threat={risk.threat_severity}, resilience={risk.resilience_deficit}, "
                f"safeguarding={risk.safeguarding_impact}"
            )

        # Core SCRPM formula (dissertation Chapter 7.3)
        score = (
            risk.threat_severity     * self.weights["threat_severity"]
            + risk.resilience_deficit  * self.weights["resilience_deficit"]
            + risk.safeguarding_impact * self.weights["safeguarding_impact"]
        )
        score = round(score, 2)

        # Classification (Table 5: thresholds calibrated via scenario testing)
        classification = self._classify(score)

        # Store on Risk object
        risk.score = score
        risk.classification = classification

        return {
            "risk_id":           risk.id,
            "description":       risk.description,
            "sector":            risk.sector,
            "category":          risk.category,
            "score":             score,
            "classification":    classification,
            "affected_systems":  risk.affected_systems,
            "dimensional_breakdown": {
                "threat_severity":     {
                    "raw":       risk.threat_severity,
                    "weighted":  round(risk.threat_severity * self.weights["threat_severity"], 3),
                    "weight":    self.weights["threat_severity"],
                },
                "resilience_deficit":  {
                    "raw":       risk.resilience_deficit,
                    "weighted":  round(risk.resilience_deficit * self.weights["resilience_deficit"], 3),
                    "weight":    self.weights["resilience_deficit"],
                },
                "safeguarding_impact": {
                    "raw":       risk.safeguarding_impact,
                    "weighted":  round(risk.safeguarding_impact * self.weights["safeguarding_impact"], 3),
                    "weight":    self.weights["safeguarding_impact"],
                },
            },
            "recommended_action": RECOMMENDED_ACTIONS.get(classification, "Review required."),
            "notes": risk.notes,
        }

    def _classify(self, score: float) -> str:
        """Classify score into SCRPM risk band (dissertation Table 5)."""
        for band, threshold in CLASSIFICATION_BANDS.items():
            if score >= threshold:
                return band
        return "LOW"

    def score_and_rank(self, risks: list[Risk]) -> list[dict]:
        """Score and rank multiple risks, highest priority first."""
        return sorted(
            [self.score_risk(r) for r in risks],
            key=lambda x: x["score"],
            reverse=True
        )

    def load_risk_register(self, filepath: str) -> list[Risk]:
        """Load risks from a JSON risk register file."""
        with open(filepath) as f:
            data = json.load(f)
        risks = []
        for r in data["risks"]:
            risk = Risk(
                id=r["id"], description=r["description"],
                threat_severity=r["threat_severity"],
                resilience_deficit=r["resilience_deficit"],
                safeguarding_impact=r["safeguarding_impact"],
                sector=r.get("sector", "Unknown"),
                category=r.get("category", "Uncategorised"),
                affected_systems=r.get("affected_systems", []),
                notes=r.get("notes", ""),
            )
            risks.append(risk)
        return risks

    def generate_report(self, scored_risks: list[dict], institution: str = "Unknown") -> str:
        """Generate a structured SCRPM priority report."""
        from collections import Counter
        counts = Counter(r["classification"] for r in scored_risks)
        emojis = {"CRITICAL": "🔴", "HIGH": "🟠", "MODERATE": "🟡", "LOW": "🟢"}
        lines = [
            "=" * 70,
            "SCRPM RISK PRIORITY REPORT",
            "Safeguarding-Centric Risk Priority Matrix",
            f"Institution: {institution}",
            "=" * 70,
            f"Total risks assessed: {len(scored_risks)}",
            "",
            "PRIORITY SUMMARY:",
        ]
        for band in ["CRITICAL", "HIGH", "MODERATE", "LOW"]:
            if counts.get(band, 0) > 0:
                lines.append(f"  {emojis.get(band, '')} {band:10}: {counts[band]} risk(s)")
        lines.append("\nDETAILED RISK REGISTER (ranked by priority):")
        lines.append("-" * 70)
        for i, r in enumerate(scored_risks, 1):
            lines.extend([
                f"\n#{i} {emojis.get(r['classification'], '')} [{r['classification']}]"
                f"  Score: {r['score']}/5.0  |  Sector: {r['sector']}",
                f"   Risk: {r['description']}",
                f"   Category: {r['category']}",
                f"   Action: {r['recommended_action'][:100]}...",
                f"   Breakdown: Threat={r['dimensional_breakdown']['threat_severity']['raw']}/5 "
                f"| Resilience Deficit={r['dimensional_breakdown']['resilience_deficit']['raw']}/5 "
                f"| Safeguarding={r['dimensional_breakdown']['safeguarding_impact']['raw']}/5",
            ])
        lines.append("\n" + "=" * 70)
        lines.append("Generated by SCRPM Framework — Md Onik Mia, UWE Bristol 2026")
        return "\n".join(lines)
