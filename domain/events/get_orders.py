from sqlalchemy.orm import joinedload

from domain.entities.order import Order
from storage.models import Order as OrderModel


def get_orders():
    models = OrderModel.query.options(joinedload("items"))
    orders = [Order.from_model(model) for model in models]

    return orders
