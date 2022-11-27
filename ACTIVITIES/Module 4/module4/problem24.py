# PROBLEM 24
def factorial(num):
    fact = 1
    counter = 1
    while counter <= num:
        fact = fact * counter;
        counter += 1
    return fact
print("Factorial of 7 = ",end='')
print(factorial(7), end='')