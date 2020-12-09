with open("data.txt", "a+") as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.seek(0)
    myfile.write(content)
    myfile.write(content)
