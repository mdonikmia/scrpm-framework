"""SCRPM Sample Risk Assessment — UK School Scenario."""
import sys
sys.path.insert(0, '..')
from framework.scrpm_engine import SCRPMEngine

def main():
    print("=" * 60)
    print("SCRPM Framework — Sample Risk Assessment")
    print("=" * 60)
    engine = SCRPMEngine()
    risks = engine.load_risk_register("data/sample_risks.json")
    print(f"\n✓ Loaded {len(risks)} risks")
    ranked = engine.score_and_rank(risks)
    emojis = {"CRITICAL":"🔴","HIGH":"🟠","MEDIUM":"🟡","LOW":"🟢","MINIMAL":"⚪"}
    for i, r in enumerate(ranked, 1):
        print(f"\n#{i} {emojis.get(r['classification'],'⚪')} [{r['classification']}] {r['total']}/100")
        print(f"   {r['description']}")
        print(f"   Action: {r['action_required']}")
    print("\n✓ Assessment complete.")

if __name__ == "__main__":
    main()
