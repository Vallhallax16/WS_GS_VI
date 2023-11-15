import re

class PaisISO:
    #Regresa una lista con los posibles códigos ISO
    @staticmethod
    def Get_ISO_Pais(correo):
    #
        lista_ISO = list()

        correo = re.sub(" - Página principal","",correo)

        separated = correo.split('.')

        for i in range(separated.__len__()):
        #
            if(separated[i].__len__() < 3):
            #
                lista_ISO.append(separated[i])
            #
        #

        return lista_ISO
    #