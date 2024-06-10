def hello(name, age):
    print("Cześć " + name + ". Masz " + str(age) + " lat")

# keyword arguments
hello(name='Paweł', age=42)


# parametry opcjonalne umieszcza się po parametrach wymaganych
def hello(name, age, last_name=None):
    print("Cześć " + name + ". Masz " + str(age) + " lat")
    if last_name is not None:
        print("Masz na nazwisko " + last_name)


hello(name='Paweł', age=42)

