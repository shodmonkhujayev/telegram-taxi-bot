from app.bot import bot


class Sender:

    async def send(
        self,
        chat_id: int,
        text: str,
    ):

        try:

            await bot.send_message(
                chat_id=chat_id,
                text=text,
                disable_web_page_preview=True,
            )

            print("📨 Lead sent")

        except Exception as e:

            print("=" * 60)
            print("[SENDER ERROR]")
            print(e)
            print("=" * 60)


sender = Sender()
