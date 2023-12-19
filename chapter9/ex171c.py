import logging
import math

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

graph = {}
graph["start"] = {}
graph["start"]["a"] = 2
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["b"] = 2
graph["b"] = {}
graph["b"]["c"] = 2
graph["b"]["fin"] = 2
graph["c"] = {}
graph["c"]["fin"] = 2
graph["fin"] = {}


costs = {}
costs["a"] = 2
costs["b"] = 2
costs["c"] = math.inf
costs["fin"] = math.inf

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["fin"] = None

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
