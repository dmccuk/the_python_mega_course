def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False

print(isDigit("-2233"))