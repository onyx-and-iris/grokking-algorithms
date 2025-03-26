import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def quicksort(arr):
    # base case. arr of length 0 or 1 don't need sorting, so return them as is
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    # split arr into 3 parts, [less] | [pivot] | [greater]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


LOWER = 0
UPPER = 100
SAMPLE_SIZE = 15
numbers = random.sample(range(LOWER, UPPER), SAMPLE_SIZE)
logging.debug(numbers)
print(quicksort(numbers))
