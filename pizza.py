"""Instructions
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Input
L
Y
N
Explicar
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28."""




print("Thank you for choosing Python Pizza Deliveries")





bill = 0

size = input("What size pizza do you want? S, M, or L ") 


if size == "s":
    bill += 15
    
elif size == "m":
    bill += 20
    
elif size == "l":
    bill += 25
    
else:
    print("what is the size your pizza please")
    
add_pepperoni = input("Do you want pepperoni? Y or N ") 

if add_pepperoni == "y":
    if size == "s":    
        bill += 2
    else:
        bill += 3
        
extra_cheese = input("Do you want extra cheese? Y or N ") 
        
if extra_cheese == "y":
    bill += 1
    
print(f"your final bill is: {bill}.")

    
    





    

    
    

    
    