# Problem 49
def parse_csv(name_file):
    print("Content: ")
    f = open(str(name_file), "r")
    new_list = []
    line = f.readline()
    while line != '':
        new_line = line.strip()
        print(new_line)
        new_list.append(new_line.split('\t'))
        line = f.readline()
    f.close()
    return new_list
print(parse_csv('a.csv'), end='')