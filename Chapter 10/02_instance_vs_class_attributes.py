class Employee:
    
    language="Py"   # Class attribute
    salary=200000

farhat=Employee()
farhat.language="Javascript"    # Instance attribute
print(farhat.language,farhat.salary)

# Instance atrribute takes preference over class attribute
# If intance attribute is provided then it will print the instance attriute only