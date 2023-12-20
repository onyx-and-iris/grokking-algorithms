import logging
import math

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

graph = {
    "start": {"a": 10},
    "a": {"c": 20},
    "b": {"a": 1, "c": 1},
    "c": {"b": 1, "fin": 30},
    "fin": {},
}

costs = {
    "a": 10,
    "b": math.inf,
    "c": math.inf,
    "fin": math.inf,
}

parents = {
    "a": "start",
    "b": None,
    "c": None,
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
