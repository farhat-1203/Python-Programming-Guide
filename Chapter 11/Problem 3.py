class Employee:
    salary=234
    increment=20

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary* (self.increment/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment= (salary/self.salary-1)*100
    

object=Employee()
print(f"The salary after increment of 20% is {object.salaryAfterIncrement}")    # here, we have directly called the function salaryAfterIncrement to get our output since we have used @property decorator
print(f"The increment based on the current salary is of {object.increment}%")