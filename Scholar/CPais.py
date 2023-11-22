class CPais:
    def __int__(self):
        self.nombre = ""
        self.conteo = 0

    def Set_Nombre(self,nombre):
        self.nombre = nombre

    def Set_Conteo(self, conteo):
        self.conteo = conteo

    def Get_Conteo(self):
        return self.conteo

    def Get_Nombre(self):
        return self.nombre