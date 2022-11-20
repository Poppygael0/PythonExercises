class bebe():
    def muestra(self):
        print("Tengo 1 o menos años de edad")

class menor():
    def muestra(self):
        print("Tengo entre 1 o 17 años de edad")

class mayor():
    def muestra(self):
        print("Tengo 18 o más años de edad")

p1=bebe()
p1.muestra()

p2=menor()
p2.muestra()

p1=mayor()
p1.muestra()  #POLIMORFISMO : ES EL MISMO OBJETO CON DIFERENTE FORMA

