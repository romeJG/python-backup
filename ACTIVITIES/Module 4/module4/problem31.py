# PROBLEM 31
def group(name_list, size):
    new_content = []
    inner_list = []
    ctr = 0
    x = len(name_list)
    get_modulo = x % size
    new = x-get_modulo
    x -= 1
    while ctr <= x:
        inner_list.append(name_list[ctr])
        if(len(inner_list) == size):
            new_content.append(inner_list)
            inner_list = []
        ctr += 1
    while new <= x:
        new_content.append(name_list[new])
        new += 1
    return new_content
print("Content =", [1,2,3,4,5,6,7,8,9])
print("3 =",group([1,2,3,4,5,6,7,8,9], 3))
print("4 =",group([1,2,3,4,5,6,7,8,9], 4), end='')