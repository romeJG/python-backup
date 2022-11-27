nums=[]
n=''
m=int(input("howmany columns: "))
for i in range(m):
    nums.append(int(input("enter a number: "))) ##transforms string input to int
#makes ls "nums" into Int
max = max(nums)#gets the highest number in the array
for i in range(max):
    for j in range(len(nums)):##logic sa forloop na to is if yung nums[j] is < the max it will print a space otherwise will print an asterisk
        if nums[j]<max:
            print(f'{n:<3}',end='') #end='' so that walang new line na ma print
        else:
            print(f'*{n:<2}',end='')## the n:<2 is to format the spacing for the output
    print()#so that it wil go to the next line :>
    max-=1
for i in nums:
    print(i,' ',end='')
    