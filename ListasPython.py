list=[]
def captura():
    for i in range(10):
        x=0
        while x<1 or x>1000:
            msg="Indica el valor de la posición ["+str(i)+"] : "
            x=int(input(msg))
            if x<1 or x>1000:
                input("Valor fuera de rango entre 1 y 1000")
        list.append(x)
        

        
def promedio():
    suma=0
    for i in list:
        suma+=i
    prom=suma/10
    print("El promedio es : ",prom)
    input("Pausa")

def list_secuencia():
    for i in list:
        print(i)
    input("Pausa")

def valor_posicion():
    pos=-1
    while pos<0 or pos>9:
        pos=int(input("Indica la posición deseada : "))
        if pos<0 or pos>9:
            input("Error, valor fuera de rango entre 0 y 9 ")
    print("El valor posición",pos,"es : ",list[pos])
    input("Pausa")
    
    
def menu():
    op="x"
    while op!="g":
        print("\n"*45)
        print("a) Promedio")
        print("b) Mayor de la lista")
        print("c) Menor de la lista")
        print("d) Lista en secuencia")
        print("e) Lista inversa")
        print("f) Valor de una posición")
        print("g) Terminar")
        op=input("Indica la operación deseada : ")
        if op<"a" or op>"g":
            input("Error, opción fuera de rango entre 'a' y 'g' ")
        else:
            if op=="a":
                promedio()
            if op=="b":
                print("El mayor de la lista es : ", max(list))
                input("Pausa")
            if op=="c":
                print("El menor de la lista es : ", min(list))
                input("Pausa")
            if op=="d":
                list_secuencia()
            if op=="e":
                list.reverse()
                list_secuencia()
                list.reverse()
            if op=="f":
                valor_posicion()
          

#Main

captura()
menu()
