
print("---Exercize 1---")
street="Hilltop View"
city="Mumbai"
country="India"
address= street +"\n"+ city +"\n"+ country
print("Address using + operator:\n",address)
address=f"{street}\n{city}\n{country}"
print("Address using f string:\n", address)


print("\n---Exercize 2---")
text= "Earth revolves around the sun"
print(text[6:13])
print(text[-3:])


print("\n---Exercize 3---")
fruits=4
veggies=2
print(f"I eat {fruits} fruits and {veggies} vegetables daily")


print("\n---Exercize 4---")
s="maine 200 banana khaye"
s=s.replace("200 banana", "10 samosa")
print(s)
