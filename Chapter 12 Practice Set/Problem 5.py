number=int(input("Enter any number: "))

table=[number*i for i in range(1,11)]
print(table)

with open("Tables.txt","a") as f:
    f.write(f"The table of {number} is shown as: {table}\n")