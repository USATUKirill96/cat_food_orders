from typing import List

import attr

from domain.entities.scalars import ID


@attr.s
class NewItem:
    detail_id = attr.ib(type=ID)
    quantity = attr.ib(type=int)

    @classmethod
    def from_input(cls, input):
        return cls(detail_id=input["detailId"], quantity=input["quantity"])


@attr.s
class NewOrder:
    user_id = attr.ib(type=ID)
    items = attr.ib(type=List[NewItem])

    @classmethod
    def from_input(cls, input):
        return cls(
            user_id=input["userId"],
            items=[NewItem.from_input(item_input) for item_input in input["items"]],
        )
