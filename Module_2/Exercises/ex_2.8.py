# 8. Stwórz program który prosi o wpisanie tekstu a następnie utwórz słownik w którym
# kluczami będą słowa wystepujące w tym tekście a wartościami liczby wystąpień każdego słowa.
# Wyświetl słwonik

# ver.1

# text = input("Wpisz tekst: ")
# words_counter = dict()
# words = text.split()
#
# for word in words:
#     words_counter[word] = words.count(word)
#
# print(words_counter)


# ver.2
text = input("Wpisz tekst: ")
words = text.split()
words_counter = dict()

for word in words:
    if word not in words_counter.keys():
        counter = 1
        words_counter[word] = counter
    else:
        counter = words_counter[word]
        counter += 1
        words_counter[word] = counter

print(words_counter)
