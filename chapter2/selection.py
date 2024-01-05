import logging
from collections import namedtuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

Data = namedtuple("Data", "artist count")

artists = [
    Data("Said Mike", 156),
    Data("The Blackout", 141),
    Data("Hondo Maclean", 35),
    Data("Enter Shikari", 94),
    Data("FFAF", 88),
]


def selectionSort(array, size):
    for index in range(size):
        min_index = index

        for j in range(index + 1, size):
            # select the minimum element in every iteration
            if array[j].count < array[min_index].count:
                min_index = j
        # swapping the elements to sort the array
        (array[index], array[min_index]) = (array[min_index], array[index])


selectionSort(artists, len(artists))
print(artists)
