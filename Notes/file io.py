fin = open('C:\\Users\\Justine Guillermo\\Google Drive\\PROG\\PYTHON\\Notes\\windows.jfif','rb') #reads the byte code
fout = open('C:\\Users\\Justine Guillermo\\Google Drive\\PROG\\PYTHON\\Notes\\windows.png','wb') #creates a file 
buf = fin.read(8767) #reads this many bytes
ctr=0

while buf: #while buf still has a value
    buf = fin.read(8767) #reads this many bytes again
    ctr += 1
    print(ctr,end='',flush=True)
fout.close()
fin.close()