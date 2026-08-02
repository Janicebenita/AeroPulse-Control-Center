# AeroPulse

AeroPulse is a frontend-only airport operations command center built for the Frontend Wars 2026 Grand Finale. It turns the supplied static CSV records into a replayable operational environment: monitor the airport, detect exceptions, investigate their causes, interpret patterns, and inspect the connected impact.

## Run locally

```bash
npm install
npm run dev
```

Open the URL printed by Vite (normally `http://localhost:5173`). Production verification: `npm run build`.

## Stack

React 19, Vite, TypeScript, Tailwind CSS, PapaParse, Framer Motion and Lucide icons. There is no Next.js, backend, database, Firebase, Supabase, or external API.

## Data integration

All eight supplied datasets are parsed once in the browser from `public/data`: flights, passengers, baggage, gate events, security screening, maintenance logs, staff shifts, and retail transactions. The source exports use numeric headers, so `lib/data.ts` applies a documented semantic adapter based on the dictionary, relationships, and observed values. `flight_id` connects flights to passengers, baggage, gate events, retail, and maintenance; passenger/passport and PNR identifiers connect the passenger journey; staff identifiers and assignments connect shifts to operational areas.

## Features

- Persisted 1×/5×/30× simulation clock and one-click demo reset
- SVG airport digital twin with live semantic gate states
- Live event feed, rolling horizon, and reasoned alerts
- Universal slide-over investigation surface and relationship explorer
- Root-cause narratives with affected passenger, baggage, gate, maintenance, and retail counts
- Ctrl/Cmd+K command palette, keyboard operation, Escape-to-close, click-away dismissal
- Loading, empty, and explicit data-error states
- Responsive single-column priority layout below desktop widths
- Judge data-lineage mode showing the datasets behind visible conclusions
- Operational Intelligence view with data-derived gate pressure visualization
- Z-score anomaly detection and real Pearson correlation analysis
- Cascade Radar: a transparent, rule-based forecast of downstream gate and passenger exposure
- All-eight-dataset relationship panel, including security records, gate staff and retail footprint
- Dedicated operational workspaces for passengers, security, baggage, maintenance, staff, retail, timeline and settings
- Nine airport-wide operational KPIs with horizontally responsive monitoring
- Cross-domain global search: passenger, baggage, maintenance and staff identifiers resolve to connected flights
- Professional desktop sidebar plus compact responsive navigation
- One-screen Airport Pulse answering delay, gate, baggage, passenger, staff and maintenance questions together
- Data-derived flight-integrity donut, security-lane load bars and ranked delay visualization
- Searchable, filterable and sortable flight operations table with sticky headers
- Operator identity card, original AeroPulse mark, and expanded local-only preferences
- Correct passenger checked-in and connection metrics from their distinct CSV fields
- Source-aware domain views: loaded baggage, lane timing, flight-linked maintenance urgency, staff functions, and retail transaction value

## Source-data transparency

Several supplied exports contain intentionally uniform fields: baggage is marked `Loaded`, security outcomes are `Clear`, maintenance source priority is `3`, staff department/gate assignments are `Ops`/`B12`, and retail store/product fields are `Duty Free`/`Perfume`. AeroPulse does not invent alternative values. It labels these limitations and derives useful operational context only through valid joins, such as flight delay exposure and functional staff-ID prefixes.

## Reliability

The app parses local CSVs only once, keeps the relational graph in memory, persists clock position in local storage, and derives every operational count from the supplied records. Status colors are paired with labels/icons and interactive map nodes support keyboard activation.
