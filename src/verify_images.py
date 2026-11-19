
from pathlib import Path
import pandas as pd

# Project folders
PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMAGE_FOLDER = PROJECT_ROOT / "data" / "raw"
METADATA_FILE = Path.home() / "Downloads" / "HAM10000_metadata.tab"

print("Checking HAM10000 dataset...\n")

# Check that the required files and folders exist
if not METADATA_FILE.exists():
    raise FileNotFoundError(
        f"Metadata file not found: {METADATA_FILE}\n"
        "Check that HAM10000_metadata.tab is in your Downloads folder."
    )

if not IMAGE_FOLDER.exists():
    raise FileNotFoundError(
        f"Image folder not found: {IMAGE_FOLDER}"
    )

# Load metadata
metadata = pd.read_csv(METADATA_FILE, sep="\t")

# Find JPG images, including images inside subfolders
image_files = list(IMAGE_FOLDER.rglob("*.jpg"))
image_files += list(IMAGE_FOLDER.rglob("*.jpeg"))

# Extract image IDs from filenames
image_ids = [path.stem for path in image_files]

metadata_ids = set(metadata["image_id"].astype(str))
extracted_ids = set(image_ids)

missing_images = metadata_ids - extracted_ids
extra_images = extracted_ids - metadata_ids

print("========== DATASET VERIFICATION ==========")
print(f"Metadata records: {len(metadata)}")
print(f"Image files found: {len(image_files)}")
print(f"Unique image IDs found: {len(extracted_ids)}")
print(f"Metadata IDs without images: {len(missing_images)}")
print(f"Images without metadata: {len(extra_images)}")

print("\nSample image filenames:")
for path in image_files[:5]:
    print(path.name)

if missing_images:
    print("\nFirst 10 metadata IDs without images:")
    for image_id in sorted(missing_images)[:10]:
        print(image_id)

if extra_images:
    print("\nFirst 10 image IDs without metadata:")
    for image_id in sorted(extra_images)[:10]:
        print(image_id)

print("\n========== RESULT ==========")

if (
    len(image_files) == 10015
    and len(extracted_ids) == 10015
    and not missing_images
    and not extra_images
):
    print("SUCCESS: All 10,015 images match the metadata.")
else:
    print("CHECK NEEDED: Review the counts and any mismatched IDs.")
