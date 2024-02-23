class Obtener_estado:

    @staticmethod
    def checar_estado(estado):
        if(estado == None):
            return "No iniciado"
        elif(estado == False):
            return "Web Scrapper trabajando"
        else:
            return "Ha terminado el Web Scrapper"