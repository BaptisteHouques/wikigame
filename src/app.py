from tkinter import *
from tkinter import messagebox
from function.search import search
from function.getLinks import getLinks
from function.getPageTitle import getPageTitle

class WikiGame:
    
    def __init__(self, parent):
        self.properties(parent)
        self.widgets(parent)

    def properties(self, app):
        self.maxLinks = 15 # Nombre maximum de liens affichés
        self.historicalList = []
        self.stopCountdown = False

    def widgets(self, app):
        self.label_title = Label(app, text="WikiGame", font=40).pack()
        # Création des labels des pages cible et actuelle
        self.label_cible = Label(app)
        self.label_cible.pack()
        self.label_actuel = Label(app)
        self.label_actuel.pack()
        self.label_tour = Label(app, text="Tour : 0")
        self.label_tour.pack()
        self.timeString = StringVar()
        self.countdownBox = Label(app, textvariable=self.timeString)
        self.countdownBox.pack()
        self.firstLine = Label(app, text="-"*30).pack()
        self.frame_links = Frame(app)
        self.frame_links.pack()
    
    # Fonction permettant le changement de la page actuelle et l'affichage des nouveaux liens
    def changeUrl(self, url):
        pageActuelle = search(url)
        actuel = getPageTitle(pageActuelle)
        self.historicalList.append(actuel.text)

        # Vérification par le titre de la page nouvellement chargée et celui de la page précédente si l'utilisateur a gagné
        if actuel == cible:
            self.stopCountdown = True
            # Suppression de tous les liens dans l'affichage actuel
            for child in self.frame_links.winfo_children():
                child.destroy()
            self.label_actuel.config(text="Actuellement : " + actuel.text) # Modification du label affichant la page actuelle
            # Affichage du message de félicitation
            Label(self.frame_links, text="Vous avez gagné en "+self.label_tour.cget("text")[-1]+" tours! Félicitations!").pack()
            Button(self.frame_links, text="Afficher l'historique", command=self.showHistoricalList).pack()
        else:
            listLiens = getLinks(pageActuelle)
            self.label_actuel.config(text="Actuellement : " + actuel.text) # Modification du label affichant la page actuelle
            numberTour = self.label_tour.cget("text")[-1] # Récupération de la dernière valeur du texte du label affichant le nombre de tours actuel
            numberTour = int(numberTour)+1
            self.label_tour.config(text="Tour : "+str(numberTour)) # Modification du label affichant le nombre de tour actuel
            self.showLinks(listLiens, 0)

    # Fonction affichant les liens entrés en paramètre à partir de la valeur renseignée jusqu'à la valeur max (ou le dernier lien de la liste)
    def showLinks(self, listLiens, start):
        # Suppression de tous les liens dans l'affichage actuel
        for child in self.frame_links.winfo_children():
            child.destroy()
        # Vérification que la valeur de commencement n'est pas plus élevée que la taille de la liste
        if len(listLiens) < start:
            print("Valeur d'entrée trop élevée")
        else:
            compt = 0 # Compte le nombre d'itération dans la boucle for
            # Affichage des liens un à un
            for lien in listLiens[start:]: # Commence à la valeur renseignée
                # Création d'un label pour le lien et ajout d'un 0 devant les 9 premiers caractères
                label = Label(self.frame_links, cursor="hand1", text="{} - {}".format('0'+str(compt+1+start) if start < 9 and compt < 9 else compt+1+start, lien.text))
                label.pack()
                # Liaison d'un évènement click sur le label permettant le changement de page en renseignant l'url du lien cliqué
                label.bind("<Button-1>", lambda event, link=lien['href']: self.changeUrl(link))
                compt += 1
                # Affiche les options de pagination quand 20 liens (ou les derniers liens de la liste) ont été affichés
                if compt == self.maxLinks or compt >= len(listLiens)-start:
                    Label(self.frame_links, text="-"*30).pack()
                    if len(listLiens) > compt and compt < len(listLiens)-start:
                        label_plus = Label(self.frame_links, cursor="hand1", text="Page suivante →")
                        label_plus.pack()
                        # Liaison d'un évènement click sur le label permettant l'affichage des liens suivants
                        label_plus.bind("<Button-1>", lambda e:self.changePage("+", listLiens, start))
                    if start > self.maxLinks-1:
                        label_moins = Label(self.frame_links, cursor="hand1", text="← Page précédente")
                        label_moins.pack()
                        # Liaison d'un évènement click sur le label permettant l'affichage des liens précédents
                        label_moins.bind("<Button-1>", lambda e:self.changePage("-", listLiens, start))
                    break

    def showHistoricalList(self):
        for item in self.historicalList:
            Label(self.frame_links, text=item).pack()


    # Fonction permettant l'affichage des liens suivants ou précédents de la liste renseignée
    def changePage(self, value, listLiens, start):
        if value == "+":
            start += self.maxLinks # Augmentation de la valeur de commencement suivant la valeur maximum d'affichage des liens
            self.showLinks(listLiens, start)
        else:
            start -= self.maxLinks # Diminution de la valeur de commencement suivant la valeur maximum d'affichage des liens
            self.showLinks(listLiens, start)

    def countdown(self, n=6000):
        n -= 1
        if not self.stopCountdown and n > 0:
            self.timeString.set("Compteur : {}".format(n))
            window.after(1000, self.countdown, n)
        if n <= 0 and not self.stopCountdown:
            messagebox.showinfo("Compteur", "Temps imparti dépassé! \n Merci d'avoir joué")
            window.destroy()

# Création de la fenêtre
window = Tk()
window.title("Wikigame")
window.geometry("800x530")
window.minsize(600,400)
window.iconbitmap("src/ressources/logo.ico")

wiki = WikiGame(window)

# Génération page cible
pageCible = search()
cible = getPageTitle(pageCible)

wiki.label_cible.config(text="Cible : "+cible.text)


# Création boite des liens & affichage de la page actuelle et de ses liens
wiki.changeUrl("/wiki/Sp%C3%A9cial:Page_au_hasard")
        
wiki.countdown()

window.mainloop()
