import logging
import random
import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


LOWER = 1000
UPPER = 1000000
SAMPLE_SIZE = 1000


def binary_search(arr, item):
    count = 1
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            logger.debug(f"found item after {count} splits")
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

        count += 1

    return None


numbers = random.sample(range(LOWER, UPPER), SAMPLE_SIZE)
numbers.sort()
logger.debug(numbers)

start = time.time()
res = None
while res is None:
    guess = random.randrange(LOWER, UPPER)
    res = binary_search(numbers, guess)


print(f"Found {guess} at index {res}. Running time {time.time() - start}")
