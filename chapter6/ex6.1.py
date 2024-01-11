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
    "s": [Node("a", 1), Node("b", 1)],
    "a": [Node("c", 0), Node("f", 0)],
    "b": [Node("c", 0), Node("d", 0)],
    "c": [],
    "d": [Node("f", 0)],
    "f": [],
}

visited = set()


def bfs():
    queue = deque()
    queue += graph["s"]

    while queue:
        logger.debug(queue)
        current_node = queue.popleft()
        if current_node.name == "f":
            return current_node.distance

        if current_node.name in visited:
            continue
        visited.add(current_node.name)

        next_nodes = graph[current_node.name]
        for node in next_nodes:
            node.distance = current_node.distance + 1
        queue += next_nodes


distance = bfs()
print(f"shortest distance from s to f: {distance}")
