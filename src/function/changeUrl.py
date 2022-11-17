from tkinter import *
from function.search import search
from function.getPageTitle import getPageTitle
from function.getLinks import getLinks
from function.showLinks import showLinks

# Fonction permettant le changement de la page actuelle et l'affichage des nouveaux liens
def changeUrl(url, label_actuel, frame_links, label_tour, max, cible):
    pageActuelle = search(url)
    actuel = getPageTitle(pageActuelle)
    print("")
    # Vérification par le titre de la page nouvellement chargée et celui de la page précédente si l'utilisateur a gagné
    if actuel == cible:
        # Suppression de tous les liens dans l'affichage actuel
        for child in frame_links.winfo_children():
            child.destroy()
        label_actuel.config(text="Actuellement : " + actuel.text) # Modification du label affichant la page actuelle
        # Affichage du message de félicitation
        Label(frame_links, text="Vous avez gagné en "+label_tour.cget("text")[-1]+" tours! Félicitations!").pack()
    else:
        listLiens = getLinks(pageActuelle)
        label_actuel.config(text="Actuellement : " + actuel.text) # Modification du label affichant la page actuelle
        numberTour = label_tour.cget("text")[-1] # Récupération de la dernière valeur du texte du label affichant le nombre de tours actuel
        numberTour = int(numberTour)+1
        label_tour.config(text="Tour : "+str(numberTour)) # Modification du label affichant le nombre de tour actuel
        showLinks(listLiens, 0, max, frame_links, label_actuel, label_tour, cible)
