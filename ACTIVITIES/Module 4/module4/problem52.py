# Problem 52
def nearly_equal(a,b):
    value_bool = True
    a = a.lower()
    b = b.lower()
    size_a = len(a)
    size_b = len(b)
    duplicate_content = []
    count = 0
    ctr = 0
    list_ab = []
    ab = a+b
    for x in ab:
        list_ab.append(x)
    while ctr < len(list_ab):
        inr_ctr = ctr + 1
        while inr_ctr < len(list_ab):
            if list_ab[ctr] == list_ab[inr_ctr]:
                duplicate_content.append(list_ab[ctr])
            inr_ctr += 1
        ctr += 1
    if size_a == size_b:
        if size_a - len(duplicate_content) <= 1:
            value_bool = True
        else:
         value_bool = False
    elif size_a > size_b:
        if size_a - len(duplicate_content) <= 1:
            value_bool = True
        else:
         value_bool = False
    else:
        if size_b - len(duplicate_content) <= 1:
            value_bool = True
        else:
         value_bool = False
    return value_bool
print("Nearly Equal (True or False)")
print("'python', 'perl' = ", nearly_equal('python', 'perl'))
print("'pearl', 'perl' = ", nearly_equal('pearl', 'perl'))
print("'python', 'jython' = ", nearly_equal('python', 'jython'))
print("'man', 'woman' = ", nearly_equal('man', 'woman'), end='')