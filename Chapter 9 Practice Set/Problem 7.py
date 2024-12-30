with open("log.txt", "r") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if ("Python" in lines):
        print(f"The word 'Python' is present at line number {lineno}")
        break        
    lineno +=1

else:
    print("The word 'Python is not present'")
        