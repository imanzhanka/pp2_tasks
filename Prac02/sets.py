# множества: неупорядоченне, неизменяемые*, уникальные элементы
# изменять нельзя, но можно добавлять новые элементы
# demo1 — создание множества
colors = {"red", "blue", "green"}
print(colors)

colors = {"red", "blue", "green", True, 0, 2}
print(colors)

colors = set(("red", "blue", "green")) #двойные скобки
print(colors)

# demo2—добавление и удаление элементов
fruits = {"apple", "banana", "cherry"}
fruits.add("kiwi")
print(fruits)

tropics = {"mango", "pineapple", "papaya"}
fruits.update(tropics)# добавить элементы из другого множества
print(fruits)

fruits.remove("banana")  #удаляет элемент, вызовет ошибку если нет
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")  #безопасное удаление
print(fruits)

removed_item = fruits.pop()  # удаляет случайный элемент

# demo 3 — объединение и операции с множествами
setA = {"x", "y", "z"}
setB = {10, 20, 30}

setC = setA.union(setB)
print(setC)

setC = setA | setB
print(setC)

setA.update(setB)
print(setA)

setC = setA.intersection(setB)
print(setC)

setC = setA & setB
print(setC)

setA.intersection_update(setB)
print(setA)

setC = setA.difference(setB)
print(setC)

setA.difference_update(setB)

setC = setA.symmetric_difference(setB)
print(setC)

setC = setA ^ setB
print(setC)

# demo 4 — неизменяемое множество
frozen_colors = frozenset({"red", "blue", "green"})
print(frozen_colors)
print(type(frozen_colors))

# demo 5 — добавление элементов
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)
