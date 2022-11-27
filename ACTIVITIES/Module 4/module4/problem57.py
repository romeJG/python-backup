# Problem 57
def invertdict(words_dict):
    new_dict = {}
    for x,y in words_dict.items():
        new_dict[y] = x
    return new_dict
print("Content = {'x':1, 'y':2, 'z':3}")
print("Inverted = ", invertdict({'x':1, 'y':2, 'z':3}), end='')