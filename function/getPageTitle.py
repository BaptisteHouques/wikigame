def getPageTitle(page):
    title = page.find('h1', {"id": "firstHeading"})
    if not title: # Si l'élément recherché correspondant au titre de la page n'existe pas, on cherche son remplaçant
        title = page.find('span', {"class": "mw-page-title-main"})
        title = title.find('i')

    return title