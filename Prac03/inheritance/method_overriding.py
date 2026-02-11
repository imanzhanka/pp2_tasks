class Person:
    def greet(self):
        return "Добрый день!"

class Student(Person):
    # Мы переписываем метод родителя под свои нужды
    def greet(self):
        return "Привет, я с пары!"

p = Person()
s = Student()
print(p.greet()) # Добрый день!
print(s.greet()) # Привет, я с пары!