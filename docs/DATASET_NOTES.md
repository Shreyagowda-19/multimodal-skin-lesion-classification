# Dataset Verification Notes

## 1. Purpose

Record the candidate dataset, source information, expected inputs, usage conditions, and verification tasks before implementation begins.

## 2. Candidate Dataset

- **Name:** HAM10000
- **Purpose:** Skin lesion classification using dermoscopic images and structured metadata.
- **Status:** Candidate identified; exact downloadable version and files still need to be verified.
- **Original dataset publication:** Tschandl, Rosendahl and Kittler (2018), *The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions*.
- **Publication DOI:** [https://doi.org/10.1038/sdata.2018.161](https://doi.org/10.1038/sdata.2018.161)

## 3. Sources Checked

### Original dataset publication

URL: [https://www.nature.com/articles/sdata2018161](https://www.nature.com/articles/sdata2018161)

The publication describes an original dataset of 10,015 dermatoscopic images for academic machine-learning research.

### Official ISIC Archive collection

URL: [https://api.isic-archive.com/collections/212/](https://api.isic-archive.com/collections/212/)

The collection page labelled HAM10000 currently lists 11,720 images and specifies a CC BY-NC 4.0 license.

### Harvard Dataverse

URL: [https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

This is a candidate location for the original dataset files and associated metadata. The exact files and version to be used must be confirmed.

## 4. Important Version Check

The original publication reports 10,015 images, while the current ISIC Archive collection page lists 11,720 images.

These counts must not be treated as interchangeable. Before selecting a download, record the precise source, version or collection identifier, image count, metadata file and applicable usage conditions.

## 5. Expected Data Components

The planned model requires:

- Dermoscopic images.
- Structured metadata associated with the relevant images or lesions.
- A diagnosis label for use as the prediction target.
- An identifier that allows image records to be matched correctly to metadata, where available.

Potential metadata fields include age, sex and anatomical site. Their actual availability, definitions, missingness and matching must be verified from the downloaded metadata documentation.

The diagnosis label must not be included as a model input.

## 6. Metadata Preview — Initial Verification

**Source:** Harvard Dataverse, HAM10000 dataset, Version 4.0  
**File:** `HAM10000_metadata.tab`  
**Preview status:** Successfully opened and inspected in the browser.

The file listing reports 10,015 observations and 8 variables.

### Columns observed

- `lesion_id` — lesion identifier.
- `image_id` — image identifier.
- `dx` — diagnosis label.
- `dx_type` — diagnostic confirmation type.
- `age` — patient age.
- `sex` — patient sex.
- `localization` — anatomical location.
- `dataset` — dataset/source category.

### Initial modelling decisions

1. Use `dx` as the prediction target, not as an input feature.
2. Investigate `age`, `sex`, and `localization` as candidate metadata inputs.
3. Use `image_id` to match image files to metadata records.
4. Investigate repeated `lesion_id` values and use a lesion-aware data split to reduce data leakage.
5. Verify the complete metadata file, image matching, missing values, and class distribution after obtaining the data.

### Evidence and limitations

A browser screenshot confirms the visible column names and sample rows. The complete dataset has not yet been downloaded or analysed, so the total number of unique lesions, missing-value counts, and class distribution remain unverified.

## 7. Verification Checklist

- [ ] Select the exact dataset version and source.
- [ ] Read and record the applicable license and attribution requirements.
- [ ] Confirm the number and format of image files.
- [ ] Identify the metadata file and inspect its column names.
- [ ] Confirm how images are matched to metadata.
- [ ] Identify the diagnosis label and available classes.
- [ ] Check missing metadata and duplicate or repeated-lesion records.
- [ ] Record the source URL and download date.
- [ ] Keep the dataset outside the public GitHub repository unless redistribution is explicitly permitted.

## 8. Current Conclusion

HAM10000 is a promising candidate for the project because the published dataset contains dermoscopic images and associated diagnostic information. However, the exact dataset version, metadata structure, matching and usage conditions must be verified before implementation.

No dataset has yet been downloaded or analysed, and no model has been trained.

## 9. Next Action

Download the metadata file `HAM10000_metadata.tab` from the verified Harvard Dataverse dataset record. Inspect the complete file locally to confirm its column names, missing values, diagnosis class distribution, image identifiers, and repeated lesion identifiers. Record the download date and verify the file-to-image matching before downloading and processing the image archives.

## 10. Initial Metadata Analysis — 13 October 2026

**Status:** Completed successfully.

### Environment
- Python: 3.13.3
- pandas: 3.0.6
- Script: `src/inspect_metadata.py`

### Verified results
- Metadata records: 10,015
- Columns: 8
- Unique lesion identifiers: 7,470
- Missing age values: 57
- Missing values in the other seven columns: 0

### Diagnosis distribution

| Diagnosis label | Image records |
|---|---:|
| nv | 6,705 |
| mel | 1,113 |
| bkl | 1,099 |
| bcc | 514 |
| akiec | 327 |
| vasc | 142 |
| df | 115 |

### Observations
1. The metadata file was successfully loaded and inspected using pandas.
2. The diagnosis labels are imbalanced, with `nv` representing the largest category.
3. Multiple image records can share a `lesion_id`. Future training and test partitions must be separated by lesion identifier to reduce data leakage.
4. Age has 57 missing values. The handling strategy has not yet been selected.
5. The metadata inspection succeeded with exit code 0.

### Limitations
These results describe the metadata table only. The image archives have not yet been downloaded or checked for matching image files. No model has been trained, and no predictive performance has been measured.

### Next action
Create a reproducible dataset-quality analysis that checks duplicate records, image identifier uniqueness, missing values, diagnosis proportions, and repeated lesion identifiers. Save the analysis output as a report before beginning model development.
