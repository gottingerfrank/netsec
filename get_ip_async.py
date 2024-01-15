#!/usr/bin/env python3


import requests
import asyncio


async def get_IP_info():
    """Gets public IP address of local machine/interface
    asynchronously using requests and asyncio libs over http(s)"""

    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, requests.get, "https://ifconfig.me/")
    content = res.text
    print(content)


asyncio.run(get_IP_info())

# If run as script ...
if __name__ == "__main__":
    import requests
    import asyncio

    get_IP_info()
