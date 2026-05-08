"""Stackly ThemeForest Gap Analysis Dashboard."""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Stackly ThemeForest Gap Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject dark theme so we don't need a .streamlit/config.toml
st.markdown("""
<style>
    .stApp { background-color: #0E1117; }

    [data-testid="stSidebar"] { background-color: #1E1E2E; }
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stCaption { color: #FAFAFA !important; }
    [data-testid="stSidebar"] .stSelectbox label { color: #D1D5DB !important; }

    .stMainBlockContainer h1 { color: #FFFFFF !important; }
    .stMainBlockContainer h2 { color: #FFFFFF !important; }
    .stMainBlockContainer h3 { color: #FFFFFF !important; }

    [data-testid="stTitle"],
    [data-testid="stSubheader"],
    [data-testid="stHeader"] { color: #FFFFFF !important; }

    .stMainBlockContainer p { color: #E5E7EB !important; }
    .stMainBlockContainer span { color: #E5E7EB !important; }
    .stMainBlockContainer label { color: #E5E7EB !important; }

    [data-testid="stMetricLabel"] { color: #D1D5DB !important; }
    [data-testid="stMetricValue"] { color: #FFFFFF !important; }
    [data-testid="stCaptionContainer"] { color: #9CA3AF !important; }

    hr { border-color: #374151 !important; }

    .stHeading h1, .stHeading h2, .stHeading h3 { color: #FFFFFF !important; }

    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3 { color: #FFFFFF !important; }
</style>
""", unsafe_allow_html=True)


COLORS = {
    "Fashion": "#3B82F6",
    "Fundraising": "#10B981",
    "Minimal-Retail": "#F59E0B",
    "Benchmark": "#EF4444",
    "Competitor": "#8B5CF6",
    "Neutral": "#6B7280",
}

WEBSITES = ["Fashion", "Fundraising", "Minimal-Retail"]
CATEGORIES = [
    "Product Quality",
    "Functionality & UX",
    "Support & Updates",
    "Marketplace Experience",
    "Technical Performance",
]


# TODO: hook up real data once we have it — for now everything is simulated
def get_gap_scores() -> pd.DataFrame:
    """Scores out of 100 across the 5 gap categories."""
    return pd.DataFrame({
        "Category": CATEGORIES,
        "Fashion":        [45, 38, 5, 12, 30],
        "Fundraising":    [62, 58, 5, 15, 55],
        "Minimal-Retail": [28, 32, 5, 10, 42],
    })


def get_feature_matrix() -> pd.DataFrame:
    # Present=2, Partial=1, Missing=0, N/A=None
    rows = [
        ("Homepage Variants",        1, 1, 0),
        ("Product/Campaign Pages",   2, 2, 2),
        ("Search Bar",               0, 0, 0),
        ("Product Filtering",        0, None, 0),
        ("Breadcrumb Navigation",    0, 0, 0),
        ("Working Social Links",     0, 0, 0),
        ("FAQ Section",              0, 2, 2),
        ("Blog Section",             2, 0, 0),
        ("Preloader",                0, 2, 0),
        ("Documentation",            0, 0, 0),
        ("SEO Meta Tags",            0, 0, 0),
        ("Open Graph Tags",          0, 0, 0),
        ("WebP Images",              0, 2, 2),
        ("Lazy Loading",             0, 0, 0),
        ("Contact Form (Visual)",    2, 2, 2),
        ("Cart (Visual)",            2, 0, 2),
        ("Login Page (Visual)",      2, 0, 2),
        ("Dashboard Page (Visual)",  0, 2, 2),
    ]
    return pd.DataFrame(rows, columns=["Feature", "Fashion", "Fundraising", "Minimal-Retail"])


def get_technical_metrics() -> pd.DataFrame:
    """Simulated technical metrics with the ThemeForest benchmark."""
    return pd.DataFrame({
        "Metric": [
            "Page Load Time (s)",
            "Performance Score",
            "Image Optimization (%)",
            "Mobile Responsiveness (%)",
            "SEO Score",
            "Accessibility Score",
        ],
        "Fashion":        [4.2, 42, 35, 60, 15, 48],
        "Fundraising":    [2.1, 68, 78, 75, 18, 55],
        "Minimal-Retail": [2.8, 55, 72, 65, 16, 50],
        "Benchmark":      [1.5, 90, 95, 95, 85, 80],
    })


def get_competitor_pages() -> pd.DataFrame:
    df = pd.DataFrame({
        "Template": [
            "Flavor (Competitor)",
            "Porto (Competitor)",
            "Charity #1 (Competitor)",
            "Hmart (Competitor)",
            "Stackly Fashion",
            "Stackly Fundraising",
            "Stackly Minimal-Retail",
        ],
        "Pages": [46, 40, 30, 26, 10, 8, 5],
        "Type":  ["Competitor"] * 4 + ["Stackly Fashion", "Stackly Fundraising", "Stackly Minimal-Retail"],
    })
    return df.sort_values("Pages", ascending=True)


def get_recommendations() -> pd.DataFrame:
    return pd.DataFrame({
        "Recommendation": [
            "Add SEO meta tags & Open Graph across all pages",
            "Implement working search bar & filtering",
            "Build proper documentation package",
            "Optimize images (WebP + lazy loading)",
            "Add breadcrumb navigation",
            "Fix broken social media links",
            "Increase homepage variants (3+ per template)",
            "Add preloader & loading states",
        ],
        "Priority": ["High", "High", "High", "High", "Medium", "Medium", "Medium", "Medium"],
        "Impact":   ["High", "High", "High", "High", "Medium", "Medium", "High", "Medium"],
        "Status":   ["Not Started"] * 8,
    })


def get_readiness_scores() -> dict:
    return {"Fashion": 26, "Fundraising": 39, "Minimal-Retail": 19}


with st.sidebar:
    st.markdown("## 📊 Stackly")
    st.caption("ThemeForest Gap Analysis")
    st.divider()

    selected_site = st.selectbox(
        "Website",
        ["All"] + WEBSITES,
        help="Filter visuals by website",
    )
    selected_category = st.selectbox(
        "Category",
        ["All"] + CATEGORIES,
        help="Filter the radar / score breakdown by category",
    )


st.title("Stackly ThemeForest Gap Analysis Dashboard")
st.caption(
    "Comparing 3 Stackly templates against ThemeForest marketplace standards — "
    "where we stand, where the gaps are, and what to fix next."
)
st.divider()


# Section 1 — KPI cards
gap_df = get_gap_scores()
feat_df = get_feature_matrix()
tech_df = get_technical_metrics()
recs_df = get_recommendations()
readiness = get_readiness_scores()

selected_sites = WEBSITES if selected_site == "All" else [selected_site]

# simple mean of the 3 readiness scores (good enough for now)
overall_readiness = round(sum(readiness[s] for s in selected_sites) / len(selected_sites), 1)

gap_count = 0
for s in selected_sites:
    gap_count += int((feat_df[s] == 0).sum() + (feat_df[s] == 1).sum())

critical_count = int((recs_df["Priority"] == "High").sum())

present_total = 0
total_features = 0
for s in selected_sites:
    present_total += int((feat_df[s] == 2).sum())
    total_features += int(feat_df[s].notna().sum())

avg_tech = round(gap_df.set_index("Category").loc["Technical Performance", selected_sites].mean(), 1)

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Overall Readiness", f"{overall_readiness}/100")
k2.metric("Total Gaps Identified", f"{gap_count}")
k3.metric("Critical Issues", f"{critical_count}", help="High-priority recommendations")
k4.metric("Features Present", f"{present_total}/{total_features}")
k5.metric("Avg Technical Score", f"{avg_tech}/100")

st.divider()


# Section 2 — Radar chart (Dan wants this as the hero visual)
st.subheader("Gap Analysis Scores by Category")
st.caption("How each template scores across the 5 ThemeForest evaluation categories (out of 100).")

cats_to_show = CATEGORIES if selected_category == "All" else [selected_category]
radar_df = gap_df[gap_df["Category"].isin(cats_to_show)]

radar_fig = go.Figure()
for site in selected_sites:
    radar_fig.add_trace(go.Scatterpolar(
        r=radar_df[site].tolist() + [radar_df[site].tolist()[0]],
        theta=radar_df["Category"].tolist() + [radar_df["Category"].tolist()[0]],
        fill="toself",
        name=site,
        line=dict(color=COLORS[site], width=2),
        opacity=0.7,
    ))

radar_fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 100], gridcolor="#374151"),
        angularaxis=dict(gridcolor="#374151"),
        bgcolor="#1E1E2E",
    ),
    showlegend=True,
    height=520,
    paper_bgcolor="#0E1117",
    font=dict(color="#FAFAFA"),
    margin=dict(t=40, b=40, l=80, r=80),
)
st.plotly_chart(radar_fig, use_container_width=True)

st.divider()


# Section 3 — Feature completion matrix
st.subheader("Feature Completion Matrix")
st.caption("Green = Present · Amber = Partial · Red = Missing · Grey = N/A")

heat_df = feat_df.set_index("Feature")[selected_sites]

heat_fig = go.Figure(data=go.Heatmap(
    z=heat_df.values,
    x=heat_df.columns,
    y=heat_df.index,
    colorscale=[
        [0.0, "#EF4444"],
        [0.5, "#F59E0B"],
        [1.0, "#10B981"],
    ],
    zmin=0,
    zmax=2,
    xgap=2,
    ygap=2,
    hovertemplate="<b>%{y}</b><br>%{x}: %{z}<extra></extra>",
    colorbar=dict(
        title="Status",
        tickvals=[0, 1, 2],
        ticktext=["Missing", "Partial", "Present"],
    ),
))
heat_fig.update_layout(
    height=600,
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font=dict(color="#FAFAFA"),
    margin=dict(t=20, b=40, l=180, r=40),
)
st.plotly_chart(heat_fig, use_container_width=True)

st.divider()


# Section 4 — Technical performance vs benchmark
st.subheader("Technical Performance vs ThemeForest Benchmark")
st.caption("How far each template is from the marketplace standard. Lower is better for Page Load Time only.")

tech_long_cols = selected_sites + ["Benchmark"]
tech_long = tech_df.melt(id_vars="Metric", value_vars=tech_long_cols, var_name="Source", value_name="Value")
color_map = {**{s: COLORS[s] for s in WEBSITES}, "Benchmark": COLORS["Benchmark"]}

tech_fig = px.bar(
    tech_long,
    x="Metric",
    y="Value",
    color="Source",
    barmode="group",
    color_discrete_map=color_map,
    text="Value",
)
tech_fig.update_traces(textposition="outside", textfont=dict(size=10))
tech_fig.update_layout(
    height=500,
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font=dict(color="#FAFAFA"),
    xaxis=dict(gridcolor="#374151"),
    yaxis=dict(gridcolor="#374151", title="Score / Value"),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    margin=dict(t=20, b=80, l=40, r=40),
)
st.plotly_chart(tech_fig, use_container_width=True)

st.divider()


# Section 5 — Competitor landscape
st.subheader("Competitor Landscape — Page Count")
st.caption("Stackly templates ship with far fewer pages than top-selling ThemeForest competitors.")

comp_df = get_competitor_pages()
comp_df["Color"] = comp_df["Type"].map({
    "Competitor": COLORS["Competitor"],
    "Stackly Fashion": COLORS["Fashion"],
    "Stackly Fundraising": COLORS["Fundraising"],
    "Stackly Minimal-Retail": COLORS["Minimal-Retail"],
})

comp_fig = go.Figure(go.Bar(
    x=comp_df["Pages"],
    y=comp_df["Template"],
    orientation="h",
    marker=dict(color=comp_df["Color"]),
    text=comp_df["Pages"],
    textposition="outside",
    hovertemplate="<b>%{y}</b><br>Pages: %{x}<extra></extra>",
))
comp_fig.update_layout(
    height=420,
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font=dict(color="#FAFAFA"),
    xaxis=dict(gridcolor="#374151", title="Total Pages"),
    yaxis=dict(gridcolor="#374151"),
    margin=dict(t=20, b=40, l=40, r=40),
)
st.plotly_chart(comp_fig, use_container_width=True)

st.divider()


# Section 6 — Recommendations tracker
st.subheader("Recommendations Priority Tracker")
st.caption("Eight recommendations from the gap analysis report — none started yet.")

def priority_badge(priority: str) -> str:
    color = "#EF4444" if priority == "High" else "#F59E0B"
    return f'<span style="background:{color};color:#FFFFFF !important;padding:3px 10px;border-radius:10px;font-size:12px;font-weight:600;">{priority}</span>'

def status_badge(status: str) -> str:
    return f'<span style="background:#374151;color:#FAFAFA !important;padding:3px 10px;border-radius:10px;font-size:12px;">{status}</span>'

def impact_badge(impact: str) -> str:
    color = "#10B981" if impact == "High" else "#6B7280"
    return f'<span style="background:{color};color:#FFFFFF !important;padding:3px 10px;border-radius:10px;font-size:12px;">{impact}</span>'

display_recs = recs_df.copy()
display_recs["Priority"] = display_recs["Priority"].apply(priority_badge)
display_recs["Impact"] = display_recs["Impact"].apply(impact_badge)
display_recs["Status"] = display_recs["Status"].apply(status_badge)

st.markdown(
    display_recs.to_html(escape=False, index=False, classes="rec-table"),
    unsafe_allow_html=True,
)

st.markdown("""
<style>
.rec-table {
    width: 100%;
    border-collapse: collapse;
    color: #FAFAFA !important;
    margin-top: 12px;
}
.rec-table th, .rec-table td {
    color: #FAFAFA !important;
}
.rec-table th {
    background-color: #1E1E2E;
    text-align: left;
    padding: 10px;
    border-bottom: 1px solid #374151;
}
.rec-table td {
    padding: 10px;
    border-bottom: 1px solid #1E1E2E;
}
.rec-table tr:hover { background-color: #1E1E2E; }
</style>
""", unsafe_allow_html=True)

st.divider()


# Section 7 — Readiness gauges (the headline numbers)
st.subheader("Marketplace Readiness")
st.caption("How close each template is to ThemeForest publish-readiness today.")

g1, g2, g3 = st.columns(3)
gauge_cols = {"Fashion": g1, "Fundraising": g2, "Minimal-Retail": g3}

for site, col in gauge_cols.items():
    score = readiness[site]
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={"suffix": "%", "font": {"size": 36, "color": "#FAFAFA"}},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#FAFAFA"},
            "bar": {"color": COLORS[site]},
            "bgcolor": "#1E1E2E",
            "borderwidth": 0,
            "steps": [
                {"range": [0, 40], "color": "#7F1D1D"},
                {"range": [40, 70], "color": "#78350F"},
                {"range": [70, 100], "color": "#064E3B"},
            ],
            "threshold": {
                "line": {"color": COLORS["Benchmark"], "width": 3},
                "thickness": 0.85,
                "value": 80,
            },
        },
        title={"text": f"<b>{site}</b>", "font": {"color": "#FAFAFA", "size": 16}},
    ))
    fig.update_layout(
        height=260,
        paper_bgcolor="#0E1117",
        font={"color": "#FAFAFA"},
        margin=dict(t=40, b=10, l=20, r=20),
    )
    col.plotly_chart(fig, use_container_width=True)

st.caption("Red threshold line marks the 80% target for ThemeForest acceptance.")

st.divider()
st.caption("Stackly · Internal Gap Analysis Dashboard · Sample data")
