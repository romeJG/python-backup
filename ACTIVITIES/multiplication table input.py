row = int(input('Row: '))
col = int(input('Col: '))
row+=1
col+=1
for i in range (1,row):
    for j in range (1,col):
        print (f'{i*j:<3}',end='')
    print()