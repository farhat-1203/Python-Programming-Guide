from functools import reduce

# Map Example:
# Map applies a function to all the items in an input_list

List1=[1,2,3,4,5]
square= lambda n:n*n  
sqList= map(square,List1)
print(f"The squared items list for the list provided is {list(sqList)}")



# Filter Example:
# Filter creates a list of items for which the function returns true.

def even(n):
    if (n%2==0):
        return True
    return False

List2=[1,2,3,4,5,6,7,8,9,10]
onlyEven=filter(even, List2)
print(f"Out of all the items in the above list, the even numbers are {list(onlyEven)}")


# Reduce Example:
List3=[1,3,5,7,9]
def sum(a:int,b:int)->int:
    return a+b                  # sum=lambda a,b:a+b


print(f"The sum of all the numbers in the given list is {reduce(sum,List3)}")

