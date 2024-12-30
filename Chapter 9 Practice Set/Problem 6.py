with open("log.txt", "r") as f:
    content=f.readlines()

if ("Python" in content):
    print("Yes, The word 'Python' is present in the content")
else:
    print("No, The word 'Python' is not present")

