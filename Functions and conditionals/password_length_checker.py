def pass_controller(value):
    if isinstance(value, str):
        if len(value) < 8:
            password = False
        else:
            password = True
    return password

password = "mypass1"

print(pass_controller(password))