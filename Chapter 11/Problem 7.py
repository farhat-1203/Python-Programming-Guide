# class Vector:

#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z

#     def __add__(self,other):
#         result= Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result
    
#     def __mul__(self,other):
#         result= self.x * other.x + self.y * other.y + self.z * other.z
#         return result
    
#     def __str__(self):
#         return f"Vector({self.x},{self.y},{self.z})"
    
#     def __len__(self):
#         return 3
    

# v1=Vector(1,2,3)
# v2=Vector(4,5,6)

# print(f"The sum of the two vectors are {v1+v2}")
# print(f"The dot produt of the two vectors are {v1*v2}")
# print(f"The length of the vector v1 is {len(v1)}")


"""
Alternate solution
"""

class Vector:

    def __init__(self,list):
        self.list=list

    def __len__(self):
        return len(self.list)
    
v1=Vector([1,2,3])
print(f"The length of the vector v1 is {len(v1)}")