import json
from src.settings import DEFAULT_SHORTCUTS


class Shortcuts:
    def __init__(self, source: str):
        self.source = source
        self.get_data()

    def get_data(self):
        try:
            self.data = self.open()
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.update(DEFAULT_SHORTCUTS)
        return self.data

    def open(self):
        with open(self.source) as f:
            return json.load(f)

    def get_all(self):
        return self.get_data()

    def get(self, key: str):
        return self.get_all().get(key)

    def update(self, data: dict):
        self.data = data
        with open(self.source, "w") as f:
            json.dump(self.data, f)
