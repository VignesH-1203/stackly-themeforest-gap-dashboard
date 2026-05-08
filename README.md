# Stackly ThemeForest Gap Analysis Dashboard

An interactive Streamlit dashboard that visualises a gap analysis comparing three Stackly website templates — **Fashion**, **Fundraising**, and **Minimal-Retail** — against ThemeForest marketplace standards. The dashboard turns the report findings into actionable insights through KPI cards, a category radar, a feature completion matrix, technical performance vs benchmark, competitor page-count comparison, a recommendations tracker, and per-template readiness gauges.

## Tech Stack

- Python 3
- Streamlit
- Plotly (Express + Graph Objects)
- Pandas

All sample data is generated inside `app.py` — no external CSV files required.

## Run Locally

Clone the repo and install the dependencies:

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
pip install -r requirements.txt
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

## Project Structure

```
.
├── app.py             # main Streamlit dashboard
├── requirements.txt   # Python dependencies
└── README.md
```

## Dashboard Sections

1. **KPI Cards** — Overall readiness, total gaps, critical issues, features present, average technical score
2. **Gap Analysis Radar** — Category scores across all 3 templates
3. **Feature Completion Matrix** — Heatmap of feature presence (Present / Partial / Missing)
4. **Technical Performance vs Benchmark** — Grouped bar chart against ThemeForest standards
5. **Competitor Landscape** — Page-count comparison with top-selling marketplace templates
6. **Recommendations Tracker** — Prioritised action items with status badges
7. **Marketplace Readiness Gauges** — Per-template readiness % vs the 80% target
