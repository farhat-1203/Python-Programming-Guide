class Employee:   # Class Employee
    
    language="Py"   # Class attribute
    salary=200000

farhat=Employee()  # Object farhat
farhat.name="Farhat"    # Object/Instance attribute
print(farhat.name,farhat.language,farhat.salary)

seemin=Employee()
seemin.name="Seemin"
print(seemin.name,seemin.language,seemin.salary)


# Here name is object attribute and salary & language are class attributes, as they directly belong to the class