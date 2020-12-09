def foo(lst):
    l = [float(i) for i in lst]
    return sum(l)

list = ['1.2', '2.6', '3.3']
print(foo(list))