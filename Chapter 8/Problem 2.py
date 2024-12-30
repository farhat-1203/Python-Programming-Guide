
temp=int(input("Enter the temperature in Fahrenhiet: "))

def f_to_c(temp):
    
    return 5*(temp-32)/9

a=f_to_c((temp))
print(f"The corresponding Celcius temperature is: {round(a,2)}")