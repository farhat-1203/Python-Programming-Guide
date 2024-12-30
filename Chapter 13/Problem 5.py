from functools import reduce


List1=[45, 67, 23, 89, 10, 4, 78, 56, 91, 33]

def maximum(a,b):
    if (a>b):
        return a
    return b

r=reduce(maximum, List1)
print(f"The maximum of all the numbers in the given list is {r}")