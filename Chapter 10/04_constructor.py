class Employee:
    language="Py"   # Class attribute
    salary=200000

    def __init__(self, name, salary, language):     # Dunder method, which is automatically called whenever an object is made.
        self.name=name                              # If we pass these 3 values as an argument to that particular object, (instead of giving each values individually)
        self.salary=salary                          # then by just giving these values in the bracket and thereafter printing them 
        self.language=language                      # would result in the print of the 3 values
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}")
        print(f"The salary is {self.salary}")

    @staticmethod   # when no attributes are being used in the function, or when no object is needed.
    def greet():
        print("Good Evening !!")



farhat=Employee("Farhat",200000,"Python")           # 
print(farhat.name,farhat.language,farhat.salary)
