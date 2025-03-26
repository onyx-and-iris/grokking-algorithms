import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class BinarySearch:
    def __init__(self, arr):
        self._arr = arr

    def search(self, item):
        low = 0
        high = len(self._arr) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = self._arr[mid]
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
numbers.extend([9000, 999999])
numbers.sort()
print(numbers)

search = BinarySearch(numbers)
print(search.search(42))
print(search.search(9000))
print(search.search(20000))
print(search.search(60000))
print(search.search(999999))
