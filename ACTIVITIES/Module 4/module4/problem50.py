# Problem 50
def parse(name_file, deli1, deli2):
    print("Content: ")
    f = open(str(name_file), "r")
    new_list = []
    line = f.readline()
    while line != '':
        new_line = line.strip()
        print(new_line)
        if str(deli1) in new_line:
            new_list.append(new_line.split(str(deli1)))
        elif str(deli2) in new_line:
            new_list.append(new_line.split(str(deli1)))
        else:
            new_list.append(new_line.split())
        line = f.readline()
    f.close()
    return new_list
print(parse('a.txt', '!', '#'), end='')