# demo1— базовые арифметические операции
a = 28
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

#demo2 — оператор присваивания в выражении
items = [10, 20, 30, 40, 50, 60]

if (total := len(items)) > 4:
    print(f"В списке {total} элементов")

# demo 3 операторы сравнения
value = 7

print(2 < value < 12)# цепочка сравнений
print(2 < value and value < 12)  # то же самое через and

# demo 4 — операторы тождественности
box1 = ["cat", "dog"]
box2 = ["cat", "dog"]
box3 = box1

print(box1 is box3)
print(box1 is not box2)
print(box1 == box2)

#demo 5 — операторы принадлежнсти
message = "OpenAI GPT"

print("O" in message)
print("gpt" in message)
print("X" not in message)
