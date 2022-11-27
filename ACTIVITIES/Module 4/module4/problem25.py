# PROBLEM 25
def reverse(char_list):
    x = len(char_list)
    x -= 1
    reverse_content = []
    while x >= 0:
        reverse_content.append(char_list[x])
        x -= 1
    return reverse_content
print("Content =", [1,2,3,4])
print("Reverse = ",reverse([1,2,3,4]))
print("Reverse then reverse =",reverse(reverse([1,2,3,4])), end='')
