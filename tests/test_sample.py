import sys
sys.path.insert(0, '.')  # Ensure root directory is accessible.

from scraper import scrape_product  # matches the file "scraper.py" exactly.

def test_scrape_product():
    # Basic test logic:
    data = scrape_product("http://example.com/test-product")
    assert isinstance(data, dict)
    assert "name" in data
    assert "price" in data
