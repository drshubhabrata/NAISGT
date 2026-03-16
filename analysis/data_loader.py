import pandas as pd

# Load district list
districts = pd.read_csv("../data/raw_data/india_district_list.csv")

# Create empty master dataset
master = districts.copy()

# Add Anganwadi indicators
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

for col in columns:
    master[col] = None

# Save template dataset
master.to_csv("../data/processed_data/anganwadi_master_template.csv", index=False)

print("Master template created successfully")
