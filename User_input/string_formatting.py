def name(value):
    message = "Hi %s" % (value)
    return message

name1 = input("Enter your name: ")
print(name(name1))