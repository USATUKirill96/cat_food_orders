from ariadne import (load_schema_from_path, make_executable_schema,
                     snake_case_fallback_resolvers)

from .detail import detail_resolvers
from .order import order_mutations, order_resolvers

type_defs = load_schema_from_path("representation/docs/")

schema = make_executable_schema(
    type_defs,
    [order_resolvers, order_mutations, detail_resolvers],
    snake_case_fallback_resolvers,
)
