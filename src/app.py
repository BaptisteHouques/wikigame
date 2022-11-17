from tkinter import *
from function.search import search
from function.getLinks import getLinks
from function.getPageTitle import getPageTitle
from function.showLinks import showLinks
from function.changeUrl import changeUrl

# Création de la fenêtre
window = Tk()
window.title("Wikigame")
window.geometry("800x550")
window.minsize(600,400)
window.iconbitmap("src/ressources/logo.ico")

label_title = Label(window, text="WikiGame", font=40).pack()


# Génération page cible
pageCible = search()
cible = getPageTitle(pageCible)

# Création des labels des pages cible et actuelle
label_cible = Label(window, text="Cible : "+cible.text).pack()
label_actuel = Label(window)
label_actuel.pack()

label_tour = Label(window, text="Tour : 0")
label_tour.pack()

# Nombre maximum de liens affichés
max = 20

# Création boite des liens & affichage de la page actuelle et de ses liens
frame_links = Frame(window)
changeUrl("/wiki/Sp%C3%A9cial:Page_au_hasard", label_actuel, frame_links, label_tour, max, cible)
frame_links.pack()

window.mainloop()
