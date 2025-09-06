import os
from dotenv import load_dotenv


load_dotenv()


API_ID = int(os.getenv('API_ID', '0'))
API_HASH = os.getenv('API_HASH', '')
SESSION = os.getenv('SESSION', 'session')


SOURCE_CHATS = [s.strip() for s in os.getenv('SOURCE_CHATS', '').split(',') if s.strip()]
TARGET_CHAT = os.getenv('TARGET_CHAT', '')


CHANNEL_LINK = os.getenv('CHANNEL_LINK', '')
APPEND_REFERENCE = os.getenv('APPEND_REFERENCE', 'true').lower() in ('1','true','yes')
BUTTON_TITLE = os.getenv('BUTTON_TITLE', 'numbers')
STATE_FILE = os.getenv('STATE_FILE', 'state.json')
FORWARD_INSTEAD = os.getenv('FORWARD_INSTEAD', 'false').lower() in ('1','true','yes')
