import tkinter
from tkinter import *
from PIL import ImageTk, Image

# create a root widget
root = Tk()

root.title("Basic window")
root.configure(background='grey')
root.minsize(200,250)
root.maxsize(1000,1000)
root.geometry("300x300+50+50")

text = Label(root, text="movies")
text.pack()

text2 = Label(root, text="- AML")
text2.pack()

image1 = Image.open("Posters/Django_Unchained.jpg")
image1 = image1.resize((300, 450))
poster = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=poster)

label1.place(x=200, y=200)

#Label(root, text = 'Position image on button')
Button(root, text = 'hello').pack(side= TOP)

root.mainloop()