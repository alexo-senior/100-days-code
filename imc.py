#This is a code for calculate imc
"""height = input("enter your height ")
weight = input("enter your weight ")

weight_int = int(weight)
height_int = float(height)

imc = weight_int / height_int ** 2
#other ways
#imc = weight_int / (height_int * height_int)

imc_int = int(imc)
print(imc_int)"""




height = float(input("write your height: "))  # in meters e.g., 1.55
weight = int(input("write your weight: "))  # in kilograms e.g., 72

bmi = weight / (height * height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
    




