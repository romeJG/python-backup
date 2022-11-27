# Problem 56
def valuesort(dict_words):
    new_content = []
    for i in sorted(dict_words.keys()):
        new_content.append(dict_words.get(i))
    return new_content
print("Content = {'x':1, 'y':2,'a':3}")
print("Sorted key's values = ", valuesort({'x':1, 'y':2,'a':3}), end='')