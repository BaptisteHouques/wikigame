from tkinter import *
from tkinter import messagebox
import time

# Fonction de compte à rebour
# Ferme la fenêtre si le temps est dépassé
def countdown(timeString, timeValue, window):
    timeValue
    while timeValue > -1:
        timeString.set("Compteur : {}".format(timeValue))
        window.update()
        time.sleep(1)

        if timeValue == 0:
            messagebox.showinfo("Compteur", "Temps imparti dépassé! \n Merci d'avoir joué")
            window.destroy()

        timeValue -= 1