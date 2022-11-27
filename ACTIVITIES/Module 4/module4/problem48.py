# Problem 48
def array(row,col):
    new_list = []
    ctr = 0
    while ctr < row:
        inner_ctr = 0
        inner_list = []
        while inner_ctr < col:
            inner_list.append("None")
            inner_ctr += 1
        new_list.append(inner_list)
        ctr += 1
    return new_list
print("a = array(2,3) = ", end='')
a = array(2,3)
print(a)
print("a[0][0] = 5 = ", end='')
a[0][0] = 5
print(a, end='')