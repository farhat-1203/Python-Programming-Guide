class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()                  # If we want to print the constructor of the parent class also 
        print("Constructor of Manager")     # In other words, if we want to access the method & property of the super (parent) class
    c=3


# object1=Employee()
# print(object1.a)    


# object2=Programmer()
# print(object2.a)   
# print(object2.b)   
   


object3=Manager()
print(object3.a)   
print(object3.b)   
print(object3.c)   