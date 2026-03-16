import pandas as pd

# Load district list
districts = pd.read_csv("../data/raw_data/india_district_list.csv")

# Create empty master dataset
master = districts.copy()

# Add NAISGT indicator columns
master["total_awcs"] = None
master["mini_awcs"] = None
master["own_buildings"] = None
master["rented_buildings"] = None
master["toilets_available"] = None
master["drinking_water_available"] = None
master["electricity_available"] = None

# Save template dataset
master.to_csv("../data/processed_data/anganwadi_master_template.csv", index=False)

print("Template dataset created")
