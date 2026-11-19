
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
METADATA_FILE = Path.home() / "Downloads" / "HAM10000_metadata.tab"
REPORT_FOLDER = PROJECT_ROOT / "reports"

REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(METADATA_FILE, sep="\t")

# 1. Basic dataset information
print("========== DATASET OVERVIEW ==========")
print(f"Total image records: {len(df)}")
print(f"Unique image IDs: {df['image_id'].nunique()}")
print(f"Unique lesion IDs: {df['lesion_id'].nunique()}")
print(f"Total columns: {len(df.columns)}")

# 2. Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 3. Diagnosis distribution
diagnosis_counts = df["dx"].value_counts().sort_values(ascending=False)

print("\n========== DIAGNOSIS COUNTS ==========")
print(diagnosis_counts)

# 4. Metadata summary
print("\n========== AGE SUMMARY ==========")
print(df["age"].describe())

print("\n========== SEX DISTRIBUTION ==========")
print(df["sex"].value_counts(dropna=False))

print("\n========== BODY LOCATION ==========")
print(df["localization"].value_counts(dropna=False))

# 5. Lesions with multiple images
images_per_lesion = df.groupby("lesion_id")["image_id"].count()

print("\n========== LESION IMAGE COUNTS ==========")
print(f"Lesions with multiple images: {(images_per_lesion > 1).sum()}")
print(f"Maximum images per lesion: {images_per_lesion.max()}")

# 6. Save diagnosis distribution chart
ax = diagnosis_counts.plot(kind="bar", figsize=(9, 5))
ax.set_title("HAM10000 Diagnosis Class Distribution")
ax.set_xlabel("Diagnosis category")
ax.set_ylabel("Number of image records")
plt.xticks(rotation=45)
plt.tight_layout()

chart_path = REPORT_FOLDER / "diagnosis_distribution.png"
plt.savefig(chart_path, dpi=150)
plt.close()

# 7. Save a text report
report_path = REPORT_FOLDER / "eda_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write("HAM10000 EXPLORATORY DATA ANALYSIS\n\n")
    file.write(f"Total image records: {len(df)}\n")
    file.write(f"Unique image IDs: {df['image_id'].nunique()}\n")
    file.write(f"Unique lesion IDs: {df['lesion_id'].nunique()}\n\n")

    file.write("Missing values:\n")
    file.write(df.isnull().sum().to_string())
    file.write("\n\nDiagnosis counts:\n")
    file.write(diagnosis_counts.to_string())
    file.write("\n\nAge summary:\n")
    file.write(df["age"].describe().to_string())
    file.write("\n\nSex distribution:\n")
    file.write(df["sex"].value_counts(dropna=False).to_string())
    file.write("\n\nBody location:\n")
    file.write(df["localization"].value_counts(dropna=False).to_string())
    file.write("\n\nLesion image counts:\n")
    file.write(f"Lesions with multiple images: {(images_per_lesion > 1).sum()}\n")
    file.write(f"Maximum images per lesion: {images_per_lesion.max()}\n")

print(f"\nEDA report saved to: {report_path}")
print(f"Diagnosis chart saved to: {chart_path}")
