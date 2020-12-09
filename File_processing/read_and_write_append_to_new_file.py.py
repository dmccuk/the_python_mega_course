with open("bear1.txt") as file:
    content = file.read()

with open("bear2.txt", "a") as file:
    file.write(content)
