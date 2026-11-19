
from pathlib import Path
import pandas as pd
import json
from sklearn.model_selection import StratifiedGroupKFold

METADATA_FILE = Path.home() / "Downloads" / "HAM10000_metadata.tab"

df = pd.read_csv(METADATA_FILE, sep="\t")

# First, reserve approximately 20% of lesions for testing.
outer_split = StratifiedGroupKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

development_idx, test_idx = next(
    outer_split.split(df, y=df["dx"], groups=df["lesion_id"])
)

development = df.iloc[development_idx].copy()
test = df.iloc[test_idx].copy()

# Split the remaining development data into training and validation.
inner_split = StratifiedGroupKFold(
    n_splits=5,
    shuffle=True,
    random_state=43
)

train_idx, val_idx = next(
    inner_split.split(
        development,
        y=development["dx"],
        groups=development["lesion_id"]
    )
)

train = development.iloc[train_idx].copy()
validation = development.iloc[val_idx].copy()

splits = {
    "Train": train,
    "Validation": validation,
    "Test": test
}

print("========== STRATIFIED GROUP SPLIT ==========")

for name, part in splits.items():
    print(f"\n{name}")
    print(f"Images: {len(part)}")
    print(f"Unique lesions: {part['lesion_id'].nunique()}")
    print("Diagnosis counts:")
    print(part["dx"].value_counts().sort_index())

# Verify that no lesion appears in more than one split.
train_ids = set(train["lesion_id"])
val_ids = set(validation["lesion_id"])
test_ids = set(test["lesion_id"])

print("\n========== LEAKAGE CHECK ==========")
print("Train/validation overlap:", len(train_ids & val_ids))
print("Train/test overlap:", len(train_ids & test_ids))
print("Validation/test overlap:", len(val_ids & test_ids))

print("\nNote: Stratification tries to balance diagnosis proportions,")
print("but exact balance is not guaranteed for grouped data.")
print("Compare these results with the previous split before choosing.")

# Save reproducible split assignments
PROJECT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

train["split"] = "train"
validation["split"] = "validation"
test["split"] = "test"

split_manifest = pd.concat(
    [train, validation, test],
    ignore_index=True
)

manifest_file = REPORTS_DIR / "data_split_manifest.csv"
split_manifest[
    ["image_id", "lesion_id", "dx", "split"]
].to_csv(manifest_file, index=False)

# Save a summary of the split settings
split_summary = {
    "method": "StratifiedGroupKFold",
    "outer_random_state": 42,
    "inner_random_state": 43,
    "total_images": len(split_manifest),
    "total_unique_lesions": split_manifest["lesion_id"].nunique(),
    "split_image_counts": {
        name: len(part) for name, part in splits.items()
    },
    "lesion_overlap": {
        "train_validation": len(train_ids & val_ids),
        "train_test": len(train_ids & test_ids),
        "validation_test": len(val_ids & test_ids)
    }
}

summary_file = REPORTS_DIR / "data_split_summary.json"
with open(summary_file, "w", encoding="utf-8") as file:
    json.dump(split_summary, file, indent=4)

print("\n========== SAVED SPLIT ==========")
print(f"Manifest: {manifest_file}")
print(f"Summary: {summary_file}")
print(f"Total assigned images: {len(split_manifest)}")