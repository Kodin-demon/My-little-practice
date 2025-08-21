class Student:

    class_year = 2024
    students_num = 0
    #^^ class variable
    # can also be accessed directly by a class name

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # ^^ instance variable
        Student.students_num += 1
        #^^ you can also change class variables


student_1 = Student("Sandy", 25)
student_2 = Student("Sponge", 20)
student_3 = Student("Patrick", 21)
student_4 = Student("Tadeus", 35)

print(f"A class of {Student.students_num} graduated in year {Student.class_year}")
print(student_1.name)
print(student_2.name)
print(student_3.name)
print(student_4.name)




