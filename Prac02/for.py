# demo1— перебор элементов списка
colors = ["red", "blue", "green"]
for shade in colors:
    print(shade)

# demo 2— перебор символов строки
for letter in "Python":
    print(letter)

#demo 3— остановка цикла по условию
pets = ["cat", "dog", "parrot"]
for animal in pets:
    print(animal)
    if animal == "dog":
        break

#demo4 — break до вывода
cities = ["Rome", "Paris", "Berlin"]
for place in cities:
    if place == "Paris":
        break
    print(place)

# demo5 — пропуск элемента
numbers = ["one", "two", "three"]
for word in numbers:
    if word == "two":
        continue
    print(word)

# demo 6 — цикл с range
for counter in range(6):
    print(counter)
