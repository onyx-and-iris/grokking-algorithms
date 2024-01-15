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
    value: int
    weight: int


def dynamic(items, n):
    # create table and zero fill it (required for calculations)
    table = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # calculate all possible max values for items in knapsack
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i - 1].weight <= w:
                table[i][w] = max(
                    items[i - 1].value + table[i - 1][w - items[i - 1].weight],
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
        row[0] = items[i - 1].name
    table[0] = [i for i in range(W + 1)]
    table[0][0] = None

    # print tabularised 2D array
    logger.info([item.name for item in items])
    logger.info(tabulate(table, tablefmt="pretty"))


# Where items = Guitar + Stereo + Laptop
items = [Item("Guitar", 1500, 1), Item("Stereo", 3000, 4), Item("Laptop", 2000, 3)]
W = 4
greatest_value = dynamic(items, len(items))

print(f"Greatest value: {greatest_value}")


# Where items = Guitar + Stereo + Laptop + Iphone
items = [
    Item("Guitar", 1500, 1),
    Item("Stereo", 3000, 4),
    Item("Laptop", 2000, 3),
    Item("Iphone", 2000, 1),
]
W = 4
greatest_value_with_iphone = dynamic(items, len(items))

print(f"Greatest value: {greatest_value_with_iphone}")
