# Родительский класс
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Привет, я {self.name}"

# Дочерний класс наследует всё от Person
class Student(Person):
    pass

s = Student("Игорь")
print(s.greet()) # Работает, хотя в Student нет метода greet!