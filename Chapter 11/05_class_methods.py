class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


object=Employee()
object.a=45
object.show()


# self use karenge toh instance attribute show karega
# cls use karenge toh class attribute show karega...by using the decorator @classmethod