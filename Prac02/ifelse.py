#demo1 — простая проверка условия
user_active = True
if user_active:
    print("Сеанс начат 👋")

# demo 2 —elif пропускает остальные варианты
x1 = 7
x2 = 45
if x2 > x1:
    print("Второе число больше первого")
elif x1 == x2:
    print("Числа равны")

#demo 3 — сокращённый if
print("Первый") if x1 > x2 else print("Второй")

#demo 4 — логическое отрицание
if not x1 > x2:
    print("x1 НЕ больше x2")

# demo 5— вложенное условие
level = 12
if level > 10:
    print("Выше десяти,")
    if level > 20:
        print("и выше двадцати!")
    else:
        print("но не выше двадцати.")

# demo 6 —pass как заглушка
score = -3

if score < 0:
    print("Отрицательное значение")
elif score == 0:
    pass  # ноль — ничего не делаем
else:
    print("Положительное значение")
