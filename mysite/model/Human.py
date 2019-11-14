class Person:
    name:str
    age:int
    weight:complex

    # Initializer / Instance Attributes
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    # Method to call
    def swim(self):
        print("The person is swimming.")

    def be_awesome(self):
        print("The person is being awesome.")
    
    def introduce(self):
        print("Hello dears! My name is "+ self.name + " and I am " + format(self.age)+". Now my weight is "+ format(self.weight))