def pide_n():
    n=0
    while n<1 or n>25 or n%2==0:
        n=int(input("Indica el valor de N : "))
        if n<1 or n>25 or n%2==0:
            input("Error, valor fuera de rango entre 1 y 25 o no es impar")
    return n

def horizontal(n):
    print("\n"*45)
    print("*"*n)
    input("Pausa")

def vertical(n):
    print("\n"*45)
    print("*\n"*n)
    input("pausa")

def diagonal1(n):
    print("\n"*45)
    for i in range(n):
        print(" "*i+"*")
    input("Pausa")

def diagonal2(n):
    print("\n"*45)
    for i in range(n-1,-1,-1):
        print(" "*i+"*")
    input("Pausa")

def cruz(n):
    print("\n"*45)
    espa=n//2
    for i in range(n):
        if i==espa:
            print("*"*n)
        else:
            print(" "*espa+"*")
    input("Pausa")

def tache(n):
    print("\n"*45)
    espa=n-2
    for i in range(n//2):
        print(" "*i+"*"+" "*espa+"*")
        espa=espa-2
    print(" "*(n//2)+"*")
    espa=1
    for i in range(n//2-1,-1,-1):
        print(" "*i+"*"+" "*espa+"*")
        espa=espa+2
    input("Pausa")

def escalera1(n):
    print("\n"*45)
    for i in range(1,n+1):
        print("*"*i)
    input("Pausa")

def escalera2(n):
    print("\n"*45)
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)
    input("Pausa")

def menu():

    op=0
    while op!=10:
        print("\n"*45)
        print("1)  Pide N")
        print("2)  Horizontal")
        print("3)  Vertical")
        print("4)  Diagonal 1")
        print("5)  Diagonal 2")
        print("6)  Cruz")
        print("7)  Tache")
        print("8)  Escalera 1")
        print("9)  Escalera 2")
        print("10) Terminar")
        op=int(input("Indica la opción : "))
        if op<1 or op>10:
            input("Error, opción fuera de rango entre 1 y 10")
        else:
            if op==1:
                x=pide_n()
            if op==2:
                horizontal(x)
            if op==3:
                vertical(x)
            if op==4:
                diagonal1(x)
            if op==5:
                diagonal2(x)
            if op==6:
                cruz(x)
            if op==7:
                tache(x)
            if op==8:
                escalera1(x)
            if op==9:
                escalera2(x)
            pass

menu()
#Termina función menu 