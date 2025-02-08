import requests
from bs4 import BeautifulSoup

def scrape_product(url):
    """
    Example scraping function.
    Replace this with your real logic for production usage.
    """
    # For now, just return a mock result for demonstration:
    return {"name": "demo product", "price": 80.0}

if __name__ == "__main__":
    dummy_url = "http://example.com/dummy-product"
    result = scrape_product(dummy_url)
    print("Product:", result["name"])
    print("Price: £", result["price"])
