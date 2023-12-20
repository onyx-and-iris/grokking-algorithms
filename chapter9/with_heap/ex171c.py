import heapq
import logging
import math

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

graph = {
    "start": {"a": 2, "b": 2},
    "a": {"b": 2},
    "b": {"c": 2, "fin": 2},
    "c": {"fin": 2},
    "fin": {},
}


def dijkstra(graph, node):
    costs = {node: math.inf for node in graph}
    costs[node] = 0
    parents = {node: None for node in graph}
    queue = [(0, node)]

    while queue:
        current_cost, current_node = heapq.heappop(queue)
        logger.debug(f"node {current_node} with cost {current_cost} popped from pqueue")

        for next_node, weight in graph[current_node].items():
            new_cost = current_cost + weight
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                parents[next_node] = current_node
                heapq.heappush(queue, (new_cost, next_node))
                logger.debug(
                    f"node {next_node} with new cost {new_cost} appended to pqueue"
                )
    return costs, parents


costs, parents = dijkstra(graph, "start")

print(f"lowest cost from start to fin: {costs['fin']}")
