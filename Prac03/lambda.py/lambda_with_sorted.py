group = [
    {"name": "Алексей", "age": 22},
    {"name": "Мария", "age": 19},
    {"name": "Иван", "age": 20}
]
sorted_group = sorted(group, key=lambda student: student["age"])
print(sorted_group)
