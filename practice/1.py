# Initialize an empty list to store the numbers
nums=[]
# Initialize a string variable
n=''

# Ask the user for the number of columns
col=int(input("howmany columns: "))
# Loop through the number of columns and ask for a number for each
for i in range(col):
     #transforms string input to int
    nums.append(int(input("enter a number: ")))
    
#gets the highest number in the array
max = max(nums)

#logic sa forloop na to is if yung nums[j] is < the max it will print a space
#otherwise will print an asterisk
for i in range(max):
    # Loop through the length of the list of numbers
    for j in range(len(nums)):
        # If the current number is less than the max, print a space
        if nums[j]<max:
            #end='' so that walang new line na ma print
            print(f'{n:<3}',end='')
        # If the current number is equal to or greater than the max, print an asterisk
        else:
            # the n:<2 is to format the spacing for the output
            print(f'*{n:<2}',end='')
    #so that it wil go to the next line :>
    print()
    max-=1
for i in nums:
    print(i,' ',end='')
    