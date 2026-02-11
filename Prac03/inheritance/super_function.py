class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, scholarship):
        # Вызываем конструктор родителя, чтобы не писать self.name = name снова
        super().__init__(name, age)
        # Добавляем уникальное свойство студента
        self.scholarship = scholarship

s = Student("Мария", 20, 5000)
print(f"{s.name}, возраст: {s.age}, стипендия: {s.scholarship}")