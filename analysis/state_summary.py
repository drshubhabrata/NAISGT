import pandas as pd

def generate_summary(df):
    # Group by state and calculate mean gap score
    state_summary = df.groupby("state")["naiskt_gap_score"].mean().reset_index()

    # Sort by highest gap (priority)
    state_summary = state_summary.sort_values(
        by="naiskt_gap_score", ascending=False
    )

    # ✅ Correct priority logic (based on 0–1 scale)
    def assign_priority(score):
        if score >= 0.5:
            return "High"
        elif score >= 0.3:
            return "Medium"
        else:
            return "Low"

    state_summary["Priority"] = state_summary["naiskt_gap_score"].apply(assign_priority)

    return state_summary
