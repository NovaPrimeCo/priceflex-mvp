import sys
import os

# Add the parent directory (project root) to sys.path so that 'scraper.py' can be found.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import get_product_details, scrape_product

def test_get_product_details():
    result = get_product_details("test product", cost=60.00, min_markup=1.2)
    assert isinstance(result, dict)
    # Expected values:
    # competitor_price = 80.00 (hard-coded)
    # margin_floor = 60.00 * 1.2 = 72.00
    # recommended_price = max(80.00, 72.00) = 80.00
    assert result["product"] == "test product"
    assert result["competitor_price"] == 80.00
    assert result["margin_floor"] == 72.00
    assert result["recommended_price"] == 80.00

def test_scrape_product():
    result = scrape_product("http://example.com/test-product")
    assert isinstance(result, dict)
    assert result["product"] == "test product"
