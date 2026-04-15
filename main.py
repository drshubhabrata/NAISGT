import os

from analysis.data_loader import load_data
from analysis.naiskt_gap_index import calculate_gap_index
from analysis.state_summary import generate_summary


def main():
    print("🚀 Running NAISGT Pipeline...")

    # Step 1: Load raw data
    df = load_data("data/raw_data/anganwadi_data.csv")

    # Step 2: Process → create gap index
    df_processed = calculate_gap_index(df)

    # Save processed data
    os.makedirs("data/processed_data", exist_ok=True)
    df_processed.to_csv("data/processed_data/anganwadi_gap_index.csv", index=False)

    # Step 3: Generate state summary
    summary = generate_summary(df_processed)

    # Step 4: Save final output
    os.makedirs("output", exist_ok=True)
    summary.to_csv("output/state_summary.csv", index=False)

    print("✅ Done!")
    print("📁 Check output/state_summary.csv")


if __name__ == "__main__":
    main()
