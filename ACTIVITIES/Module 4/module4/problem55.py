# Problem 55
def anagrams(words_list):
    ctr = 0
    new_conten = []
    while ctr < len(words_list):
        inner_ctr = 0
        inner_list = []
        while inner_ctr < len(words_list):
            word1 = sorted(words_list[ctr])
            word2 = sorted(words_list[inner_ctr])
            if word1 == word2:
                if words_list[inner_ctr] not in inner_list:
                    inner_list.append(words_list[inner_ctr])
            inner_ctr += 1
        if inner_list not in new_conten:
            new_conten.append(inner_list)
        ctr += 1
    return new_conten
print("Content =", ['eat','ate','done','tea','soup','node'])
print("Anagrams = ",anagrams(['eat','ate','done','tea','soup','node']),end='')