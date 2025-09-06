import re


URL_RE = re.compile(r'https?://(t\.?me|telegram\.me|telegram\.dog)/[^\s]+', flags=re.IGNORECASE)
AT_USERNAME_RE = re.compile(r'@\w{5,64}')
INVITE_RE = re.compile(r'(https?://)?t\.me/joinchat/[^\s]+', flags=re.IGNORECASE)


def remove_telegram_links(text: str) -> str:
if not text:
return text
t = URL_RE.sub('', text)
t = INVITE_RE.sub('', t)
t = AT_USERNAME_RE.sub('', t)
t = re.sub(r'\n\s+','\n', t)
t = re.sub(r'\s{2,}',' ', t)
return t.strip()
