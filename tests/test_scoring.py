"""
SCRPM Unit Tests
=================
Validates the SCRPM scoring engine against the dissertation's
algorithm specification (Chapter 7.3) and Table 5 thresholds.
"""
import pytest
import sys
sys.path.insert(0, '.')
from framework.scrpm_engine import SCRPMEngine, Risk, WEIGHTS

def r(**kw):
    """Helper: create a Risk with sensible defaults."""
    d = dict(id="TEST", description="Test risk",
             threat_severity=3.0, resilience_deficit=3.0, safeguarding_impact=3.0)
    d.update(kw)
    return Risk(**d)


class TestWeights:
    def test_weights_sum_to_one(self):
        """Dissertation constraint: weights must sum to 1.0"""
        assert abs(sum(WEIGHTS.values()) - 1.0) < 0.001

    def test_safeguarding_equals_resilience_weight(self):
        """Dissertation design: safeguarding and resilience weighted equally at 0.35"""
        assert WEIGHTS["safeguarding_impact"] == WEIGHTS["resilience_deficit"]

    def test_safeguarding_higher_than_threat(self):
        """Dissertation design: safeguarding > threat severity weight"""
        assert WEIGHTS["safeguarding_impact"] > WEIGHTS["threat_severity"]

    def test_invalid_weights_raise(self):
        with pytest.raises(ValueError, match="sum to 1.0"):
            SCRPMEngine(weights={"threat_severity": 0.5, "resilience_deficit": 0.5, "safeguarding_impact": 0.5})


class TestScoring:
    engine = SCRPMEngine()

    def test_max_score(self):
        """Score 5/5/5 → 5.0 (maximum)"""
        result = self.engine.score_risk(r(threat_severity=5, resilience_deficit=5, safeguarding_impact=5))
        assert result["score"] == 5.0

    def test_min_score(self):
        """Score 1/1/1 → 1.0 (minimum)"""
        result = self.engine.score_risk(r(threat_severity=1, resilience_deficit=1, safeguarding_impact=1))
        assert result["score"] == 1.0

    def test_formula_calculation(self):
        """Validate exact formula: (T×0.30) + (R×0.35) + (S×0.35)"""
        risk = r(threat_severity=4, resilience_deficit=3, safeguarding_impact=5)
        result = self.engine.score_risk(risk)
        expected = round(4*0.30 + 3*0.35 + 5*0.35, 2)
        assert result["score"] == expected

    def test_invalid_score_above_5(self):
        with pytest.raises(ValueError):
            self.engine.score_risk(r(threat_severity=6))

    def test_invalid_score_below_1(self):
        with pytest.raises(ValueError):
            self.engine.score_risk(r(threat_severity=0))


class TestClassification:
    engine = SCRPMEngine()

    def test_critical_classification(self):
        """Score ≥4.0 → CRITICAL (dissertation Table 5)"""
        result = self.engine.score_risk(r(threat_severity=5, resilience_deficit=5, safeguarding_impact=5))
        assert result["classification"] == "CRITICAL"

    def test_low_classification(self):
        """Score 1.0-2.0 → LOW"""
        result = self.engine.score_risk(r(threat_severity=1, resilience_deficit=1, safeguarding_impact=1))
        assert result["classification"] == "LOW"

    def test_ranking_order(self):
        """Higher score must rank first."""
        risks = [
            r(id="LOW",  threat_severity=1, resilience_deficit=1, safeguarding_impact=1),
            r(id="HIGH", threat_severity=5, resilience_deficit=5, safeguarding_impact=5),
        ]
        ranked = self.engine.score_and_rank(risks)
        assert ranked[0]["risk_id"] == "HIGH"


class TestDissertationInsight:
    """
    Tests encoding the dissertation's key empirical finding:
    The 'school vulnerability inversion' (Chapter 6.7):
        Schools face lower breach exposure but higher per-incident harm
        due to safeguarding obligations and weak resilience.
    """
    engine = SCRPMEngine()

    def test_school_vulnerability_inversion(self):
        """
        Primary school with moderate threat but weak resilience and high
        safeguarding obligations should score HIGHER than a university
        with high threat but strong resilience and low safeguarding impact.
        """
        primary_school = r(
            id="PRIMARY",
            description="Primary school: moderate threat, weak resilience, high safeguarding",
            threat_severity=3,      # moderate threat
            resilience_deficit=5,   # very weak resilience (58% formal risk assessment)
            safeguarding_impact=5   # maximum safeguarding obligation
        )
        university = r(
            id="UNIVERSITY",
            description="University: high threat, strong resilience, low safeguarding",
            threat_severity=5,      # high threat (97% breach rate)
            resilience_deficit=2,   # strong resilience (92% dedicated staff)
            safeguarding_impact=1   # minimal safeguarding obligation
        )
        school_result = self.engine.score_risk(primary_school)
        uni_result    = self.engine.score_risk(university)

        assert school_result["score"] > uni_result["score"], (
            "School vulnerability inversion violated: "
            f"school={school_result['score']}, university={uni_result['score']}"
        )

    def test_safeguarding_impact_dominates_threat_severity(self):
        """
        Two risks with identical threat severity — the one with higher
        safeguarding impact must score higher. Validates safeguarding weight.
        """
        high_safeguard = r(threat_severity=3, resilience_deficit=3, safeguarding_impact=5)
        low_safeguard  = r(threat_severity=3, resilience_deficit=3, safeguarding_impact=1)
        r1 = self.engine.score_risk(high_safeguard)
        r2 = self.engine.score_risk(low_safeguard)
        assert r1["score"] > r2["score"]

    def test_compliance_capability_gap(self):
        """
        An institution with high resilience deficit (poor actual capability)
        should score higher than one with low deficit, even at same threat level.
        Reflects the compliance-capability gap (Chapter 5.2).
        """
        weak_institution   = r(threat_severity=3, resilience_deficit=5, safeguarding_impact=3)
        strong_institution = r(threat_severity=3, resilience_deficit=1, safeguarding_impact=3)
        r1 = self.engine.score_risk(weak_institution)
        r2 = self.engine.score_risk(strong_institution)
        assert r1["score"] > r2["score"]
