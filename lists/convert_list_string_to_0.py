def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]

list = [99, 'no data', 95, 94, 'no data']
print(foo(list))