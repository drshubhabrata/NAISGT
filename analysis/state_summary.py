import pandas as pd

df = pd.read_csv("../data/processed_data/anganwadi_gap_index.csv")

state_summary = df.groupby("state")["naiskt_gap_score"].mean().reset_index()

state_summary = state_summary.sort_values(by="naiskt_gap_score", ascending=False)

print(state_summary)
