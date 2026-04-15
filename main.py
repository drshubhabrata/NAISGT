import os

from analysis.data_loader import create_master_template
from analysis.naiskt_gap_index import calculate_gap_index
from analysis.state_summary import generate_summary


def main():
    print("🚀 Running NAISGT Pipeline...")

    # ------------------------------
    # Step 1: Create master dataset
    # ------------------------------
    print("📥 Step 1: Creating master dataset...")
    master_df = create_master_template()

    # ------------------------------
    # Step 2: Calculate gap index
    # ------------------------------
    print("⚙️ Step 2: Calculating gap index...")
    gap_df = calculate_gap_index(master_df)

    # 🔥 Sort and rank districts properly
    gap_df = gap_df.sort_values(by="naiskt_gap_score", ascending=False)
    gap_df["gap_rank"] = range(1, len(gap_df) + 1)

    # Save processed data
    os.makedirs("data/processed_data", exist_ok=True)
    gap_df.to_csv("data/processed_data/anganwadi_gap_index.csv", index=False)

    # ------------------------------
    # Step 3: Generate state summary
    # ------------------------------
    print("📊 Step 3: Generating state summary...")
    summary_df = generate_summary(gap_df)

    # ------------------------------
    # Step 4: Save outputs
    # ------------------------------
    print("💾 Step 4: Saving outputs...")
    os.makedirs("output", exist_ok=True)

    # Main outputs
    gap_df.to_csv("output/district_gap_index.csv", index=False)
    summary_df.to_csv("output/state_summary.csv", index=False)

    # 🔥 Top insights (VERY POWERFUL)
    top_states = summary_df.head(5)
    top_districts = gap_df.head(10)

    top_states.to_csv("output/top_5_states.csv", index=False)
    top_districts.to_csv("output/top_10_districts.csv", index=False)

    # ------------------------------
    # Final message
    # ------------------------------
    print("\n✅ Pipeline completed successfully!")
    print("📁 Outputs generated:")
    print("   - data/processed_data/anganwadi_gap_index.csv")
    print("   - output/state_summary.csv")
    print("   - output/district_gap_index.csv")
    print("   - output/top_5_states.csv")
    print("   - output/top_10_districts.csv")


if __name__ == "__main__":
    main()
