
from pathlib import Path

import pandas as pd

# Read the original metadata without modifying it.
metadata_path = (
    Path.home() / "Downloads" / "HAM10000_metadata.tab"
)

if not metadata_path.exists():
    raise FileNotFoundError(
        f"Metadata file not found: {metadata_path}"
    )

df = pd.read_csv(metadata_path, sep="\t")

# Store the report inside the project.
project_root = Path(__file__).resolve().parent.parent
report_dir = project_root / "reports"
report_dir.mkdir(exist_ok=True)

report_path = report_dir / "metadata_quality_report.txt"

lines = []

def add_section(title):
    lines.append("\n" + "=" * 55)
    lines.append(title)
    lines.append("=" * 55)


add_section("HAM10000 METADATA QUALITY REPORT")

lines.append(f"Total image records: {len(df)}")
lines.append(f"Total columns: {len(df.columns)}")
lines.append(f"Unique lesion IDs: {df['lesion_id'].nunique()}")
lines.append(f"Unique image IDs: {df['image_id'].nunique()}")

add_section("DUPLICATE CHECKS")

lines.append(
    f"Fully duplicated rows: {df.duplicated().sum()}"
)
lines.append(
    f"Repeated image IDs: {df['image_id'].duplicated().sum()}"
)

add_section("MISSING VALUES")

lines.append(df.isnull().sum().to_string())

add_section("DIAGNOSIS COUNTS")

diagnosis_counts = df["dx"].value_counts(dropna=False)
lines.append(diagnosis_counts.to_string())

add_section("DIAGNOSIS PROPORTIONS (%)")

diagnosis_percentages = (
    df["dx"].value_counts(normalize=True, dropna=False) * 100
)
lines.append(diagnosis_percentages.round(2).to_string())

add_section("IMAGES PER LESION")

images_per_lesion = df.groupby("lesion_id")["image_id"].count()

lines.append(
    f"Lesions with more than one image: "
    f"{(images_per_lesion > 1).sum()}"
)
lines.append(
    f"Maximum images for one lesion: "
    f"{images_per_lesion.max()}"
)

report_text = "\n".join(lines)

report_path.write_text(report_text, encoding="utf-8")

print(report_text)
print(f"\nReport saved to: {report_path}")
