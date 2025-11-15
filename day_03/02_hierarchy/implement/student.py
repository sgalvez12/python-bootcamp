class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def introduce(self):
        return f"I'm {self.first_name} {self.last_name}!"


class Student(Person):
    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    def introduce(self):
        return super().introduce() + " I'm a student."

student = Student("Jackie", "Chan", "123")
print(student.introduce())

#2 parent class (will take person)
#class Student(Person, Employee):
    #def introduce(self):
        #return super().introduce() + " I'm a student."

#2 parent class (will take employee)
#class Student(Person, Employee):
    #def introduce(self):
        #return Employee.introduce(self) + " I'm a student."