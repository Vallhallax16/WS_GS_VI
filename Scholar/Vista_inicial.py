"""NOTA IMPORTANTE:
Sería bueno ordenar to.dos estos códigos en una arquitectura MVC o algo similar
los vestigios de ello se pueden ver en las carpetas vistas, controladores y
variables globales, sin embargo Python hace un lio con los directorios y
habría que invertir un poco de tiempo en arreglarlo"""

import tkinter
import math
import ctypes

from Cont_Estado_Web_Scrapper import Obtener_estado
from Cont_Color_estado_web_scrapper import Definir_color_x_edo
from Cont_destruir_ventana import Destruir_ventana
from Cont_Iniciar_WS import Inicializar_WS
from Variables_globales import Var_glob

sistema = ctypes.windll.user32

var_glob = Var_glob()
var_glob.init()

dimension_X = sistema.GetSystemMetrics(0)//3
dimension_Y = sistema.GetSystemMetrics(1)//3

dimensiones = str(dimension_X) + "x" + str(dimension_Y)

ventana = tkinter.Tk()
ventana.geometry(dimensiones)
ventana.title("VI Web Scrapper")

ventana_dim_X = ventana.winfo_x()
ventana_dim_Y = ventana.winfo_y()

ventana.positionfrom

marco_nota = tkinter.Frame(master = ventana)
marco_btn_inicio = tkinter.Frame(master = ventana)
marco_lbl_estado = tkinter.Frame(master = ventana)
marco_lbl_estado_actual = tkinter.Frame(master = ventana)
marco_btn_salir = tkinter.Frame(master = ventana)

nota = tkinter.Label(master=marco_nota, text= "Actualmente solo Google Scholar está disponible en este Web Scrapper")
nota.pack(side= tkinter.BOTTOM);

txt_estado_ws = tkinter.Label(master = marco_lbl_estado, text="Estado del Web Scrapper:");
txt_estado_ws.pack(pady = 10)

txt_estado_Actual = tkinter.Label(master = marco_lbl_estado_actual, text= Obtener_estado.checar_estado(var_glob), foreground= Definir_color_x_edo.establecer_color(var_glob))
txt_estado_Actual.pack(pady = 5)

boton_inicio = tkinter.Button(master=marco_btn_inicio, text="Iniciar Web Scrapper",
                              width= math.floor(ventana_dim_X * 0.025), height= math.floor(ventana_dim_Y * 0.009),
                              command = lambda: Inicializar_WS.Iniciar_ejecucion(var_glob,ventana,txt_estado_Actual, marco_lbl_estado_actual))
boton_inicio.pack(pady = 30)

boton_salir = tkinter.Button(master = marco_btn_salir, text="Salir del Web Scrapper",
                             width= math.floor(ventana_dim_X * 0.03), height= math.floor(ventana_dim_Y * 0.009),
                             command=lambda: Destruir_ventana.cerrar(ventana))
boton_salir.pack(pady = 25)

marco_btn_inicio.pack(fill=tkinter.BOTH)
marco_lbl_estado.pack(fill= tkinter.BOTH)
marco_lbl_estado_actual.pack(fill = tkinter.BOTH)
marco_btn_salir.pack(fill= tkinter.BOTH)
marco_nota.pack(fill=tkinter.BOTH ,side= tkinter.BOTTOM)

ventana.iconbitmap('Icono_WS.ico')
ventana.mainloop()