import img2pdf
pic = open('C:\\Users\\Justine Guillermo\\Google Drive\\PROG\\PYTHON\\Notes\\windows.jfif','rb') #reads the byte code
pdf = open('C:\\Users\\Justine Guillermo\\Google Drive\\PROG\\PYTHON\\Notes\\windows.pdf','wb') #creates a 

pdf.write(img2pdf.convert(pic))
print("Succesfully Converted!")

pic.close()
pdf.close()


# from PIL import Image
# import os
# ImgFile = Image.open("C:\\Users\\Justine Guillermo\\Google Drive\\PROG\\PYTHON\\Notes\\windows.jfif")

# if ImgFile.mode == "RGBA":
#   ImgFile = ImgFile.convert("RGB")

# ImgFile.save("C:\\Users\\Justine Guillermo\\Google Drive\\PROG\\PYTHON\\Notes\\windows.pdf","PDF")

# ImgFile.close()