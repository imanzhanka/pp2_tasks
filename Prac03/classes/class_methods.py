class Staff:
    base_salary = 50000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_base_salary(cls, new_amount):
        """Метод класса принимает 'cls' вместо 'self'"""
        cls.base_salary = new_amount
        print(f"Базовая зарплата всех сотрудников теперь: {cls.base_salary}")

    @classmethod
    def from_string(cls, data_str):
        """Создает объект Staff из строки 'Имя-Зарплата'"""
        name, salary = data_str.split("-")
        return cls(name, int(salary))

# 1. Используем метод класса для изменения общей переменной
Staff.set_base_salary(55000)

# 2. Используем метод класса как фабрику для создания объекта
new_teacher = Staff.from_string("Иван Петров-60000")
print(f"Сотрудник: {new_teacher.name}, Зарплата: {new_teacher.salary}")