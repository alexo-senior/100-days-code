
"""print(8/3)
#por medio de esta funcion round() se eliminan las aproximaciones 
print(round(8/3))
#si quiero redondearlo con los decimales que necesite solo coloco una coma y el numero de decimales
print(round(8 / 3, 2))
#other ways
print(round(2.66666666, 2))

#mas sencillo: si no queremos decimales arrroja 2 como resultado sin decimales
print(8 // 3)
#verificamos que es un entero y no decimal
print(type(8 // 3))
#en c aso de variables 
result = 4 / 2
#usando los signos /=, *=, +=, -=
result /= 2
print(result)"""

score = 0
#users scores a point
score += 1
print(score)
#cadenas y su conversion
#en el caso que tengamos que convertir varios tipos de datos para ahorrar codigo usamos el
#f-string

score = 0
height = 1.8
isWinning = True
# de esta forma nos ahorramo el tener que estar convirtiendo datos , f antes de las comillas
#y la variable entre llaves
print(f"your score is {score}, your height is {height}, you are Winning is {isWinning} ")






