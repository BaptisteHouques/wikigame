from tkinter import *
from app import *

window = Tk()
window.title("Wikigame")
window.geometry("600x400")
window.minsize(600,400)
window.iconbitmap("src/ressources/logo.ico")

label_title = Label(window, text="WikiGame", font=40)
label_title.pack()

window.mainloop()