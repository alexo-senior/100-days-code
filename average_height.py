#saber el promedio de altura de un grupo de estudiantes
#average height
#sin usar las funciones len() y sum()
#lista de altura de estudiantes
student_heights = [156, 178, 165, 171, 187]
#inicializa la variable en cero llamada total peso

total_height = 0
#ciclo for que recorre las altutas de los estudiantes y va a sumar por cada ciclo
for height in student_heights:
    total_height += height
print(f"total height is {total_height}")
    
#ahora un ciclo for con el numero de estudiantes

number_of_students = 0

for students in student_heights:
    number_of_students += 1
print(f"number_of_students = {number_of_students}")

average_heights = round(total_height / number_of_students)
print(f"average height = {average_heights}")



