"""Crea una calculadora de propinas, que reciba el total de la cuennta a pagar
el valor de la propina ; que puede variar del 10, 12 o 15 por ciento, luego se 
suma este valor al total de la cuenta a pagar y se divide entre las personas 
que disfrutaron la comida en el restaurante.Debes redondear el total de la 
cuennta con dos digitos de punto flotante."""

print("Welcome to tip calculator!")

bill = float(input("what is the total bill?: "))

tip = int(input("HOw much tip would you like to give?: 10, 12, or 15 "))

people = int(input("How many people to spllit the bill?: "))

tip_percent = tip / 100

total_tip_amount = bill * tip_percent

total_bill = bill + total_tip_amount

total_bill_person = total_bill / people

final_amount = round(total_bill_person, 2)

print(f"total to pay for person is:${final_amount}")






