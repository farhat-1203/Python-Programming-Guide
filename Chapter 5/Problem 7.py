d={}

key1=input("Enter your name: ")
value1=input("Enter your fav language: ")
d.update({key1:value1})
key2=input("Enter your name: ")
value2=input("Enter your fav language: ")
d.update({key2:value2})
key3=input("Enter your name: ")
value3=input("Enter your fav language: ")
d.update({key3:value3})
key4=input("Enter your name: ")
value4=input("Enter your fav language: ")
d.update({key4:value4})

print(d)

# The values entered later will be updated
#  If the names of two friends are same, it will return the second value provided; since here we've used update() method.
#  i.e. If the keys are same, it will return the second value provided.