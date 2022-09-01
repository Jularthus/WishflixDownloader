from requests import *
from download import downloadList
from bs4 import BeautifulSoup
import os 
l = []
baseurl = str(input('Quelle est l\'URL de votre série ? '))
nbrsaisonmax = 0
dico = {}
name = BeautifulSoup(get(baseurl).content,'lxml').find('h1').getText()
name = name[0:-1]

if "strangersthings" in baseurl:
    baseurl = baseurl.replace('strangersthings','strangerthings')

while True:
    a = get(baseurl + f"/ep01s{nbrsaisonmax + 1:02d}.html")
    if a.status_code == 404:
        break
    nbrsaisonmax += 1


for i in range(nbrsaisonmax):
    nbrepmax = 0
    while True:
        b = get(baseurl + f"/ep{nbrepmax + 1:02d}s{i+1:02d}.html")
        if b.status_code == 404:
            break
        nbrepmax += 1
    dico[i+1] = nbrepmax


for saison in dico.keys():
    for ep in range(1, dico[saison]+1):
        soup = BeautifulSoup(get(baseurl + f"/ep{ep:02d}s{saison:02d}.html").content, 'lxml')
        uqload = soup.find('iframe')['src']
        l.append(uqload)
    downloadList(l, name, f"Saison {saison:02d}")
    l = []

