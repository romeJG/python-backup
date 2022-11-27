# Problem 32
def lensort(words):
    num = []
    new_content = []
    ctr = 0
    for x in words:
        num.append(len(x))
    num.sort()
    while ctr < len(num):
        in_ctr = 0
        while in_ctr < len(words):
            if(len(words[in_ctr]) == num[ctr]):
                if words[in_ctr] not in new_content:
                    new_content.append(words[in_ctr])
            in_ctr += 1
        ctr += 1
    return new_content
print("Content =", ['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
print("Sort by length =", lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']),end='')