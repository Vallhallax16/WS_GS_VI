from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import re
import Scholar

#s = requests.Session()

MAXRESULTADOS = 2359
#MAXRESULTADOS = 5
MAX_SEGUNDOS = 3

#def fetch(url,data = None):
#    if data is None:
#        return s.get(url).content
#    else:
#        return s.post(url, data = data).content

def findSrc(string):
    i=0
    for x in string:
        if string[i]=='s':
            if string[i+1]=='r':
                if string[i+2]=='c':
                    if string[i+3]=='=':
                        if string[i+4]=='"':
                            j=i+5
                            src = ""
                            while string[j]!='"':
                                src = src + string[j]
                                j = j+1
                            break
        i = i+1
    return src

def getLinksGS():
    links = list()
    nombres = list()
    imagenes = list()
    url = 'https://scholar.google.com/citations?view_op=search_authors&mauthors=la+salle&hl=es&oi=drw'
    driver = webdriver.Firefox()
    driver.get(url)
    cont = 0

    while(True):
        driver.implicitly_wait(MAX_SEGUNDOS)
        html = BeautifulSoup(driver.page_source, 'lxml')

        html.findAll()
        profiles = html.findAll('div', attrs={'class': "gsc_1usr"})

        for profile in profiles:
            link = profile.findAll('a')
            nombre = profile.find('h3',attrs={'class':"gs_ai_name"})
            links.append("https://scholar.google.com" + link[0].get('href'))
            nombres.append(nombre.text)

            picture = profile.find('span',attrs={'class':'gs_rimg gs_pp_sm'})
            picture = str(picture)
            imagen = findSrc(picture)
            imagen = imagen.replace("&amp;","&")
            imagenes.append(imagen)

            cont = cont + 1
        if(cont>=MAXRESULTADOS):
            break
        try:
            driver.find_element(By.CSS_SELECTOR,'button.gs_btnPR.gs_in_ib.gs_btn_half.gs_btn_lsb.gs_btn_srt.gsc_pgn_pnx').click()
        except:
            break
    
    driver.close()
    return links,nombres,imagenes

def getLinksS():
    links = list()
    url = 'https://goo.gl/nSu8f3'
    driver = webdriver.Firefox()
    driver.get(url)

    while(True):
        driver.implicitly_wait(MAX_SEGUNDOS)
        html = BeautifulSoup(driver.page_source, 'lxml')

        profiles = html.find('div',attrs={'id':"srchResultsList"})
        profiles2 = profiles.findAll('li')

        for profile in profiles2:
            temp = profile.find('div',attrs={'class':'dataCol2'})
            link = temp.find('a')
            try:
                #36 11 
                #"/author/submit/profile.uri?authorId=55489701300&amp;origin=AuthorNamesList&amp;offset=1&amp;authorSt1=Universidad+de+la+Salle+Bajio&amp;authorSt2=&amp;resultsKey="
                linkCompleto = link.get('href')
                profileID = ""
                profileID = profileID + linkCompleto[36]
                profileID = profileID + linkCompleto[37]
                profileID = profileID + linkCompleto[38]
                profileID = profileID + linkCompleto[39]
                profileID = profileID + linkCompleto[40]
                profileID = profileID + linkCompleto[41]
                profileID = profileID + linkCompleto[42]
                profileID = profileID + linkCompleto[43]
                profileID = profileID + linkCompleto[44]
                profileID = profileID + linkCompleto[45]
                profileID = profileID + linkCompleto[46]
                profileID = profileID + linkCompleto[47]

                links.append("https://scopus.com/authid/detail.uri?authorId=" + profileID)
            except:
                print("No link found")
        try:
            driver.find_element_by_css_selector('a.jsEnabled.nextBtn.cursorPointer').click()
        except:
            break

    driver.close()

    url = 'https://goo.gl/MYSJdb'
    driver = webdriver.Firefox()
    driver.get(url)

    driver.implicitly_wait(MAX_SEGUNDOS)
    html = BeautifulSoup(driver.page_source, 'lxml')

    profiles = html.find('div',attrs={'id':"srchResultsList"})
    profiles2 = profiles.findAll('li')

    for profile in profiles2:
        temp = profile.find('div',attrs={'class':'dataCol2'})
        link = temp.find('a')
        try:
            linkCompleto = link.get('href')
            profileID = ""
            profileID = profileID + linkCompleto[36]
            profileID = profileID + linkCompleto[37]
            profileID = profileID + linkCompleto[38]
            profileID = profileID + linkCompleto[39]
            profileID = profileID + linkCompleto[40]
            profileID = profileID + linkCompleto[41]
            profileID = profileID + linkCompleto[42]
            profileID = profileID + linkCompleto[43]
            profileID = profileID + linkCompleto[44]
            profileID = profileID + linkCompleto[45]
            profileID = profileID + linkCompleto[46]
            profileID = profileID + linkCompleto[47]

            links.append("https://scopus.com/authid/detail.uri?authorId=" + profileID)
        except:
            print("No link found")

    driver.close()        
    return links

def getLinksRG():
    links = list()
    url = 'https://www.researchgate.net/search/authors?q=la%2Bsalle'
    driver = webdriver.Firefox()
    driver.get(url)

    while(True):
        driver.implicitly_wait(MAX_SEGUNDOS)
        html = BeautifulSoup(driver.page_source, 'lxml')

        profiles = html.findAll('div',attrs={'class':"account-container"})

        for profile in profiles:
            link = profile.findAll('a')
            try:
                actualLink = link[0].get('href')
                actualLink = actualLink[:-84]
                print(actualLink)
                links.append(actualLink)
            except:
                print("No link found")
        try:
            driver.find_element_by_css_selector('a.navi-next pager-link').click()
        except:
            break

    driver.close()
    return links