students = ["ivanov", "petrov", "sidorov"]
# Применяем метод .upper() к каждому элементу
diploma_names = list(map(lambda name: name.upper(), students))
print(diploma_names)
