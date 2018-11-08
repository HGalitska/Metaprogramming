import cool_module
from importlib import reload


def new_func(a, b):
    return a + b


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


def refactor_name_in_module(old_name, new_name):
    file = open(r'cool_module.py', 'r')
    contents = file.read()
    file.close()

    contents = contents.replace(old_name, new_name)
    file = open(r'cool_module.py', 'w')
    file.write(contents)
    file.close()
    reload(cool_module)


def change_line_in_module(line_no, replace_with):
    file = open(r'cool_module.py', 'r+')
    contents = file.readlines()
    file.close()

    contents[line_no] = replace_with

    file = open(r'cool_module.py', 'w')
    contents = "".join(contents)
    file.write(contents)
    file.close()
    reload(cool_module)


def insert_line_to_module(line_no, insert_line):
    file = open(r'cool_module.py', 'r+')
    contents = file.readlines()
    file.close()

    contents.insert(line_no, insert_line)

    file = open(r'cool_module.py', 'w')
    contents = "".join(contents)
    file.write(contents)
    file.close()
    reload(cool_module)


def insert_new_func_to_module():
    func = "\n\ndef new_func(a, b):\n    return a + b\n"
    insert_line_to_module(2, func)

    print(cool_module.new_func(23, 23))


def insert_new_func_to_this_module():
    file = open(r'main.py', 'r+')
    contents = file.readlines()
    file.close()

    func = "\n\ndef new_func(a, b):\n    return a + b\n"
    contents.insert(2, func)

    file = open(r'main.py', 'w')
    contents = "".join(contents)
    file.write(contents)
    file.close()


insert_new_func_to_this_module()

# refactor_name_in_module("func", "funky")
# insert_new_func_to_module()
