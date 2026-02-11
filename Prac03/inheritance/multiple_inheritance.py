class Athlete:
    def practice(self):
        return "Тренируюсь в спортзале"

class Leader:
    def organize(self):
        return "Организую собрание группы"

# Наследуем способности обоих классов
class StarStudent(Athlete, Leader):
    pass

top_student = StarStudent()
print(top_student.practice()) # От Athlete
print(top_student.organize()) # От Leader