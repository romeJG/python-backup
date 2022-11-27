# PROBLEM 23
def product(name_list):
    total_product = 1
    for x in name_list:
        total_product = total_product * x
    return total_product
print([1,2,3])
print("Prodcut =",product([1,2,3]), end='')