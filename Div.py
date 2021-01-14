def div(a, b):
    numbers = list(range(a, b+1))
    final_numbers = []
    for i in range(0, b):
        if numbers[i] % 2 == 0 and numbers[i] % 3 != 0:
            final_numbers.append(numbers[i])
    return final_numbers

print(div(1, 16))
