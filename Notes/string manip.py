str1 = "abcde"
print("normal")
for i in range(0, len(str1)): #normal
    print(str1[i])
print("Reverse")
for i in range(0, len(str1)): #reverse
    print(str1[4-i])


str2 = "            the quick brown fox"

print (str2[-9:-4])
print("not striped")
print(str2)
print("stripped")
print(str2.strip()) #strip removes the excess spaces
str2=str2.strip()
print(str2.replace('o','0'))

for s in str2.split(' '): #this makes the string into tokens spliting them using the char in the paramiter
    print(s)

n = 123
m = 456
print("the value of n is {1} and the value of m {0} respectively using Format".format(n,m))
print(f"the value of n is {n} and the value of m {m} respectively using F")
print(f'the value of n is "{n:<9}" and the value of m "{m:>9}" respectively adding spaces')


str3 = 'the quick brown fox' #finding shit in a string
if 'the' in str3:
    print('"the" is found in string "'+str3+'"')

name = input('enter your name: ')
print ('welcome '+name)