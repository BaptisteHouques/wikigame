import os
from function.search import search
from function.getLinks import getLinks
from function.getPageTitle import getPageTitle
from function.showLinks import showLinks
from function.enterValue import enterValue

# Génération page cible & actuelle
pageCible = search()
cible = getPageTitle(pageCible)
pageActuelle = search()

# Nombre maximum de liens affichés
max = 30

tour = 0
win = False
while not win:
    os.system('cls' if os.name == 'nt' else 'clear')
    if pageActuelle == pageCible:
        win = True
        break

    tour += 1
    intro = "*"*10+"WikiGame **** tour {}\nDépart : Python (langage)\nCible : {}\nActuellement : {}\n".format(tour, cible.text, getPageTitle(pageActuelle).text)
    print(intro)

    listLiens = getLinks(pageActuelle) # Récupération des liens de la page générée

    start = 0 # Où commence la liste
    showLinks(listLiens, start, max) # Affichage des premiers liens de la liste

    userChoice = enterValue() # Demande de renseignement d'une valeur

    # Boucle de pagination
    end = False
    while not end:
        if userChoice == "+":
            # Vérifie si l'utilisateur est à la fin de la liste.
            if start+max > len(listLiens):
                print("Vous êtes à la dernière page")
            else:
                start += max
            print(intro)
            showLinks(listLiens, start, max)
            userChoice = enterValue()
        elif userChoice == "-":
            if start <= max-1:
                print("Vous êtes à la première page")
            else:
                start -= max
            print(intro)
            showLinks(listLiens, start, max)
            userChoice = enterValue()
        # Si un nombre est saisi
        else:
            url = listLiens[userChoice-1]['href'] # Récupération de l'url contenu dans l'objet lien sélectionné par l'utilisateur
            pageActuelle = search(url)
            end = True

print("Félicitation!!! Vous avez trouvé la page cible en {} tours!".format(tour))

