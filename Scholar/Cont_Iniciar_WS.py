from Cont_Actualizador import Actualizar
from mainfunc import Iniciar_WS_GS

class Inicializar_WS:

    @staticmethod
    def Iniciar_ejecucion(var_glob,ventana,txt_estado_Actual, marco_lbl_estado_actual):
        var_glob.set_var(False)

        txt_estado_Actual = Actualizar.actualizar_etiqueta(var_glob,txt_estado_Actual,marco_lbl_estado_actual)
        Actualizar.actualizar_ventana(ventana)

        terminado = Iniciar_WS_GS()

        var_glob.set_var(terminado)

        Actualizar.actualizar_etiqueta(var_glob, txt_estado_Actual, marco_lbl_estado_actual)
        Actualizar.actualizar_ventana(ventana)