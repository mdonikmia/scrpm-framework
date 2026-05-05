"""Unit tests for SCRPM scoring engine."""
import pytest
import sys
sys.path.insert(0, '..')
from framework.scrpm_engine import SCRPMEngine, Risk

def r(**kw):
    d = dict(id="T001",description="Test",safeguarding_impact=5,data_sensitivity=5,likelihood=5,operational_impact=5,regulatory_exposure=5)
    d.update(kw); return Risk(**d)

def test_weights_sum_to_one():
    assert abs(sum(SCRPMEngine().weights.values()) - 1.0) < 0.001

def test_max_score():
    assert SCRPMEngine().score_risk(r(safeguarding_impact=10,data_sensitivity=10,likelihood=10,operational_impact=10,regulatory_exposure=10))["total"] == 100.0

def test_min_score():
    assert SCRPMEngine().score_risk(r(safeguarding_impact=1,data_sensitivity=1,likelihood=1,operational_impact=1,regulatory_exposure=1))["total"] == 10.0

def test_critical_classification():
    assert SCRPMEngine().score_risk(r(safeguarding_impact=10,data_sensitivity=9,likelihood=9,operational_impact=9,regulatory_exposure=9))["classification"] == "CRITICAL"

def test_invalid_raises():
    with pytest.raises(ValueError):
        SCRPMEngine().score_risk(r(safeguarding_impact=11))

def test_ranking_order():
    engine = SCRPMEngine()
    risks = [r(id="LOW",safeguarding_impact=1,data_sensitivity=1,likelihood=1,operational_impact=1,regulatory_exposure=1),
             r(id="HIGH",safeguarding_impact=9,data_sensitivity=9,likelihood=9,operational_impact=9,regulatory_exposure=9)]
    assert engine.score_and_rank(risks)[0]["risk_id"] == "HIGH"

def test_safeguarding_dominates():
    engine = SCRPMEngine()
    high = engine.score_risk(r(safeguarding_impact=10,data_sensitivity=1,likelihood=1,operational_impact=1,regulatory_exposure=1))
    low  = engine.score_risk(r(safeguarding_impact=1,data_sensitivity=10,likelihood=10,operational_impact=10,regulatory_exposure=10))
    assert high["breakdown"]["safeguarding_impact"] > low["breakdown"]["safeguarding_impact"]
