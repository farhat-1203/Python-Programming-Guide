class Calculator:

    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square of this number is {self.n*self.n}")

    def cube(self):
        print(f"The cube of this number is {self.n*self.n*self.n}")

    def square_root(self):
        print(f"The square root of this number is {self.n**1/2}")
    
    @staticmethod
    def greet():
        print("Hello user")


a=Calculator(4)
a.square()
a.cube()
a.square_root()
a.greet()