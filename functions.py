
print("---Exercize 1---")
def calculate_area(base,height):
    area_of_triangle=(1/2)*base*height
    return area_of_triangle


b=4
h=8
Area=calculate_area(base=b,height=h)
print(Area)


print("\n---Exercize 2---")

def calculate_area(dim1,dim2,shape):
   if shape=="triangle":
       area=(1/2)*dim1*dim2
   elif shape=="reactangle":
       area=dim1*dim2
   else:
       print("Invalid input!!")
       area=None

   return area

dim1=int(input("Enter thee first dimension:"))
dim2=int(input("Enter thee second dimension:"))
shape=input("Enter the shape (traingle,recatngle):")
area=calculate_area(dim1,dim2,shape)
if area is not None:
    print(f"The area of the {shape} with dimensions {dim1} and {dim2} is {area}")
else:
    print("Couldn't calculate the area due to invalid shape input.")


