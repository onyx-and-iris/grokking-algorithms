import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


LOWER = 1000
UPPER = 1000000
SAMPLE_SIZE = 1000


numbers = random.sample(range(LOWER, UPPER), SAMPLE_SIZE)
numbers.sort()

result = None
while result is None:
    guess = random.randrange(LOWER, UPPER)
    logger.debug(f"guess: {guess}")
    result = binary_search(numbers, guess)


print(f"Found {guess} at index {result}.")
