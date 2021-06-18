import attr

from domain.entities.scalars import ID


@attr.s(frozen=True)
class Detail:
    id = attr.ib(type=ID)
    name = attr.ib(type=str)

    @classmethod
    def from_model(cls, model):
        return cls(id=model.id, name=model.name)
