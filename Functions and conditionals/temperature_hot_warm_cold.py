def temp_hot_warm_cold(value):
    if isinstance(value, int):
        if int(value) > 25:
            temp = "Hot"
        elif int(value) >= 15 and int(value) <= 25:
            temp = "Warm"
        elif int(value) < 15:
            temp = "Cold"
    return temp

temp = 26

print(temp_hot_warm_cold(temp))