"""mad lib"""

salir=False

while(salir!=True):
    noun = input("Selecciona un sustantivo: ")
    p_noun = input("Selecciona un sustantivo en plural: ")
    noun2 = input("Selecciona un sustantivo: ")
    place = input("Nombra un lugar: ")
    adjective = input("Selecciona un adjetivo (Describe una palabra): ")
    noun3 = input("Selecciona un sustantivo: ")
    
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
    
    if (input('introduce "z" si quieres salir. sino pulsa cualquier cosa:')=='z'):
        salir=True