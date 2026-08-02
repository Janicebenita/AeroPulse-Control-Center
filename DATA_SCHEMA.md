# Source schema adapter

The supplied exports contain numeric headers (`0`, `1`, …) rather than semantic field names. The included data dictionary documents the entities and relationships but does not enumerate columns. AeroPulse therefore uses a conservative adapter based on data types, recurring identifiers, and the dictionary's relationship statement.

## Fields used by the application

- `flights`: 0 flight_id, 1 airline, 3 origin, 4 destination, 5 scheduled time, 6 actual/updated time, 9 aircraft type, 10 registration, 11 capacity, 12 passenger count, 13 status, 14 delay minutes, 15 delay reason, 16 terminal, 17 gate.
- `passengers`: 0 PNR, 2 masked passport/passenger key, 10 flight_id.
- `baggage`: 1 PNR, 2 flight_id, 3 masked passport/passenger key, 8 current location/gate, 9/10 timestamps, 12 status.
- `gate_events`: 1 flight_id, 2 gate, 3 terminal, 4 event type, 5 event timestamp, 9 conflict flag.
- `security_screening`: 1 masked passport/passenger key, 2 PNR, 3 lane, 4 event timestamp, 7 outcome, 12 processing/capacity interval, 15 staff shift.
- `maintenance_logs`: 1 aircraft registration, 2 flight_id, 3 work type, 5 event timestamp, 9 defect, 11 severity.
- `staff_shifts`: 0 staff_id, 1 name, 2 department, 3 role, 7 terminal, 8 gate, 9 assignment/supervisor ID.
- `retail_transactions`: 1 staff/store ID, 2 store, 4 masked passport/passenger key, 5 flight_id, 6 timestamp, 9/10 monetary fields, 14 terminal.

Unused columns remain available in each normalized entity's `raw` record so the adapter can be refined without re-parsing or losing source fidelity.
