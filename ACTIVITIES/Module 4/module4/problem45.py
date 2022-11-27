# Problem 45
def even(x):
    return x%2 == 0
print("Even Numbers of range(10)")
print(list(filter(even, range(10))), end='')