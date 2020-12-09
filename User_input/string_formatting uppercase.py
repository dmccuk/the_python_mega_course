def name(value):
    first = value.capitalize()
    message = "Hi %s" % (first)
    return message

name1 = input("Enter your name: ")
print(name(name1))