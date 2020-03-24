import asyncio
from datetime import timedelta

import aiofiles
import aiohttp
import pandas as pd
from src.helpers import generate_url

# generate links
caiso_urls = {}
for date in pd.date_range("2020-02-01", "2020-03-01"):
    start_time = date.isoformat()[:-3].replace('-', '')
    end_time = (date + timedelta(days=1)).isoformat()[:-3].replace('-', '')
    caiso_urls[start_time] = generate_url(start_time, end_time)


async def download(url: str, filename: str) -> None:
    """Downloads caiso zip file."""
    print(f"starting {filename}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.content.read()
        async with aiofiles.open("src/temp_data/" + filename + ".zip", 'wb') as f:
            await f.write(content)
            print(f"finished {filename}")


async def main():
    coroutines = []
    for url in caiso_urls:
        coroutines.append(download(caiso_urls.get(url), url))
    await asyncio.gather(*coroutines)


if __name__ == '__main__':
    for date in caiso_urls:
        print(date, caiso_urls.get(date))

    asyncio.run(main())
