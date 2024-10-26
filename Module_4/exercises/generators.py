# Napisz generator, który generuje liczby od 1 do 10.
def generate_numbers():
    for i in range(1, 11):
        yield i


numbers = generate_numbers()

print(numbers)
for i in generate_numbers():
    print(i)

# Napisz generator, który generuje pierwszych 10 liczb z ciągu Fibonacciego.

fibonacci = (x for x in range(1, 11))

def fibonacci():
    val = 1
    prev_val = 1
    for i in range(1, 11):
        prev_val = val - prev_val
        val = val + prev_val
        yield val


for num in fibonacci():
    print(num)

