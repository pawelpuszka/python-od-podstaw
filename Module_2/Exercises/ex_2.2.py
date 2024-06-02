# 2. Stwórz listę która będzie zawierać 10 słów. Nastepnie stwórz listę która będzie zawierać tylko te słowa
# które mają więcej niż 5 liter

words = ['Oko', 'Głowa', 'Komputer', 'Pamięć', 'Bazy danych', 'Java', 'Python', 'Oracle', 'PostgreSQL', 'PyCharm']
more_than_5_letters_words = list()

for word in words:
    if len(word) > 5:
        more_than_5_letters_words.append(word)

print(more_than_5_letters_words)