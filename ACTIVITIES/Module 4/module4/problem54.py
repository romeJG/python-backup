def word_frequency(words):
    print("Frequency: ")
    frequency = {}
    for w in words:
        for ch in w:
            frequency[ch] = frequency.get(ch, 0) + 1
    return frequency

def read_words(filename):
    print("\nContent of the file:")
    print(open(filename).read(), "\n")
    return open(filename).read().split()

def main(filename):
    frequency = word_frequency(read_words(filename))
    for word, count in sorted(frequency.items(), key=lambda w: w[1]):
        print('%s: %d' % (word, count))
import sys
import os
files = os.listdir()
print("Files = ", files)
input_file = input("Enter a file: ")
check_input_file = input_file.split('.')
print("\nFile = ",end='')
if check_input_file[-1] == 'py':
    print("Python Program File")
elif check_input_file[-1] == 'c':
    print("C Program File")
elif check_input_file[-1] == 'txt':
    print("Text File")
else:
    print("Unknown File")
main(input_file)