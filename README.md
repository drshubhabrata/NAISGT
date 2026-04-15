# NAISGT

## National Anganwadi Infrastructure & Service Gap Tracker

NAISGT is a data-driven public health platform that identifies infrastructure, workforce, and service delivery gaps in Anganwadi Centres across India, and converts them into actionable insights for decision-making.

---

## 🚀 How to Use NAISGT (Quick Start)

### 1. Download the project

Click **Code → Download ZIP**
OR use:
git clone https://github.com/drshubhabrata/NAISGT.git

---

### 2. Install requirements

pip install pandas streamlit

---

### 3. Add your data

Place your dataset here:

data/raw_data/anganwadi_data.csv

---

### 4. Run the pipeline

python main.py

---

### 5. View results

Check the `output/` folder:

* state_summary.csv → State-level gap analysis
* district_gap_index.csv → District ranking & gap scores
* top_5_states.csv → Highest priority states
* top_10_districts.csv → Most critical districts

---

### 6. (Optional) Run dashboard

streamlit run dashboard.py

---

## 🎯 Objective

To build a national evidence-based monitoring system that highlights critical gaps in Anganwadi infrastructure, human resources, and service delivery using structured datasets.

---

## 📊 Gap Index Methodology

A composite **Anganwadi Gap Score** is calculated using:

Gap Score =
(0.5 × Infrastructure Gap) +
(0.3 × Worker Vacancy Rate) +
(0.2 × Helper Vacancy Rate)

This weighted index helps prioritize districts with the most critical service gaps.

---

## ⚙️ How the System Works

Raw Data → Master Dataset → Gap Index Calculation → State Summary → Priority Outputs

NAISGT automatically processes district-level data and generates decision-ready outputs for program planning.

---

## 📂 Project Structure

NAISGT/
├── analysis/ → Core logic modules
├── data/
│   ├── raw_data/ → Input data
│   └── processed_data/ → Intermediate outputs
├── output/ → Final results
├── main.py → Run entire pipeline
├── dashboard.py → Interactive dashboard

---

## 📊 Outputs

* District Gap Severity Index
* Ranked list of districts (with gap scores & categories)
* State-level prioritization
* Top critical states and districts
* Dashboard visualization (optional)

---

## 🔍 Key Findings (Pilot Analysis)

* Narmada (Gujarat) shows high gap levels
* Maharashtra districts (Gadchiroli, Chandrapur, Nanded) show consistent service gaps
* Urban districts (Hyderabad, Bengaluru, Chennai) also show emerging gaps
* Kerala districts show relatively lower gap scores

---

## 📂 Data Sources

* ICDS administrative data
* Poshan Tracker datasets
* NFHS survey data
* Census demographic data

---

## 🏥 Policy Implications

* High-gap districts require urgent infrastructure strengthening
* Workforce vacancies significantly impact service delivery
* Targeted recruitment and monitoring can improve outcomes
* Model supports ICDS and Poshan Abhiyaan planning

---

## 🧪 Pilot Districts

* Narmada (Gujarat)
* Gadchiroli (Maharashtra)
* Chandrapur (Maharashtra)
* Nanded (Maharashtra)

---

## 🚀 Future Scope

* Block-level and facility-level analysis
* Real-time integration with Poshan Tracker
* Advanced dashboards and visualization
* AI-driven insights for policy planning

---

## 👨‍⚕️ Author

Dr. Shubhabrata Das
Public Health Professional | Homoeopathic Doctor

---
