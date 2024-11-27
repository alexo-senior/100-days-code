
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 

nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

"""pasword = ""

for l in range(1, nr_letters + 1):
    pasword += random.choice(letters)
        
for l in range(1, nr_symbols + 1):
    pasword += random.choice(numbers)
    
for l in range(1, nr_numbers + 1):
    pasword += random.choice(symbols)
    
    
    print(pasword)"""

#otherwise a little hard but secure
#se crea una lista vacia        
pasword_list = ""

for l in range(1, nr_letters + 1):
#a medida que el ciclo for recorre la lista de letras desde el principio y sumandole uno, con random.choice
#se van agregando de forma aleatoria las letras desde letters hacia pasword_list
    pasword_list += random.choice(letters)
        
for l in range(1, nr_symbols + 1):
    pasword_list += random.choice(numbers)
    
for l in range(1, nr_numbers + 1):
    
    pasword_list += random.choice(symbols)
    #pasword_list = pasword_list + pasword_list(random.choice(symbols))
    
    
print(pasword_list)

"""random.shuffle(pasword_list)
print(pasword_list)
    
pasword = ""
    
for l in pasword_list:
    pasword += l
        
print(f"tour password is:{pasword}")"""
#para transformar de nuevo en un string
pasword = ""

for l in pasword_list:
    pasword += l
#print(pasword)
print(pasword)
        
        
    

    
    