import sys
sys.path.insert(0, '.')  # Ensures the root (.) is in sys.path

from scraper import scrape_product  # Must match the exact file name "scraper.py"

def test_scrape_product():
    # Provide any URL or dummy string as needed; 
    # your function can handle it or return a mock for now.
    result = scrape_product("http://example.com/test-product")
    assert isinstance(result, dict)
    assert "name" in result
    assert "price" in result
