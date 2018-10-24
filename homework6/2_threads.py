"""
Download bunch of files using threads.
"""
import concurrent.futures
from datetime import datetime
import os
from urllib.parse import urlparse
import urllib.request

from common import generate_string

ADDRESS = 'http://localhost/download/'


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


if __name__ == '__main__':
    start = datetime.now()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {}

        for i in range(10):
            filename = generate_string() + '.jpg'
            url = ADDRESS + filename
            future_to_url[executor.submit(load_url, url, 60)] = url

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            data = future.result()
            filename = os.path.basename(urlparse(url).path)
            with open(filename, 'wb') as f:
                f.write(data)

    print('Finished in', datetime.now() - start, 'sec')
