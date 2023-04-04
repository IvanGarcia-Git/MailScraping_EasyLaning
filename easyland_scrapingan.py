from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import date
from selenium import webdriver
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import urllib
import requests
import json
import pymysql
import os


def main():

    ################################
    # Conexión a la Base de Datos: #
    ################################

    # connection = pymysql.connect(
    #     host="localhost",
    #     user="root",
    #     password="",
    #     db="easyland"
    # )
    # mycursor = connection.cursor()

    ################################
    # Bucle para scrapear paginas: #
    ################################
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://accounts.clickbank.com/mkplSearchResult.htm?dores=true#' # URL de la pagina a scrapear
    driver.get(url) # Scrapea la pagina definida

    for i in range(317): # Aumentar numero de Range para scrapear mucho mas contenido
        # Estructura del contenido:
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')

        # Scraping de contenido:
        next_link = driver.find_element_by_xpath(".//a[@title='Próxima página']") # Seleccionamos el elemento que permite ir a la siguiente pagina
        next_link.click() # Hacemos click en el elemento
        mails = soup.findAll('span',class_='affiliateSupportEmailContent')

        # Recorrer todo:

        mailtxt = list() # Creamos una lista/array para guardar los correos
        for mail in mails: # Recorremos todos los que hayan en la página actual
            # print(mail.text)
            mailtxt.append(mail.text) # Añadimos el elemento al array
        # print(mailtxt)

        # Guardar correos en un CSV:
        mi_ruta = 'V:\Ivan\Proyectos\EasyLand\lista.csv'
        f = open(mi_ruta, 'a+')

        for i in mailtxt:
            # wr = csv.writer(f,delimiter='')
            # wr.writerow(i)
            if i != '':
                f.write(i)
                f.write('\n')
        f.close()

        # df = pd.DataFrame(mailtxt, columns = ['Correo'])
        # df.to_csv('prueba.csv')
        time.sleep(2)
        
main()
