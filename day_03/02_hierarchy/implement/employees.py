class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)

    def introduce(self):
        return f"Employee {self.name} created with ID {self.id}"


class Recruiter(Employee):

    def recruit(self):
        self.add_work("recruit")

    def work(self, work):
        self.work.append(work)



class Developer(Employee):
    def __init__(self, name, id, work="programming"):
        super().__init__(name, id)
        self.work = work

    def introduce(self):
        return super().introduce() +  "." + f" Employee is assigned to {self.work}."

class Manager(Employee):
    def __init__(self, name, id, work="managing people"):
        super().__init__(name, id)
        self.work = work

    def introduce(self):
        return super().introduce() + "." + f" Employee is assigned to {self.work}."


developer = Developer("Thurston Iya", "0806")
recruiter = Recruiter ("Saffi Iya", "0802")
manager = Manager ("Shirley Galvez", "0912")
print(developer.introduce())
print(recruiter.introduce())
print(manager.introduce())