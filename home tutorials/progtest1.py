arr = [5,7,9,6,12,14,18,17,12,12,10,2]
space = 0

for i in range(len(arr)):
    print(arr[i])
    if i < len(arr):
        if arr[i]<arr[i+1]:
            space+=1
        elif arr[i]>arr[i+1]:
            space-=1
    for j in range(space):
        print(' ',end='')
