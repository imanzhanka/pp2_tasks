class Course:
    max_score = 100 
    university_name = "Global Tech University"

    def __init__(self, title):
        self.title = title # Переменная экземпляра

course_a = Course("Python")
course_b = Course("Data Science")

print(course_a.university_name) # "Global Tech University"
print(course_b.university_name) # "Global Tech University"