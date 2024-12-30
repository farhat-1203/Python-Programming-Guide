class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The vector is {self.i}i+{self.j}j")



class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)       
        self.k=k

    def show(self):
        print(f"The vector is {self.i}i+{self.j}j+{self.k}k")

object1=TwoDVector(1,2)
object1.show()
object2=ThreeDVector(1,2,3)
object2.show()