# DVC Setup Documentation

## Google Drive Remote Setup
### 1. Setup Google Cloud
1. Create a new project and enable the Google Drive API.
2. Create credentials (OAuth client ID) and download the credentials JSON file.
3. Save the JSON file as `gdrive_credentials.json` in the project directory.

### 2. Configure DVC
1. Initialize DVC:
    ```bash
    dvc init
    ```

2. Add Google Drive Remote:
    ```bash
    dvc remote add -d myremote gdrive://<folder-id>/mlops
    dvc remote modify myremote gdrive_service_account_json_path gdrive_credentials.json
    ```

3. **Workflow Documentation & Challenges:**
   - Document the overall workflow and challenges in `docs/workflow_and_challenges.md`.

**`docs/workflow_and_challenges.md`**
```markdown
# Workflow & Challenges

## Workflow
1. **Data Extraction:**
   - Extract links and articles from BBC and Dawn homepages.

2. **Data Transformation:**
   - Clean and preprocess extracted data.

3. **Data Version Control:**
   - Use DVC to version control the processed data.
   - Push data to Google Drive using a DVC remote.

4. **Apache Airflow:**
   - Automate the entire process using an Airflow DAG.

## Challenges
1. **Authentication with Google Drive:**
   - Needed to correctly configure Google Cloud credentials for DVC.

2. **Data Cleaning:**
   - Different structures of articles on BBC and Dawn required tailored extraction logic.
