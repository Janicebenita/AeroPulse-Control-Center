"""Deterministic disruption-review worker for the AeroPulse demo data."""
from __future__ import annotations


def analyze_disruption(event: dict) -> dict:
    """Return an evidence-linked incident brief without taking airport action."""
    delay = max(int(event.get("delay_minutes", 0)), 0)
    gate_conflicts = max(int(event.get("gate_conflicts", 0)), 0)
    maintenance_flags = list(event.get("maintenance_flags") or [])
    missed_connections = max(int(event.get("missed_connections", 0)), 0)
    evidence = []
    for field, value in (
        ("delay_minutes", delay),
        ("gate_conflicts", gate_conflicts),
        ("maintenance_flags", maintenance_flags),
        ("missed_connections", missed_connections),
    ):
        if value:
            evidence.append({"field": field, "value": value})
    severity = "critical" if maintenance_flags or delay >= 120 else "major" if delay >= 45 or gate_conflicts else "minor"
    confidence = round(min(1.0, len(evidence) / 4), 2)
    return {
        "flight_id": event.get("flight_id"),
        "severity": severity,
        "confidence": confidence,
        "evidence": evidence,
        "unknowns": [name for name in ("flight_id", "timestamp") if not event.get(name)],
        "recommended_review": "Airport operator verifies source records and selects any response.",
        "human_approval_required": True,
    }
