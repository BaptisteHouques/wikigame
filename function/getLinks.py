# Fonction de récupérations des liens intéressants de la page entrée en paramètre
# Renvoi une liste de liens
def getLinks(page):
    listLiens = []
    liens = page.find('div', {'id': 'bodyContent'}).find_all('a', href=True) # Récupère tous les liens valide de la partie principale de la page wiki

    # Triage des liens
    for reponse in liens:
        if reponse.text and not reponse.find(class_='new'): # Vérifie si le lien possède un texte et si le lien mène vers une page complétée
            if reponse.text != '': # Vérifie que le texte n'est pas vide
                if '/wiki/' in reponse['href'] and not any(x in reponse['href'] for x in ['/wiki/Wikipédia', '/wiki/Aide:', '/wiki/Cat%C3%A9gorie:', 'www.wikidata.org', 'en.wikipedia.org']): # Vérifie que le lien redirige bien vers une page wikipedia normale
                    listLiens.append(reponse)
    
    return listLiens