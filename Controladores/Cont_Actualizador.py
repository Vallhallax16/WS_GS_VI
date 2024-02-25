from Controladores.Cont_Color_estado_web_scrapper import Definir_color_x_edo
from Controladores.Cont_Estado_Web_Scrapper import Obtener_estado

import tkinter

class Actualizar:

    @staticmethod
    def actualizar_ventana(ventana):
        ventana.update()
        ventana.update_idletasks()

    @staticmethod
    def actualizar_etiqueta(var_glob,txt_estado_Actual, marco_lbl_estado_actual):
        txt_estado_Actual.destroy()

        txt_estado_Actual = tkinter.Label(master=marco_lbl_estado_actual, text=Obtener_estado.checar_estado(var_glob),
                                          foreground=Definir_color_x_edo.establecer_color(var_glob))
        txt_estado_Actual.pack(pady=5)

        return txt_estado_Actual
