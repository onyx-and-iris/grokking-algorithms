import math

num_steps = int(math.log2(128*2))
print(
    f"A binary search would take maximum {num_steps} steps "
    "to search a list of 256 items."
)
