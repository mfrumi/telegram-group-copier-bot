import asyncio
import logging
from telethon import TelegramClient, events, Button
from config import API_ID, API_HASH, SESSION, SOURCE_CHATS, TARGET_CHAT, CHANNEL_LINK, APPEND_REFERENCE, BUTTON_TITLE, FORWARD_INSTEAD, STATE_FILE
from sanitizer import remove_telegram_links
from state_store import StateStore


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


state = StateStore(STATE_FILE)
client = TelegramClient(SESSION, API_ID, API_HASH)


def make_button():
return [Button.url(BUTTON_TITLE, CHANNEL_LINK)] if CHANNEL_LINK else None


@client.on(events.NewMessage(chats=SOURCE_CHATS))
async def handler(event):
try:
msg = event.message
src_id, msg_id = event.chat_id, msg.id


if state.seen(src_id, msg_id):
return


if FORWARD_INSTEAD:
await client.forward_messages(TARGET_CHAT, msg)
else:
cleaned = remove_telegram_links(msg.message or '')
if APPEND_REFERENCE:
cleaned += f"\n\n-- shared via {TARGET_CHAT}"
await client.send_message(TARGET_CHAT, cleaned or '\u200b', buttons=make_button())


state.mark(src_id, msg_id)
except Exception as e:
logger.exception('Error: %s', e)


async def main():
await client.start()
logger.info('Bot started. Listening for messages...')
await client.run_until_disconnected()


if __name__ == '__main__':
asyncio.run(main())
