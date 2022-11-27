#A
setA = ['a', 'b', 'c', 'd', 'f', 'g']
setB = ['b', 'c', 'h', 'l', 'm', 'o']
setC = ['c', 'd', 'f', 'j', 'h', 'i', 'k']

andb = setA + setB
print('How many elements are there in set A and B: ', len(set(andb)))

andc = setA + setC
if setB not in andc:
    val = (list(set(setB).difference(set(andc))))
print('How many elements are there in B that is not part of A and C: ', len(val))

if setC not in andb:
    val2 = (list(set(setC).difference(set(andb))))

num3 = list(set(setB).intersection(setC)) + list(set(val2))
num3.remove('c')

num4 = list(set(setA).intersection(setB, setC)) + \
    list(set(setA).intersection(setC))

num5 = list(set(setA).intersection(setB, setC)) + \
    list(set(setA).intersection(setB)) + list(set(setB).intersection(setC))

num6 = list(set(setA).intersection(setC))
num6.remove('c')

print(sorted(list(set(num3))))
print(sorted(list(set(num4))))
print(sorted(list(set(num5))))
print(sorted(list(set(num6))))
print(list(set(setA).intersection(setB, setC)))
print(sorted(list(val)))

# #B
# thisisdict = {"Apple": 15, "Orange": 16,  "Mango": 25,  "Banana": 7,  "Strawberry": 35, "Ponkan": 6}
# print(thisisdict)
# print("Total Number of Items: ", len(thisisdict))
# print("Items: ", end='')
# for x in thisisdict:
#     print(x ,end=' ')
# print("\nSorted Items: ", end='')
# for x in sorted(thisisdict):
#     print(x ,end=' ')
# print()
# search = 'Apple'
# print(f'Searched Item: {search}')
# if search in thisisdict:
#     print('Items: ',search,' with a price of ',thisisdict.get(search))
# print('Items Selection: ')
# item = 'Banana'
# quan = 3
# print(item,f'({quan})', quan*thisisdict.get(item))