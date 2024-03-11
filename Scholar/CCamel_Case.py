import re


class Formato_camello:
#
    #Formatea en camello por defecto
    def Formatear(self, cadena):
    #
        cadena = re.sub("·", "", cadena)
        cadena = cadena.strip()
        cadena = cadena.lower()
        cadena_pedazos = cadena.split(' ')
        cadena_completa = ""

        for i in range(cadena_pedazos.__len__()):
        #
            temp_cadena = cadena_pedazos[i]

            if(temp_cadena.__len__() >= 2):
            #
                temp_cadena, es_compuesto = self.Incluye_guion(temp_cadena)

                if(not es_compuesto):
                #
                    cadena_completa += ''.join([temp_cadena[0].upper(), temp_cadena[1:]])
                    cadena_completa += " "
                #
                else:
                #
                    cadena_completa += temp_cadena
                    cadena_completa += " "
                #
            #
            elif (cadena.__len__() == 1):
            #
                cadena_completa += temp_cadena[0].upper()
                cadena_completa += " "
            #
        #

        return cadena_completa
    #

    #Formatea para que solo la inicial sea mayúscula
    def Formateo_escaso(self, cadena):
        cadena = re.sub("·", "", cadena)
        cadena = cadena.strip()
        cadena = cadena.lower()

        if(cadena.__len__() >= 2):
            return "".join( [ cadena[0].upper(), cadena[1:] ] )
        elif(cadena.__len__() == 1):
            return cadena[0].upper()
        else:
            return cadena

    def Incluye_guion(self, cadena):
    #
        if(cadena.__contains__("-")):
        #
            texto = str()
            decompuesto = cadena.split("-")

            for i in range(decompuesto.__len__()):
            #
                texto += self.Formateo_escaso(decompuesto[i])

                if((i+1) != decompuesto.__len__()):
                #
                    texto += "-"
                #
            #

            return texto, True
        #
        else:
        #
            return cadena, False
        #
    #
#