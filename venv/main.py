import cool_module
from importlib import reload


def append_func_to_cool_module():
    file = open(r'cool_module.py', 'a')
    file.write('\n\ndef my_func(a, b):\n')
    file.write('    return a ** b\n')
    file.close()

    reload(cool_module)
    print(cool_module.my_func(2, 5))


def check_func_in_cool_module():
    file = open(r'cool_module.py', 'r')
    contents = file.read()

    print('def my_func(a, b):\n    return a ** b' in contents)
    file.close()
    reload(cool_module)


def refactor_name_in_module(old_name: 'Name to be replaced', new_name: 'New name') \
        -> 'Refactored names':
    file = open(r'cool_module.py', 'r')
    contents = file.read()
    file.close()

    contents = contents.replace(old_name, new_name)
    file = open(r'cool_module.py', 'w')
    file.write(contents)
    file.close()
    reload(cool_module)


print(refactor_name_in_module.__annotations__)


def change_line_in_module(line_no, replace_with):
    file = open(r'cool_module.py', 'r')
    contents = file.readlines()
    file.close()

    contents[line_no] = replace_with

    file = open(r'cool_module.py', 'w')
    contents = "".join(contents)
    file.write(contents)
    file.close()
    reload(cool_module)


def insert_line_to_module(line_no, insert_line):
    file = open(r'cool_module.py', 'r')
    contents = file.readlines()
    file.close()

    contents.insert(line_no, insert_line)

    file = open(r'cool_module.py', 'w')
    contents = "".join(contents)
    file.write(contents)
    file.close()
    reload(cool_module)


def insert_new_func_to_module():
    func_text = "\n\ndef new_func(a, b):\n    return a + b\n"
    insert_line_to_module(2, func_text)

    print(cool_module.new_func(23, 23))


def insert_new_func_to_this_module():
    file = open(r'main.py', 'r')
    contents = file.readlines()
    file.close()

    func_text = "\n\ndef new_func(a, b):\n    return a + b\n"
    contents.insert(187, func_text)

    file = open(r'main.py', 'w')
    contents = "".join(contents)
    file.write(contents)
    file.close()


# --------------------------------------------------------------------------
# Immutable: numbers, strings, tuples, frozen sets
# Mutable: lists, dictionaries, sets

# func(values, names=value, *sequences, **dicts)
# func(names, names=value, *names, *, names=value, **names)

# filter(function, iterable)
# zip(*iterables)
# map(function, *iterables)
# if 't' in n_sum.__dir__(): return n_sum.t
# for x ... : if not isinstance(x, list)

def list_cool_module_attributes():
    print(dir(cool_module))


def slices():
    a = 'Python'
    print(a[:])  # Result: Python
    print(a[2:])  # Result: thon
    print(a[:-4])  # Result: Py
    print(a[2:4])  # Result: th
    print(a[3:-1])  # Result: ho
    print(a[::-1])  # Result: nohtyP
    print(a[2:6:2])  # Result: to
    print(a[2::2])  # Result: to


def dictionaries():
    # a = dict([[1, 'Tom'], [2, 'Stoppard']])
    b = dict(name='Bob', surname='Johnson')
    b['name'] = 'Kate'
    del b['surname']

    a = tuple([[1, 'Tom'], 3, 4, 'wow'])
    print(a)


def files():
    file = open(r'file.txt', 'w')
    file.writelines(['how ', 'are ', 'you?'])
    file.flush()
    print(file.tell())
    file.seek(10)
    file.writelines(['23'])
    file.close()  # how are yo23


def lines_to_lists_of_words():
    file = open(r'cool_module.py')
    for line in file:
        print(line.split(), end=' ')
    file.close()


def iterators():
    a = list(range(1, 5, 2))
    iterator = iter(a)
    print(next(iterator))
    print(iterator.__next__())

    file = open(r'file.txt')
    print(file.__next__(), end='')
    print(next(file), end='')
    file.close()

    b = [1, 2.4, 'huh', {1, 2}, [23]]
    print(list(enumerate(b, 23)))  # [(23, 1), (24, 2.4), (25, 'huh'), (26, {1, 2}), (27, [23])]

    a = [1, 2.8, 4, 0, 9]
    print(all(a))


bi = 1


def globals_non_locals():
    global bi
    bi = 2
    t = 5 + bi

    def int_func():
        k = 5
        nonlocal t
        t += 5
        return t + k

    return int_func() + t


# print(globals_non_locals())  # 29


def numbers(a, *some_numbers):
    sun = a
    for n in some_numbers:
        sun += n
    print(sun)


def generators():
    a = [1, 'a', 3, (1, 2)]
    print([x * 2 for x in a if x == 3 or isinstance(x, tuple)])
