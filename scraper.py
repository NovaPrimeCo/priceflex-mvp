import requests
from bs4 import BeautifulSoup

def scrape_product(url):
    """
    Example scraping function.
    Replace with your real logic in production.
    """
    # For demonstration, return a mock dictionary:
    return {
        "name": "demo product",
        "price": 80.0,
    }

if __name__ == "__main__":
    example_url = "http://example.com/dummy-product"
    result = scrape_product(example_url)
    print(f"Scraped product name: {result['name']}, Price: £{result['price']}")
