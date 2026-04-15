import pandas as pd
import os


def create_master_template(
    input_path="data/raw_data/india_district_list.csv",
    output_path="data/processed_data/anganwadi_master_template.csv"
):
    print("📥 Loading district list...")

    districts = pd.read_csv(input_path)

    print("⚙️ Creating master template...")

    # Create base dataset
    master = districts.copy()

    # Anganwadi indicators
    columns = [
        "total_awcs",
        "mini_awcs",
        "own_buildings",
        "rented_buildings",
        "toilets_available",
        "drinking_water_available",
        "electricity_available",
        "kitchen_available",
        "worker_sanctioned",
        "worker_in_position",
        "helper_sanctioned",
        "helper_in_position"
    ]

    # Add empty columns
    for col in columns:
        master[col] = None

    # Ensure folder exists
    os.makedirs("data/processed_data", exist_ok=True)

    # Save file
    master.to_csv(output_path, index=False)

    print("✅ Master template created successfully!")
    print(f"📁 Saved at: {output_path}")

    return master
