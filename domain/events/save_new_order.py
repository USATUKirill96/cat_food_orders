from domain.entities.new_order import NewOrder
from domain.entities.order import Status
from storage import database
from storage.models import Item as ItemModel
from storage.models import Order as OrderModel


def save_new_order(new_order: NewOrder):
    order = OrderModel(user_id=new_order.user_id, payed=False, status=Status.NEW.value)

    item_models = [
        ItemModel(quantity=item.quantity, order=order, detail_id=item.detail_id)
        for item in new_order.items
    ]

    order.items.append(*item_models)

    database.session.add(order)
    database.session.commit()
