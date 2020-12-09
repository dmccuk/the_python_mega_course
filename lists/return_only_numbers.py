def foo(lst):
    return [i if i(str) else 0 for i in lst if  isinstance(i, int)]


numbers = [99, 'no data', 95, 94, 'no data']
print(foo(numbers))