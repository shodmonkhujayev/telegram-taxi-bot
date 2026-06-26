from dataclasses import dataclass


@dataclass
class Order:

    order_type: str

    from_city: str

    to_city: str

    date: str

    phone: str

