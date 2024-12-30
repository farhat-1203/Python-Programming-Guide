"""
print("---Exercize 1---")

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for i in result:
    if i=="heads":
        count=count+1
print("Total heads found:", count)


print("\n---Exercize 2---")

for i in range(11):
    if i%2==1:
        print(i*i)


print("\n---Exercize 3---")

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
expense=int(input("Enter your expense: "))

if expense in expense_list:
    month_index=expense_list.index(expense)
    print(f"The expense of {expense} is occured in the month of {month_list[month_index]}")
else:
    print("Expense not found") 



print("\n---Exercize 4---")


or i in range(1, 6):  
    response = input(f"Are you tired after completing {i} km? (yes/no): ")
    if response == "yes":
        print("You didn't finish the race.")
        break
    elif response == "no":
        if i == 5:
            print("Congratulations! You finished the 5 km race.")
    else:
            print("Invalid response. Please reply with 'yes' or 'no'.") """


print("\n---Exercize 5---")

for i in range(6):
    for j in i:
        print("*")

