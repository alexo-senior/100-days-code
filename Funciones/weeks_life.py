
"""age = input("write your ages ")

Year_left = 100 - int(age)
weeks = Year_left * 52
#cada año tiene 52 semanas
print(f"you have:{weeks} left.")
#para saber los años restantes, semanas convertidas a años
year_life = weeks / 52
#imprime los años restantes con f-string
print(f"your years left are: {year_life}")"""

#PROGRAMA PARA SABER CUANTAS SEMANAS Y AÑOS DE VIDA LE QUEDAN A UNA PERSONA
#BASANDOSE Y QUIZA EXAGERANDO UNA EDAD PROMEDIO DE LA ACTUALIDAD

#ESTA VEZ CON UNA FUNCION

#primero definimos la funcion

def life_in_weeks():
#creamos el imput para obtener las edad actual de la persona

    life = input("write your age ")
#creamos una variable con el dato base de 90 años - la edad actual(life)

    year_left = 90 - int(life)
#creamos la variable que guarda la operacion matematica para saber las semanas

    weeks_left = year_left * 52 
#crea otra variable que calcula los años restantes    
    year_life = weeks_left / 52
#imprime el resultado con un fsring 

    print(f"your years left are:{weeks_left} and your years next life are {year_life}")

life_in_weeks()


#otherwise

"""def life_in_weeks(age):
#creamos el imput para obtener las edad actual de la persona

    year_left = 100 - age

    weeks_left = year_left * 52 

    print(f"your years left are:{weeks_left}")

life_in_weeks()
"""



