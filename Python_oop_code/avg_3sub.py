class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hii{self.name},your average of subjects is {sum/3}")


s1 = student("Ajay", [12, 45, 22])
s1.avg()
