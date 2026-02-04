#demo1— сопоставление по числу
code = 3
match code:
    case 1:
        print("Alpha")
    case 2:
        print("Beta")
    case 3:
        print("Gamma")
    case 4:
        print("Delta")
    case 5:
        print("Epsilon")
    case 6:
        print("Zeta")
    case 7:
        print("Omega")

#demo2— вариант по умолчанию
code = 8
match code:
    case 6:
        print("Режим: выходной")
    case 7:
        print("Режим: праздник")
    case _:
        print("Обычный рабочий день")

# demo3 —объединённые условия
index = 6
match index:
    case 1 | 2 | 3 | 4 | 5:
        print("Будний день")
    case 6 | 7:
        print("Долгожданный отдых")

# demo4 —условие с guard
season = 2
step = 5
match step:
    case 1 | 2 | 3 | 4 | 5 if season == 1:
        print("Первая фаза")
    case 1 | 2 | 3 | 4 | 5 if season == 2:
        print("Вторая фаза")
    case _:
        print("Совпадений нет")
