from rubpy.bot.models import Keypad, KeypadRow, Button
from rubpy.bot.enums import ButtonTypeEnum

HOME_Keypad = Keypad(
    rows=[
        KeypadRow(
            [
            Button(
                id="vip",
                type=ButtonTypeEnum.SIMPLE,
                button_text="⚜ اشتراک vip"
            ),
            Button(
                id="support",
                type=ButtonTypeEnum.SIMPLE,
                button_text="🔆 پشتیبان"
            )
            ]
        ),
        KeypadRow(
            [Button(
                id="channels",
                type=ButtonTypeEnum.SIMPLE,
                button_text="💌 کانال های ما"
            )
            ]
        )
    ],
    resize_keyboard= True
)
