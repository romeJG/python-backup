x = 1
def f():
    y = x
    x = 2
    return x + y
print(x)
print(f())
print(x)