# AeroPulse

### Airport operations, alive in one pulse.

[![React 19](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=081526)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-6-646CFF?logo=vite&logoColor=white)](https://vite.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Frontend Only](https://img.shields.io/badge/Architecture-Frontend%20Only-2EE6A6)](#rule-compliance)
[![8 Connected CSVs](https://img.shields.io/badge/Data-8%20Connected%20CSVs-51D7F4)](#connected-data-model)
[![Live on Vercel](https://img.shields.io/badge/Live-Vercel-000000?logo=vercel)](https://aeropulse-frontend-wars-2026.vercel.app)

## [Launch the Live Command Center](https://aeropulse-frontend-wars-2026.vercel.app)

AeroPulse is a frontend-only **Airport Operations Control Center** created for the **Frontend Wars 2026 Grand Finale**.

It transforms eight supplied static airport datasets into a connected, replayable operational environment where an airport operator can:

> **Monitor → Detect → Investigate → Act**

AeroPulse is not a collection of unrelated charts. Flights, gates, passengers, baggage, security, maintenance, staff and retail activity are connected into one operational graph so every disruption can be traced from its cause to its downstream impact.

---

## The Problem

Airport operations are highly interconnected, but operators often have to work across disconnected systems.

A delayed departure may actually begin with:

- A crowded security checkpoint
- A late gate release
- Delayed baggage loading
- An active maintenance task
- Insufficient staff coverage
- A previous aircraft occupying the assigned gate

AeroPulse brings these relationships together and answers the questions that matter during live operations:

- Which flights need attention right now?
- Which gates are occupied, available or at risk?
- Which passengers and bags are affected?
- Which security lanes are under pressure?
- Which staff members are currently assigned?
- Which maintenance tasks may affect departures?
- What caused the problem?
- What should the operator investigate next?

---

## Why AeroPulse Is Different

### 1. Connected Operational Graph

Selecting a flight reveals its complete operational context:

```text
Flight
  ↓
Assigned Gate
  ↓
Gate Events
  ↓
Passengers
  ↓
Security Screening
  ↓
Baggage
  ↓
Staff Coverage
  ↓
Maintenance
  ↓
Retail Activity
  ↓
Operational Timeline
```

The same relationship model works when an operator starts from a gate, passenger, baggage record, employee or alert.

### 2. Interactive Airside Digital Twin

The Command Center includes an original SVG airport movement map with:

- Status-aware gate nodes
- Occupied-gate selection
- Aircraft taxi simulation
- Animated taxi routes
- Gate risk visualization
- Operational status changes
- Clear interaction guidance
- Reduced-motion accessibility support

Operators can select a glowing occupied gate and launch its connected aircraft along a visible taxi route.

### 3. Explainable Operational Intelligence

Alerts do more than show a red warning.

Each reasoned alert explains:

- What happened
- Why it happened
- Which flight or gate is affected
- How many passengers are exposed
- Which baggage records are connected
- What the likely downstream impact is
- What the operator should investigate next

The Intelligence Center also provides:

- Statistical anomaly detection
- Gate-pressure ranking
- Domain health analysis
- Pearson correlation
- Rule-based cascade forecasting
- Transparent confidence indicators

These calculations run entirely in the browser without an external AI service.

### 4. Judge Mode Data Lineage

Lineage Mode reveals which supplied datasets contribute to important values, alerts and conclusions.

This allows judges to verify that displayed insights are derived from the provided data and makes the application architecture easy to explain during a live demonstration.

---

## Core Features

### Command Center

- Airport health assessment
- Active-flight overview
- Passenger journey monitoring
- Security queue visibility
- Active gate availability
- Maintenance exposure
- Live event feed
- Reasoned active alerts
- Rolling operations timeline
- Interactive airport movement map

### Real-Time Simulation

- Frontend simulation clock
- `1×`, `5×` and `30×` speeds
- Pause and resume controls
- Timestamp-based event revelation
- Aircraft taxi animation
- Gate status transitions
- Live operational notifications
- Persistent clock position
- One-click demo reset

### Flight Operations

- Flight number and airline search
- Exact airline filtering
- Status filtering
- Terminal filtering
- Delay, passenger and flight-number sorting
- Connected flight investigation drawer
- Passenger and baggage exposure
- Gate and maintenance relationships
- Root-cause narratives
- Suggested operator actions

### Airport Workspaces

AeroPulse provides connected operational workspaces for:

- Dashboard
- Flights
- Passengers
- Gates
- Security
- Baggage
- Maintenance
- Staff
- Retail
- Timeline
- Insights
- Settings

These are not isolated pages. Every workspace uses the same shared relationship graph.

### Global Command Palette

Press `Ctrl + K` or `Cmd + K` to search across:

- Flights
- Gates
- Passengers
- Staff
- Baggage
- Maintenance records

The palette supports keyboard navigation, recent entities, no-result states and direct drill-down.

### Accessibility and Reliability

- Keyboard-operable interactions
- Descriptive status labels
- Status is never communicated through colour alone
- Reduced-motion support
- Responsive desktop, laptop, tablet and mobile layouts
- Loading skeletons
- Empty states
- Visible CSV error states
- Persistent operator preferences

---

## Connected Data Model

All eight supplied CSV files are parsed locally in the browser using PapaParse.

| Dataset | Operational purpose | Relationship |
|---|---|---|
| `flights.csv` | Flight schedules, routes, gates, terminals, status and delays | Central flight identifier |
| `gate_events.csv` | Gate assignments, occupancy and event history | Flight and gate identifiers |
| `passengers.csv` | Passenger journeys, check-in, boarding and connection exposure | Flight and passenger identifiers |
| `baggage.csv` | Bag lifecycle, handling and flight exposure | Flight and passenger identifiers |
| `security_screening.csv` | Screening lane, timing and clearance outcome | Passenger identity and event time |
| `maintenance_logs.csv` | Aircraft work orders, faults and operational impact | Flight and aircraft identifiers |
| `staff_shifts.csv` | Shift coverage, staff function and duty assignment | Staff and operational assignment |
| `retail_transactions.csv` | Journey-linked commercial activity | Passenger and flight identifiers |

### Relationship Structure

```text
                         ┌─────────────────┐
                         │     Flight      │
                         └────────┬────────┘
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
             ▼                    ▼                    ▼
       Gate Events           Passengers            Baggage
             │                    │                    │
             ▼                    ▼                    │
           Gates         Security Screening           │
             │                    │                    │
             └──────────────┬─────┴──────────────┬─────┘
                            │                    │
                            ▼                    ▼
                      Staff Coverage       Retail Activity
                            │                    │
                            └─────────┬──────────┘
                                      ▼
                               Maintenance
                                      │
                                      ▼
                           Alerts and Insights
```

The data layer parses and normalizes the files once, applies documented semantic mappings, creates indexes for natural join keys and exposes a shared in-memory relationship graph to every workspace.

No operational total is retrieved from an external API or database.

---

## Application Architecture

```text
public/data/*.csv
        │
        ▼
PapaParse client-side parsing
        │
        ▼
Schema normalization and semantic mapping
        │
        ▼
Normalized in-memory relationship graph
        │
        ├── Simulation clock
        ├── Event revelation
        ├── Search and filtering
        ├── Entity relationship lookup
        ├── Health-score calculation
        ├── Reasoned alert generation
        ├── Statistical insight engine
        └── React operational workspaces
```

Local storage is used only for:

- Simulation position
- Simulation speed
- Operator role
- Interface density
- Lineage preference
- Audio preference
- Dismissed interaction guidance

The application remains completely functional without a backend.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| React 19 | Component and application architecture |
| TypeScript | Type-safe data modelling |
| Vite | Development and production build tooling |
| Tailwind CSS | Responsive interface styling |
| PapaParse | Client-side CSV parsing |
| Framer Motion | Operational transitions and aircraft movement |
| Lucide React | Accessible interface iconography |

---

## Local Installation

### Requirements

- Node.js 18 or later
- npm

### Setup

```bash
git clone https://github.com/Janicebenita/aeropulse-frontend-wars-2026.git
cd aeropulse-frontend-wars-2026
npm install
npm run dev
```

Open the URL displayed by Vite, normally:

```text
http://localhost:5173
```

### Production Build

```bash
npm run build
npm run preview
```

---

## 90-Second Judge Demo

### 0–15 seconds: Establish the product

Open the landing page and enter the Command Center.

Explain:

> AeroPulse turns eight static airport datasets into one simulated real-time operations environment.

### 15–30 seconds: Show situational awareness

Point out:

- Airport health
- Active flights
- Passenger exposure
- Security pressure
- Gate availability
- Maintenance issues
- Active alerts

### 30–45 seconds: Demonstrate the digital twin

Select a glowing occupied gate and launch its connected aircraft.

Explain that the flight and gate information comes from the supplied flight and gate-event records.

### 45–60 seconds: Investigate a disruption

Open a delayed flight and show its relationships with:

- Gate events
- Passengers
- Baggage
- Security
- Maintenance
- Staff
- Retail activity

### 60–75 seconds: Show reasoning

Open an active alert and demonstrate:

- Root cause
- Affected entities
- Passenger exposure
- Baggage exposure
- Predicted downstream effect
- Suggested operator action

### 75–90 seconds: Show the differentiator

Open the Intelligence Center and demonstrate:

- Gate pressure
- Statistical anomalies
- Cascade Radar
- Data lineage

Finish with:

> AeroPulse does not only show what is happening. It connects why it is happening, who is affected and what the operator should investigate next.

---

## Source-Data Transparency

AeroPulse preserves the supplied dataset values instead of inventing artificial variety.

Where source fields are uniform, the application derives additional operational meaning only through valid relationships such as:

- Flight-delay exposure
- Event timing
- Passenger linkage
- Baggage linkage
- Security lane distribution
- Gate pressure
- Maintenance impact
- Staff coverage
- Retail association

The simulation changes how events are revealed and interpreted. It does not replace the supplied records with dummy operational data.

---

## Rule Compliance

| Requirement | Status |
|---|---|
| Frontend-only application | ✅ Compliant |
| React 19 | ✅ Compliant |
| TypeScript | ✅ Compliant |
| Vite | ✅ Compliant |
| Tailwind CSS | ✅ Compliant |
| Supplied CSV data is the primary data source | ✅ Compliant |
| Minimum four datasets integrated | ✅ All eight connected |
| No Next.js | ✅ Compliant |
| No backend development | ✅ Compliant |
| No Firebase or Supabase | ✅ Compliant |
| No database | ✅ Compliant |
| No external APIs | ✅ Compliant |
| Local storage only for local state | ✅ Compliant |
| Simulated real-time behaviour | ✅ Implemented |
| Responsive interface | ✅ Implemented |
| Search, filters and drill-down | ✅ Implemented |
| Original interface | ✅ No pre-built dashboard template |
| GitHub repository | ✅ Available |
| Live deployment | ✅ Available |

---

## Judging Criteria Coverage

| Judging area | AeroPulse implementation |
|---|---|
| Product Thinking | Monitor → detect → investigate → act workflow |
| User Experience | Connected drill-down, global search and clear operational hierarchy |
| Visual Design | Original mission-control interface and interactive airside twin |
| Functionality | Filters, alerts, simulation, search, movement and investigation |
| Code Quality | Typed models, shared graph, reusable components and separated logic |
| Creativity | Relationship Explorer, Cascade Radar and Judge Mode lineage |
| Performance | Parse-once data model, memoized derivations and controlled simulation updates |
| Data Visualization | Airport map, lane capacity, gate pressure, health and timelines |

---

## Documentation

- [`DATA_SCHEMA.md`](./DATA_SCHEMA.md) — field mappings, dataset semantics and join relationships
- [`PROJECT_EXPLANATION.md`](./PROJECT_EXPLANATION.md) — product thinking and architecture
- [`DEMO_SCRIPT.md`](./DEMO_SCRIPT.md) — rehearsed judging walkthrough

---

## Important Links

- **Live Application:** [aeropulse-frontend-wars-2026.vercel.app](https://aeropulse-airport-operation-lhar.vercel.app/)
- **GitHub Repository:** [github.com/Janicebenita/aeropulse-frontend-wars-2026](https://github.com/Janicebenita/AeroPulse-Control-Center)

---

## Author

Developed by **Janice Benita F** as an original frontend engineering submission for:

**Frontend Wars 2026 Grand Finale — Airport Operations Control Center**

> **AeroPulse — Monitor. Understand. Act.**
