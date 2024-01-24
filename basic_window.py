from tkinter import *

# create a root widget
root = Tk()

root.title("Basic window")
root.configure(background='grey')
root.minsize(200,250)
root.maxsize(500,500)
root.geometry("300x300+50+50")

text = Label(root, text="movies")
text.pack()

text2 = Label(root, text="- AML")
text2.pack()

root.mainloop()