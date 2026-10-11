# Multimodal AI Framework for Early Disease Prediction

## Skin Lesion Classification Using Dermoscopic Images and Patient Metadata

### 1. Project Overview

This project explores a multimodal artificial intelligence approach for skin lesion classification by combining dermoscopic images with structured patient/lesion metadata.

The objective is to investigate whether combining visual information from skin images with relevant metadata can improve classification performance compared with using either modality independently.

**Working implementation scope:** Skin lesion classification using dermoscopic images and patient/lesion metadata.

This is an academic machine learning project. Its predictions are intended for research and educational evaluation, not for clinical diagnosis or treatment decisions.

### 2. Problem Statement

Skin lesion assessment involves visual characteristics and relevant patient or lesion information. A model using images alone may not capture all information available in structured metadata.

This project will investigate image-only, metadata-only, and multimodal approaches under a consistent evaluation setup to understand the contribution of each modality.

### 3. Project Objectives

- Identify and verify a suitable, appropriately licensed skin lesion dataset.
- Explore the available images, metadata fields and target labels.
- Prepare and preprocess the image and metadata inputs.
- Develop an image-only baseline model.
- Develop a metadata-only baseline model.
- Develop a multimodal model that combines information from both modalities.
- Compare model performance using appropriate evaluation metrics.
- Document experiments, limitations, and findings.
- Explore explainability and a demonstration interface if feasible within the project scope.

### 4. Proposed Data Source

**Candidate dataset:** HAM10000, with the ISIC Archive as a potential access source.

The exact dataset version, download source, access conditions, metadata columns, label definitions and image-to-record matching must be verified before implementation.

The diagnosis label will be treated as the prediction target, not as an input feature.

The dataset will not be uploaded directly to this repository. Only permitted documentation, code and non-sensitive project artifacts will be maintained here.

### 5. Proposed Methodology

1. Verify the dataset and its usage conditions.
2. Inspect the dataset structure and document the available fields.
3. Perform data-quality checks and exploratory data analysis.
4. Establish a suitable, reproducible train/validation/test split.
5. Build and evaluate an image-only baseline.
6. Build and evaluate a metadata-only baseline.
7. Build and evaluate a multimodal fusion model.
8. Compare the approaches using consistent evaluation criteria.
9. Document limitations and investigate explainability where feasible.
10. Prepare the final report, presentation and demonstration.

Data splitting will be designed to reduce leakage, including checking whether multiple images belong to the same lesion.

### 6. Planned Technology Stack

The final tools and libraries will be confirmed after dataset verification and environment setup.

Potential components include:

- **Programming language:** Python
- **Data analysis:** pandas, NumPy
- **Image processing:** Pillow or OpenCV
- **Machine learning:** scikit-learn and an appropriate deep learning framework
- **Visualization:** Matplotlib
- **Version control and documentation:** Git and GitHub

These are proposed tools, not a claim that the implementation is complete.

### 7. Evaluation Plan

The models will be evaluated using suitable classification metrics, potentially including:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Per-class performance

Because the dataset may contain imbalanced classes, accuracy alone will not be treated as sufficient evidence of model quality.

No performance results will be reported until experiments have actually been run.

### 8. Current Project Status

**Stage:** Project setup and dataset verification.

Completed:
- Literature survey assignment.
- Module understanding and placement-aligned upskilling assignment.
- Proposed system design assignment.
- GitHub repository creation.

Not yet confirmed as completed:
- Dataset download and verification.
- Data cleaning and exploratory analysis.
- Model implementation and training.
- Model evaluation.
- Explainability and demonstration interface.

### 9. Repository Documentation Plan

Project records will be maintained as the work progresses:

- `README.md` — project overview, scope and current status.
- `docs/PROJECT_LOG.md` — dated progress records, evidence and next steps.
- `docs/DATASET_NOTES.md` — dataset source, version, fields, labels and access conditions.
- `docs/EXPERIMENT_LOG.md` — model configurations and actual experimental results.

Additional folders and files will be created when they become necessary.

### 10. Important Limitations

- Skin lesion classification is not the same as proving early cancer detection.
- Dataset labels and metadata may have limitations or missing values.
- Model performance on a dataset does not establish clinical reliability.
- Any results must be reported honestly, with appropriate limitations.
- Patient privacy, dataset terms and responsible use must be respected.

### 11. Project Progress

This repository will be updated incrementally with implementation code, documentation and evidence of completed work. Planned work will be distinguished from completed work.

**Last updated:** 11 October 2026
