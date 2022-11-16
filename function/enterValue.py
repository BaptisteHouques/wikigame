# Fonction demandant d'entrer une valeur et vérifiant qu'elle soit correcte
# Retourn la valeur entrée
def enterValue():
    choice = ''
    while True:
        choice = input("Sélectionner un nombre ou bien la page suivante/précédente à l'aide des symboles '+' et '-' : ")
        if choice in ("+", "-"):
            return choice
        if choice.isdigit():
            return int(choice)
        print("La valeur entrée n'est pas bonne")