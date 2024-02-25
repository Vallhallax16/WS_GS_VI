class Definir_color_x_edo:

    @staticmethod
    def establecer_color(var_glob):

        if(var_glob.get_var() == None):
            return "red"
        elif(var_glob.get_var() == False):
            return "orange"
        else:
            return "green"