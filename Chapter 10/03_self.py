class Employee:
    language="Py"   # Class attribute
    salary=200000

    def getInfo(self):   # self woh object hai jaha par ye method getInfo() run hora hai # It can be any object listed below from (farhat,seemin) 
        print(f"The language is {self.language}")
        print(f"The salary is {self.salary}")

    @staticmethod   # when no attributes are being used in the function, or when no object is needed.
    def greet():
        print("Good Evening !!")



farhat=Employee()  # Object
# farhat.name="Farhat"    # Object/Instance attribute
# print(farhat.name,farhat.language,farhat.salary)
farhat.getInfo()        # = Employee.getInfo(farhat)   ....1 positional argument farhat
farhat.greet()


seemin=Employee()
seemin.name="Seemin"
print(f"\nEmployee Name: {seemin.name}")
seemin.getInfo()

