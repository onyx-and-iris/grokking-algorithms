def factorial(x):
    if x == 1:  # This is the base case
        return 1
    return x * factorial(x - 1)  # This is the recursive case


print(factorial(4))
