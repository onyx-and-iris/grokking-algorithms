import heapq
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


def dijkstra(graph, node):
    costs = {node: math.inf for node in graph}
    costs[node] = 0
    parents = {node: None for node in graph}
    queue = [(0, node)]

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        for next_node, weight in graph[current_node].items():
            new_cost = current_cost + weight
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                parents[next_node] = current_node
                heapq.heappush(queue, (new_cost, next_node))
    return costs, parents


costs, parents = dijkstra(graph, "start")
print(f"lowest cost route: {costs['fin']}")