with open("files/bear.txt", "r") as myfile:
        chars90 = myfile.read(90)
      
with open("first.txt", "w") as myfile1:
        myfile1.write(chars90)

#OR
#with open("bear.txt") as file:
#    content = file.read()
#
#with open("first.txt", "w") as file:
#    file.write(content[:90])