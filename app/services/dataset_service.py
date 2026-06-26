import json
from pathlib import Path
from datetime import datetime


class DatasetService:

    def __init__(self):

        Path("data").mkdir(exist_ok=True)

        self.file = Path("data/raw_messages.jsonl")

    def save(
        self,
        group: str,
        profile: str,
        text: str,
    ):

        row = {
            "time": datetime.now().isoformat(),
            "group": group,
            "profile": profile,
            "text": text,
        }

        with self.file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


dataset_service = DatasetService()
