from collections import Counter, namedtuple

text = "To jest zdanie, to zdanie zdanie"
counter = Counter(text.lower().replace(',', '').split())

print(counter.most_common())
print(counter['to'])
