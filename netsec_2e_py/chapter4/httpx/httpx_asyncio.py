import httpx
import asyncio


async def request_http1():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://www.google.es")
        print("******* response ********")
        print(response)
        print("******* response.text (utf-8/ascii text) ********")
        print(response.text)
        print("******* response.http_version ********")
        print(response.http_version)
        print("******* response.content (binary: Bytes) ********")
        print(response.content)
        print("******* response.headers ********")
        print(response.headers)
        print(response.charset_encoding)
		
asyncio.run(request_http1())
