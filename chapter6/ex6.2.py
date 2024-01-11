import logging
from collections import deque
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@dataclass
class Node:
    name: str
    distance: int


graph = {
    "cab": [Node("cat", 1), Node("car", 1)],
    "cat": [Node("mat", 0), Node("bat", 0)],
    "car": [Node("cat", 0), Node("bar", 0)],
    "mat": [Node("bat", 0)],
    "bar": [Node("bat", 0)],
    "bat": [],
}

visited = []


def bfs():
    queue = deque()
    queue += graph["cab"]

    while queue:
        logger.debug(queue)
        current_node = queue.popleft()
        if current_node.name == "bat":
            return current_node.distance

        if current_node.name in visited:
            continue
        visited.append(current_node.name)

        next_nodes = graph[current_node.name]
        for node in next_nodes:
            node.distance = current_node.distance + 1
        queue += next_nodes


distance = bfs()
print(f"shortest distance from cab to bat: {distance}")
