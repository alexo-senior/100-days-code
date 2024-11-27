
"""Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:
 
i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

Example Input 1
10
Example Output 1
30
Example Input 2"""
#creo el objetivo de el numero  con un input

"""target = int(input("type your number "))
#crea una variable inicializada en cero que va a recibir la suma del numero ingresado
even_numbers = 0
#el ciclo comienza en 2 porque buscamos pares, luego el objetivo mas uno porque el ciclo en range se detiene en uno antes del numero
#dado en el input y luego queremos ir añadiendo de dos en dos
#recuerda que range() recibe hasta tres parametros start end y el incremento
for numbers in range(2, target + 1, 2):
#a la variable en cero se le añaden progresivamente el ciclo numbers
    even_numbers += numbers
#si indentamos el print aqui se imprime de forma detallada hasta llegar al numero total
    #print(even_numbers)
#si lo indentamos al principio se imprime la suma total en un solo numero
print(even_numbers)"""
    
    
#otra forma de hacer el codigo es :

target = int(input("type the number "))        

sum_numers = 0

for number in range(2, target + 1, 2):
    if number % 2  == 0:
        sum_numers += number
        
print(sum_numers)

"""import random

frutas = ["manzana", "banana", "naranja", "pera"]
fruta_aleatoria = random.choice(frutas)
print(f"La fruta aleatoria es: {fruta_aleatoria}")"""

"""import random
frase = "Hola, mundo!"
letra_aleatoria = random.choice(frase)
print(f"La letra aleatoria es: {letra_aleatoria}")"""
        


