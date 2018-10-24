"""
Download bunch of files using aiohttp package.
"""
import asyncio
from datetime import datetime
import os
from urllib.parse import urlparse

import aiohttp

from common import generate_string

ADDRESS = 'http://localhost/download/'


async def download_file(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
            filename = os.path.basename(urlparse(url).path)
            with open(filename, 'wb') as f:
                f.write(content)


if __name__ == '__main__':
    start = datetime.now()

    tasks = []
    for i in range(10):
        filename = generate_string() + '.jpg'
        url = ADDRESS + filename
        tasks.append(asyncio.ensure_future(download_file(url)))

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    print('Finished in', datetime.now() - start, 'sec')
