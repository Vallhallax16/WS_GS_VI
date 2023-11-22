import csv

import pandas

class CSV_GS:

    @staticmethod
    def Contar_por_pais():
        nombre_archivo = "dataGS.csv"

        archivo = csv.reader(open(nombre_archivo, 'r', newline=''))

        index = 0
        lista = []

        for renglon in archivo:
            if(index != 0):
                for campo in renglon:
                    print(campo + "\n")

            elif(index == 0):
                index += 1