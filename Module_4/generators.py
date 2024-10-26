# suma liczb 0 - 1000

# print(sum([x for x in range(1_000_000_000)]))  # nie policzy tej sumy

# generator to obiekt którego elemnety nie są niegdzie zapisywane tylko są genrowane i wykorzystywane na bieżąco

# def billion_integers():
#     for number in range(1_000_000_000):
#         yield number
#
#
# print(sum(billion_integers()))



# generator comprehension
#print(sum(x for x in range(1_000_000_000)))

gen_comprehension = (x for x in range(1_000))
list_comprehension = [x for x in range(1_000)]

print(type(list_comprehension))
print(type(gen_comprehension))