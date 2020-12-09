def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for x in string:
        if x in vowels:
            string = string.replace(x, "")
    return string

# and this one!
#def disemvowel(s):
#    for i in "aeiouAEIOU":
#        s = s.replace(i,'')
#    return s