class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fobjectname} {self.lobjectname}"     # kuch bhi return kar sakte hai directly by calling the function
    
    @name.setter
    def name(self,value):
        self.fobjectname=value.split(" ")[0]
        self.lobjectname=value.split(" ")[1]



object=Employee()
object.a=45
object.name="Farhat Momin"
print(object.fobjectname)
object.show()


# here we don't have the instance attribute 'name', 
# but we have created an instance atribute that is derived from the existing attribute
# for more clarity, refer to Problem 3 