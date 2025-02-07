import asyncio
import pytest
from async_scraper import scrape_competitor_price_async, scrape_multiple_pages

# For testing purposes, we will simulate an HTML response.
# In a real-world scenario, you would use a library like 'aiohttp.test_utils' or monkeypatch the ClientSession.get method.

# Here is a helper function to simulate fetching a page:
async def fake_fetch_page(session, url):
    # Return a fixed HTML snippet containing a price.
    return '<html><body><span class="price">£99.99</span></body></html>'

# Monkey-patch the fetch_page function in async_scraper for testing.
@pytest.fixture(autouse=True)
def patch_fetch_page(monkeypatch):
    monkeypatch.setattr("async_scraper.fetch_page", fake_fetch_page)

@pytest.mark.asyncio
async def test_scrape_competitor_price_async():
    url = "http://example.com/dummy"
    price = await scrape_competitor_price_async(url)
    assert price == 99.99, f"Expected price 99.99, got {price}"

@pytest.mark.asyncio
async def test_scrape_multiple_pages():
    urls = ["http://example.com/dummy1", "http://example.com/dummy2"]
    prices = await scrape_multiple_pages(urls)
    # Since fake_fetch_page returns the same HTML, both prices should be 99.99.
    assert prices == [99.99, 99.99]
