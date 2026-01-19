from bs4 import BeautifulSoup
import csv
import os

import requests

def scrape_data():
    print("Select scraping source:")
    print("1. Local HTML file (index.html)")
    print("2. URL")
    choice = input("Enter choice (1 or 2): ")

    if choice == '2':
        url = input("Enter URL to scrape: ")
        try:
            response = requests.get(url)
            html = response.text
            print(f"Fetched content from {url}")
        except Exception as e:
            print(f"Error fetching URL: {e}")
            return
    else:
        html_file = os.path.join(os.path.dirname(__file__), "index.html")
        # Create dummy HTML if not exists
        if not os.path.exists(html_file):
            with open(html_file, "w") as f:
                f.write("""
                <html>
                <body>
                    <div class="act">Reading</div>
                    <div class="act">Coding</div>
                    <div class="act">Sleeping</div>
                </body>
                </html>
                """)
        with open(html_file, "r") as f:
            html = f.read()
        print(f"Read content from {html_file}")
        
    soup = BeautifulSoup(html, "html.parser")
    # For demo purposes, we still look for .act class, but user can modify
    acts = [a.text for a in soup.select(".act")]
    
    if not acts:
        print("No elements with class '.act' found. You may need to adjust the CSS selector in the script.")
        # Print title as fallback to show something happened
        if soup.title:
            print(f"Page Title: {soup.title.string}")
    
    output_file = os.path.join(os.path.dirname(__file__), "activity_scraped.csv")
    with open(output_file, "w", newline="") as wcsv:
        writer = csv.writer(wcsv)
        writer.writerow(["activity"])
        for act in acts:
            writer.writerow([act])
            
    print(f"Scraped {len(acts)} items to {output_file}")

if __name__ == "__main__":
    scrape_data()
