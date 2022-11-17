from tkinter import *

# Fonction affichant les liens entrés en paramètre à partir de la valeur renseignée jusqu'à la valeur max (ou le dernier lien de la liste)
def showLinks(listLiens, start, max, frame_links, label_actuel, label_tour, cible):
    # Suppression de tous les liens dans l'affichage actuel
    for child in frame_links.winfo_children():
        child.destroy()
    # Vérification que la valeur de commencement n'est pas plus élevée que la taille de la liste
    if len(listLiens) < start:
        print("Valeur d'entrée trop élevée")
    else:
        compt = 0 # Compte le nombre d'itération dans la boucle for
        # Affichage des liens un à un
        for lien in listLiens[start:]: # Commence à la valeur renseignée
            # Création d'un label pour le lien et ajout d'un 0 devant les 9 premiers caractères
            label = Label(frame_links, cursor="hand1", text="{} - {}".format('0'+str(compt+1+start) if start < 9 and compt < 9 else compt+1+start, lien.text))
            label.pack()
            # Liaison d'un évènement click sur le label permettant le changement de page en renseignant l'url du lien cliqué
            label.bind("<Button-1>", lambda event, link=lien['href']: changeUrl(link, label_actuel, frame_links, label_tour, max, cible))
            compt += 1
            # Affiche les options de pagination quand 20 liens (ou les derniers liens de la liste) ont été affichés
            if compt == max or compt >= len(listLiens)-start:
                if len(listLiens) > compt and compt < len(listLiens)-start:
                    label_plus = Label(frame_links, cursor="hand1", text="Page suivante")
                    label_plus.pack()
                    # Liaison d'un évènement click sur le label permettant l'affichage des liens suivants
                    label_plus.bind("<Button-1>", lambda e:changePage("+", listLiens, start, max, frame_links, label_actuel, label_tour, cible))
                if start > max-1:
                    label_moins = Label(frame_links, cursor="hand1", text="Page précédente")
                    label_moins.pack()
                    # Liaison d'un évènement click sur le label permettant l'affichage des liens précédents
                    label_moins.bind("<Button-1>", lambda e:changePage("-", listLiens, start, max, frame_links, label_actuel, label_tour, cible))
                break

# Importation en bas de page pour permettre une importation circulaire
from function.changeUrl import changeUrl
from function.changePage import changePage
