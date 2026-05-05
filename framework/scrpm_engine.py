"""
SCRPM Engine — Core Risk Scoring Module
Safeguarding-Centric Risk Priority Matrix
UWE Bristol Dissertation 2026 — Md Onik Mia
"""
from __future__ import annotations
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

WEIGHTS = {
    "safeguarding_impact": 0.35,
    "data_sensitivity":    0.25,
    "likelihood":          0.20,
    "operational_impact":  0.12,
    "regulatory_exposure": 0.08,
}

THRESHOLDS = {"CRITICAL": 80, "HIGH": 60, "MEDIUM": 40, "LOW": 20, "MINIMAL": 0}

ACTIONS = {
    "CRITICAL": "Immediate escalation to SLT. Invoke incident response plan.",
    "HIGH":     "Action within 24-48 hours. Notify Data Protection Officer.",
    "MEDIUM":   "Planned remediation within 30 days.",
    "LOW":      "Monitor quarterly. Include in annual security review.",
    "MINIMAL":  "Accept risk with documentation. Review annually.",
}

@dataclass
class Risk:
    """Single cybersecurity risk for SCRPM scoring."""
    id: str
    description: str
    safeguarding_impact: float
    data_sensitivity: float
    likelihood: float
    operational_impact: float
    regulatory_exposure: float
    category: str = "Uncategorised"
    notes: str = ""
    score: Optional[float] = field(default=None, init=False)
    classification: Optional[str] = field(default=None, init=False)

    def validate(self) -> bool:
        return all(1 <= f <= 10 for f in [
            self.safeguarding_impact, self.data_sensitivity,
            self.likelihood, self.operational_impact, self.regulatory_exposure
        ])

class SCRPMEngine:
    """
    Core SCRPM scoring engine.
    Score = (weighted_sum) x 10  →  range 0-100
    Weights calibrated against NCSC Cyber Essentials + KCSIE.
    """
    def __init__(self, weights: dict = None):
        self.weights = weights or WEIGHTS
        if abs(sum(self.weights.values()) - 1.0) > 0.001:
            raise ValueError("Weights must sum to 1.0")

    def score_risk(self, risk: Risk) -> dict:
        if not risk.validate():
            raise ValueError(f"Risk {risk.id}: all scores must be between 1-10")
        raw = sum([
            risk.safeguarding_impact * self.weights["safeguarding_impact"],
            risk.data_sensitivity    * self.weights["data_sensitivity"],
            risk.likelihood          * self.weights["likelihood"],
            risk.operational_impact  * self.weights["operational_impact"],
            risk.regulatory_exposure * self.weights["regulatory_exposure"],
        ])
        total = round(raw * 10, 2)
        classification = next(k for k, v in THRESHOLDS.items() if total >= v)
        risk.score = total
        risk.classification = classification
        return {
            "risk_id": risk.id,
            "description": risk.description,
            "total": total,
            "classification": classification,
            "breakdown": {k: round(getattr(risk, k) * self.weights[k] * 10, 2) for k in self.weights},
            "action_required": ACTIONS.get(classification, "Review required"),
        }

    def score_and_rank(self, risks: list) -> list:
        return sorted([self.score_risk(r) for r in risks], key=lambda x: x["total"], reverse=True)

    def load_risk_register(self, filepath: str) -> list:
        with open(filepath) as f:
            data = json.load(f)
        return [Risk(**r) for r in data["risks"]]

    def generate_report(self, scored_risks: list) -> str:
        from collections import Counter
        counts = Counter(r["classification"] for r in scored_risks)
        lines = ["="*60, "SCRPM RISK PRIORITY REPORT", "="*60, ""]
        for band in ["CRITICAL","HIGH","MEDIUM","LOW","MINIMAL"]:
            if counts.get(band):
                lines.append(f"  {band:10}: {counts[band]} risk(s)")
        lines.append("\nDETAILED REGISTER:\n" + "-"*60)
        for i, r in enumerate(scored_risks, 1):
            lines += [f"\n#{i} [{r['classification']}] {r['total']}/100", f"   {r['description']}", f"   -> {r['action_required']}"]
        return "\n".join(lines)
