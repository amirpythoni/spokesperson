import yt_dlp
import requests
from rubpy.bot.models import Keypad, KeypadRow, Button
from rubpy.bot.enums import ButtonTypeEnum
from rubpy.bot.enums import ChatKeypadTypeEnum

users_media = {

}

async def info(message, url):
    global users_media
    rows = [
    ]
    response = (requests.get(f"https://onyxapi.ir/v1/youtube/?url={url}")).json()
    if response['ok']:
        data = response['data']['info']
        stats = response['data']['stats']
        medias = response['data']['mediaItems']
        image = data['imagePreviewUrl']
        txt = f"""📍 عنوان: {data['title']}\n\n🎭 تعداد فالوور: {stats['followersCount']}\n👁‍🗨 ویو: {stats['viewsCount']}\n\n☄ کیفیت را تعیین کنید:"""
        dic = {}
        for i in range(0, len(medias), 3):
            rows_2 = []
            first = medias[i]
            second = medias[i + 1] if i + 1 < len(medias) else None
            third = medias[i + 2] if i + 2 < len(medias) else None
            t1 = "🎬" if first['type'] == "Video" else "🎧"
            rows_2.append(Button(
                id=f"media-{i}",
                type=ButtonTypeEnum.SIMPLE,
                button_text=f"{t1} {((first['url']).split('/'))[-1]}({first['size']})"
            ))
            dic[f"media-{i}"] = first
            if second:
                dic[f"media-{i+1}"] = second

                t2 = "🎬" if first['type'] == "Video" else "🎧"
                rows_2.append(Button(
                id=f"media-{i+1}",
                type=ButtonTypeEnum.SIMPLE,
                button_text=f"{t2} {((second['url']).split('/'))[-1]}({second['size']})"
            ))
            if third:
                dic[f"media-{i+2}"] = third
                t3 = "🎬" if first['type'] == "Video" else "🎧"
                rows_2.append(Button(
                id=f"media-{i+2}",
                type=ButtonTypeEnum.SIMPLE,
                button_text=f"{t3} {((third['url']).split('/'))[-1]}({third['size']})"
            ))
            rows.append(KeypadRow(rows_2))
#        print(dic)
        users_media[message.chat_id] = dic
        keypad = Keypad(
            rows=rows,
            resize_keyboard= True
        )
        return await message.reply_photo({"file_name":'image.png', "url":image}, text=txt, chat_keypad=keypad, chat_keypad_type=ChatKeypadTypeEnum.NEW)
    await message.reply("❗ خطا")
    return False
def download_video(url):
    response = requests.get(f"https://onyxapi.ir/v1/youtube/?url={url}")
    if response['ok']:
        pass
