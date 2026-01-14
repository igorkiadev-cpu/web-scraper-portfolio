import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_companies():
    """
    Placeholder function — here we will later:
    - fetch companies
    - parse HTML
    - extract structured data
    """
    companies = []

    # Example structure for a company (to be filled later)
    companies.append({
        "Company": "Example",
        "Website": "https://example.com",
        "Industry": "SaaS",
        "Country": "USA",
        "Email": None
    })

    return companies


def save_to_csv(companies, filename="data/dataset.csv"):
    df = pd.DataFrame(companies)
    df.to_csv(filename, index=False)
    print(f"Saved CSV to {filename}")


def save_to_excel(companies, filename="data/dataset.xlsx"):
    df = pd.DataFrame(companies)
    df.to_excel(filename, index=False)
    print(f"Saved Excel to {filename}")


def main():
    companies = fetch_companies()
    save_to_csv(companies)
    save_to_excel(companies)


if __name__ == "__main__":
    main()
