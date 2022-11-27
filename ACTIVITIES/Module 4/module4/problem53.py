def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def read_words(filename):
    print("Content of sample.txt:")
    print(open(filename).read(), "\n")
    return open(filename).read().split()

def main(filename):
    frequency = word_frequency(read_words(filename))
    for word, count in sorted(frequency.items(), key=lambda w: w[1]):
        print('%s: %d' % (word, count))
import sys
main("sample.txt")