class Employee:             # Base class
    company="ITC"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")



# class Programmer:
#     company="ITC Infotech"

#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

# def showLanguage(self):
#         print(f"The name is {self.name} and he is good at {self.language} language")
                            # OR 

class Programmer(Employee):     # Derived class
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good at {self.language} language")

a=Employee()
b=Programmer()
print(a.company, b.company)