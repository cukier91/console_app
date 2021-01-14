def name_sorter(names):
    dict_names = {'male': '',
                  'female': ''}
    list_of_female_names = []
    list_of_male_names = []
    for name in names:
        if name[-1] == 'a':
            list_of_female_names.append(name)
        else:
            list_of_male_names.append(name)
    dict_names['female'] = sorted(list_of_female_names)
    dict_names['male'] = sorted(list_of_male_names)
    return dict_names
lista_2 = ['Jolanta', 'Andrzej', "Anna", "Barbara", "Agnieszka","Wioletta","Grzegorz", "Bartek"]
print(name_sorter(lista_2))
