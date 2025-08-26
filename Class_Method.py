
class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"
    # ^^ Instance Method

    @classmethod
    def get_count(cls):
        return f"Total amount of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa of students: {cls.total_gpa / cls.count: .2f}"

good_student = Student("Bruno",1.9)
average_student = Student("Amanda",3.4)
bad_student = Student("Niko",4.8)

print(Student.get_count())
print(Student.get_average_gpa())
