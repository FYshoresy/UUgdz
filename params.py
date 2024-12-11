def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ('Привет', False, 71)
values_dict = {'a': None, 'b': 'Пока', 'c': 23}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('Как ты?', 12)

print_params(*values_list_2, 42)
