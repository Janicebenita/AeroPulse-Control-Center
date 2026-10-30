# AeroPulse Disruption Analyst: Explainability

## Decision and reasoning

The agent's intended decision is which plausible disruption cause and next operator action to put first in an incident brief. It reasons from connected flight, gate, passenger, baggage, screening, staffing, maintenance, retail, and timeline records, and should distinguish direct evidence from an inferred downstream effect. The existing AeroPulse application supplies relationship exploration and rule-based insights; a separate agent execution path must be implemented and demonstrated before claiming that this investigation runs autonomously.

## Inputs and data sources

The intended input is a selected flight or event, an operator's investigation request, and the eight supplied CSV datasets used by AeroPulse. Data sources are `flights.csv`, `gate_events.csv`, `passengers.csv`, `baggage.csv`, `security_screening.csv`, `maintenance_logs.csv`, `staff_shifts.csv`, and `retail_transactions.csv`. The application parses these files locally and joins related records using documented identifiers; it does not obtain live airport data.

## Limits and known constraints

The primary limitation is that AeroPulse is a frontend-only simulation built from supplied records, so its findings cannot establish the actual state of an airport. Missing records, uncertain joins, and simulated time can change an apparent cause or the number of affected entities. The agent should present proposals for human review and should not assert that it has executed operational actions or verified real-world outcomes.

## Implementation in This Repository

`agent.py` now implements the worker's deterministic `analyze_disruption(event)` function. It normalizes delay, gate-conflict, maintenance, and missed-connection facts; records every non-zero fact as field/value evidence; assigns minor, major, or critical severity from declared thresholds; reports missing identity/time fields; and always requires operator approval. `test_agent.py` verifies that a maintenance flag produces a critical, cited result.

The Vite demonstration is declared by `package.json`, configured by `vite.config.ts`, and entered through `index.html`; `DATA_SCHEMA.md` defines the supplied CSV entities and joins. No production airport API or action service exists, so operational action remains outside the implementation.
