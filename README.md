# TalentFlow Analytics (Python version)

A web app that models monthly recruiting revenue and interview capacity.

- **Placement planner** - Linear Programming (SciPy / HiGHS) with sensitivity analysis. Any number of job types.
  - **Profit gained and cost saved** - compares the best plan with the hires you make today.
  - **Solutions for the bottlenecks** - says which limits to raise, how much, what it costs, and shows the best plan after the fix.
- **Interview queue** - M/M/s queueing model, with cost saved against your current team and ways to cut the wait.

Open on Streamlit. Click the Streamlit badge below.
<a href="https://talentflowanalytics-suqxb68cqsnhqls4zzhirj.streamlit.app/">
  <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit" height="70">
</a>

## Files

| File | What it is |
|---|---|
| `app.py` | Starts the web page (Streamlit): page setup and the three tabs. |
| `model.py` | The math: LP, sensitivity analysis, bottleneck solutions, queueing. |
| `ui/style.py` | Colors, banner and sidebar. |
| `ui/helpers.py` | Shared number formats, wide tables and metric cards. |
| `ui/planner.py` | Placement planner page. |
| `ui/queue_tab.py` | Interview queue page. |
| `ui/about.py` | About page. |
| `test_model.py` | Checks the math against your Excel results. |
| `requirements.txt` | The Python libraries the app needs. |
| `.streamlit/config.toml` | The app's colors. |

Each page has two steps: **1. Enter your numbers**, then **2. Your results**, which are split into tabs
(Best plan, Profit gained, Bottleneck fixes, Limits and sensitivity, Charts for the planner; Recommendation,
Cost saved, Solutions for the wait, Compare team sizes for the queue).

## Troubleshooting

- `command not found: streamlit` - the environment is not on. Repeat the "turn it on" step.
- `ModuleNotFoundError` - run `pip install -r requirements.txt` again with the environment on.
- Port already in use - run `streamlit run app.py --server.port 8502`.
