m1=int(input("Enter marks of subject 1: "))
m2=int(input("Enter marks of subject 2: "))
m3=int(input("Enter marks of subject 3: "))

# Check for total percentage
total_percentage=((m1+m2+m3)/300)*100

if (total_percentage>=40) and (m1>=33) and (m2>=33) and (m3>=33):
    print("Congrats! You are passed.", total_percentage)
else:
    print("You fail, try again next year.", total_percentage)