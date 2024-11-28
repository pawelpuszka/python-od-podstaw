name = 'Paweł'

def display_name():
    print(name)

display_name()

name = 'Ania'

display_name()


def change_name():
    name = 'Filip'  # zmienna lokalna przesłonięta przez zmienną globalną


def change_name_2():
    global name
    name = 'Filip'

change_name_2()
display_name()

############################################

counter = 0

def method_a():
    global counter
    counter += 1

def method_b():
    global counter
    counter += 1

method_a()
method_b()


print(counter)