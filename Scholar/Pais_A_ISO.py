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

        for nomb_pais in lineas_paises:
            if(nomb_pais.replace('\n','') != N_pais):
                index += 1
            else:
                break

        return lineas_iso[index].replace('\n','')