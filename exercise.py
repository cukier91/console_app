def shortener(variable):
    control_list = []
    count = []
    for word in variable.split(" "):
        control_list.append(word)
    for i in range(0, len(control_list)):
        count.append(control_list[i][0].upper())
    return ''.join(count)

print(shortener("Wielki zielony napis kurwa jego mac"))


