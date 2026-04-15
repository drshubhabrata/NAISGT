import pandas as pd
import os
from analysis.state_summary import generate_summary

def load_data():
    print("Loading data...")
    return pd.read_csv("data/anganwadi_gap_index.csv")

def process_data(df):
    print("Generating state summary...")
    return generate_summary(df)

def save_output(df):
    print("Saving output...")
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/state_summary.csv", index=False)

def main():
    df = load_data()
    result = process_data(df)
    save_output(result)
    print("Done! Check output/state_summary.csv")

if __name__ == "__main__":
    main()
