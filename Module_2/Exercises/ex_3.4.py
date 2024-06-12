# 4. Napisz funkcję reverse_string(s), która przyjmuje tekst i zwraca go w odwrotnej kolejności. Nie korzystaj z funkcji reversed().

def reverse_strings(text: str):
    text_list = text.split()
    text_rev = list()

    words_count = len(text_list)
    iter = words_count - 1

    for i in range(iter, -1, -1):
        text_rev.append(text_list[i])

    return " ".join(text_rev)


text = "Python jest dobry w analizie danych"
print(reverse_strings(text))


