with open("Donkey.txt","r") as f:
    content=f.read()

contentNew=content.replace("Donkey","#####")

with open("Donkey.txt", "w") as f:
    f.write(contentNew)
    
