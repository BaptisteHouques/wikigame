from urllib import response
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Fonction de recherche de page Wikipédia aléatoire
# Renvoie les données de la page
def search(url=None):
    if not url:
        url="https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"
    else:
        url="https://fr.wikipedia.org"+url
    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup