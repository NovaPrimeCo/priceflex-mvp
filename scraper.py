import requests
from bs4 import BeautifulSoup

def scrape_competitor_price(product_name):
    """
    Synchronously "scrape" a competitor price.
    (For now, this returns a fixed mock value.)
    """
    # In a production version, you would make an HTTP request and parse the HTML.
    competitor_price = 80.00  # Mock price for demonstration
    return competitor_price

def scrape_product(url):
    """
    Given a URL, scrape the product details.
    For demonstration, this calls scrape_competitor_price with a dummy product name.
    """
    # In a production version, fetch the URL content and parse for product details.
    product_name = "test product"
    return scrape_competitor_price(product_name)

# If run directly, perform a simple demonstration.
if __name__ == "__main__":
    url = "http://example.com/test-product"
    price = scrape_product(url)
    cost = 60.00          # Example merchant cost
    min_markup = 1.2      # 20% markup
    floor_price = cost * min_markup
    recommended_price = max(price, floor_price)
    print(f"Product: test product")
    print(f"Competitor Price: £{price}")
    print(f"Margin Floor: £{floor_price}")
    print(f"Recommended Price: £{recommended_price}")
