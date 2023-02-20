
numero= int(input("¿En que numero estas pensando? "))

def valido(numero):
    while (numero<0 or numero>1000):
        numero= int(input("¿En que numero estas pensando? "))
    return True

def par(numero):
    if valido(numero):
        return "numero par" if numero%2==0 else "impar primo"

print(par(numero))