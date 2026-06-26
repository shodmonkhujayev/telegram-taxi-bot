import asyncio
from datetime import datetime

from app.scanner import scanner
from app.state import state


class ScanService:

    def __init__(self):
        self.task = None

    def _task_done(self, task: asyncio.Task):
        try:
            task.result()
        except asyncio.CancelledError:
            print("🛑 Scanner task cancelled")
        except Exception as e:
            print(f"❌ Scanner task error: {e}")

    async def start(self, limit: int = 10):

        if state.running:
            return False

        state.running = True
        state.lead_count = 0
        state.lead_limit = limit
        state.started_at = datetime.now()

        print("🚀 Creating scanner task...")

        self.task = asyncio.create_task(scanner.start())
        self.task.add_done_callback(self._task_done)

        return True

    async def stop(self):

        state.running = False

        if self.task:
            self.task.cancel()
            self.task = None

    def add_lead(self):
        state.lead_count += 1

        if state.lead_count >= state.lead_limit:
            state.running = False

    def status(self):

        if state.running:
            return (
                f"🟢 Scanner ishlayapti\n\n"
                f"Lead: {state.lead_count}/{state.lead_limit}"
            )

        return (
            f"🔴 Scanner to'xtagan\n\n"
            f"Lead: {state.lead_count}/{state.lead_limit}"
        )


scan_service = ScanService()
