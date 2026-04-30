import aiohttp, mimetypes, asyncio

async def get_file(file_inline):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(file_inline) as result:
            return await result.read()
