import pandas as pd

# Load dataset
df = pd.read_csv("../data/processed_data/anganwadi_master_dataset.csv")

# Infrastructure gap
df["infra_gap"] = (df["total_awcs"] - df["own_buildings"]) / df["total_awcs"]

# Worker vacancy
df["worker_vacancy_rate"] = (
    df["worker_sanctioned"] - df["worker_in_position"]
) / df["worker_sanctioned"]

# Final NAISGT Gap Score
df["naiskt_gap_score"] = (
    0.6 * df["infra_gap"] +
    0.4 * df["worker_vacancy_rate"]
)

# Save output
df.to_csv("../data/processed_data/anganwadi_gap_index.csv", index=False)

print("Gap index calculated")
