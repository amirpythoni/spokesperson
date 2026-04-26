
import asyncio
from http_my import send_http, send_post_http, send_http_aiohttp
import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from random import randint
from bs4 import BeautifulSoup

app = FastAPI()
nonce_main = "d5044671b4"
@app.post("/text-generator/")
async def send_message(request: Request):
    try:
        async def main():
                global nonce_main
                body = await request.json()
                input_text = body.get("text", "")
                input_text = input_text
                data = {
    "action":"deepseek_chat",
    "message": input_text,
    "model": "deepseek-reasoner",
    "nonce": nonce_main,
    "save_conversation": 0,
    "session_only": 1
}
                re = await send_post_http(url="https://chat-deep.ai/wp-admin/admin-ajax.php", data=data, output_json=True)
                if re.get("nonce"):
                    nonce_main = re.get("nonce")
                    return
                return re['data']['response']
                # re = await send_http(f"https://ssasassasdsad.liara.run/text-generator/?text={input_text}")
                # print(re)
                # return re['results'][0]

        result = await main()
        result = result.replace("\n", """
    """)
        return JSONResponse(content={"results":[result]})
    except:pass

@app.get("/nonce/")
async def nonce2(request: Request, nonce):
    global nonce_main
    nonce_main = nonce

@app.get("/tala-2233/")
async def def_tala(request: Request):
    url = f"https://talasea.ir/geram18"
    response = await send_http_aiohttp(url)
# try:
    content = response
    response_web_page = BeautifulSoup(content, "html.parser")
    talas = response_web_page.find_all("div", class_='w-full flex flex-col group')
    result = []
    for tala in talas[:7]:
        txt = tala.find("a", class_="text-body1Bold").text
        txt = txt.replace("قیمت ", "")
        nerkh = (tala.find("div", class_="flex-center")).find("span").text
        taghir = (tala.find("span", class_="pr-1.5")).text
        float_t = float(taghir.replace("%", ""))
        if float_t > 0:
            emoji = "📈"
        else:
            emoji = "📉"
        result.append(f"» {txt}: {nerkh} تومان\n•تغییر: {emoji} {taghir} ({(float_t*float(nerkh.replace(',','')))//100})\n")
    return JSONResponse(content={"results":result})
    # except:
    #     return {'status': 403}


@app.get("/seke-2233/")
async def def_tala(request: Request):
    url = f"https://talasea.ir/geram18"
    response = await send_http_aiohttp(url, headers={"User-Agent":"python-httpx/0.28.1"})
    try:
        content = response
        response_web_page = BeautifulSoup(content, "html.parser")
        talas = response_web_page.find_all("div", class_='w-full flex flex-col group')
        result = []
        for tala in talas[7:]:
            txt = tala.find("a", class_="text-body1Bold").text
            txt = txt.replace("قیمت ", "")
            nerkh = (tala.find("div", class_="flex-center")).find("span").text
            taghir = (tala.find("span", class_="pr-1.5")).text
            float_t = float(taghir.replace("%", ""))
            if float_t > 0:
                emoji = "📈"
            else:
                emoji = "📉"
            result.append(f"» {txt}: {nerkh} تومان\n•تغییر: {emoji} {taghir} ({(float_t*float(nerkh.replace(',','')))//100})\n")
        return JSONResponse(content={"results":result})
    except:
        return {'status': 403}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80, access_log=False)
