import pandas as pd

# Load NAISGT master dataset
df = pd.read_csv("../data/processed_data/anganwadi_master_dataset.csv")

# ------------------------------
# Infrastructure Gap Calculation
# ------------------------------
df["infra_gap"] = (df["total_awcs"] - df["own_buildings"]) / df["total_awcs"]

# ------------------------------
# Worker Vacancy Rate
# ------------------------------
df["worker_vacancy_rate"] = (
    df["worker_sanctioned"] - df["worker_in_position"]
) / df["worker_sanctioned"]

# ------------------------------
# Helper Vacancy Rate
# ------------------------------
df["helper_vacancy_rate"] = (
    df["helper_sanctioned"] - df["helper_in_position"]
) / df["helper_sanctioned"]

# ------------------------------
# Final NAISGT Gap Score
# ------------------------------
df["naiskt_gap_score"] = (
    0.5 * df["infra_gap"] +
    0.3 * df["worker_vacancy_rate"] +
    0.2 * df["helper_vacancy_rate"]
)

# ------------------------------
# Rank Districts by Gap Score
# ------------------------------
df["gap_rank"] = df["naiskt_gap_score"].rank(ascending=False)

# ------------------------------
# Save Output Dataset
# ------------------------------
df.to_csv("../data/processed_data/anganwadi_gap_index.csv", index=False)

print("NAISGT Gap Index calculated successfully.")
def classify_gap(score):
    if score > 0.5:
        return "Critical"
    elif score > 0.3:
        return "High"
    elif score > 0.15:
        return "Moderate"
    else:
        return "Low"

df["gap_category"] = df["naiskt_gap_score"].apply(classify_gap)
