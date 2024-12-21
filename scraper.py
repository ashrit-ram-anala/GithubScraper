import requests
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(credentials)

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
WORKSHEET_NAME = "PostingTracker"

README_URLS = [
    "https://github.com/cvrve/Summer2025-Internships/blob/main/README.md",
    "https://github.com/SimplifyJobs/Summer2025-Internships/blob/dev/README.md",
]

def fetch_and_parse_github_readme(url):
    """
    Fetch and parse a single GitHub README file into structured table data.
    """
    print(f"Fetching and parsing README from: {url}")
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch README at {url}. Status code: {response.status_code}")

    rows = []
    for line in response.text.splitlines():
        if "|" in line:
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if len(cells) > 1:
                rows.append(cells)

    return rows[1:] 

def update_google_sheet(data):
   
    sheet = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sheet.worksheet(WORKSHEET_NAME)

    worksheet.clear()

    headers = ["Company", "Role", "Location", "Application/Link", "Date Posted", "Source"]
    data.insert(0, headers)

    for i, row in enumerate(data, start=1):
        worksheet.insert_row(row, i)

def run_scraper_and_update_sheet():

    print("Scraping GitHub README files...")
    combined_data = []

    for url in README_URLS:
        table_data = fetch_and_parse_github_readme(url)
        combined_data.extend([row + [url] for row in table_data])

    print("Updating Google Sheet...")
    update_google_sheet(combined_data)
    print("Google Sheet updated successfully")

if __name__ == "__main__":
    run_scraper_and_update_sheet()
