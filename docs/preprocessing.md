# Data Extraction & Preprocessing Documentation

## 1. Data Extraction
### Sources
- **BBC**
- **Dawn**

### Process
1. Extract links and article titles & descriptions from the homepage of each source.
2. Convert the extracted data into a Pandas DataFrame and save as `data/articles.csv`.

### Script
See `data_extraction.py`.

## 2. Data Preprocessing
### Process
1. Load `data/articles.csv`.
2. Remove articles missing titles or descriptions.
3. Save the cleaned dataset as `data/processed_articles.csv`.

### Script
Preprocessing is handled directly in the Airflow DAG.
