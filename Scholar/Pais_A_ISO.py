class Pais_A_ISO:

    @staticmethod
    def Get_ISO(N_pais):
        lineas_iso = str()
        lineas_paises = str()

        N_pais = N_pais.replace(' ','')

        with open("Alpha 2 ISO 3661.txt","r",encoding = "utf-8") as txt_ISO:
            lineas_iso = txt_ISO.readlines()

        with open("Nombres de paises ES.txt","r",encoding = "utf-8") as txt_Nombres:
            lineas_paises = txt_Nombres.readlines()

        index = 0
        encontrado = False
        codigo_ISO_obj = str()

        for nomb_pais in lineas_paises:
            if(nomb_pais.replace('\n','') != N_pais):
                index += 1
            else:
                encontrado = True
                break

        if(not encontrado):
        #
            codigo_ISO_obj = "S/D"
        #
        else:
        #
            codigo_ISO_obj = lineas_iso[index].replace('\n','')
        #

        return codigo_ISO_obj