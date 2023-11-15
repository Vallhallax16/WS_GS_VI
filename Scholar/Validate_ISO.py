class Validate_ISO:

    #Regresa el codigo ISO del país correspondiente, si no lo hay
    #retorna un objeto None
    @staticmethod
    def Validar_ISO(posibles):
        evaluar = str()

        ISOs = list()

        with open("Alpha 2 ISO 3661.txt","r",encoding="UTF-8") as arch_leido:
            ISOs = arch_leido.readlines()

        for iso in posibles:
        #
            for iso_archivo in ISOs:
            #
                if(iso.upper() == iso_archivo):
                #
                    return iso_archivo
                #
            #
        #

        return None