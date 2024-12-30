class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3


object1=Employee()
print(object1.a)   # Prints the a attribute i.e. 1
print(object1.b)   # Throws an error as there is no b attribute in Employee class


object2=Programmer()
print(object2.a)    # Prints the a attribute i.e. 1
print(object2.b)    # Prints the b attribute i.e. 2
print(object2.c)    # Throws an error as there is no c attribute in Programmer class


object3=Manager()
print(object3.a)    # Prints the a attribute i.e. 1
print(object3.b)    # Prints the b attribute i.e. 2
print(object3.c)    # Prints the c attribute i.e. 3