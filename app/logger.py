from datetime import datetime
from pathlib import Path


class Logger:

    def __init__(self):

        Path("logs").mkdir(exist_ok=True)

        self.file = Path("logs/bot.log")

    def info(self, text: str):

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{now}] INFO  {text}\n"

        print(line, end="")

        with self.file.open("a", encoding="utf-8") as f:
            f.write(line)

    def error(self, text: str):

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{now}] ERROR {text}\n"

        print(line, end="")

        with self.file.open("a", encoding="utf-8") as f:
            f.write(line)


logger = Logger()

