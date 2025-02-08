# tests/test_sample.py
import pytest
from scraper import scrape_product, get_product_details

def test_scrape_product():
    # Test that the function returns the expected hard-coded value.
    result = scrape_product("http://example.com/test-product")
    # Since scrape_product calls scrape_competitor_price (which returns 80.00)
    assert result == 80.00

def test_get_product_details():
    details = get_product_details("http://example.com/test-product")
    assert details["competitor_price"] == 80.00
    # floor_price should be 60.00 * 1.2 = 72.00, so recommended is max(80.00, 72.00)
    assert details["floor_price"] == 72.00
    assert details["recommended_price"] == 80.00
