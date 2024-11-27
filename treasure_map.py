
#listas dadas para las posiciones de la ubicacion 

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

#variable map que contiene las listas anidadas

map = [line1, line2, line3]

#mensaje del juego
print("Hiding your treasure! X marks the spot.")

#para pedir la posicion de la x
position = input("Where do you want to put the treasure? ") # Where do you want to put the treasure?

#se asigna la varible posicion con la informacion de entrada indice cero
# , es decir captura la primera posicion y luego se pasa a minusculas 
#asi se evitan errores si se escriben mayusculas 
letter = position[0].lower()

#variable abc con posiciones en letras con las posibles letras
abc = ["a", "b", "c"]

#utilizando el metodo index() hacemos comparacion, tomamos el nombre de la lista a,b,c y luego
#escribimos el indice y luego en el parentesis pasamos lo que sea que vayamos a comprobar 
#que existe en la lista
letter_index = abc.index(letter)


number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"


print(f"{line1}\n{line2}\n{line3}")