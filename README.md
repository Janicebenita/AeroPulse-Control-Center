<p align="center">
  <img src="./public/aeropulse-logo.png" alt="AeroPulse Logo" width="190" />
</p>

<h1 align="center">✈️ AeroPulse Control Center</h1>

<h3 align="center">Airport operations, alive in one pulse.</h3>

<p align="center">
  A frontend-only Airport Operations Control Center that connects eight supplied CSV datasets into one simulated real-time operational experience.
</p>

<p align="center">
  <a href="https://aeropulse-airport-operation-lhar.vercel.app/"><strong>🚀 Live Demo</strong></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/Janicebenita/AeroPulse-Control-Center"><strong>💻 Source Code</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=081526" alt="React 19" />
  <img src="https://img.shields.io/badge/Vite-6-646CFF?logo=vite&logoColor=white" alt="Vite 6" />
  <img src="https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Tailwind-CSS-06B6D4?logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/Architecture-Frontend%20Only-2EE6A6" alt="Frontend Only" />
</p>

<p align="center"><strong>Frontend Wars 2026 Grand Finale — Airport Operations Control Center</strong></p>

---

## 📌 Overview

Airport disruptions are connected. A crowded security lane can delay boarding, hold a gate and affect the next flight, its passengers, baggage and airport revenue.

**AeroPulse** transforms static airport records into one connected operational workflow:

<p align="center"><strong>MONITOR → DETECT → INVESTIGATE → ACT</strong></p>

It helps an operator understand **what is happening, why it is happening, who is affected and what should happen next**.

---

## 🌟 What Makes AeroPulse Unique

| Signature feature | Operational value |
|---|---|
| 🔗 **Relationship Explorer** | Connects a selected flight, gate or passenger to security, baggage, staff, maintenance, retail and timeline records. |
| 🛫 **Airside Digital Twin** | Displays live gate conditions and launches the selected aircraft along an animated SVG taxi route. |
| 🧠 **Explainable Intelligence** | Shows root cause, affected entities, downstream exposure and a recommended operator action. |
| 📡 **Cascade Radar** | Uses transparent rule-based analysis to forecast the next connected operational impact. |
| 🧬 **Judge Mode Lineage** | Reveals which supplied CSV datasets contribute to visible metrics and insights. |

```text
Flight → Gate → Passengers → Security → Baggage
       → Staff → Maintenance → Retail → Timeline
```

---

## ⚡ Key Features

- ⏱️ Simulation clock with `1×`, `5×` and `30×` speeds
- 📰 Live operational event feed and rolling timeline
- 🚨 Reasoned alerts with affected passenger and baggage counts
- 🗺️ Interactive airport map with gate selection and aircraft movement
- 🔍 Search, filters, sorting and connected entity drill-down
- ⌨️ Global `Ctrl/Cmd + K` command palette
- 📊 Passenger, gate, security, baggage, maintenance, staff and retail workspaces
- 📈 Statistical anomaly detection and gate-pressure insights
- 💾 Persistent simulation state with one-click demo reset
- ♿ Responsive layout, keyboard navigation and reduced-motion support

---

## 🗂️ Connected Datasets

All eight supplied CSV files are parsed locally in the browser using PapaParse and joined through natural identifiers.

| Dataset | Purpose |
|---|---|
| `flights.csv` | Schedule, route, gate, terminal, status and delay |
| `gate_events.csv` | Gate assignment, occupancy and event history |
| `passengers.csv` | Journey, check-in, boarding and connection exposure |
| `baggage.csv` | Bag lifecycle and flight/passenger handling context |
| `security_screening.csv` | Screening lane, timing and outcome |
| `maintenance_logs.csv` | Work orders and aircraft operational impact |
| `staff_shifts.csv` | Staff function, shift and coverage |
| `retail_transactions.csv` | Journey-linked commercial activity |

### Data flow

```text
CSV files
    ↓
PapaParse + semantic normalization
    ↓
In-memory relationship graph
    ↓
Simulation · Alerts · Insights · Operational Workspaces
```

The datasets are parsed once and cached in memory. `localStorage` is used only for simulation state and operator preferences.

---

## 🧰 Tech Stack

| Technology | Usage |
|---|---|
| **React 19** | Application and component architecture |
| **TypeScript** | Typed data models and safer relationships |
| **Vite** | Fast development and production builds |
| **Tailwind CSS** | Responsive operational interface |
| **PapaParse** | Client-side CSV parsing |
| **Framer Motion** | State transitions and aircraft animation |
| **Lucide React** | Accessible interface icons |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Janicebenita/AeroPulse-Control-Center.git
cd AeroPulse-Control-Center
```

### 2. Install dependencies

```bash
npm install
```

### 3. Start the application

```bash
npm run dev
```

Open the local URL displayed by Vite, normally `http://localhost:5173`.

### Production build

```bash
npm run build
npm run preview
```

---

## 🎬 90-Second Demo Flow

1. Enter the Command Center and introduce the simulation clock.
2. Show airport health, event feed and active reasoned alerts.
3. Select an occupied gate and launch its connected aircraft.
4. Open a delayed flight and reveal its cross-dataset relationships.
5. Explain its root-cause narrative and affected journeys.
6. Open **Insights** and demonstrate Cascade Radar.
7. Enable **Lineage Mode** to reveal the data behind each conclusion.

---

## 🏆 Judging Criteria Coverage

| Criterion | AeroPulse response |
|---|---|
| **Product Thinking** | Real monitor → detect → investigate → act workflow |
| **User Experience** | Global search, drill-down panels and clear operational hierarchy |
| **Visual Design** | Original mission-control UI and interactive digital twin |
| **Functionality** | Simulation, filtering, alerts, movement and investigation |
| **Creativity** | Relationship Explorer, Cascade Radar and Lineage Mode |
| **Performance** | Parse-once model, indexed joins and controlled clock updates |
| **Data Visualization** | Gate map, lane load, pressure, health and timeline views |
| **Code Quality** | Typed models, reusable components and separated data logic |

---

## ✅ Rule Compliance

- ✅ Frontend-only application
- ✅ React 19, TypeScript, Vite and Tailwind CSS
- ✅ All eight supplied CSV datasets meaningfully integrated
- ✅ No backend or server-side application logic
- ✅ No Firebase, Supabase or database
- ✅ No external APIs
- ✅ No Next.js
- ✅ No pre-built dashboard template
- ✅ Simulated real-time behaviour derived from supplied records
- ✅ Responsive and keyboard-accessible interface

---

## 📚 Documentation

- [`DATA_SCHEMA.md`](./DATA_SCHEMA.md) — field mappings and relationships
- [`PROJECT_EXPLANATION.md`](./PROJECT_EXPLANATION.md) — product and architecture explanation
- [`DEMO_SCRIPT.md`](./DEMO_SCRIPT.md) — judging walkthrough

---

<h3 align="center">✈️ Monitor. Understand. Act.</h3>

<p align="center">
  Built by <strong>Janice Benita F</strong> for the<br />
  <strong>Frontend Wars 2026 Grand Finale</strong>
</p>
