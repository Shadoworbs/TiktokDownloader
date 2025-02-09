from cgitb import text
import os
from telethon import TelegramClient, sync, events
from telethon.tl.types import ReplyInlineMarkup
from telethon.tl.types import KeyboardButtonRow
from telethon.tl.types import KeyboardButtonUrl
from telethon.tl.types import KeyboardButtonCallback
from dotenv import load_dotenv

load_dotenv()

apiid = os.environ.get("API_ID")
apihash = os.environ.get("API_HASH")
tokenbot = os.environ.get("TOKEN_BOT")

keyboard = ReplyInlineMarkup(rows=[
    KeyboardButtonRow(buttons=[KeyboardButtonUrl(
        text="Cracked Software", url="https://t.me/+F5TYQGKbBrExYzZk") ]),
    KeyboardButtonRow(buttons=[KeyboardButtonUrl(
        text="Latest Movies", url="https://t.me/+BdXh4y_MFqBhZTA0") ]),
    KeyboardButtonRow(buttons=[KeyboardButtonUrl(
        text="Owner", url="https://t.me/shadoworbs")])
])




def sendVideo(chat_id: int, video: str, caption: str, message_id: int):
    try:
        if not os.path.exists("session"):
            os.makedirs("session")
        app = TelegramClient(session=f"session/bot",
                             api_id=apiid, api_hash=apihash)
        app.start(bot_token=tokenbot)
        res = app.send_file(entity=chat_id, file=open(
            video, 'rb'), caption=caption, buttons=keyboard, reply_to=message_id)
        os.remove("video.mp4")
        app.disconnect()
    except Exception as e:
        app.disconnect()
        print(f"- {e}")
