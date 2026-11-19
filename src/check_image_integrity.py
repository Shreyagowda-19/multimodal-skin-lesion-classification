
from pathlib import Path
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMAGE_FOLDER = PROJECT_ROOT / "data" / "raw"

image_files = [
    path
    for path in IMAGE_FOLDER.rglob("*")
    if path.is_file()
    and path.suffix.lower() in {".jpg", ".jpeg"}
]
readable = 0
unreadable = []
dimensions = {}

for index, image_path in enumerate(image_files, start=1):
    try:
        with Image.open(image_path) as image:
            image.verify()

        # Reopen the image to read its dimensions
        with Image.open(image_path) as image:
            dimensions[image.size] = dimensions.get(image.size, 0) + 1

        readable += 1

    except Exception as error:
        unreadable.append((image_path.name, str(error)))

    if index % 1000 == 0:
        print(f"Checked {index}/{len(image_files)} images")

print("\n========== IMAGE INTEGRITY REPORT ==========")
print(f"Total image files: {len(image_files)}")
print(f"Readable images: {readable}")
print(f"Unreadable images: {len(unreadable)}")

print("\nImage dimensions (width, height):")
for size, count in sorted(dimensions.items()):
    print(f"{size}: {count} images")

if unreadable:
    print("\nFirst 10 unreadable files:")
    for filename, error in unreadable[:10]:
        print(f"{filename}: {error}")

print("\n========== RESULT ==========")
if image_files and not unreadable:
    print("SUCCESS: All discovered images are readable.")
else:
    print("CHECK NEEDED: Review the image count and errors.")
