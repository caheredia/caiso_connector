import asyncio
from datetime import timedelta

import aiofiles
import pandas as pd
from aiohttp import ClientSession
from src.constants import IBM_API_KEY, SAVE_FOLDER

# generate links
caiso_urls = {}
for date in pd.date_range("2019-01-01", "2019-02-01"):
    start_time = date.isoformat()[:-3].replace('-', '').split('T')[0]
    end_time = (date + timedelta(days=1)).isoformat()[:-3].replace('-', '').split('T')[0]
    caiso_urls[start_time] = f"http://api.weather.com/v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=33.0917%2C-95.0417&startDateTime={start_time}0000&endDateTime={end_time}0000&apiKey={IBM_API_KEY}"


async def download(url: str, filename: str, session: ClientSession) -> None:
    """Downloads caiso zip file."""
    print(f"starting {filename}")
    resp = await session.get(url)
    resp.raise_for_status()
    content = await resp.content.read()

    async with aiofiles.open(SAVE_FOLDER + filename + ".json", 'wb') as f:
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

    asyncio.run(main())
