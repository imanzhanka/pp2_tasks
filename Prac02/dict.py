# Dictionaries: ordered, mutable, no duplicate keys

#demo 1 — создание словаря
profile = {
    "username": "Neo",
    "rank": "Operator",
    "level": 7
}

profile = dict(nickname="Luna", score=91, city="Oslo")
print(profile)

# demo2 — доступ к элементам
value1 = profile["score"]      # через ключ
value2 = profile.get("score") # безопасный доступ
all_keys = profile.keys()     # список всех ключей

# demo3 — изменение данных
profile["score"] = 100
profile.update({"score": 120})  # массовое обновление

# demo 4 добавление и удаление
profile["status"] = "online"     # новый элемент
profile.update({"status": "away"})

profile.pop("city")    # удалить по ключу
profile.popitem()     # удалить последний элемент
del profile["nickname"]

# demo 5 —перебор словаря
stats = {
    "device": "Tablet",
    "os": "Android",
    "year": 2022
}

for key in stats:
    print(key)  # выводим ключи

for val in stats.values():
    print(val)  # выводим значения

for key in stats:
    print(stats[key])  # значения через ключи

for key in stats.keys():
    print(key)

for key, val in stats.items():
    print(key, "=>", val)

# demo 6 — копирование
clone1 = stats.copy()
clone2 = dict(stats)
print(clone1)

# demo 7 — вложенные словари
userA = {"name": "Aria", "year": 2010}
userB = {"name": "Blaze", "year": 2012}
userC = {"name": "Cyra", "year": 2015}

team = {
    "alpha": userA,
    "beta": userB,
    "gamma": userC
}

print(team["beta"]["name"])  # доступ к вложенному значению

for group, member in team.items():
    print(group)
    for field in member:
        print(field + ":", member[field])
