import logging
from dataclasses import dataclass

from tabulate import tabulate

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s\n\r%(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


@dataclass
class Location:
    name: str
    time: int
    rating: int


def dynamic(items, n):
    # create table and zero fill it (required for calculations)
    table = [[0 for _ in range(2 * (W + 1) - 1)] for _ in range(n + 1)]

    # calculate all possible max values for items in knapsack
    for i in range(1, n + 1):
        for w in range(1, 2 * (W + 1) - 1):
            if items[i - 1].time <= w:
                table[i][w] = max(
                    items[i - 1].rating + table[i - 1][w - items[i - 1].time],
                    table[i - 1][w],
                )
            else:
                table[i][w] = table[i - 1][w]

    format_and_print(table)

    return table[-1][-1]


def format_and_print(table):
    # enumerate first row (headings) + label each row in column0
    for i, row in enumerate(table):
        if i == 0:
            continue
        row[0] = locations[i - 1].name
    table[0] = [i / 2 for i in range(2 * (W + 1) - 1)]
    table[0][0] = None

    # print tabularised 2D array
    logger.info([item.name for item in locations])
    logger.info(tabulate(table, tablefmt="pretty"))


# values converted to integers
locations = [
    Location("Westminster Abbey", 1, 7),
    Location("Globe Theater", 1, 6),
    Location("National Gallery", 2, 9),
    Location("British Museum", 4, 9),
    Location("St. Pauls Cathedral", 1, 8),
]
W = 2
greatest_value = dynamic(locations, len(locations))

print(f"Greatest value: {greatest_value}")
