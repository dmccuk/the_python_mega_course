colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for list in colors:
    if isinstance(list, int) and int(list) > 50:
        print(list)