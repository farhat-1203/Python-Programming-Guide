def remove_strip(lst, word):
    n = []
    for item in lst:
        if isinstance(item, str):
            if word in item:
                stripped_item = item.replace(word, '')
                n.append(stripped_item.strip())
            else:
                n.append(item.strip())
        else:
            n.append(item)
    return n

lst = ["Farhat", 31, 72.5, "Seemin", True]
print(remove_strip(lst, "in"))
