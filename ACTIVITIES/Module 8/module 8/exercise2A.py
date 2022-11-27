
from tkinter import *

app = Tk()
app.title("GUI Example")
app.geometry('200x100')
def changeLabelText():
    print("The current text is", l1['text'])
    l1['text'] = "Changed Text"
b1 = Button(app, text="Change Text", command=changeLabelText)

l1 = Label(app, text="Text")
l1.pack(side='bottom')
b1.pack(side='bottom')


app.mainloop()
