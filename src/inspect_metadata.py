
from pathlib import Path

import pandas as pd

# The original metadata file is currently in the Downloads folder.
metadata_path = Path.home() / "Downloads" / "HAM10000_metadata.tab"

if not metadata_path.exists():
    print(f"Metadata file not found: {metadata_path}")
    print("Check your Downloads folder and the filename.")
else:
    df = pd.read_csv(metadata_path, sep="\t")

    print("=== DATASET OVERVIEW ===")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\n=== COLUMN NAMES ===")
    print(df.columns.tolist())

    print("\n=== FIRST 5 ROWS ===")
    print(df.head().to_string(index=False))

    print("\n=== MISSING VALUES ===")
    print(df.isnull().sum().to_string())

    print("\n=== DIAGNOSIS COUNTS ===")
    print(df["dx"].value_counts(dropna=False).to_string())

    print("\n=== UNIQUE LESIONS ===")
    print(df["lesion_id"].nunique())
