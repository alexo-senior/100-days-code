"""Ruleta de quien paga la cuenta del restaurante.
Crear un programa que elija al azar o de forma aleatoria a una persona 
de la lista para pagar la cuenta del restaurante"""

#definimos una variable con los nombres las personas

names_string = "Alexis, Tatiana, Daniel, Diego"
#importamos el modulo random
import random
#asignamos a la variable nombres el nombre de la lista. split separados por comas
names = names_string.split(", ")
#dividimos la lista de nombres con la funcion len para saber el numero de personas
num_items = len(names)
#asignamos a la variable random_choice el modulo random.randint y le colocamos
#el inicio de la posicion de la lista luego el num de items y el final -1
randon_choice = random.randint(0, num_items -1)

#imprimimos el mensaje de quien le toca pagar la cuenta

print(names[randon_choice],"is going to buy the meal today!",)




