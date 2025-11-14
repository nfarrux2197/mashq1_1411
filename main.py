class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            raise ValueError("Baho 0–100 oralig‘ida bo‘lishi kerak.")

    def get_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)


class Teacher:
    def __init__(self, name):
        self.name = name

    def put_grade(self, student, grade):
        student.add_grade(grade)


s = Student("Ali", 101)
t = Teacher("Ustod Karimov")

t.put_grade(s, 90)
t.put_grade(s, 75)
t.put_grade(s, 88)

print("O‘rtacha baho:", s.get_average())
