def processing(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

print(processing("c"))