import json
from pathlib import Path


class StateStore:
def __init__(self, path: str):
self.path = Path(path)
if not self.path.exists():
self._data = {'processed': []}
self._write()
else:
self._read()


def _read(self):
with open(self.path, 'r', encoding='utf8') as f:
self._data = json.load(f)


def _write(self):
with open(self.path, 'w', encoding='utf8') as f:
json.dump(self._data, f, indent=2)


def seen(self, chat_id, msg_id) -> bool:
return f"{chat_id}:{msg_id}" in self._data['processed']


def mark(self, chat_id, msg_id):
key = f"{chat_id}:{msg_id}"
if key not in self._data['processed']:
self._data['processed'].append(key)
self._write()
