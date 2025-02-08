import pytest
from scraper import scrape_product, scrape_competitor_price

def test_scrape_product():
    # Test that the synchronous scraping function returns the expected mock price.
    url = "http://example.com/test-product"
    price = scrape_product(url)
    assert price == 80.00

def test_scrape_competitor_price():
    # Test the direct competitor price scraping function.
    product_name = "dummy"
    price = scrape_competitor_price(product_name)
    assert price == 80.00
