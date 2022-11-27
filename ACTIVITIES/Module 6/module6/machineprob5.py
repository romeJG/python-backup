# # Number 1
# import os
# from PIL import Image
# files = os.listdir()
# print(files)
# try:
#     des = input('Enter the name of file and the extension: ')
#     im = Image.open(des)
#     print('SAVE IT AS: ')
#     print('1.) jpg')
#     print('2.) png')
#     print('3.) pdf')
#     choice = int(input('Enter choice: '))
#     if choice == 1:
#         rgb_im = im.convert('RGB')
#         rgb_im.save('new_jpeg_image.jpg')
#         print('Conversion is Sucessful.')
#     elif choice == 2:
#         rgb_im = im.convert('RGB')
#         rgb_im.save('new_png_image.png')
#         print('Conversion is Sucessful.')
#     elif choice == 3:
#         rgb_im = im.convert('RGB')
#         rgb_im.save('new_pdf_image.pdf')
#         print('Conversion is Sucessful.')
#     else:
#         print('Not in the choices try again.')
# except FileNotFoundError:
#     print('File was not found.')

# # Number 2
# import os
# from PIL import Image
# files = os.listdir()
# print(files)
# file_entered = input("Enter the name of File: ")
# img = Image.open(file_entered)
# pix_val = list(img.getdata())
# print(pix_val)
