dict = { 
"key": "value", 
"harry": "code", 
"marks": "100", 
"list": [1, 2, 9] 
} 

# print(dict.items())
# print(dict.keys())
# print(dict.values())
# dict.update({"harry":"programming","renuka":"engineer"})
# print(dict)
print(dict.get("harry"))   # prints None if keydoesn't exist in the dictionary
print(dict["harry"])       # returns an error if keydoesn't exist in the dictionary