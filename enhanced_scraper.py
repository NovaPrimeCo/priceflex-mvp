import asyncio
import aiohttp
import async_timeout
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
async def fetch_with_retry(url, session):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()

async def get_page_content(url):
    async with aiohttp.ClientSession() as session:
        try:
            html = await fetch_with_retry(url, session)
            return html
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

# Sample synchronous wrapper for testing
def get_page_content_sync(url):
    return asyncio.run(get_page_content(url))
