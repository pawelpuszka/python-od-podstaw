# Napisz funkcję is_palindrome(s), która przyjmuje tekst i zwraca True jeśli jest palindromem i False jeśli tekst nie jest palindromem.
# rollor
# civic

def is_palindrome(word: str):
    letters = list(word)

    if len(letters) % 2 == 0:
        last_idx = (len(letters) // 2)
    else:
        last_idx = (len(letters) // 2) + 1

    for i in range(0, last_idx):
        flag = True
        j = i + 1
        if letters[i] == letters[-j]:
            continue
        else:
            flag = False
            break

    return flag


print(is_palindrome('kinnikinnik'))

