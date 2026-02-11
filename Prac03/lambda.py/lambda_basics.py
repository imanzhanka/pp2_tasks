#ex1
students = [("Иван", 22, 4.5), ("Анна", 19, 4.9), ("Борис", 20, 3.8)]
students.sort(key=lambda student: student[2], reverse=True)
print(students) 
#название = lambda аргумент : выражение_которое_вернется
#anonymous function inside another function.
#ex2
heights = [160, 185, 172, 190, 155, 180]
tall_students = list(filter(lambda h: h > 175, heights))
print(tall_students)

#ex3
prices = [100, 500, 1000, 250]
prices_with_tax = list(map(lambda p: p * 1.2, prices))
print(prices_with_tax) 

#ex4
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
