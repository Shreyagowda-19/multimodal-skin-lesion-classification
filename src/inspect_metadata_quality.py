
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
METADATA_FILE = Path.home() / "Downloads" / "HAM10000_metadata.tab"
REPORT_FOLDER = PROJECT_ROOT / "reports"

df = pd.read_csv(METADATA_FILE, sep="\t")

print("========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== UNKNOWN / SPECIAL VALUES ==========")

for column in ["age", "sex", "localization", "dx_type"]:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False).head(20))

print("\n========== AGE CHECK ==========")
print("Age below zero:", (df["age"] < 0).sum())
print("Age above 100:", (df["age"] > 100).sum())
print("Age equal to zero:", (df["age"] == 0).sum())

print("\n========== DUPLICATE CHECK ==========")
print("Duplicate image IDs:", df["image_id"].duplicated().sum())
print("Duplicate full rows:", df.duplicated().sum())

REPORT_FOLDER.mkdir(parents=True, exist_ok=True)
report_path = REPORT_FOLDER / "metadata_quality_details.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write("METADATA QUALITY DETAILS\n\n")
    file.write("Missing values:\n")
    file.write(df.isnull().sum().to_string())

    for column in ["age", "sex", "localization", "dx_type"]:
        file.write(f"\n\n{column} value counts:\n")
        file.write(df[column].value_counts(dropna=False).to_string())

    file.write("\n\nAge checks:\n")
    file.write(f"Age below zero: {(df['age'] < 0).sum()}\n")
    file.write(f"Age above 100: {(df['age'] > 100).sum()}\n")
    file.write(f"Age equal to zero: {(df['age'] == 0).sum()}\n")

    file.write("\nDuplicate checks:\n")
    file.write(f"Duplicate image IDs: {df['image_id'].duplicated().sum()}\n")
    file.write(f"Duplicate full rows: {df.duplicated().sum()}\n")

print(f"\nReport saved to: {report_path}")
# Check whether each lesion has a consistent diagnosis label
lesion_dx_counts = df.groupby("lesion_id")["dx"].nunique()
inconsistent = lesion_dx_counts[lesion_dx_counts > 1]

print("\n========== LESION LABEL CONSISTENCY ==========")
print("Lesions with multiple diagnosis labels:", len(inconsistent))

if not inconsistent.empty:
    print(
        df[df["lesion_id"].isin(inconsistent.index)]
        [["lesion_id", "image_id", "dx"]]
        .sort_values("lesion_id")
        .to_string(index=False)
    )
