"""Asset-class specific research strategies (paper-only)."""

ASSET_CLASSES = {
    "major": {"risk_cap": 0.08, "cost_bps": 8},
    "large_alt": {"risk_cap": 0.04, "cost_bps": 14},
    "stable": {"risk_cap": 0.0, "cost_bps": 0},
    "defi": {"risk_cap": 0.02, "cost_bps": 22},
    "meme": {"risk_cap": 0.005, "cost_bps": 45},
    "l2": {"risk_cap": 0.03, "cost_bps": 16},
    "rwa": {"risk_cap": 0.02, "cost_bps": 12},
    "perp": {"risk_cap": 0.02, "cost_bps": 10},
}

def score_signal(asset_class: str, regime: str, factors: dict) -> float:
    """Multi-factor score. Research only."""
    if regime == "stress":
        return 0.0
    base = factors.get("strength", 0.5)
    # Add correlation, anomaly, etc. adjustments
    if factors.get("anomaly", 0) > 0.7:
        base *= 0.5
    return min(base, ASSET_CLASSES.get(asset_class, {}).get("risk_cap", 0.0))
