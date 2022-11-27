# Problem 12
def count_digits(num):
    count = 0
    num_string = str(num)
    for letter in num_string:
        if letter.isnumeric():
            count += 1
    return count
print("Content = 12345")
print("Number of digits =",count_digits(12345), end='')