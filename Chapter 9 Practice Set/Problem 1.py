with open("poems.txt","r") as f:
    lines=f.read()
    if ("twinkle" in lines):
        print("Yes the poem contains the word 'twinkle' ")
    else:
        print("The word 'twinkle' is not present in the file")
    