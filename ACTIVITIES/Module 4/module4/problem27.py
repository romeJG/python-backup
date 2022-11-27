# PROBLEM 27
def cumulative_sum(char_list):
    new_char_list = []
    x = len(char_list)
    x -= 1
    ctr = 0
    while ctr <= x:
        if ctr == 0:
            new_char_list.append(char_list[ctr])
        else:
            inner_ctr = 0
            total = 0
            while inner_ctr <= ctr:
                total = total + char_list[inner_ctr]
                inner_ctr += 1
            new_char_list.append(total)
        ctr += 1
    return new_char_list
print([1,2,3,4], "= ", end='')
print(cumulative_sum([1,2,3,4]))
print([4,3,2,1], "= ", end='')
print(cumulative_sum([4,3,2,1]), end='')