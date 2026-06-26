from app.ai.client import client
from app.ai.prompts import CLASSIFY_PROMPT


class AIClassifier:

    @staticmethod
    def classify(text: str) -> str:

        text = text.strip()

        if not text:
            return "other"

        lower = text.lower()

        # ===== FAST DRIVER FILTER =====

        driver_keywords = [
            "joy bor",
            "bo'sh joy",
            "bosh joy",
            "mashinam bor",
            "ketaman",
            "yuraman",
            "odam olaman",
            "odam olamiz",
            "chiqaman",
            "kim boradi",
            "kim ketadi",
            "3 ta joy",
            "2 ta joy",
            "1 ta joy",
        ]

        for keyword in driver_keywords:
            if keyword in lower:
                print(f"[FAST] driver | {text}")
                return "driver"

        # ===== GEMINI =====

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"{CLASSIFY_PROMPT}\n\n{text}",
            )

            result = response.text.strip().lower()

        except Exception as e:

            print(f"[AI ERROR] {e}")
            return "other"

        print("=" * 60)
        print(f"[AI] {result}")
        print(text)
        print("=" * 60)

        if result not in {
            "passenger",
            "cargo_sender",
            "driver",
            "other",
        }:
            return "other"

        return result


classifier = AIClassifier()
