class Example:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Object {self.name} is created")

    def __del__(self):
        print(f"Object {self.name}, Age: {self.age} is destroyed")


obj = Example("Test", 25)

del obj