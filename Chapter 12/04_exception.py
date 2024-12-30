try:
    a=int(input("Enter a number:"))
    print(a)

except Exception as e:
    print(e)

print("Thank You")

# Here in this code, Thank You will be printed anyhow, 
# whether try statement is executed or the except statement is executed popping up any error or warning message.



"""
a=int(input("Enter any number:"))
print("Thank You")

But here in this code snippet, if the user doesn't enter any integer value, 
then Thank You will not be printed, displaying only error.

"""