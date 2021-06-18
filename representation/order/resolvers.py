from ariadne import QueryType

from domain.events.get_orders import get_orders

order_resolvers = QueryType()


@order_resolvers.field("orders")
def resolve_orders(_, info):
    orders = get_orders()

    return orders
