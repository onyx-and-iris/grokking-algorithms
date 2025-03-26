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
class Item:
    name: str
    priority: int
    weight: int


def dynamic(items, n):
    # create table and zero fill it (required for calculations)
    table = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # calculate all possible max values for items in knapsack
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i - 1].weight <= w:
                table[i][w] = max(
                    items[i - 1].priority + table[i - 1][w - items[i - 1].weight],
                    table[i - 1][w],
                )
            else:
                table[i][w] = table[i - 1][w]

    format_and_print(table)

    return get_items_in_knapsack(table[-1][-1], items, n, table)


def format_and_print(table):
    # enumerate first row (headings) + label each row in column0
    for i, row in enumerate(table):
        if i == 0:
            continue
        row[0] = items[i - 1].name
    table[0] = [None, *[i for i in range(1, W + 1)]]

    # print tabularised 2D array
    logger.info([item.name for item in items])
    logger.info(tabulate(table, tablefmt="pretty"))


def get_items_in_knapsack(highest_value, items, n, table):
    in_knapsack = []

    w = W
    res = highest_value
    for i in range(n, 0, -1):
        if res <= 0:
            break

        if res == table[i - 1][w]:
            continue
        else:
            in_knapsack.append(items[i - 1].name)

            res = res - items[i - 1].priority
            w = w - items[i - 1].weight

    return in_knapsack


items = [
    Item("Water", 10, 3),
    Item("Book", 3, 1),
    Item("Food", 9, 2),
    Item("Jacket", 5, 2),
    Item("Camera", 6, 1),
]
W = 6
in_knapsack = dynamic(items, len(items))

print(f"Knapsack contains: {in_knapsack}")
