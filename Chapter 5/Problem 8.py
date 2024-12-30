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

# Nothing will happen. The values can be same.
# A value can be same in a dictionary, but a key (basically an identifier) cannot be same; and if it is same,then it will return the updated value.