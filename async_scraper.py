import asyncio
from scraper import scrape_competitor_price

async def scrape_competitor_price_async(product_name):
    # Mimic asynchronous behavior; in production, use aiohttp instead of requests.
    await asyncio.sleep(0)  # Simulate async delay
    return scrape_competitor_price(product_name)

async def scrape_multiple_pages(urls):
    # Given a list of URLs, concurrently fetch competitor prices.
    tasks = [scrape_competitor_price_async("test product") for _ in urls]
    return await asyncio.gather(*tasks)
