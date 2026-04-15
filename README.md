# NAISGT

## National Anganwadi Infrastructure & Service Gap Tracker

NAISGT is a data-driven public health platform that identifies infrastructure, workforce, and service delivery gaps in Anganwadi Centres across India and converts them into actionable insights for decision-making.

---

#  How to Use NAISGT (Step-by-Step Guide)

##  Step 1: Install Python

1. Go to: https://www.python.org/downloads/
2. Download Python (latest version)
3. During installation, **IMPORTANT**:

☑ Tick: **Add Python to PATH**
Then click **Install Now**

---

##  Step 2: Download the Project

Click **Code → Download ZIP**
OR use:

git clone https://github.com/drshubhabrata/NAISGT.git

---

##  Step 3: Open Terminal / Command Prompt

Navigate to the project folder:

cd path_to_downloaded_folder/NAISGT

Example:

cd Downloads/NAISGT-main

---

##  Step 4: Install Required Libraries

Run:

python -m pip install pandas streamlit

---

##  Step 5: Add Your Data

Place your dataset in:

data/raw_data/anganwadi_data.csv

 Your data should include columns like:

* state
* district
* total_awcs
* own_buildings
* worker_sanctioned
* worker_in_position
* helper_sanctioned
* helper_in_position

---

##  Step 6: Run the Pipeline

python main.py

---

##  Outputs Generated

Check the **output/** folder:

* state_summary.csv → State-level gap analysis
* district_gap_index.csv → District ranking & gap scores
* top_5_states.csv → Highest priority states
* top_10_districts.csv → Most critical districts

---

#  Dashboard (Visual Interface)

## ▶️ Run Dashboard

streamlit run dashboard.py

---

##  What You Will See

* 📊 State-wise gap score chart
* 🔥 Top 5 high-priority states
* 📍 District ranking table
* 🔍 Filter districts by state

---

##  Why Dashboard is Useful

* No need to open CSV files
* Easy for non-technical users
* Interactive filtering and visualization

---

# ⚙️ How the System Works

Raw Data
→ Master Dataset Creation
→ Gap Index Calculation
→ District Ranking
→ State Summary
→ Priority Outputs

---

# 📊 Gap Index Methodology

Gap Score =
(0.5 × Infrastructure Gap) +
(0.3 × Worker Vacancy Rate) +
(0.2 × Helper Vacancy Rate)

---

# 📈 Outputs

* District Gap Severity Index
* Ranked district list (with categories)
* State-level prioritization
* Top critical states and districts
* Interactive dashboard

---

# 🏥 Use Cases

* Government program monitoring (ICDS, Poshan Abhiyaan)
* NGO and CSR planning
* Public health research
* District-level intervention prioritization

---

# 📂 Project Structure

NAISGT/
├── analysis/ → Core logic modules
├── data/
│   ├── raw_data/ → Input data
│   └── processed_data/ → Intermediate files
├── output/ → Final outputs
├── main.py → Run pipeline
├── dashboard.py → Visual dashboard

---

#  Future Scope

* Block-level analysis
* Real-time data integration
* AI-based insights
* Advanced dashboards with maps

---

# 👨‍⚕️ Author

Dr. Shubhabrata Das
Public Health Professional | Homoeopathic Doctor
