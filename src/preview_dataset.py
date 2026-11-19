
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMAGE_FOLDER = PROJECT_ROOT / "data" / "raw"
METADATA_FILE = Path.home() / "Downloads" / "HAM10000_metadata.tab"

metadata = pd.read_csv(METADATA_FILE, sep="\t")

# Select one example from each diagnosis class
sample_rows = (
    metadata.dropna(subset=["dx"])
    .groupby("dx", sort=True)
    .first()
    .reset_index()
)

fig, axes = plt.subplots(2, 4, figsize=(16, 8))
axes = axes.flatten()

for ax in axes:
    ax.axis("off")

for ax, (_, row) in zip(axes, sample_rows.iterrows()):
    image_path = IMAGE_FOLDER / f"{row['image_id']}.jpg"

    if not image_path.exists():
        ax.set_title(f"Image not found: {row['image_id']}")
        continue

    with Image.open(image_path) as image:
        ax.imshow(image.copy())

    ax.set_title(
        f"Diagnosis: {row['dx']}\nImage: {row['image_id']}",
        fontsize=9
    )
    ax.axis("off")

fig.suptitle("HAM10000: Example Images by Diagnosis Class")
plt.tight_layout()

output_folder = PROJECT_ROOT / "reports"
output_folder.mkdir(parents=True, exist_ok=True)

output_path = output_folder / "dataset_image_preview.png"
plt.savefig(output_path, dpi=150, bbox_inches="tight")
print(f"Image preview saved to: {output_path}")

plt.show()
