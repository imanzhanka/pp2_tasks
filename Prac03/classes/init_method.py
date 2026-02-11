class Student:
    def __init__(self, name, major, gpa):
        # self ссылается на конкретного студента, который создается
        self.name = name    
        self.major = major  
        self.gpa = gpa     


student1 = Student("Алиса", "Физика", 4.8)
student2 = Student("Марк", "История", 3.5)

print(f"Студент: {student1.name}, Факультет: {student1.major}")