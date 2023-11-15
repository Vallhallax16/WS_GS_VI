from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import requests

from Link_In_Text import Link_In_Text
from PaisISO import PaisISO
from Validar_codigo_ISO import Validar_codigo_ISO
from Search_Place import Search_place

s = requests.Session()

def fetch(url, data=None):
    if data is None:
        return s.get(url).content
    else:
        return s.post(url, data=data).content


def GetInfoGS(url):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(30)

    html = BeautifulSoup(driver.page_source, 'lxml')

    driver.close()

    tabla = html.find('table', attrs={'id': "gsc_rsb_st"})
    trs = tabla.findAll('tr')

    perfil = html.find('div', attrs={'id': "gsc_prf_i"})
    prs = perfil.findAll('div')

    text_link = list()
    palabras_clave = ""

    for div in prs:
        a = div.findAll('a')
        link_in_text = Link_In_Text()

        if (list(a).__len__() > 1):
            max_index = list(a).__len__()
            index = 0

            list_a = list(a)
            for link in list_a:
                #
                extracted_text = link_in_text.Extract_Text(str(link))
                if (index == 0 or (index + 1) == max_index):
                    palabras_clave += extracted_text
                else:
                    palabras_clave += ", " + extracted_text

                index += 1
            #
            text_link.append(palabras_clave)
        else:
            extracted_text = link_in_text.Extract_Text(str(a))
            text_link.append(extracted_text)

    cont = 1
    for tr in trs:
        if tr.find('td') != None:
            numeros = tr.findAll('td', attrs={'class': 'gsc_rsb_std'})
            # print(numeros[0].text)
            if cont == 1:
                citas = numeros[0].text
            elif cont == 2:
                indiceh = numeros[0].text
            elif cont == 3:
                indicei10 = numeros[0].text
            cont += 1
    cont = 0
    for pr in prs:
        if cont == 2:
            # universidad = pr.text
            if (text_link[cont] != None):
                universidad = text_link[cont]
            else:
                universidad = "No data"
        elif cont == 3:
            correo = pr.text
        elif cont == 4:
            palabras = palabras_clave
        cont += 1

    pais_iso = PaisISO()
    lista_isos = PaisISO.Get_ISO_Pais(correo)
    pais = Validar_codigo_ISO.Validar_ISO(lista_isos)

    if(pais == None):
        if(universidad != "No data"):
            driver = webdriver.Firefox()
            url = Search_place.Construct_URL(universidad)
            driver.get(url)
            driver.implicitly_wait(30)

            html = BeautifulSoup(driver.page_source, 'lxml')
            print(html.prettify())

            driver.close()

            pais = "No data"

            """
            BUSCAR PLUS CODE
            </span>
                         <span class="EmLCAe fontBodyMedium" jstcache="180">
                          <span jsinstance="*0" jstcache="184">
                           Carrer de Claravall, Barcelona, España
                          </span>
            """
        else:
            pais = "No data"

    return citas.strip(), indiceh.strip(), indicei10.strip(), universidad.strip(), correo.strip(), palabras.strip(), pais.strip()


def GetInfoS(url):
    html = BeautifulSoup(fetch(url), 'html.parser')

    nombre = html.find('h2', attrs={'class': 'wordBreakWord'})
    nom = nombre.text
    nom = nom.strip()
    try:
        affiliation = html.find('div', attrs={'class': 'authAffilcityCounty'})
        universidad = affiliation.find('span', attrs={'class': 'anchorText'})
        uni = universidad.text
        uni = uni.strip()
    except:
        cit = "none"
    try:
        author_id = html.find('div', attrs={'class': 'authId'})
        aid = author_id.text
        aid = aid[11:]
        aid = aid.strip()
    except:
        cit = "none"
    try:
        citas = html.find('span', attrs={'id': 'totalCiteCount'})
        cit = citas.text
        cit = cit.strip()
    except:
        cit = "none"
    try:
        indiceh = html.find('div', attrs={'class': 'panel-body'})
        ind = indiceh.text
        ind = ind.strip()
    except:
        ind = "none"
    try:
        documentos = html.find('span', attrs={'fontLarge pull-left'})
        doc = documentos.text
        doc = doc.strip()
    except:
        doc = "none"

    return nom, uni, aid, cit, ind, doc


def GetInfoRG(url):
    html = BeautifulSoup(fetch(url), 'html.parser')

    try:
        nombre = html.find('span', attrs={'class': 'fn'})
        nom = nombre.text
        nom = nom.strip()
    except:
        nom = "none"
    try:
        universidad = html.find('a', attrs={
            'class': 'nova-e-link nova-e-link--color-inherit nova-e-link--theme-bare gtm-institution-item'})
        uni = universidad.text
        uni = uni.strip()
    except:
        uni = "none"
    try:
        posicion = html.find('li', attrs={'class': 'nova-e-list__item nova-v-institution-item__info-section-list-item'})
        pos = posicion.text
        pos = pos.strip()
    except:
        pos = "none"
    try:
        datos = html.findAll('div', attrs={
            'nova-e-text nova-e-text--size-xl nova-e-text--family-sans-serif nova-e-text--spacing-none nova-e-text--color-inherit'})
        try:
            cit = datos[0].text
            cit = cit.strip()
        except:
            cit = "none"

        try:
            lec = datos[1].text
            lec = lec.strip()
        except:
            lec = "none"

        try:
            inv = datos[2].text
            inv = inv.strip()
        except:
            inv = "none"
    except:
        print("no data found")

    return nom, uni, pos, cit, lec, inv