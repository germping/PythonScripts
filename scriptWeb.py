# Script para descargar de una pagina

import urllib2
from bs4 import BeautifulSoup
import requests

urlPrincipal= 'http://9092.ultratv100.com:9090/karaokes/'

def descargarArtista(artista):
    # se comprueba que haya datos del artista
    urlArtista=urlPrincipal+artista
    #print(urlArtista)
    try:
        response = urllib2.urlopen(urlArtista)
        html = response.read()
        if html is None:
            print "Artista no encontrado None"
        else:
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a'):
                    try:
                        url = urlArtista+"/"+link.get('href')
                        print("url "+url)
                        r = requests.get(url)
                        print("seguimiento")
                        with open('/home/german/Python/'+link.get('href'), 'wb') as f:
                            f.write(r.content)
                    except:
                        print("url no encontrada")

    except:
        print "Artista no encontrado except"

descargarArtista("METALLICA")

response = urllib2.urlopen(urlPrincipal)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
