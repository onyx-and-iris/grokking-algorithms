import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def maximum(nums, size):
    if size == 1:
        return nums[0]
    return max(nums[size - 1], maximum(nums, size - 1))


randomlist = random.sample(range(10, 300), 5)
logger.debug(randomlist)
print(maximum(randomlist, len(randomlist)))
