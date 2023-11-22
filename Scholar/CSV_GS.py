import csv
from CPais import CPais

class CSV_GS:

    @staticmethod
    def Contar_por_pais():
    #
        nombre_archivo = "dataGS.csv"

        archivo = csv.reader(open(nombre_archivo, 'r', newline=''))

        is_header = True
        lista = list()

        for renglon in archivo:
        #
            if(is_header == False):
            #
                campo_pais = renglon[renglon.__len__() - 1]

                if(campo_pais != "No data"):
                #
                    if(lista.__len__() == 0):
                    #
                        pais = CPais()
                        pais.nombre = campo_pais
                        pais.conteo = 1

                        lista.append(pais)
                    #
                    else:
                    #
                        CSV_GS._Check_list(lista,campo_pais)
                    #
                #

            #
            elif(is_header == True):
            #
                is_header = False
            #
        #
        CSV_GS._Create_stats(lista)
    #
    @staticmethod
    def _Check_list(lista,pais):
    #
        insertado = False

        for c_pais in lista:
        #
            if(c_pais.nombre == pais):
            #
                c_pais.Ipp_Conteo()
                insertado = True
            #
        #

        if(insertado == False):
        #
            cn_pais = CPais()
            cn_pais.nombre = pais
            cn_pais.conteo = 1

            lista.append(cn_pais)
        #
    #

    @staticmethod
    def _Create_stats(lista):
    #
        l = list()
        nombre_archivo = "dataGS_stats.csv"
        nombre_columnas = ["Pais (ISO 3661)","No. Investigadores"]

        archivo_stats = csv.writer(open(nombre_archivo,"w",newline=''))

        archivo_stats.writerow(nombre_columnas)

        for c_pais in lista:
            archivo_stats.writerow([c_pais.nombre,c_pais.conteo])
    #