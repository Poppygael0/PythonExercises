class autos():
    def __init__(self="",Marca="",Submarca="",Modelo="",motor="",color=""):
        self.__Marca=Marca #ENCAPSULAMIENTO
        self.Submarca=Submarca
        self.Modelo=Modelo
        self.Motor=motor
        self.color=color
    
    def __del__(self):
        pass
    
    def despliega(self):
        print("Marca    : ",self.__Marca)
        print("Submarca : ",self.Submarca)
        print("Modelo   : ",self.Modelo)
        print("Motor    : ",self.Motor)
        print("Color    : ",self.color)
#Termina clase auto

#Inicia principal
print("-"*45)

a1=autos("Nissan","March",2018,1600,"Azul")
a1.despliega()

print("-"*45)

a2=autos("Nissan","Versa",2020,1600,"Rojo")
a2.despliega()

print("-"*45)

a1.Marca="Ford"
a1.despliega() #SE MANDA A LLAMAR EL CAMBIO PERO NO SE PUEDE MODIFICAR FUERA DE LA CLASE