import logging
import math

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


### setup the graph

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

### set up costs

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = math.inf

### setup parents

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

### our processed queue

processed = set()

### algorithm


def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # find lowest-cost node not already processed
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    logger.debug(f"node: {node} cost: {cost} neighbor: {neighbors}")
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    logger.debug(f"processed: {processed}")
    node = find_lowest_cost_node(costs)


route = []
next = "fin"
while next != "start":
    route.append(next)
    next = parents[next]
route.append("start")

print(f"route: {list(reversed(route))}")
