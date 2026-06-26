import asyncio

from telethon import TelegramClient, events
from telethon.sessions import StringSession

from app.config import config
from app.repositories.group_repository import group_repository
from app.services.lead_service import lead_service


class Scanner:

    def __init__(self):

        self.client = TelegramClient(
    StringSession(config.SESSION_STRING),
    config.API_ID,
    config.API_HASH,
)

        self.groups = group_repository.get_all()

    async def start(self):

        while True:

            try:

                await self.client.start()

                print("✅ Telethon connected")
                print(f"📡 Listening groups: {len(self.groups)}")

                @self.client.on(events.NewMessage(chats=self.groups))
                async def handler(event):

                    chat = await event.get_chat()
                    sender = await event.get_sender()

                    group = getattr(chat, "title", "Unknown")
                    profile = getattr(sender, "first_name", "Unknown")

                    text = event.raw_text or ""

                    try:
                        link = (
                            f"https://t.me/c/"
                            f"{str(event.chat_id).replace('-100', '')}/"
                            f"{event.id}"
                        )
                    except Exception:
                        link = ""

                    await lead_service.process(
                        text=text,
                        group=group,
                        profile=profile,
                        link=link,
                    )

                await self.client.run_until_disconnected()

            except Exception as e:

                print("=" * 60)
                print("[SCANNER ERROR]")
                print(e)
                print("🔄 Reconnecting in 5 seconds...")
                print("=" * 60)

                await asyncio.sleep(5)


scanner = Scanner()
