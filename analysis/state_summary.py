import pandas as pd

def generate_summary(df):
    # Group by state and calculate mean gap score
    state_summary = df.groupby("state")["naiskt_gap_score"].mean().reset_index()

    # Sort by highest gap (priority)
    state_summary = state_summary.sort_values(
        by="naiskt_gap_score", ascending=False
    )

    return state_summary
