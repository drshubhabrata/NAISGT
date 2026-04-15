import pandas as pd
import os

def load_data():
    print("Loading data...")
    return pd.read_csv("data/anganwadi_gap_index.csv")

def process_data(df):
    print("Processing data...")
    
    # Example logic (you will improve later)
    df["Priority"] = df["Gap_Index"].apply(
        lambda x: "High" if x > 50 else "Medium"
    )
    
    return df

def save_output(df):
    print("Saving output...")
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/result.csv", index=False)

def main():
    df = load_data()
    df = process_data(df)
    save_output(df)
    print("Done! Check output/result.csv")

if __name__ == "__main__":
    main()
