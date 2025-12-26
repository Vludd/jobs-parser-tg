from datetime import datetime, timezone
from telethon import events
from app.parsers.message_parser import parse_vacancy
from app.dependencies import CLIENT as client
from app.dependencies import FORMATTER as fm
from app.dependencies import PARSING_TARGETS

from app.config import SEND_TO, WHITELIST, BLACKLIST

from app.utils.types import ParseMode

parse_mode = ParseMode.MD

print(f"Followed Chats: {', '.join(PARSING_TARGETS)}")

@client.on(events.NewMessage(chats=PARSING_TARGETS))
async def handler(event):
    text = event.message.message
    
    chat = await event.get_chat()
    chat_name = getattr(chat, 'title', getattr(chat, 'username', 'Unknown'))
    
    source_link = f"https://t.me/c/{str(event.chat_id)[4:]}/{event.message.id}" if event.chat_id < 0 else None

    print(f"[{datetime.now(timezone.utc)}]: Received message from: {chat_name}")
    vacancy = parse_vacancy(text, source_link, WHITELIST, BLACKLIST)
    if vacancy:
        await client.send_message(
            SEND_TO,
            fm.format(vacancy, parse_mode),
            link_preview=False,
            parse_mode=parse_mode.value
        )