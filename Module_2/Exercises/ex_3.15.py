# 15. Napisz funkcję, która przyjmuje listę imion i wypisuje je w odwrotnej kolejności, używając pętli.

def print_reversed(names: list):
    last_idx = len(names) + 1

    for i in range(1, last_idx):
        print(names[-i])




names = ['Zosia', 'Stefan', 'Jerzy', 'Zdzisław']
print_reversed(names)