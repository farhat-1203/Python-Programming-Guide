
n=int(input("Enter the row number: "))
def pattern(n):
    if (n==0):
        return 
    print("*"*n)
    pattern(n-1)

pattern(n)