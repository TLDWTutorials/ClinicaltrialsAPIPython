# ClinicalTrials.gov API Data Extraction w/ Python

## Overview
This script retrieves clinical trial data from ClinicalTrials.gov API v2. It extracts key details, including NCT ID, Title, Lead Sponsor, Organization, Location, Completion Date, and Study Description. The results are saved in an Excel file for further analysis.

## Features
✅ Fetches clinical trial data using search terms <br>
✅ Extracts key fields: NCTId, Title, Lead Sponsor, Organization, Location, Summary, etc. <br>
✅ Handles missing data gracefully <br>
✅ Supports pagination for larger datasets <br>
✅ Exports results to Excel (clinical_trials_results.xlsx)<br>

## Requirements
Make sure you have the following Python packages installed:

```bash
pip install requests pandas openpyxl
```
## Usage

- Modify the search terms in the script (search_terms = ["diabetes", "a1c"])
- Run the script:
```bash
python Clinicaltrials_json_using_api.py
```

- The output will be saved as clinical_trials_results.xlsx

## API Reference
This script uses the ClinicalTrials.gov API v3:

## API Documentation: ClinicalTrials.gov API
Base URL:
```bash
https://clinicaltrials.gov/api/v2/studies
```

## License
This project is licensed under the MIT License. 

## Contribution
Feel free to submit pull requests or report issues if you'd like to improve the script!

## YouTube
This code is based on my clinicaltrials.gov data YouTube video: https://youtu.be/kzl2VhpwkE4
