

def divisibility_by_5(n:int):
    if (n%5==0):
        return True
    return False


List1=[45, 67, 23, 89, 10, 4, 78, 56, 91, 33]

divisible_by_5 = filter(divisibility_by_5, List1)
print(list(divisible_by_5))


