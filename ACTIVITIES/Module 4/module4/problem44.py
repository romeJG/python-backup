# PROBLEM 44
def square(x):
    return x*x
result = map(square, range(5))
print("Squared of range(5)")
print(list(result), end='')