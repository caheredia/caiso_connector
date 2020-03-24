import asyncio
from datetime import timedelta

import aiofiles
from aiohttp import ClientSession
import pandas as pd
from src.constants import IB

# generate links
caiso_urls = {}
for date in pd.date_range("2019-01-01", "2019-01-02"):
    start_time = date.isoformat()[:-3].replace('-', '')
    end_time = (date + timedelta(days=1)).isoformat()[:-3].replace('-', '')
    caiso_urls[start_time] = "https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=33.0917%2C-95.0417&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"


async def download(url: str, filename: str, session: ClientSession) -> None:
    """Downloads caiso zip file."""
    print(f"starting {filename}")
    resp = await session.get(url)
    resp.raise_for_status()
    content = await resp.content.read()

    async with aiofiles.open("src/temp_data/" + filename + ".zip", 'wb') as f:
        await f.write(content)
        print(f"finished {filename}")


async def main():
    async with ClientSession() as session:
        coroutines = []
        for url in caiso_urls:
            coroutines.append(download(caiso_urls.get(url), url, session))
        await asyncio.gather(*coroutines)


if __name__ == '__main__':
    for date in caiso_urls:
        print(date, caiso_urls.get(date))

    #asyncio.run(main())
