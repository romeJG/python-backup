# PROBLEM 30
def dups(name_list):
    duplicate_content = []
    ctr = 0
    x = len(name_list)
    x-=1
    while ctr <= x:
        inr_ctr = ctr + 1
        while inr_ctr <= x:
            if name_list[ctr] == name_list[inr_ctr]:
                duplicate_content.append(name_list[ctr])
            inr_ctr += 1
        ctr += 1
    return duplicate_content
print("Content =",[1,2,1,3,2,5])
print("Duplicate =",dups([1,2,1,3,2,5]), end='')