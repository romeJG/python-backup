# Number 1
def number_of_vowels(word_string):
    count = 0
    for x in word_string:
        if x.lower() == 'a' or x.lower() == 'e' or x.lower() == 'i' or x.lower() == 'o' or x.lower() == 'u':
            count += 1
    return count
input_word = str(input("Enter a string: "))
print("Number of Vowels = ", number_of_vowels(input_word), end='')

# Number 2
def check_palindrome(word_string):
    new_word = word_string[::-1]
    value = "Not a Palindrome"
    if new_word == word_string:
        value = "Palindrome"
    return value

input_word = str(input("Enter a string: "))
print(check_palindrome(input_word), end='')

# Number 3
def sum_of_numbers(word_string):
    count = 0
    for x in word_string:
        if x.isnumeric():
            count += int(x)
    return count
input_word = str(input("Enter a string: "))
print("Sum of Numbers = ", sum_of_numbers(input_word), end='')

# Number 4
def number_of_words(word_string):
    count = 0
    for x in word_string.split(' '):
            count += 1
    return count
input_word = str(input("Enter a string: "))
print("Numbers= of Words = ", number_of_words(input_word), end='')