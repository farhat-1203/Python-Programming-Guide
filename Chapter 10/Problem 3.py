class Demo:
    a=4

object = Demo()
print(object.a)    # prints the class attribute 4, because the instance attribute is nit present
object.a=0         # Instance attribute is set
print(object.a)    # prints the instance attribute because instance attribute is present
print(Demo.a)      # prints the class attribute