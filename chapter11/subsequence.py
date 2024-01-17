import logging

from tabulate import tabulate

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s\n\r%(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def longest_common_subsequence(X, Y, len_x, len_y):
    # create table and zero fill it
    table = [[0 for _ in range(len_x + 1)] for _ in range(len_y + 1)]

    for i in range(1, len_y + 1):
        for j in range(1, len_x + 1):
            if X[j - 1] == Y[i - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    format_and_print(X, Y, table)

    return table[-1][-1]


def format_and_print(X, Y, table):
    # enumerate first row (headings) + label each row in column0
    for i, row in enumerate(table):
        if i == 0:
            continue
        row[0] = Y[i - 1]
    table[0] = [None, *X]

    # print tabularised 2D array
    logger.info(tabulate(table, tablefmt="pretty"))


X = "fosh"
Y = "fort"

logger.info(f"words: {X} {Y}")
longest_subsequence = longest_common_subsequence(X, Y, len(X), len(Y))
print(f"Longest common subsequence: {longest_subsequence}")


X = "fosh"
Y = "fish"

logger.info(f"words: {X} {Y}")
longest_subsequence = longest_common_subsequence(X, Y, len(X), len(Y))
print(f"Longest common subsequence: {longest_subsequence}")
