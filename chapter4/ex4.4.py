import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def binary_search(arr, low, high, x):
    # x not found, low has overlapped high so we return None
    if high < low:
        return

    mid = (high + low) // 2

    # x found at middle of split, return its index
    if arr[mid] == x:
        return mid

    # x in left side of split
    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)

    # x in right side of split
    else:
        return binary_search(arr, mid + 1, high, x)


LOWER = 1000
UPPER = 1000000
SAMPLE_SIZE = 1000

numbers = random.sample(range(LOWER, UPPER), SAMPLE_SIZE)
numbers.sort()

seen = set()
count = 0
result = None
while result is None:
    guess = random.randrange(LOWER, UPPER)
    if guess not in seen:
        count += 1
        seen.add(guess)
        result = binary_search(numbers, 0, len(numbers) - 1, guess)

print(f"Found {guess} at index {result} after {count} attempts.")
