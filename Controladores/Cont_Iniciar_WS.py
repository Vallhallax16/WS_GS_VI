import tkinter

from Controladores.Cont_Actualizador import Actualizar

class Inicializar_WS:

    @staticmethod
    def Iniciar_ejecucion(var_glob,ventana,txt_estado_Actual, marco_lbl_estado_actual):
        var_glob.set_var(False)

        txt_estado_Actual = Actualizar.actualizar_etiqueta(var_glob,txt_estado_Actual,marco_lbl_estado_actual)
        Actualizar.actualizar_ventana(ventana)

        var_glob.set_var(True)

        Actualizar.actualizar_etiqueta(var_glob, txt_estado_Actual, marco_lbl_estado_actual)
        Actualizar.actualizar_ventana(ventana)