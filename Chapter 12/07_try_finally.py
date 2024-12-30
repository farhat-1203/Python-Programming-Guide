try:
    a=int(input("Enter a number:"))
    print(a)

except Exception as e:
    print(e)

finally:
    print("I am inside finally")        # Executed regardless of error 
                                        # 'finally' statement chalega hi chalega, even if the functions pops-up any error
                                        # if we do not use 'finally' and just simply prints the statement, inside a function
                                        # then the print statement will not be executed under any situation,(even if there's no error)

"""
def main():
    try:
        a=int(input("Enter a number:"))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("I am inside finally") 
        
"""