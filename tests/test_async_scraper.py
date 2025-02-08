import pytest
import asyncio
from async_scraper import scrape_competitor_price_async, scrape_multiple_pages

@pytest.mark.asyncio
async def test_scrape_competitor_price_async():
    price = await scrape_competitor_price_async("test product")
    assert price == 80.00

@pytest.mark.asyncio
async def test_scrape_multiple_pages():
    urls = ["http://example.com/page1", "http://example.com/page2"]
    prices = await scrape_multiple_pages(urls)
    # Since our async function calls the same synchronous function, expect all prices equal 80.00.
    assert prices == [80.00, 80.00]
