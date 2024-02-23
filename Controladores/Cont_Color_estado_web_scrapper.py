class Definir_color_x_edo:

    @staticmethod
    def establecer_color(estado):
        if(estado == None):
            return "red"
        elif(estado == False):
            return "yellow"
        else:
            return "green"