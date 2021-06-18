from typing import Optional

import attr

from domain.entities.detail import Detail
from domain.entities.scalars import ID


@attr.s(frozen=True)
class Item:
    id = attr.ib(type=ID)
    detail = attr.ib(type=Detail)
    quantity = attr.ib(type=int)

    @classmethod
    def from_model(cls, model):
        return cls(
            id=model.id, quantity=model.quantity, detail=Detail.from_model(model.detail)
        )
