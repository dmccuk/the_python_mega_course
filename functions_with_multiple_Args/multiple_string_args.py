def concat(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(concat('habc', 'efg'))