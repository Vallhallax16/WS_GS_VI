from Variables_globales.Variables_globales import Var_glob

class Obtener_estado:

    @staticmethod
    def checar_estado(var_glob):

        if(var_glob.get_var() == None):
            return "No iniciado"
        elif(var_glob.get_var() == False):
            return "Web Scrapper trabajando"
        else:
            return "Ha terminado el Web Scrapper"