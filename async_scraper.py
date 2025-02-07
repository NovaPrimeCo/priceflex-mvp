import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_page(session, url):
    """Fetch a single page and return its HTML text."""
    async with session.get(url) as response:
        response.raise_for_status()  # raise an error for bad status codes
        return await response.text()

async def scrape_competitor_price_async(url):
    """
    Asynchronously fetch the page at the given URL and attempt to parse
    a competitor price from a <span class="price"> element.
    Returns a float price if found, otherwise None.
    """
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        soup = BeautifulSoup(html, "html.parser")
        # For demonstration, assume the price is in a <span class="price">
        price_span = soup.find("span", class_="price")
        if price_span:
            text = price_span.get_text(strip=True)
            try:
                # Remove any currency symbols and convert to float.
                return float(text.replace("£", "").replace("$", ""))
            except ValueError:
                return None
        return None

async def scrape_multiple_pages(urls):
    """
    Given a list of URLs, concurrently fetch and extract competitor prices.
    Returns a list of prices (floats) or None for any page that fails.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        pages = await asyncio.gather(*tasks, return_exceptions=True)
    
    results = []
    for page in pages:
        if isinstance(page, Exception):
            results.append(None)
        else:
            soup = BeautifulSoup(page, "html.parser")
            price_span = soup.find("span", class_="price")
            if price_span:
                text = price_span.get_text(strip=True)
                try:
                    price = float(text.replace("£", "").replace("$", ""))
                except ValueError:
                    price = None
            else:
                price = None
            results.append(price)
    return results

# Example usage when running this module directly:
if __name__ == "__main__":
    # Example list of URLs (replace with real competitor URLs when available)
    urls = [
        "http://example.com/product1",
        "http://example.com/product2",
        "http://example.com/product3"
    ]
    prices = asyncio.run(scrape_multiple_pages(urls))
    print("Scraped Prices:", prices)
