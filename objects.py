class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


student1 = Student("Joyce", 21)
student2 = Student("Brian", 22)

student1.display()
student2.display()