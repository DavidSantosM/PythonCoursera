#prueba de loops# previo a estructura de datos 
"""_summary_

cuenta10=10
def contador(numero):
    while numero>0:
        if numero==2:
            continue
        print("xupala",numero)
        numero=numero-1

print(contador(cuenta10))
"""
cadena="caracol"
numbers = [0, 1, 2, 3, 4, 5]
for i in range(len(cadena)): # number is temporary name to refer to the list's items, valid only inside this loop
    print(cadena[i])       # the numbers will be printed line by line, from 0 to 5
    