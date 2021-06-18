import datetime
from enum import Enum
from typing import List

import attr

from .item import Item
from .scalars import ID


class Status(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    READY = "READY"
    DELIVERED = "DELIVERED"


@attr.s
class Order:
    id = attr.ib(type=ID)
    created_at = attr.ib(type=datetime)
    user_id = attr.ib(type=ID)
    payed = attr.ib(type=bool)
    status = attr.ib(type=Status)
    items = attr.ib(type=List[Item])

    @classmethod
    def from_model(cls, model):
        return cls(
            id=model.id,
            created_at=model.created_at,
            user_id=model.user_id,
            payed=model.payed,
            status=model.status,
            items=[Item.from_model(item) for item in model.items],
        )
