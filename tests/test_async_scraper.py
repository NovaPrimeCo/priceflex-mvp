# tests/test_sample.py

# Update the import to match the functions defined in scraper.py.
# For example, if your scraper.py defines scrape_competitor_price, import that.
from scraper import scrape_competitor_price

def test_scrape_competitor_price():
    product = "test product"
    price = scrape_competitor_price(product)
    # Assert that a valid price (float) is returned and is above zero.
    assert isinstance(price, float)
    assert price > 0
