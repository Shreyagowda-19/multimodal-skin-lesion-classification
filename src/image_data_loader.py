
from pathlib import Path

import pandas as pd
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]

IMAGE_DIR = PROJECT_ROOT / "data" / "raw"
MANIFEST_FILE = PROJECT_ROOT / "reports" / "data_split_manifest.csv"

# Diagnosis labels
CLASSES = ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]

CLASS_TO_INDEX = {
    label: index for index, label in enumerate(CLASSES)
}


# Image preprocessing
image_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


# Custom dataset class
class SkinLesionDataset(Dataset):

    def __init__(self, dataframe, image_dir, transform=None):
        self.dataframe = dataframe.reset_index(drop=True)
        self.image_dir = image_dir
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, index):

        row = self.dataframe.iloc[index]

        image_path = self.image_dir / f"{row['image_id']}.jpg"

        image = Image.open(image_path).convert("RGB")

        label = CLASS_TO_INDEX[row["dx"]]

        if self.transform:
            image = self.transform(image)

        return image, label


# Load the saved split manifest
df = pd.read_csv(MANIFEST_FILE)

train_df = df[df["split"] == "train"]
val_df = df[df["split"] == "validation"]
test_df = df[df["split"] == "test"]


# Create datasets
train_dataset = SkinLesionDataset(
    train_df, IMAGE_DIR, image_transform
)

val_dataset = SkinLesionDataset(
    val_df, IMAGE_DIR, image_transform
)

test_dataset = SkinLesionDataset(
    test_df, IMAGE_DIR, image_transform
)


# Create data loaders
train_loader = DataLoader(
    train_dataset, batch_size=16, shuffle=True, num_workers=0
)

val_loader = DataLoader(
    val_dataset, batch_size=16, shuffle=False, num_workers=0
)

test_loader = DataLoader(
    test_dataset, batch_size=16, shuffle=False, num_workers=0
)


# Test one training batch
images, labels = next(iter(train_loader))

print("Image Data Loader Test")
print("----------------------")
print("Training images:", len(train_dataset))
print("Validation images:", len(val_dataset))
print("Testing images:", len(test_dataset))
print("Number of classes:", len(CLASSES))
print("Image batch shape:", images.shape)
print("Label batch shape:", labels.shape)
print("First batch labels:", labels.tolist())
print("Data loader working successfully!")
