class Formatter:

    @staticmethod
    def lead(
        lead_type: str,
        group: str,
        profile: str,
        message: str,
        link: str,
    ) -> str:

        if lead_type == "passenger":
            title = "🚕 YO'LOVCHI"

        elif lead_type == "cargo_sender":
            title = "📦 POCHTA"

        else:
            title = "📄 LEAD"

        return (
            f"{title}\n\n"
            f"📍 Guruh:\n{group}\n\n"
            f"👤 Profil:\n{profile}\n\n"
            f"💬 Xabar:\n{message}\n\n"
            f"🔗 Xabar:\n{link}"
        )


formatter = Formatter()

