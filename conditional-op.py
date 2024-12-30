# EXERCIZE 1:

India=["Mumbai","Bangalore","Delhi","Chennai"]
Pakistan=["Lahore","Karachi","Islamabad"]
Bangladesh=["Dhaka","Khulna","Rangpur"]

print("---Exercise 1---")

city=input("Enter any city: ")
if city in India:
    print(f"{city} belongs to India ")
elif city in Pakistan:
    print(f"{city} belongs to Pakistan ")
elif city in Bangladesh:
    print(f"{city} belongs to Banngladesh")
else:
    print("Based on my limited knowldege, I don't have the relavant information")


print("\n---Exercise 2---")

city_1=input("Enter first city: ")
city_2=input("Enter second city: ")
if city_1 in India and city_2 in India:
    print(f"{city_1}and {city_2}, Both cities are in India")
elif city_1 in Pakistan and city_2 in Pakistan:
    print(f"{city_1}and {city_2}, Both cities are in Pakistan")
elif city_1 in Bangladesh and city_2 in Bangladesh:
    print(f"{city_1}and {city_2} Both cities are in Bangladesh")
else:
    print("oops sorry !! no info available ")


# EXERCIZE 2:

sugar_level=int(input("Enter your sugar level: "))

if sugar_level< 80 and 100:
    print("Your sugar is low.")
elif sugar_level>80 and 100:
    print("Your sugar is high.")
else:
    print("Congrats, You've maintained a good sugar level.")
