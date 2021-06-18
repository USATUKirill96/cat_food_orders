from ariadne import MutationType

from domain.entities.new_order import NewOrder
from domain.events.save_new_order import save_new_order

order_mutations = MutationType()


@order_mutations.field("createOrder")
def resolve_create_order(_, _info, input):
    new_order = NewOrder.from_input(input)
    save_new_order(new_order)
    return True
