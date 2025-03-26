import logging
import math

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

graph = {
    "start": {"a": 5, "b": 2},
    "a": {"b": 8, "c": 4, "d": 2},
    "b": {"a": 8, "d": 7},
    "c": {"d": 6, "fin": 3},
    "d": {"fin": 1},
    "fin": {},
}

costs = {
    "a": 5,
    "b": 2,
    "c": math.inf,
    "d": math.inf,
    "fin": math.inf,
}

parents = {
    "a": "start",
    "b": "start",
    "c": None,
    "d": None,
    "fin": None,
}

processed = set()


def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs)

print(f"lowest cost route: {costs['fin']}")


def get_full_route():
    route = []
    next = "fin"
    while next != "start":
        route.append(next)
        next = parents[next]
    route.append("start")
    return list(reversed(route))


print(f"route: {get_full_route()}")
