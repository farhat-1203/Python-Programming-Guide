class Programmer:
    company="Mircosoft"

    def __init__(self, name, salary, post):
        self.name=name
        self.salary=salary
        self.post=post

    
emp_1=Programmer("Farhat",200000,"Data Science and Machine Learning Engineer")
print(emp_1.company,emp_1.name,emp_1.salary,emp_1.post)
emp_2=Programmer("Seemin",200000,"MERN Stack Developer")
print(emp_2.company,emp_2.name,emp_2.salary,emp_2.post)
emp_3=Programmer("Kaish",300000,"Data Engineer")
print(emp_3.company,emp_3.name,emp_3.salary,emp_3.post)