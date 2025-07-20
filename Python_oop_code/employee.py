class Employees:
    def __init__(self, role, dep, sal):
        self.role = role
        self.dep = dep
        self.sal = sal

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.dep)
        print("Salary:", self.sal)


class Engineer(Employees):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 70000)

    def showDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().showDetails()


e1 = Engineer("Rajat", 25)
e1.showDetails()
