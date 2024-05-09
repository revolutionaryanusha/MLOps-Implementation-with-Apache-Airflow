import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def fetch_links_and_articles():
    """Fetch links and article information from BBC and Dawn."""
    sources = [
        {"name": "BBC", "url": "https://www.bbc.com"},
        {"name": "Dawn", "url": "https://www.dawn.com"},
    ]
    articles = []

    for source in sources:
        response = requests.get(source["url"])
        soup = BeautifulSoup(response.content, "html.parser")

        # BBC extraction
        if source["name"] == "BBC":
            for item in soup.select(".media-list__item"):
                title = item.select_one(".media__title").get_text(strip=True) if item.select_one(".media__title") else "N/A"
                description = item.select_one(".media__summary").get_text(strip=True) if item.select_one(".media__summary") else "N/A"
                link = item.select_one("a")["href"]
                if not link.startswith("https://"):
                    link = "https://www.bbc.com" + link

                articles.append({"source": "BBC", "title": title, "description": description, "link": link})

        # Dawn extraction
        elif source["name"] == "Dawn":
            for item in soup.select(".story"):
                title = item.select_one(".story__title").get_text(strip=True) if item.select_one(".story__title") else "N/A"
                description = item.select_one(".story__excerpt").get_text(strip=True) if item.select_one(".story__excerpt") else "N/A"
                link = item.select_one("a")["href"]
                if not link.startswith("https://"):
                    link = "https://www.dawn.com" + link

                articles.append({"source": "Dawn", "title": title, "description": description, "link": link})

    # Convert to DataFrame and save as CSV
    df = pd.DataFrame(articles)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/articles.csv", index=False)
    return df

if __name__ == "__main__":
    fetch_links_and_articles()
