def temp_warm_or_cold(value):
    if isinstance(value, int):
        if int(value) > 7:
            temp = "Warm"
        else:
            if int(value) <=7:
                temp = "Cold"
    return temp

temp = 8

print(temp_warm_or_cold(temp))