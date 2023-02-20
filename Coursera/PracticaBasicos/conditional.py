""" Exercise 1
year= int(input("Dime que edad tienes: "))

if(year>=18):
    print("machote que tienes tus 18 jeje")
if(year<18):
    print("uff sigues siendo menor bb","\n todavia te quedan: ", 18-year, " para ser mayorcete")

"""

"""Exercise 2 


year = int(input("dime que edad tienes: "))
my_year=24

if(year<my_year):
    print("chupala enano")
    if ((my_year-year)==1):
        print("bueno no tan peque")
else:
    print("eres mas viejo que yo")

"""


"""
exercise3 
muy ez pasamos al 4

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F


def Score(score):
    if(score<=49):
        return "your score",score,"tiene nota: F"
    elif(score>=50 and score<=59):
        return "your score",score,"tiene nota: D"
    elif(score>=60 and score<=69):
        return "your score",score,"tiene nota: C"
    elif(score>=70 and score<=89):
        return "your score",score,"tiene nota: B"
    elif(score>=90 and score<=100):
        return "your score",score,"tiene nota: A"
    
print(Score(50))

"""

""" Exercise 4
Check if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, the season is Autumn.
December, January or February, the season is Winter. March, April or May
, the season is Spring June, July or August, the season is Summer


Aatumn=['Septembre','Octobre','Novembre']
Winter=['Decembre','January','February']
Spring=['March','April','May']
Summer=['June','July','August']

def Season(season):
    if(season in Aatumn):
        return ("Estas en otoño chavalin")
    elif(season in Winter):
        return ("Estas en invierno")
    elif(season in Summer):
        return ("Estas en verano")
    elif(season in Spring):
        return ("Estas en primavera")
   
        
print(Season("June"))
"""