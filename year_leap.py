#codigo para comprobar si un año es bisiesto

year = int(input("what year do you know: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year}is a year leap!")
        else:
            print(f"{year} is not year leap!")
    else:
        print(f"{year} is year leap")
        
else:
    print(f"{year} is not year leap")
    
#otherwise        
#funcion para comprobar si un año es o no bisiesto
#debe cumplir las tres condiciones   

"""def year_is_leap(years):
    
    if years % 4 == 0:
        if years % 100 == 0:
            if years % 400 == 0:
                return "leap year"
            else:
                return "not leap year"
        else:
            return "leap year"
    else:
        return"not leap year"
    
#print(year_is_leap(2000))
print(year_is_leap())"""

        

    
        


        
        
    
            
            
            
    
    
        
