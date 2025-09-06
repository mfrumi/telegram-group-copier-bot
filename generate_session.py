from telethon.sync import TelegramClient
from telethon.sessions import StringSession


API_ID = int(input("Enter your API ID: "))
API_HASH = input("Enter your API Hash: ")


with TelegramClient(StringSession(), API_ID, API_HASH) as client:
print("\nYour session string is:\n")
print(client.session.save())
print("\nCopy this string into your .env file under SESSION=...")
