from rubpy.bot import filters
from my import BotClientMy as BotClient
from rubpy.bot.models import Update
from db import *
import re
from search import search_media
from get import *
from inline import HOME_Keypad
from rubpy.bot.enums import ChatKeypadTypeEnum
from rubpy.utils import AntiSpam, Hyperlink
import asyncio
bot = BotClient("BDGDB0BKTXDTDMZZREHZWLFKCFEVSPBCOJILNIYRVRFPYKABNVXAJKAPBYWEBUUN", use_webhook=True)

create_tables()
anti:AntiSpam = None
async def AntiSpams():
    global anti
    anti = AntiSpam(3, 7, 250)

async def delete_mes(chat_id, id_1):
    try:
        await asyncio.sleep(50)
        await bot.delete_message(chat_id, str(id_1))
    except:
        pass

users = {}
@bot.on_update(filters.private, filters.commands("start"))
async def start(client:BotClient, message:Update):
    add_user(message.chat_id)
    if users.get(message.chat_id, 0) <= 1:
        users[message.chat_id] = users.get(message.chat_id, 0) + 1
        await message.reply(f"""⚠️ برای استفاده از ربات لطفاً ابتدا در کانال‌های زیر عضو شوید:

🔹 {Hyperlink('@FastBots', 'https://go.rubika.ir/link*ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjBlWEJsSWpvaWIzQmxibU5vWVhRaUxDSnZjR1Z1WDJOb1lYUmZaR0YwWVNJNmV5SnZZbXBsWTNSZlozVnBaQ0k2SW1Nd1ExZEtlSFV3TVRCalpUaGhZV0V6TkdSak5XWTNaRFU0TlRZM1ltUXdJaXdpYjJKcVpXTjBYM1I1Y0dVaU9pSkRhR0Z1Ym1Wc0lpd2liV1Z6YzJGblpWOXBaQ0k2TVRNMk9ESXlNekkxTkRVeU1qTTFOQ3dpWVhOclgycHZhVzVmWTJoaGJtNWxiQ0k2ZEhKMVpYMTkuMzBQMjNZR25RMUNNOGdncVQyaU5wSGlfZ3JSZEstc3Nmc1JIYTJacExQWQ--')}

🔹 {Hyperlink('@Theme_Doni', 'https://go.rubika.ir/link*ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjBlWEJsSWpvaWIzQmxibU5vWVhRaUxDSnZjR1Z1WDJOb1lYUmZaR0YwWVNJNmV5SnZZbXBsWTNSZlozVnBaQ0k2SW1Nd1F6aFNjbWd3TVRBM1ptWmlOVFZtTjJZd01EZ3dOelZqT0RJME56WTNJaXdpYjJKcVpXTjBYM1I1Y0dVaU9pSkRhR0Z1Ym1Wc0lpd2liV1Z6YzJGblpWOXBaQ0k2TVRZME5qWTJOREF4TXpBMU16a3hOaXdpWVhOclgycHZhVzVmWTJoaGJtNWxiQ0k2ZEhKMVpYMTkuTVZOSy0zLVNtR2Fad19IYVhQUGJiYTdrX25WblFZVVhsVXFzVDFMQlVsWQ--')}

🔹 {Hyperlink('@flpwoman', 'https://go.rubika.ir/link*ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjBlWEJsSWpvaWIzQmxibU5vWVhRaUxDSnZjR1Z1WDJOb1lYUmZaR0YwWVNJNmV5SnZZbXBsWTNSZlozVnBaQ0k2SW1Nd1EyaEpaRUl3T1dFNFl6YzNZV1EzTkRNME5UWmpOR05tWWpFM04ySmpJaXdpYjJKcVpXTjBYM1I1Y0dVaU9pSkRhR0Z1Ym1Wc0lpd2liV1Z6YzJGblpWOXBaQ0k2TVRZMU5qTXlNRE0wTVRNM01UQXhNQ3dpWVhOclgycHZhVzVmWTJoaGJtNWxiQ0k2ZEhKMVpYMTkudUs3eUxGY2Zmd0pDNWhfSmFLd1VEQWU2Q18xc0RvdmUwUjZ2NlhDRVVNQQ--')}
""")
        return
    await message.reply("""👋 سلام! به ربات دانلودر یوتیوب خوش اومدی.

اینجا چه خبره؟
🔗 لینک ویدئو رو می‌فرستی
🎬 بات کیفیت‌های مختلف رو بهت نشون میده (از 144p تا 4K!)
📥 هرکدومو خواستی انتخاب کن، تحویل بگیر!
🔍 سرچ محتوا

خب، بزن بریم! لینکتو یا متن جستوجتو بفرست 👇😉""", chat_keypad=HOME_Keypad, chat_keypad_type=ChatKeypadTypeEnum.NEW)
    await bot.set_commands([{"command": "start", "description": "روشن کردن ربات" }])

@bot.on_update(filters.button("channels"))
async def send_msg_channels(client: BotClient, message: Update):
    text = """╭────┈ ↷
│           ✎┊ channels
│╭────────────╯
││• 🤖 @FastBots
││• 👧 @flpwoman
││• 🧸 @Theme_Doni
│╰───────────
│
╰------------ ~ 𝓉ℎ𝒶𝓃𝓀 𝒴ℴ𝓊!❤ ~
    """
    await message.reply(text)

@bot.on_update(filters.button("vip"))
async def send_msg_channels(client: BotClient, message: Update):
#     text = """برای تهیه اشتراک 💎vip مبلغ 69 هزار تومن بپردازید و فیش واریزی را به ادمین ارسال نمایید.❤\n\n6219-8619-7912-9391

# بلو بانک
# امیر حسین عظیمی

# ادمین: @Adminfastbot"""
    await message.reply("بزودی💌")

@bot.on_update(filters.button("support"))
async def send_msg_support(client: BotClient, message: Update):
    text = """📢 برای گزارش مشکل یا ارسال انتقادهای خود، به @AdminFastBot ارسال کنید.🌷\n\nتقدیم با ❤ تیم فست بات"""
    await message.reply(text)

@bot.on_update(filters.private, filters.button("media.*", regex=True))
async def get_media(client:BotClient, message:Update):
    text = message.new_message.aux_data.button_id
    media = users_media.get(message.chat_id)
    if await anti.is_spammer(message.chat_id, message=text):
        await message.reply("اسپم نکنید❗ (4دقیقه سکوت)")
        return
    if media:
        m = media[text]
        file_name = "video.mp4" if m['type'] == "Video" else 'music.mp3'
        if m['type'] == "Video":
            mes = await message.reply("در حال ارسال..📥")
            mfile = await message.reply_video({"file_name":file_name, "url":m['mediaPreviewUrl']}, chat_keypad_type=ChatKeypadTypeEnum.NONE, text="در پیام های ذخیره شده خود ارسال کنید.(50 ثانیه دیگر حذف میشود)")
            asyncio.create_task(delete_mes(message.chat_id, mfile.message_id))
            await mes.delete()
        else:
            mes = await message.reply("در حال ارسال..📥")
            mfile = await message.reply_file({"file_name":file_name, "url":m['mediaPreviewUrl']}, chat_keypad_type=ChatKeypadTypeEnum.NONE, text="در پیام های ذخیره شده خود ارسال کنید.(50 ثانیه دیگر حذف میشود)")
            asyncio.create_task(delete_mes(message.chat_id, mfile.message_id))

            await mes.delete()
        return
    mes = await message.reply("❗ یافت نشد.")




@bot.on_update(filters.private)
async def search(client:BotClient, message:Update):
    text = message.new_message.text
    chat_id = message.chat_id
    pattern = r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)"
    username = (await client.get_chat(message.chat_id)).username
    if username == "adminfastbot":
        if text and text.startswith("ارسال در پیوی"):
            await message.reply(f"در حال اجرا....")
            txt = text[13:]
            groups = get_all_users()
            n = 0
            tasks = []
            async def send(group):
                nonlocal n
                try:
                    await client.send_message(group, txt)
                    n += 1
                except:
                    pass
            for group in groups:
                tasks.append(send(group[0]))
            await asyncio.gather(*tasks)
            await message.reply(f"پیام با موفقیت در {n} پیوی ارسال شد✅")

    links = re.findall(pattern, text)
    if await anti.is_spammer(message.chat_id, message=text):
        await message.reply("اسپم نکنید❗ (4دقیقه سکوت)")
        return
    if not links:
        mes = await message.reply("در حال جستجو🔍..")
        await mes.delete()

        text = search_media(text)
        if text:
            await message.reply(text)
            await message.reply("ℹ برای دانلود لینک مورد نظر را ارسال کنید.")
            return
        await message.reply("❗ مطالبی یافت نشد.")
        return
    mes = await message.reply("در حال دریافت..🌌")
    if int(get_counter_get(chat_id)) >= 1 or True:
        file = await info(message,links[0])
        await mes.delete()
        if file == False:
            return
 #       counter = decrease_counter_get(chat_id)
#        await message.reply(f"💠 تعداد درخواست باقیمانده: {counter}")
        return
    await message.reply("❌ اشتراک رایگان امروز شما به پایان رسید.")
    await mes.delete()
    # await message.reply_file({"file_name":'video.mp4', "url":file})

async def main_run():
    await AntiSpams()
    await bot.run(webhook_url="http://amirpython.runflare.run", path="/wh",port=80)
asyncio.run(main_run())

