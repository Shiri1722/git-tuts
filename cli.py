import argparse
import csv
from pubmed_fetcher.fetch import fetch_pubmed_papers

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file name.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    
    args = parser.parse_args()
    
    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    paper_ids = fetch_pubmed_papers(args.query)
    
    if args.file:
        with open(args.file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["PubmedID"])
            for paper_id in paper_ids:
                writer.writerow([paper_id])
        print(f"Results saved to {args.file}")
    else:
        print("Pubmed IDs:", paper_ids)

if __name__ == "__main__":
    main()
