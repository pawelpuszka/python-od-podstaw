for num in range(2, 101):
    div_counter = 0
    for i in range(1, num+1):
        if num % i == 0:
            div_counter += 1
            if div_counter > 2:
                break

    if div_counter == 2:
        print(num)