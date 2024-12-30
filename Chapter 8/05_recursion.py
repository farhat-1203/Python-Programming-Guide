"""
factorial(0)=1
factorial(1)=1
factorial(2)=2*factorial(1)
factorial(3)=3*factorial(2)
factorial(4)=4*factorial(3)
factorial(5)=5*factorial(4)
factorial(n)=n*factorial(n-1)
"""



n=int(input("Enter the number: "))
def factorial(n):
    if (n==1) or (n==0):
        return 1

    return n*factorial(n-1)

print(f"The factorial of this number is {factorial(n)}")