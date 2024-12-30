

# EXERCIZE 01:

print("---Exercize 1---")

population={"China":143,"India":136,"USA":32,"Pakistan":21}
print(population)



print("\n---Exercize 2---")

choice = input("Enter your choice (print/add/remove/query): ").strip().lower()

if choice == "print":
    for country, pop in population.items():
        print(f"{country} ==> {pop}")
elif choice == "add":
    new_country = input("Enter the name of the country you want to add: ").strip()
    if new_country in population:
        print("Country already exists.")
    else:
        new_pop = int(input(f"Enter population for the country {new_country}: "))
        population[new_country] = new_pop
        print("The updated dictionary is: ")
        for country, pop in population.items():
            print(f"{country} ==> {pop}")
elif choice == "remove":
    remove_country = input("Enter the name of the country you want to remove: ").strip()
    if remove_country not in population:
        print("Country doesn't exist in our dictionary.")
    else:
        del population[remove_country]
        print("The updated dictionary is: ")
        for country, pop in population.items():
            print(f"{country} ==> {pop}")
elif choice == "query":
    query_country = input("Enter the name of the country you want to query: ").strip()
    if query_country not in population:
        print("Country doesn't exist in our dictionary.")
    else:
        print(f"The population of {query_country} is {population[query_country]}")
else:
    print("Invalid input!")


# EXERCIZE 02:

stock={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}

def calculate_average(prices):
    return sum(prices)/len(prices)

operation=input("Enter the operation you want to perform (print/add) : ")

if operation=="print":
    for ticker,prices in stock.items():
        avg=calculate_average(prices)
        print(f"{ticker}==>{prices}==>avg:{avg:.2f}")
elif operation == "add":
    stock_ticker = input("Enter the new stock ticker you want to add: ").strip()
    price = int(input("Enter the new price details: ").strip())
    if stock_ticker in stock:
        stock[stock_ticker].append(price)
    else:
        stock[stock_ticker] = [price]
    print(f"Updated stock prices for {stock_ticker}: {stock[stock_ticker]}")
else:
    print("Invalid operation! Please enter 'print' or 'add'.")



# EXERCIZE 03:

def circle_calc(radius):
    Area=3.14*radius**2
    Circumference=2*3.14*radius
    Diameter=2*radius
    return Area, Circumference, Diameter

if __name__=="__main__":
     radius=float(input("Enter the radius of the circle: "))
     Area, Circumference, Diameter = circle_calc(radius)
     print(f"The area of the circle is: {Area}")
     print(f"The circumference of the circle is: {Circumference}")
     print(f"The diameter of the circle is: {Diameter}")
