# Fonction affichant les liens entrée en paramètre à partir de la valeur renseignée jusqu'à la valeur max (ou le dernier lien de la liste)
def showLinks(listLiens, start, max):
    if len(listLiens) < start: # Vérifie que la valeur de commencement n'est pas plus élevée que la taille de la liste
        print("Valeur d'entrée trop élevée")
    else:
        compt = 0 # Compte le nombre d'itération dans la boucle for
        for lien in listLiens[start:]: # Commence à la valeur renseignée
            print("{} - {}".format('0'+str(compt+1+start) if start < 9 and compt < 9 else compt+1+start, lien.text)) # Affiche un 0 devant les 9 premiers caractères
            compt += 1
            # Affiche les options de pagination quand 20 liens (ou les derniers liens de la liste) ont été affichés
            if compt == max or compt >= len(listLiens)-start:
                if len(listLiens) > compt and compt < len(listLiens)-start:
                    print("{} - {}".format('+', 'Page suivante'))
                if start > max-1:
                    print("{} - {}".format('-', 'Page précédente'))
                break