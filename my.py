from pathlib import Path
from typing import Literal, Optional, Union
from rubpy.bot import BotClient
import aiohttp, asyncio
from rubpy.bot.enums import ChatKeypadTypeEnum
from rubpy.bot.models import Keypad, MessageId
import io
from builtins import type as type_
from get_file import get_file

class BotClientMy(BotClient):
    async def send_file(self,
        chat_id: str,
        file: Optional[Union[str, Path]] = None,
        file_id: Optional[str] = None,
        text: Optional[str] = None,
        file_name: Optional[str] = None,
        type: Literal["File", "Image", "Voice", "Music", "Gif", "Video"] = "File",
        chat_keypad: Optional[Keypad] = None,
        inline_keypad: Optional[Keypad] = None,
        disable_notification: bool = False,
        reply_to_message_id: Optional[str] = None,
        chat_keypad_type: ChatKeypadTypeEnum = ChatKeypadTypeEnum.NONE,
        parse_mode = None,
        metadata=None,) :
        if file and type_(file) == dict:
            file_name = file.get('file_name')
            file = file.get('url')

        return await super().send_file(chat_id, file, file_id, text, file_name, type, chat_keypad, inline_keypad, disable_notification, reply_to_message_id, chat_keypad_type)

    async def upload_file(self, url: str, file_name: str, file_path: str) -> str:
        form = aiohttp.FormData()
        form.add_field(
            name="file",
            value=io.BytesIO(await get_file(file_path)),
            filename=file_name,
            content_type="application/octet-stream",  # یا نوع فایل واقعی مثل image/png
        )

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=form, ssl=False) as res:
                if res.status != 200:
                    text = await res.text()
                    raise aiohttp.ClientResponseError(
                        res.request_info, res.history, status=res.status, message=text
                    )
                data = await res.json()
                return data["data"][
                    "file_id"
                ]  # اطمینان حاصل کن که ساختار JSON این‌طوریه
