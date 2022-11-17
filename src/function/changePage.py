from tkinter import *
from function.showLinks import showLinks

# Fonction permettant l'affichage des liens suivants ou précédents de la liste renseignée
def changePage(value, listLiens, start, max, frame_links, label_actuel, label_tour, cible):
    if value == "+":
        start += max # Augmentation de la valeur de commencement suivant la valeur maximum d'affichage des liens
        showLinks(listLiens, start, max, frame_links, label_actuel, label_tour, cible)
    else:
        start -= max # Diminution de la valeur de commencement suivant la valeur maximum d'affichage des liens
        showLinks(listLiens, start, max, frame_links, label_actuel, label_tour, cible)