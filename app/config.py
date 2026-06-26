from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass(frozen=True)
class Config:
    API_ID: int = int(os.getenv("API_ID", "0"))
    API_HASH: str = os.getenv("API_HASH", "")

    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    OWNER_ID: int = int(os.getenv("OWNER_ID", "0"))

    SESSION_STRING: str = os.getenv("SESSION_STRING", "")

    SCAN_LIMIT: int = 10
    SCAN_TIMEOUT: int = 3600


config = Config()
