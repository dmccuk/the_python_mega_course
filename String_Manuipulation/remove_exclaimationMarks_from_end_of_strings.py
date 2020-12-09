def remove(s):
    while True:
        if s[-1:] == '!':
            s = s[:-1]
        else:
            return s