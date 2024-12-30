class Employee:             # Base class 1
    company="ITC"
    name="Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")


class Coder:                # Base class 2
    language="Python"
    def printlanguages(self):
        print(f"Out of all the languages, here is your language {self.language}")


class Programmer(Employee, Coder):     # Derived class
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name of the employee is {self.name} and he is good at {self.language} language")


a=Employee()
b=Programmer()
b.show()
b.printlanguages()
b.showLanguage()
