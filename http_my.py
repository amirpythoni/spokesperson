from httpx import AsyncClient
import asyncio
session = AsyncClient(timeout=40)

async def send_http(url, json=False, headers=None):
    global session
    try:
        if session.is_closed:
            session = AsyncClient()
        response = await session.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            return response.text
        return {'ok': False, 'status': response.status_code}
    except:
        return {'ok': False}

async def send_post_http(output_json=False, **kwrags):
    global session
    try:
        if session.is_closed:
            session = AsyncClient()
        response = await session.post(**kwrags)
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                return data
            re = await send_http_aiohttp("https://chat-deep.ai/deepseek-chat/")
            return {"nonce": re[re.index("nonce")+7:re.index("nonce")+17]}
        return {'ok': False, 'status': response.status_code}
    except:
        return {'ok': False}


import aiohttp
import asyncio

async def send_http_aiohttp(url, headers=None):
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }

    if headers:
        default_headers.update(headers)

    try:
        async with aiohttp.ClientSession(headers=default_headers) as session:
            async with session.get(url, timeout=30) as response:
                text = await response.text()
                return text if response.status == 200 else {'ok': False, 'status': response.status}
    except Exception as e:
        return {'ok': False, 'error': str(e)}
