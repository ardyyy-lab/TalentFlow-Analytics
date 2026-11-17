"""
TalentFlow Analytics - Streamlit app (entry point)
Prescriptive Analytics | Recruitment & staffing

Run it with:   streamlit run app.py

Where things live:
    model.py        the math (no Streamlit in it)
    ui/style.py    page style, banner, sidebar
    ui/planner.py  Placement planner page
    ui/queue_tab.py Interview queue page
    ui/about.py    About page
"""
import streamlit as st

st.set_page_config(page_title="TalentFlow Analytics", page_icon=":material/insights:", layout="wide",
                   initial_sidebar_state="expanded")

from ui import about, planner, queue_tab, style  # noqa: E402  (after set_page_config, which must come first)

style.apply_style()
style.banner()
style.sidebar()

tab_plan, tab_queue, tab_about = st.tabs([":material/groups: Placement planner",
                                          ":material/schedule: Interview queue",
                                          ":material/menu_book: About"])
with tab_plan:
    planner.render()
with tab_queue:
    queue_tab.render()
with tab_about:
    about.render()
