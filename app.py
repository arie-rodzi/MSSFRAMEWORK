import streamlit as st
import json
from pathlib import Path

# =========================================================
# MSS 2026–2035 STRATEGIC INTELLIGENCE PORTAL
# Premium dark executive version
# Required file in same folder: mss_master_database.json
# =========================================================

st.set_page_config(
    page_title="MSS 2026–2035 Strategic Intelligence Portal",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

DATA_PATH = Path(__file__).parent / "mss_master_database.json"

if not DATA_PATH.exists():
    st.error("Missing data file: mss_master_database.json. Please place it in the same folder as app.py.")
    st.stop()

with open(DATA_PATH, "r", encoding="utf-8") as f:
    DB = json.load(f)

# ---------- Helpers ----------
def safe_get(dct, key, default=""):
    return dct.get(key, default) if isinstance(dct, dict) else default


def render_list(items):
    if not items:
        st.markdown('<div class="empty-note">No record available.</div>', unsafe_allow_html=True)
        return
    for item in items:
        st.markdown(f'<div class="lux-list-item">{item}</div>', unsafe_allow_html=True)


def render_premium_section(title, body=None):
    st.markdown(f'<div class="section-title"><span></span>{title}</div>', unsafe_allow_html=True)
    if body:
        st.markdown(f'<div class="lux-paragraph">{body}</div>', unsafe_allow_html=True)


# ---------- CSS ----------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap');

:root {
    --navy-950:#020617;
    --navy-900:#06111f;
    --navy-800:#0b1f3a;
    --navy-700:#123b63;
    --gold-100:#fff6cf;
    --gold-200:#f8e7a1;
    --gold-300:#f4d35e;
    --gold-500:#d4af37;
    --gold-700:#9f7611;
    --cyan:#5eead4;
    --emerald:#10b981;
    --white:#f8fafc;
    --muted:#b8c7da;
    --glass:rgba(8, 19, 36, .72);
    --glass2:rgba(255,255,255,.075);
}

[data-testid="stSidebar"], [data-testid="collapsedControl"] {display:none !important;}
[data-testid="stHeader"] {background:rgba(2,6,23,0) !important;}
[data-testid="stToolbar"] {display:none !important;}
.main .block-container {
    padding-top: 1.2rem;
    padding-bottom: 3rem;
    max-width: 1580px;
}

html, body, [class*="css"], .stMarkdown, .stTextInput, .stButton, .stTabs {
    font-family: 'Manrope', 'Segoe UI', Arial, sans-serif !important;
}

.stApp {
    color: var(--white);
    background:
        radial-gradient(circle at 12% 8%, rgba(212,175,55,.22), transparent 24%),
        radial-gradient(circle at 82% 12%, rgba(94,234,212,.15), transparent 22%),
        radial-gradient(circle at 70% 86%, rgba(212,175,55,.12), transparent 30%),
        linear-gradient(135deg, #020617 0%, #06111f 42%, #08182d 72%, #020617 100%);
}

.stApp::before {
    content:"";
    position:fixed;
    inset:0;
    pointer-events:none;
    z-index:0;
    background-image:
      linear-gradient(rgba(255,255,255,.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px);
    background-size: 58px 58px;
    mask-image: linear-gradient(to bottom, rgba(0,0,0,.75), rgba(0,0,0,.08));
}

.block-container {position:relative; z-index:1;}

h1, h2, h3, h4, h5, h6, p, li, label, span, div {color:inherit;}

/* HERO */
.hero-shell {
    position:relative;
    overflow:hidden;
    border-radius:34px;
    padding:1px;
    background:linear-gradient(135deg, rgba(255,246,207,.95), rgba(212,175,55,.36), rgba(94,234,212,.25), rgba(212,175,55,.70));
    box-shadow:0 28px 95px rgba(0,0,0,.55), 0 0 36px rgba(212,175,55,.16);
}
.hero-shell::after {
    content:"";
    position:absolute;
    inset:-140px;
    background:conic-gradient(from 45deg, transparent, rgba(255,246,207,.18), transparent, rgba(94,234,212,.10), transparent);
    animation:spinGlow 13s linear infinite;
    pointer-events:none;
}
@keyframes spinGlow {to {transform:rotate(360deg);}}
.hero {
    position:relative;
    z-index:1;
    border-radius:33px;
    padding:34px 38px 32px 38px;
    background:
      linear-gradient(135deg, rgba(2,6,23,.97), rgba(7,21,43,.92) 55%, rgba(15,38,68,.88)),
      url("data:image/svg+xml,%3Csvg width='1200' height='420' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' stroke='%23D4AF37' stroke-opacity='.12'%3E%3Cpath d='M0 320 C180 210 240 400 420 300 S760 120 980 245 1180 280 1200 190'/%3E%3Cpath d='M0 120 C240 220 300 70 500 150 S850 310 1200 95'/%3E%3C/g%3E%3C/svg%3E");
    border:1px solid rgba(255,246,207,.22);
}
.hero-kicker {
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    margin-bottom:18px;
}
.badge {
    display:inline-flex;
    align-items:center;
    gap:8px;
    padding:9px 14px;
    border-radius:999px;
    color:var(--gold-100);
    background:linear-gradient(135deg, rgba(212,175,55,.20), rgba(255,255,255,.06));
    border:1px solid rgba(248,231,161,.34);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.10), 0 0 24px rgba(212,175,55,.12);
    font-size:.80rem;
    font-weight:900;
    letter-spacing:.09em;
    text-transform:uppercase;
}
.hero h1 {
    font-family:'Playfair Display', Georgia, serif !important;
    color:#fffaf0;
    font-size:clamp(2.35rem, 4vw, 4.6rem);
    line-height:1.02;
    letter-spacing:-.04em;
    margin:0 0 18px 0;
    text-shadow:0 0 28px rgba(212,175,55,.35), 0 16px 45px rgba(0,0,0,.45);
}
.hero-grid {display:grid; grid-template-columns:1.15fr .85fr; gap:22px; align-items:stretch;}
.hero-text p {
    color:#dbeafe;
    font-size:1.02rem;
    line-height:1.62;
    margin:.35rem 0;
}
.hero-text b {color:var(--gold-200);}
.logic-card {
    border-radius:26px;
    padding:20px 22px;
    background:rgba(255,255,255,.06);
    border:1px solid rgba(255,246,207,.18);
    box-shadow:inset 0 1px 0 rgba(255,255,255,.12), 0 22px 60px rgba(0,0,0,.22);
}
.logic-card .label {
    color:var(--gold-200);
    font-weight:900;
    font-size:.82rem;
    text-transform:uppercase;
    letter-spacing:.12em;
}
.logic-card .chain {
    color:#f8fafc;
    font-size:1rem;
    line-height:1.55;
    margin-top:10px;
}

/* METRICS */
.metric-card {
    position:relative;
    overflow:hidden;
    min-height:132px;
    border-radius:24px;
    padding:19px 18px;
    background:linear-gradient(145deg, rgba(255,255,255,.105), rgba(255,255,255,.035));
    border:1px solid rgba(248,231,161,.22);
    box-shadow:0 22px 60px rgba(0,0,0,.32), inset 0 1px 0 rgba(255,255,255,.12);
}
.metric-card::before {
    content:"";
    position:absolute;
    top:-45px; right:-45px;
    width:120px; height:120px;
    border-radius:50%;
    background:radial-gradient(circle, rgba(212,175,55,.33), transparent 62%);
}
.metric-card h3 {
    position:relative;
    margin:0;
    color:var(--gold-200);
    font-size:2.25rem;
    font-weight:900;
    letter-spacing:-.05em;
}
.metric-card p {
    position:relative;
    margin:5px 0 0;
    color:#dbeafe;
    font-size:.92rem;
    font-weight:750;
}
.metric-card small {
    color:#93c5fd;
    font-size:.72rem;
    text-transform:uppercase;
    letter-spacing:.12em;
    font-weight:900;
}

/* HEADINGS */
.premium-heading {
    margin:34px 0 12px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:14px;
}
.premium-heading h2 {
    margin:0;
    color:#fffaf0;
    font-size:1.52rem;
    letter-spacing:-.02em;
    font-weight:900;
}
.premium-heading .sub {
    color:#9fb4cc;
    font-size:.9rem;
    font-weight:650;
}
.gold-line {
    height:1px;
    flex:1;
    background:linear-gradient(90deg, rgba(212,175,55,.75), transparent);
}

/* EXPANDER + TABS */
.streamlit-expanderHeader {
    background:rgba(255,255,255,.055) !important;
    border:1px solid rgba(248,231,161,.20) !important;
    border-radius:18px !important;
    color:#fffaf0 !important;
    font-weight:900 !important;
}
div[data-testid="stExpander"] {
    border:1px solid rgba(248,231,161,.14) !important;
    border-radius:22px !important;
    background:rgba(255,255,255,.035) !important;
    box-shadow:0 16px 48px rgba(0,0,0,.24);
}
.stTabs [data-baseweb="tab-list"] {
    gap:10px;
    background:rgba(255,255,255,.035);
    border:1px solid rgba(248,231,161,.14);
    padding:10px;
    border-radius:22px;
}
.stTabs [data-baseweb="tab"] {
    border-radius:16px;
    color:#dbeafe;
    font-weight:900;
    padding:10px 14px;
    background:rgba(255,255,255,.04);
}
.stTabs [aria-selected="true"] {
    background:linear-gradient(135deg, rgba(212,175,55,.28), rgba(255,255,255,.08)) !important;
    color:var(--gold-100) !important;
    border:1px solid rgba(248,231,161,.28);
}

/* MATRIX */
.matrix-head {
    min-height:82px;
    display:flex;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:12px 8px;
    border-radius:18px;
    background:linear-gradient(135deg, rgba(212,175,55,.24), rgba(18,59,99,.72));
    border:1px solid rgba(248,231,161,.32);
    color:#fff6cf;
    font-weight:950;
    font-size:.82rem;
    line-height:1.25;
    box-shadow:0 16px 44px rgba(0,0,0,.28), inset 0 1px 0 rgba(255,255,255,.12);
}
.row-head {
    height:124px;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    text-align:center;
    padding:10px;
    border-radius:20px;
    background:linear-gradient(135deg, rgba(2,6,23,.95), rgba(18,59,99,.72));
    border:1px solid rgba(248,231,161,.28);
    box-shadow:0 16px 46px rgba(0,0,0,.30), inset 0 1px 0 rgba(255,255,255,.10);
}
.row-head strong {
    display:block;
    color:var(--gold-200);
    font-size:1.08rem;
    font-weight:950;
    margin-bottom:5px;
}
.row-head span {
    color:#dbeafe;
    font-size:.72rem;
    line-height:1.15;
    font-weight:750;
}

div.stButton > button {
    position:relative;
    overflow:hidden;
    min-height:124px;
    white-space:normal;
    border-radius:20px;
    padding:12px 10px;
    color:#fffaf0;
    font-weight:950;
    line-height:1.18;
    border:1px solid rgba(248,231,161,.22);
    background:
      radial-gradient(circle at top left, rgba(212,175,55,.24), transparent 36%),
      linear-gradient(145deg, rgba(11,31,58,.96), rgba(2,6,23,.94));
    box-shadow:0 18px 48px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.10);
    transition:all .18s ease;
}
div.stButton > button::before {
    content:"";
    position:absolute;
    inset:0;
    background:linear-gradient(120deg, transparent 0%, rgba(255,255,255,.13) 45%, transparent 60%);
    transform:translateX(-120%);
    transition:.45s ease;
}
div.stButton > button:hover {
    transform:translateY(-4px) scale(1.01);
    color:#fff6cf;
    border-color:rgba(248,231,161,.66);
    background:
      radial-gradient(circle at top left, rgba(248,231,161,.34), transparent 38%),
      linear-gradient(145deg, rgba(18,59,99,.98), rgba(6,17,31,.98));
    box-shadow:0 24px 70px rgba(0,0,0,.48), 0 0 26px rgba(212,175,55,.20), inset 0 1px 0 rgba(255,255,255,.17);
}
div.stButton > button:hover::before {transform:translateX(120%);}
div.stButton > button p {font-size:.82rem;}

/* SELECTED PANEL */
.panel {
    position:relative;
    overflow:hidden;
    border-radius:30px;
    padding:28px 30px;
    background:
       radial-gradient(circle at 88% 10%, rgba(212,175,55,.20), transparent 26%),
       linear-gradient(135deg, rgba(255,255,255,.105), rgba(255,255,255,.045));
    border:1px solid rgba(248,231,161,.28);
    box-shadow:0 30px 90px rgba(0,0,0,.44), inset 0 1px 0 rgba(255,255,255,.13);
}
.panel::before {
    content:"";
    position:absolute;
    left:0; top:0; bottom:0;
    width:6px;
    background:linear-gradient(180deg, var(--gold-200), var(--gold-500), transparent);
}
.panel-kicker {
    color:var(--gold-200);
    margin:0 0 9px 0;
    font-size:.80rem;
    letter-spacing:.15em;
    text-transform:uppercase;
    font-weight:950;
}
.panel-title {
    color:#fffaf0;
    margin:0 0 10px 0;
    font-size:clamp(1.75rem, 2.8vw, 3rem);
    line-height:1.05;
    font-weight:950;
    letter-spacing:-.045em;
}
.panel-meta {
    color:#dbeafe;
    font-weight:800;
    margin-bottom:12px;
}
.panel-meta b {color:var(--gold-200);}
.panel-summary {
    color:#d7e6f8;
    font-size:1rem;
    line-height:1.65;
    max-width:1180px;
}

/* CONTENT CARDS */
.section-title {
    display:flex;
    align-items:center;
    gap:10px;
    margin:20px 0 9px;
    color:#fffaf0;
    font-size:1.05rem;
    font-weight:950;
    letter-spacing:-.01em;
}
.section-title span {
    width:9px;
    height:24px;
    border-radius:99px;
    background:linear-gradient(180deg, var(--gold-200), var(--gold-700));
    box-shadow:0 0 18px rgba(212,175,55,.40);
}
.lux-paragraph, .lux-list-item {
    color:#dbeafe;
    line-height:1.65;
    font-size:.96rem;
}
.lux-list-item {
    margin:8px 0;
    padding:12px 14px 12px 16px;
    border-radius:16px;
    background:rgba(255,255,255,.055);
    border:1px solid rgba(248,231,161,.14);
    box-shadow:inset 0 1px 0 rgba(255,255,255,.08);
}
.tag {
    display:inline-block;
    padding:8px 11px;
    border-radius:999px;
    margin:5px 5px 5px 0;
    color:#fff6cf;
    font-size:.82rem;
    font-weight:900;
    background:linear-gradient(135deg, rgba(212,175,55,.23), rgba(255,255,255,.06));
    border:1px solid rgba(248,231,161,.24);
    box-shadow:0 10px 28px rgba(0,0,0,.20);
}
.trace {
    padding:20px;
    border-radius:22px;
    color:#fffaf0;
    font-weight:900;
    line-height:1.55;
    background:
      radial-gradient(circle at 10% 10%, rgba(212,175,55,.27), transparent 25%),
      linear-gradient(135deg, rgba(6,17,31,.98), rgba(18,59,99,.86));
    border:1px solid rgba(248,231,161,.30);
    box-shadow:0 22px 66px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.12);
}
.empty-note {color:#94a3b8; font-style:italic; padding:8px 0;}

/* Streamlit native adjustments */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background:rgba(255,255,255,.045) !important;
    border:1px solid rgba(248,231,161,.15) !important;
    border-radius:22px !important;
    box-shadow:0 18px 52px rgba(0,0,0,.25);
}
.stAlert {
    background:rgba(212,175,55,.10) !important;
    border:1px solid rgba(248,231,161,.22) !important;
    color:#fffaf0 !important;
    border-radius:18px !important;
}
input {
    background:rgba(2,6,23,.78) !important;
    color:#fffaf0 !important;
    border:1px solid rgba(248,231,161,.28) !important;
    border-radius:16px !important;
}
label {color:#fff6cf !important; font-weight:900 !important;}

.footer {
    margin-top:28px;
    padding:18px 20px;
    border-radius:22px;
    color:#9fb4cc;
    font-size:.82rem;
    background:rgba(255,255,255,.04);
    border:1px solid rgba(248,231,161,.12);
}

@media (max-width: 1000px) {
    .hero-grid {grid-template-columns:1fr;}
    .hero {padding:26px 22px;}
    .matrix-head {font-size:.72rem; min-height:72px;}
    .row-head, div.stButton > button {height:auto; min-height:110px;}
}
</style>
""",
    unsafe_allow_html=True,
)

meta = DB.get("meta", {})

# ---------- Hero ----------
st.markdown(
    f"""
<div class="hero-shell">
  <div class="hero">
    <div class="hero-kicker">
      <span class="badge">◆ MSS 2026–2035</span>
      <span class="badge">Strategic Intelligence Portal</span>
      <span class="badge">36-Cell Matrix Explorer</span>
    </div>
    <div class="hero-grid">
      <div class="hero-text">
        <h1>{safe_get(meta, 'title', 'Malaysian Standardisation Strategy 2026–2035')}</h1>
        <p><b>Vision:</b> {safe_get(meta, 'vision', '-')}</p>
        <p><b>Mission:</b> {safe_get(meta, 'mission', '-')}</p>
      </div>
      <div class="logic-card">
        <div class="label">Executive logic chain</div>
        <div class="chain">{safe_get(meta, 'logic_chain', 'Pillars → Domains → Strategic Cells → Initiatives → Outcomes → 2035 Targets')}</div>
      </div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ---------- Metrics ----------
metric_cols = st.columns(6)
cards = [
    ("6", "Pillars", "Strategic architecture"),
    ("6", "Domains", "National focus areas"),
    ("36", "Strategic Cells", "Clickable framework"),
    ("23+16", "Initiatives", "Implementation engine"),
    ("6", "Outcomes", "Performance logic"),
    ("2035", "Target Horizon", "Long-range transformation"),
]
for col, (num, label, note) in zip(metric_cols, cards):
    with col:
        st.markdown(
            f'<div class="metric-card"><small>{note}</small><h3>{num}</h3><p>{label}</p></div>',
            unsafe_allow_html=True,
        )

# ---------- Overview ----------
st.write("")
with st.expander("Executive Overview: Pillars, Domains and Strategic Outcomes", expanded=False):
    c1, c2, c3 = st.columns(3)
    with c1:
        render_premium_section("Strategic Pillars")
        for pid, p in DB.get("pillars", {}).items():
            st.markdown(
                f'<div class="lux-list-item"><b style="color:#f8e7a1">{pid}. {p.get("name", "")}</b><br>{p.get("core_question", "")}</div>',
                unsafe_allow_html=True,
            )
    with c2:
        render_premium_section("Strategic Domains")
        for did, d in DB.get("domains", {}).items():
            st.markdown(
                f'<div class="lux-list-item"><b style="color:#f8e7a1">{did}. {d.get("name", "")}</b><br>{d.get("summary", "")}</div>',
                unsafe_allow_html=True,
            )
    with c3:
        render_premium_section("Strategic Outcomes")
        for sid, s in DB.get("outcomes", {}).items():
            st.markdown(
                f'<div class="lux-list-item"><b style="color:#f8e7a1">{sid}. {s.get("name", "")}</b><br>{s.get("description", "")}</div>',
                unsafe_allow_html=True,
            )

# ---------- Matrix ----------
st.markdown(
    """
<div class="premium-heading">
  <div>
    <h2>Interactive 6×6 Strategic Framework Matrix</h2>
    <div class="sub">Click any box to open the full Executive Strategic Card. No sidebar is used.</div>
  </div>
  <div class="gold-line"></div>
</div>
""",
    unsafe_allow_html=True,
)

headers = [
    "Pillar",
    "D1<br>Infrastructure & Utilities",
    "D2<br>Industrial & Manufacturing",
    "D3<br>Consumer Safety",
    "D4<br>Agrofood, Halal & Biosecurity",
    "D5<br>Emerging Tech & Sustainability",
    "D6<br>Institutional Liaison",
]

hcols = st.columns([0.58, 1, 1, 1, 1, 1, 1])
for i, h in enumerate(headers):
    with hcols[i]:
        st.markdown(f'<div class="matrix-head">{h}</div>', unsafe_allow_html=True)

for p in range(1, 7):
    cols = st.columns([0.58, 1, 1, 1, 1, 1, 1])
    pid = f"P{p}"
    pillar_name = DB.get("pillars", {}).get(pid, {}).get("name", pid)
    with cols[0]:
        st.markdown(f'<div class="row-head"><strong>{pid}</strong><span>{pillar_name}</span></div>', unsafe_allow_html=True)

    for d in range(1, 7):
        key = f"P{p}D{d}"
        cell_title = DB.get("cells", {}).get(key, {}).get("title", "Strategic Cell")
        button_label = f"{key}\n\n{cell_title}"
        with cols[d]:
            if st.button(button_label, key=f"btn_{key}", use_container_width=True):
                st.session_state["selected_cell"] = key

selected = st.session_state.get("selected_cell", "P1D1")
cell = DB.get("cells", {}).get(selected, {})

if not cell:
    st.error(f"Selected cell {selected} was not found in the database.")
    st.stop()

# ---------- Selected Cell Panel ----------
st.write("")
st.markdown(
    f"""
<div class="panel">
  <p class="panel-kicker">Selected Strategic Cell</p>
  <h2 class="panel-title">{cell.get('cell_id', selected)} · {cell.get('title', '')}</h2>
  <div class="panel-meta"><b>{cell.get('pillar', '')}</b> × <b>{cell.get('domain', '')}</b></div>
  <div class="panel-summary">{cell.get('executive_summary', '')}</div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- Tabs ----------
tabs = st.tabs(["Executive Brief", "Framework", "Implementation", "Performance", "Traceability", "Evidence"])

with tabs[0]:
    render_premium_section("Strategic Purpose", cell.get("strategic_purpose", ""))
    render_premium_section("Strategic Rationale", cell.get("strategic_rationale", ""))
    render_premium_section("Why This Matters", cell.get("why_this_matters", ""))
    render_premium_section("Expected National Impact")
    render_list(cell.get("expected_national_impact", []))

with tabs[1]:
    c1, c2 = st.columns(2)
    with c1:
        render_premium_section("Focus Areas")
        st.markdown("".join([f'<span class="tag">{x}</span>' for x in cell.get("focus_areas", [])]), unsafe_allow_html=True)
        render_premium_section("Related NSCs")
        render_list(cell.get("related_nsc", []))
    with c2:
        render_premium_section("Key Regulatory Interfaces")
        render_list(cell.get("key_regulatory_interfaces", []))
        render_premium_section("Report Alignment Note", cell.get("report_alignment_note", ""))

with tabs[2]:
    render_premium_section("Related Strategic Initiatives")
    for iid in cell.get("related_initiatives", []):
        ini = cell.get("initiative_details", {}).get(iid, {})
        with st.container(border=True):
            st.markdown(f"### {iid} · {ini.get('name', '')}")
            st.markdown(f"**Pillar / Domain:** {ini.get('pillar_domain', '-')}")
            st.markdown(f"**Phase:** {ini.get('phase', '-')}")
            st.markdown(f"**Lead / Owner:** {ini.get('owner', '-')}")
            st.markdown(f"**Deliverable:** {ini.get('deliverable', '-')}")
            st.caption(f"Evidence: {ini.get('evidence', '-')}")
    render_premium_section("Lead / Owner")
    render_list(cell.get("lead_owner", []))

with tabs[3]:
    render_premium_section("Strategic Outcome")
    for sid, outcome in cell.get("outcome_details", {}).items():
        st.markdown(
            f'<div class="lux-list-item"><b style="color:#f8e7a1">{sid} · {outcome.get("name", "")}</b><br>{outcome.get("description", "")}</div>',
            unsafe_allow_html=True,
        )
    render_premium_section("KPI Framework")
    render_list(cell.get("kpi_framework", []))
    render_premium_section("2035 Target")
    render_list(cell.get("target_2035", []))
    render_premium_section("Key Risks")
    render_list(cell.get("key_risks", []))
    render_premium_section("Critical Success Factors")
    render_list(cell.get("success_factors", []))

with tabs[4]:
    render_premium_section("Traceability Chain")
    chain = " → ".join(cell.get("traceability_chain", []))
    st.markdown(f'<div class="trace">{chain}</div>', unsafe_allow_html=True)
    render_premium_section("Readable Chain")
    for i, item in enumerate(cell.get("traceability_chain", []), start=1):
        st.markdown(f'<div class="lux-list-item"><b style="color:#f8e7a1">{i}.</b> {item}</div>', unsafe_allow_html=True)

with tabs[5]:
    render_premium_section("Evidence Pages")
    render_list(cell.get("evidence_pages", []))
    st.caption("Evidence page references are based on the uploaded MSS Section 7.4–7.11 extract used to build this portal.")

# ---------- Search ----------
st.markdown(
    """
<div class="premium-heading">
  <div>
    <h2>Search & Strategic Explorer</h2>
    <div class="sub">Search by NSC, initiative, KPI, cell title, domain, pillar, agency or keyword.</div>
  </div>
  <div class="gold-line"></div>
</div>
""",
    unsafe_allow_html=True,
)

query = st.text_input(
    "Search keyword",
    placeholder="Example: NSC 09, A8, SCPI, Halal, D5, B23",
    label_visibility="collapsed",
)

if query:
    q = query.lower().strip()
    results = []
    for cid, c in DB.get("cells", {}).items():
        blob = json.dumps(c, ensure_ascii=False).lower()
        if q in blob:
            results.append((cid, c.get("title", ""), c.get("pillar", ""), c.get("domain", "")))

    st.markdown(f'<div class="lux-paragraph"><b style="color:#f8e7a1">{len(results)}</b> related strategic cell(s) found.</div>', unsafe_allow_html=True)
    for cid, title, pillar, domain in results[:36]:
        st.markdown(
            f'<div class="lux-list-item"><b style="color:#f8e7a1">{cid} · {title}</b><br>{pillar} × {domain}</div>',
            unsafe_allow_html=True,
        )

# ---------- Initiative Directory ----------
st.write("")
with st.expander("Full Initiative Directory", expanded=False):
    for iid, ini in DB.get("initiatives", {}).items():
        st.markdown(
            f'<div class="lux-list-item"><b style="color:#f8e7a1">{iid} · {ini.get("name", "")}</b><br>{ini.get("pillar_domain", "-")} · {ini.get("phase", "-")} · {ini.get("owner", "-")}</div>',
            unsafe_allow_html=True,
        )

st.markdown(
    """
<div class="footer">
Prepared as an interactive premium executive prototype for MSS 2026–2035 strategic communication. Content is sourced from the uploaded MSS strategy report extract and can be further refined after formal validation.
</div>
""",
    unsafe_allow_html=True,
)
