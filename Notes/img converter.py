from PIL import image
def conv(fin, fout):
    buf = fin.read(8767) #reads this many bytes
    ctr=0
    while buf: #while buf still has a value
        buf = fin.read(8767) #reads this many bytes again
        ctr += 1
        print(ctr,end='',flush=True)

fin = open('C:\\Users\\Justine Guillermo\\Google Drive\\PROG\\PYTHON\\Notes\\windows.jfif','rb') #reads the byte code

print ('[1] convert to .png')
print ('[2] convert to .jpg')
print ('[3] convert to .gif')
print ('[0] exit')
ch = input('>')

if (ch=='1'):
    print('converting to png...')
    fout = open('C:\\Users\\Justine Guillermo\\Google Drive\\PROG\\PYTHON\\Notes\\windows.png','wb')
    conv(fin,fout)
    print ('Converted to png')




