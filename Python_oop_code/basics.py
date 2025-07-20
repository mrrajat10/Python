class student:
    college_name = "ABC college"

    def __init__(self, fullname, marks):
        # print(self)
        self.name = fullname
        self.marks = marks

    def welcome(self):
        print("Welcome student,", self.name)

    def get_marks(self):
        return self.marks


s1 = student("Karan", 87)
print(s1.name, s1.marks)
s2 = student("ajay", 93)
print(s2.name, s2.marks)
print(s1.welcome())
print(s2.get_marks())
