import openpyxl

class Excel_GS:

    @staticmethod
    def Contar_por_pais():
        nombre_archivo = "dataGS.csv"

        archivo = openpyxl.load_workbook(nombre_archivo)

        lista_hojas = archivo.get_sheet_names()