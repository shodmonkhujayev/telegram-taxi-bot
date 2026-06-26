from app.ai.classifier import classifier
from app.config import config
from app.sender import sender
from app.utils.duplicate_filter import duplicate_filter
from app.utils.formatter import formatter


class LeadService:

    async def process(
        self,
        text: str,
        group: str,
        profile: str,
        link: str,
    ):

        if not text.strip():
            return False

        if duplicate_filter.is_duplicate(text):
            print("[SKIP] Duplicate")
            return False

        result = classifier.classify(text)

        print(f"[CLASSIFIED] {result}")

        if result not in ("passenger", "cargo_sender"):
            print("[SKIP] Not a lead")
            return False

        message = formatter.lead(
            lead_type=result,
            group=group,
            profile=profile,
            message=text,
            link=link,
        )

        await sender.send(
            chat_id=config.OWNER_ID,
            text=message,
        )

        print("[LEAD SENT]")

        return True


lead_service = LeadService()
