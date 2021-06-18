from domain.entities.detail import Detail
from storage.models import Detail as DetailModel


def get_details():
    models = DetailModel.query.all()
    orders = [Detail.from_model(model) for model in models]

    return orders
