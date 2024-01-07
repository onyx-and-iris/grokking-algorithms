class Number:
    def __init__(self, value):
        self.value = value


def summation(nums):
    if len(nums) == 1:
        return nums[0].value
    return nums[0].value + summation(nums[1:])


nums = [Number(i) for i in range(0, 100, 3)]
print(summation(nums))
