import logging
from collections import deque
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@dataclass
class Person:
    name: str
    distance: int

    @property
    def is_seller(self):
        return self.name.endswith("m")


graph = {
    "you": [
        Person("bob", 1),
        Person("claire", 1),
        Person("alice", 1),
    ],
    "claire": [
        Person("thom", 0),
        Person("jonny", 0),
    ],
    "alice": [
        Person("peggy", 0),
    ],
    "bob": [
        Person("peggy", 0),
        Person("anuj", 0),
    ],
    "thom": [],
    "jonny": [],
    "peggy": [],
    "anuj": [],
}

visited = set()


def bfs():
    queue = deque()
    queue += graph["you"]

    while queue:
        logger.debug(queue)
        current_person = queue.popleft()
        if current_person.is_seller:
            return current_person

        if current_person.name in visited:
            continue
        visited.add(current_person.name)

        next_persons = graph[current_person.name]
        for p in next_persons:
            p.distance = current_person.distance + 1
        queue += next_persons


to_word = ["", "first", "second", "third"]

person = bfs()
print(f"{person.name} is a {to_word[person.distance]} degree mango seller.")
