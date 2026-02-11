#ex1
def calculate_integral_area(width, height):
    return width * height #one return
result = calculate_integral_area(5.0, 10.0)
print(f"Area: {result}") 

#ex2
def get_prime_factors(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    # Returning a full list object
    return factors
print(get_prime_factors(84)) 

#ex3
def get_rectangle_properties(a, b):
    perimeter = 2 * (a + b)
    area = a * b
    # Возвращаем два значения сразу
    return perimeter, area

p, s = get_rectangle_properties(5, 10)
print(f"Периметр: {p}, Площадь: {s}")

#ex4
def is_student_stressed(hours_of_sleep):
    # Возвращает результат логического выражения
    return hours_of_sleep < 6
sleep = 4
if is_student_stressed(sleep):
    print("Студенту пора отдохнуть!")
else:
    print("Студент в норме.")