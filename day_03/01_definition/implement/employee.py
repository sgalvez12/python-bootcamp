class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {name} created with {id}")

    def work(self, task):
        print(f"Working {task} ...")
        self.tasks.append(task)


employee1 = Employee("Shirley", "0912")
employee2 = Employee("Saffi", "0802")

employee1.work("Create slides")
employee2.work("Report")
employee1.work("Payroll")
print(employee1)


