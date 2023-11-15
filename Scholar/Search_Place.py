import re

class Search_place:
    @staticmethod
    def Construct_URL(Lugar):
        Lugar = str(Lugar)
        Lugar = re.sub(",","",Lugar)
        pedazos_Lugar = Lugar.split(" ")

        url = "https://www.google.com/maps/search/"

        for i in range(pedazos_Lugar.__len__()):
            url += pedazos_Lugar[i]

            if(i + 1 != pedazos_Lugar.__len__()):
                url += "+"
            else:
                url += "/"

        return url