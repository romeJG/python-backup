# PROBLEM 33
def unique(name_list, tolowers):
    unique_content = []
    for x in name_list:
        if tolowers(x) in unique_content:
            continue
        else:
            unique_content.append(tolowers(x))
    return unique_content
print("Content = ['Python', 'java', 'python', 'Java', 'Sample', 'sampLE']")
print("Unique  =", unique(['Python', 'java', 'python', 'Java', 'Sample', 'sampLE'], lambda s: s.lower()),  end='')