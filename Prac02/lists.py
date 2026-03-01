#demo1 — создание списка
box = list(("red", "blue", "green"))  # двойные скобки обязательны
print(box)

palette = ["red", "blue", "green"]

# demo 2 — изменение, добавление и удаление элементов

box[1:2] = ["purple", "yellow"]
print(box)

box.insert(2, "yellow")
print(box)

box.append("black")
print(box)

box = ["red", "blue", "green"]
warm = ["orange", "pink", "brown"]
box.extend(warm)
print(box)

box = ["red", "blue", "green", "blue", "white"]
box.remove("blue")# удаляется только первое совпадение
print(box)

box = ["red", "blue", "green"]
box.pop(1)
print(box)# удаление по индексу

del box[0]
print(box)#удаление по индексу

box.clear()#очищает список полностью









#demo 3 —list comprehension
box = ["red", "blue", "green"]
[print(color) for color in box]

shades = ["red", "blue", "green", "white", "black"]

filtered = [c for c in shades if "e" in c]
print(filtered)

nums = [n for n in range(12) if n % 2 == 0]

upper_colors = [c.upper() for c in shades]

# demo 4 — сортировка, копирование, разворот
scores = [88, 12, 47, 99, 30]
scores.sort(reverse=True)
print(scores)

def distance(val):
    return abs(val - 40)

scores = [88, 12, 47, 99, 30]
scores.sort(key=distance)
print(scores)

names = ["Lime", "orange", "Apple", "grape"]
names.reverse()
print(names)

copy1 = names.copy()

box = ["red", "blue", "green"]
copy2 = list(box)
print(copy2)

# demo 5 — объединение списков
group1 = ["x", "y", "z"]
group2 = [10, 20, 30]

mix = group1 + group2

for item in group2:
    group1.append(item)
print(group1)

group1.extend(group2)
print(group1)
