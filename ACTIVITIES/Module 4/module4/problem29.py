# PROBLEM 29
def unique(name_list):
    unique_content = []
    for x in name_list:
        if x in unique_content:
            continue
        else:
            unique_content.append(x)
    return unique_content
print("Content =",[1,2,1,3,2,5])
print("Unique =",unique([1,2,1,3,2,5]), end='')