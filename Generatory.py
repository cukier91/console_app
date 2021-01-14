def dividers(number):
    for i in range(1, number+1):
        if int(number) % i == 0:
            yield i


for x in dividers(3227):
    print(x)
