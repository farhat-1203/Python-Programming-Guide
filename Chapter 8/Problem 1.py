
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

def greatest_number(a,b,c):
    if (a>b) and (a>c):
        print(f"{a} is the greatest number.")
    elif (b>a) and (b>c):
        print(f"{b} is the greatest number.")
    else:
        print(f"{c} is the greatest number.")


greatest_number(a,b,c)
