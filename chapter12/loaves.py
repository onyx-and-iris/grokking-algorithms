import logging
from dataclasses import dataclass

import numpy as np

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


@dataclass
class Point:
    identifier: str
    weather: int
    is_weekend: bool
    is_game_on: bool
    sold: int = 0
    distance: int = 0

    @property
    def array(self):
        return np.array([self.weather, int(self.is_weekend), int(self.is_game_on)])


def knn(point: Point, neighbours):
    for neighbour in neighbours:
        neighbour.distance = np.linalg.norm(point.array - neighbour.array)
        logger.debug(f"{neighbour.identifier}: {neighbour.distance}")

    average = 0
    for n in sorted(neighbours, key=lambda x: x.distance)[:K]:
        average += n.sold
    return average / K


neighbours = [
    Point("A", 5, True, False, 300),  # A
    Point("B", 3, True, True, 225),  # B
    Point("C", 1, True, False, 75),  # C
    Point("D", 4, False, True, 200),  # D
    Point("E", 4, False, False, 150),  # E
    Point("F", 2, False, False, 50),  # F
]

point = Point("T", 4, True, False)
K = 4
average_distance = knn(point, neighbours)

logger.debug(average_distance)
print(f"Number of loaves to make: {int(round(average_distance, 0))}")
