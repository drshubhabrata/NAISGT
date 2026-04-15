import os

from analysis.data_loader import create_master_template
from analysis.naiskt_gap_index import calculate_gap_index
from analysis.state_summary import generate_summary


def main():
    print("🚀 Running NAISGT Pipeline...")

    # Step 1: Create master dataset
    master_df = create_master_template()

    # Step 2: Calculate gap index
    gap_df = calculate_gap_index(master_df)

    # Save processed data
    os.makedirs("data/processed_data", exist_ok=True)
    gap_df.to_csv("data/processed_data/anganwadi_gap_index.csv", index=False)

    # Step 3: Generate state summary
    summary_df = generate_summary(gap_df)

    # Step 4: Save final output
    os.makedirs("output", exist_ok=True)
    summary_df.to_csv("output/state_summary.csv", index=False)

    print("✅ Pipeline completed successfully!")
    print("📁 Check:")
    print("   - data/processed_data/")
    print("   - output/")


if __name__ == "__main__":
    main()
