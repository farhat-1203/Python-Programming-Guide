try:
    a:int = int(input("Enter first number: "))
    b:int = int(input("Enter second number: "))
    print(a/b)

except ZeroDivisionError as Z:
    print("Infinite")