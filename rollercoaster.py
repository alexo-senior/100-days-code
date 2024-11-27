# condicional anidados

print("welcome to the rollercoaster!")

bill = 0

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
#esta parte es un condicional anidado 
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5 dollars")
    elif age <= 18:
        bill = 7
        print("Please pay $7 dollars.")
    elif age >= 45 and age <= 55:
        print("Everithing is going to be ok.Hve a free ride on us!")#usamos los operadores log and, or y not
    else:
        bill = 12
        print("Please pay $12 dollars")
    wants_photo = input("Do you want a photo taken? y or n ")
    if wants_photo == "y":
        bill = bill + 3 
    print(f"Your final bill is:{bill}")    
    
else: 
    print("Sorry, you have to grow taller before you can ride.")
        

    
    