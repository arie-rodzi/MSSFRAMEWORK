
import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="MSS 2026-2035 Strategic Intelligence Portal", layout="wide", initial_sidebar_state="collapsed")

DATA_PATH = Path(__file__).parent / "mss_master_database.json"
with open(DATA_PATH, "r", encoding="utf-8") as f:
    DB = json.load(f)

st.markdown("""
<style>
[data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none !important;}
.main .block-container {padding-top: 1.2rem; max-width: 1500px;}
html, body, [class*="css"] {font-family: Inter, Segoe UI, Arial, sans-serif;}
.stApp {
    background:
      radial-gradient(circle at 15% 10%, rgba(197,160,23,0.20), transparent 25%),
      radial-gradient(circle at 90% 20%, rgba(0,38,84,0.25), transparent 25%),
      linear-gradient(135deg, #07152b 0%, #0d1f3d 42%, #f7f4ec 42%, #ffffff 100%);
}
.hero {
    background: linear-gradient(135deg, rgba(0,24,69,.98), rgba(3,47,98,.94));
    border: 1px solid rgba(212,175,55,.55);
    border-radius: 28px;
    padding: 30px 34px;
    color: white;
    box-shadow: 0 24px 70px rgba(0,0,0,.32);
}
.hero h1 {font-size: 2.35rem; margin: 0; letter-spacing: .5px;}
.hero p {font-size: 1rem; opacity: .92;}
.badge {
    display:inline-block; padding:8px 14px; border-radius:999px;
    background:rgba(212,175,55,.18); border:1px solid rgba(212,175,55,.55);
    color:#fff3c1; font-weight:700; margin-right:8px; font-size:.86rem;
}
.metric-card {
    background: rgba(255,255,255,.95);
    border: 1px solid rgba(197,160,23,.35);
    border-radius: 18px;
    padding: 16px 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,.10);
    min-height: 115px;
}
.metric-card h3 {margin:0; color:#001845; font-size:1.8rem;}
.metric-card p {margin:4px 0 0; color:#334;}
.matrix-head {
    background: linear-gradient(135deg, #001845, #063970);
    color: white;
    text-align:center;
    padding: 12px 8px;
    border-radius: 14px;
    border: 1px solid rgba(212,175,55,.55);
    font-weight:800;
}
.row-head {
    background: linear-gradient(135deg, #001845, #102f58);
    color: #fff3c1;
    text-align:center;
    padding: 18px 8px;
    border-radius: 16px;
    border: 1px solid rgba(212,175,55,.55);
    font-weight:900;
    height: 112px;
    display:flex; align-items:center; justify-content:center;
}
div.stButton > button {
    min-height: 112px;
    white-space: normal;
    border-radius: 18px;
    border: 1px solid rgba(212,175,55,.62);
    background: linear-gradient(145deg, #ffffff, #fffaf0);
    color: #001845;
    font-weight: 800;
    box-shadow: 0 12px 26px rgba(0,0,0,.11);
    transition: all .15s ease;
    padding: 10px 12px;
}
div.stButton > button:hover {
    transform: translateY(-3px);
    border: 1px solid #c5a017;
    box-shadow: 0 18px 40px rgba(0,24,69,.24);
    background: linear-gradient(145deg, #fff7d9, #ffffff);
}
.panel {
    background: rgba(255,255,255,.98);
    border: 1px solid rgba(197,160,23,.48);
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0 24px 70px rgba(0,0,0,.16);
}
.panel-title {
    color:#001845; margin:0; font-size:2rem; font-weight:900;
}
.gold {color:#a77c00; font-weight:900;}
.small-note {font-size:.88rem; color:#6a5d3a;}
.trace {
    background: linear-gradient(135deg, #001845, #0d3b66);
    color:white; border-radius:18px; padding:18px; border:1px solid rgba(212,175,55,.55);
    font-weight:700;
}
.tag {
    display:inline-block; padding:7px 10px; border-radius:999px; background:#f7efd0;
    border:1px solid #d4af37; margin:4px; color:#001845; font-weight:700; font-size:.85rem;
}
</style>
""", unsafe_allow_html=True)

meta = DB["meta"]

st.markdown(f"""
<div class="hero">
  <span class="badge">MSS 2026–2035</span>
  <span class="badge">Strategic Intelligence Portal</span>
  <span class="badge">36-Cell Matrix Explorer</span>
  <h1>{meta['title']}</h1>
  <p><b>Vision:</b> {meta['vision']}</p>
  <p><b>Mission:</b> {meta['mission']}</p>
  <p class="small-note">Logic Chain: {meta['logic_chain']}</p>
</div>
""", unsafe_allow_html=True)

st.write("")
m1,m2,m3,m4,m5,m6 = st.columns(6)
cards = [("6","Pillars"),("6","Domains"),("36","Strategic Cells"),("23+16","Initiatives"),("6","Outcomes"),("2035","Target Horizon")]
for col,(num,label) in zip([m1,m2,m3,m4,m5,m6],cards):
    with col:
        st.markdown(f'<div class="metric-card"><h3>{num}</h3><p>{label}</p></div>', unsafe_allow_html=True)

st.write("")
with st.expander("Executive Overview: Pillars, Domains and Strategic Outcomes", expanded=False):
    c1,c2,c3 = st.columns(3)
    with c1:
        st.subheader("Strategic Pillars")
        for pid,p in DB["pillars"].items():
            st.markdown(f"**{pid}. {p['name']}**  \n{p['core_question']}")
    with c2:
        st.subheader("Strategic Domains")
        for did,d in DB["domains"].items():
            st.markdown(f"**{did}. {d['name']}**  \n{d['summary']}")
    with c3:
        st.subheader("Strategic Outcomes")
        for sid,s in DB["outcomes"].items():
            st.markdown(f"**{sid}. {s['name']}**  \n{s['description']}")

st.markdown("## Interactive 6×6 Strategic Framework Matrix")
st.caption("Click any box to open the full Executive Strategic Card. No sidebar is used.")

headers = ["", "D1 Infrastructure & Utilities", "D2 Industrial & Manufacturing", "D3 Consumer Safety", "D4 Agrofood, Halal & Biosecurity", "D5 Emerging Tech & Sustainability", "D6 Institutional Liaison"]
hcols = st.columns([.55,1,1,1,1,1,1])
for i,h in enumerate(headers):
    with hcols[i]:
        if h:
            st.markdown(f'<div class="matrix-head">{h}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="matrix-head">Pillar</div>', unsafe_allow_html=True)

for p in range(1,7):
    cols = st.columns([.55,1,1,1,1,1,1])
    pid = f"P{p}"
    with cols[0]:
        st.markdown(f'<div class="row-head">{pid}<br>{DB["pillars"][pid]["name"]}</div>', unsafe_allow_html=True)
    for d in range(1,7):
        key = f"P{p}D{d}"
        with cols[d]:
            if st.button(f"{key}\n\n{DB['cells'][key]['title']}", key=f"btn_{key}", use_container_width=True):
                st.session_state["selected_cell"] = key

selected = st.session_state.get("selected_cell", "P1D1")
cell = DB["cells"][selected]

st.write("")
st.markdown(f"""
<div class="panel">
  <p class="gold">SELECTED STRATEGIC CELL</p>
  <h2 class="panel-title">{cell['cell_id']} · {cell['title']}</h2>
  <p><b>{cell['pillar']}</b> × <b>{cell['domain']}</b></p>
  <p>{cell['executive_summary']}</p>
</div>
""", unsafe_allow_html=True)

tabs = st.tabs(["Executive Brief", "Framework", "Implementation", "Performance", "Traceability", "Evidence"])

with tabs[0]:
    st.subheader("Strategic Purpose")
    st.write(cell["strategic_purpose"])
    st.subheader("Strategic Rationale")
    st.write(cell["strategic_rationale"])
    st.subheader("Why This Matters")
    st.write(cell["why_this_matters"])
    st.subheader("Expected National Impact")
    for item in cell["expected_national_impact"]:
        st.markdown(f"- {item}")

with tabs[1]:
    c1,c2 = st.columns(2)
    with c1:
        st.subheader("Focus Areas")
        st.markdown("".join([f'<span class="tag">{x}</span>' for x in cell["focus_areas"]]), unsafe_allow_html=True)
        st.subheader("Related NSCs")
        for n in cell["related_nsc"]:
            st.markdown(f"- {n}")
    with c2:
        st.subheader("Key Regulatory Interfaces")
        for r in cell["key_regulatory_interfaces"]:
            st.markdown(f"- {r}")
        st.subheader("Report Alignment Note")
        st.info(cell["report_alignment_note"])

with tabs[2]:
    st.subheader("Related Strategic Initiatives")
    for iid in cell["related_initiatives"]:
        ini = cell["initiative_details"][iid]
        with st.container(border=True):
            st.markdown(f"### {iid} · {ini['name']}")
            st.markdown(f"**Pillar / Domain:** {ini['pillar_domain']}")
            st.markdown(f"**Phase:** {ini['phase']}")
            st.markdown(f"**Lead / Owner:** {ini['owner']}")
            st.markdown(f"**Deliverable:** {ini['deliverable']}")
            st.caption(f"Evidence: {ini['evidence']}")
    st.subheader("Lead / Owner")
    for o in cell["lead_owner"]:
        st.markdown(f"- {o}")

with tabs[3]:
    st.subheader("Strategic Outcome")
    for sid, outcome in cell["outcome_details"].items():
        st.markdown(f"### {sid} · {outcome['name']}")
        st.write(outcome["description"])
    st.subheader("KPI Framework")
    for k in cell["kpi_framework"]:
        st.markdown(f"- {k}")
    st.subheader("2035 Target")
    for t in cell["target_2035"]:
        st.markdown(f"- {t}")
    st.subheader("Key Risks")
    for r in cell["key_risks"]:
        st.markdown(f"- {r}")
    st.subheader("Critical Success Factors")
    for s in cell["success_factors"]:
        st.markdown(f"- {s}")

with tabs[4]:
    st.subheader("Traceability Chain")
    chain = " → ".join(cell["traceability_chain"])
    st.markdown(f'<div class="trace">{chain}</div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("Readable Chain")
    for i, item in enumerate(cell["traceability_chain"], start=1):
        st.markdown(f"**{i}.** {item}")

with tabs[5]:
    st.subheader("Evidence Pages")
    for e in cell["evidence_pages"]:
        st.markdown(f"- {e}")
    st.caption("Evidence page references are based on the uploaded MSS Section 7.4–7.11 extract used to build this portal.")

st.write("")
st.markdown("## Search & Explorer")
query = st.text_input("Search by NSC, initiative, KPI, cell title, domain, pillar, agency or keyword", placeholder="Example: NSC 09, A8, SCPI, Halal, D5, B23")
if query:
    q = query.lower()
    results = []
    for cid,c in DB["cells"].items():
        blob = json.dumps(c, ensure_ascii=False).lower()
        if q in blob:
            results.append((cid,c["title"],c["pillar"],c["domain"]))
    st.write(f"Found {len(results)} related cells.")
    for cid,title,pillar,domain in results[:36]:
        st.markdown(f"**{cid} · {title}** — {pillar} × {domain}")

st.write("")
with st.expander("Full Initiative Directory"):
    for iid, ini in DB["initiatives"].items():
        st.markdown(f"**{iid} · {ini['name']}** — {ini['pillar_domain']} · {ini['phase']} · {ini['owner']}")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Prepared as an interactive prototype for MSS 2026–2035 strategic communication. Content is sourced from the uploaded MSS strategy report extract and can be further refined after formal validation.")
