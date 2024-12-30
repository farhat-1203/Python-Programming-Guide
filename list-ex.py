# EXERCIZE 1
expenses=[2200,2350,2600,2130,2190]


print("---Exercize 1---")
print("Dollars spent extra in Feb as compared to Jan: ",expenses[1]-expenses[0])


print("\n---Exercize 2---")
print("Total expense in first quarter of the year: ",expenses[0]+expenses[1]+expenses[2])


print("\n---Exercize 3---")
print(2000 in expenses)


print("\n---Exercize 4---")
expenses.append(1980)
print("Expenses at the end of the June",expenses)


print("\n---Exercize 5---")
expenses.insert(3,2330)
print("Changes in the monthly expense of April after the refund: ", expenses)



# EXERCIZE 2
heros=["spider man","thor","hulk","iron man","captain america"]


print("\n\n---Exercize 1---")
print(len(heros))


print("\n---Exercize 2---")
heros.append("black panther")
print(heros)


print("\n---Exercize 3---")
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)


print("\n---Exercize 4---")
heros[1:3]=["doctor strange"]
print(heros)


print("\n---Exercize 5---")
heros.sort()
print(heros)






