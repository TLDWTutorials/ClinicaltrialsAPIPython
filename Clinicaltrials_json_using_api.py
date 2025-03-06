import requests
import pandas as pd

# Base URL for ClinicalTrials.gov API v2
BASE_URL = "https://clinicaltrials.gov/api/v2/studies"

# Function to fetch studies
def fetch_studies(search_term):
    params = {
        "format": "json",  # Ensure JSON format
        "query.term": search_term,  # Search term
        "pageSize": 50  # Fetch up to 50 results per request
    }
    
    response = requests.get(BASE_URL, params=params)

    # Debug: Print API response status
    print(f"Fetching data for '{search_term}'... Status Code: {response.status_code}")

    if response.status_code != 200:
        print(f"❌ API Error {response.status_code}: {response.text}")
        return []

    data = response.json()
    return data.get("studies", [])

# Function to extract relevant fields, excluding PI
def process_study(study):
    """Extracts key details from the study JSON."""
    
    # Extract Organization from Responsible Party or Lead Sponsor
    organization = study.get("protocolSection", {}).get("sponsorCollaboratorsModule", {}).get("responsibleParty", {}).get("organization", "") or \
                   study.get("protocolSection", {}).get("sponsorCollaboratorsModule", {}).get("leadSponsor", {}).get("name", "")

    return {
        "NCTId": study.get("protocolSection", {}).get("identificationModule", {}).get("nctId", ""),
        "OfficialTitle": study.get("protocolSection", {}).get("descriptionModule", {}).get("officialTitle", ""),
        "LeadSponsor": study.get("protocolSection", {}).get("sponsorCollaboratorsModule", {}).get("leadSponsor", {}).get("name", ""),
        "Organization": organization,  # ✅ NEW: Extracted Organization Name
        "Location": study.get("protocolSection", {}).get("locationsModule", {}).get("locations", [{}])[0].get("city", ""),
        "State": study.get("protocolSection", {}).get("locationsModule", {}).get("locations", [{}])[0].get("state", ""),
        "PrimaryCompletionDate": study.get("protocolSection", {}).get("statusModule", {}).get("primaryCompletionDate", ""),
        "BriefSummary": study.get("protocolSection", {}).get("descriptionModule", {}).get("briefSummary", ""),
        "DetailedDescription": study.get("protocolSection", {}).get("descriptionModule", {}).get("detailedDescription", ""),
        "URL": f"https://clinicaltrials.gov/study/{study.get('protocolSection', {}).get('identificationModule', {}).get('nctId', '')}",
    }

# Main script
search_terms = ["diabetes", "a1c"]  # Modify search terms as needed

all_studies = []
for term in search_terms:
    studies = fetch_studies(term)
    processed = [process_study(study) for study in studies if study]
    all_studies.extend(processed)

# Convert to DataFrame and export
if all_studies:
    df = pd.DataFrame(all_studies)
    df.to_excel("clinical_trials_results.xlsx", index=False)
    print("✅ Data saved to 'clinical_trials_results.xlsx'")
else:
    print("❌ No valid data found.")
