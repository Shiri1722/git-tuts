import requests
import pandas as pd
import re
from typing import List, Dict

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[Dict]:
    """Fetch papers from PubMed based on a query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    response = requests.get(PUBMED_API_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from PubMed: {response.status_code}")

    data = response.json()
    paper_ids = data["esearchresult"].get("idlist", [])
    
    return paper_ids

def filter_non_academic_authors(authors: List[Dict]) -> List[Dict]:
    """Identify non-academic authors based on their affiliations."""
    non_academic_authors = []
    company_keywords = ["Pharma", "Biotech", "Inc.", "Ltd.", "Corporation"]
    
    for author in authors:
        affiliation = author.get("affiliation", "")
        if any(keyword in affiliation for keyword in company_keywords):
            non_academic_authors.append(author)
    
    return non_academic_authors
