from ariadne import QueryType

from domain.events.get_details import get_details

detail_resolvers = QueryType()


@detail_resolvers.field("details")
def resolve_details(_, info):
    details = get_details()

    return details
