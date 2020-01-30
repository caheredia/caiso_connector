import aiohttp
import asyncio
import aiofiles

temp1 = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&startdatetime=20190201T00:00-0000&enddatetime=20190202T00:00-0000&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"
temp2 = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&startdatetime=20190202T00:00-0000&enddatetime=20190203T00:00-0000&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"
temp3 = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&startdatetime=20190203T00:00-0000&enddatetime=20190204T00:00-0000&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"

links = {'temp1': temp1, 'temp2': temp2, 'temp3': temp3}


async def download(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.content.read()
        async with aiofiles.open(filename + ".zip", 'wb') as f:
            await f.write(content)


async def main():
    coroutines = []
    for link in links:
        coroutines.append(download(links.get(link), link))
    await asyncio.gather(*coroutines)


if __name__ == '__main__':
    asyncio.run(main())
