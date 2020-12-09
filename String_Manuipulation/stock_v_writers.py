o = 790
h = 6
names_rating = {"Lucy": 18, "Mary": 12, "Henry": 10, "Stacey": 11, "Loulou": 5}

print("")
print("Hours to comlete %s orders" % o)
for i in names_rating.values():
    x = o / i
    print(round(x,1))
print("")

print("Hours taken for everyone working together to complete %s order" % o)
print(o / sum(names_rating.values()))

print("")
print("Ornaments completed in %s hours - per Person" % h)
for i in names_rating:
    print(i, names_rating[i] * h)


print("")
print("Ornements Per Hour with eveyone working")
print(h / h * sum(names_rating.values()))
print("")