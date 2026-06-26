from dataclasses import dataclass


@dataclass
class Lead:

    lead_type: str

    group_name: str

    profile: str

    message: str

    message_link: str
