"""Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.
Definicion de numero primo: Un número natural (1, 2, 3, 4, 5, 6, etc.) 
se denomina número primo (o primo ) si es mayor que 1 y no se puede 
escribir como el producto de dos números naturales menores. 
Los números mayores que 1 que no son primos se denominan números
compuestos"""

def prime_checker_number(number):
    is_prime = True
    for p in range(2, number):
        if number % p == 0:
            is_prime = False
    if is_prime:
        print("it's a prime number")        
    else:
        print("is's not number prime")
        
numbers = int(input("type your number "))
    
prime_checker_number(number=numbers)

        
    
    