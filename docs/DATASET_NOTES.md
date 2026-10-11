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

## 6. Verification Checklist

- [ ] Select the exact dataset version and source.
- [ ] Read and record the applicable license and attribution requirements.
- [ ] Confirm the number and format of image files.
- [ ] Identify the metadata file and inspect its column names.
- [ ] Confirm how images are matched to metadata.
- [ ] Identify the diagnosis label and available classes.
- [ ] Check missing metadata and duplicate or repeated-lesion records.
- [ ] Record the source URL and download date.
- [ ] Keep the dataset outside the public GitHub repository unless redistribution is explicitly permitted.

## 7. Current Conclusion

HAM10000 is a promising candidate for the project because the published dataset contains dermoscopic images and associated diagnostic information. However, the exact dataset version, metadata structure, matching and usage conditions must be verified before implementation.

No dataset has yet been downloaded or analysed, and no model has been trained.

## 8. Next Action

Verify the selected source and obtain the permitted dataset files. Inspect the actual file structure and metadata before deciding on preprocessing or model implementation.
