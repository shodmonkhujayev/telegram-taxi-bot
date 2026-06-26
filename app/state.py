from dataclasses import dataclass
from datetime import datetime


@dataclass
class ScanState:
    running: bool = False

    lead_count: int = 0
    lead_limit: int = 10

    started_at: datetime | None = None

    timeout_seconds: int = 3600


state = ScanState()
