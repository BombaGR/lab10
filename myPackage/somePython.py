import json
import os

recipies_path = 'porady'


def recipies_load():
    if os.path.exists(recipies_path):
        with open(recipies_path, 'r') as file:
            recipies = json.load(file)
        return recipies
    else:
        return []


def recipies_save(recipies):
    with open(recipies_path, 'w') as file:
        json.dump(recipies, file)


def save_rece():
    recipies_save(recipies)


curr_recipie = 0
recipies = recipies_load()


def recipie_search():
    if recipies:
        pattern = input('Podaj tytuł: ')
        for recipie in recipies:
            if pattern.lower() in recipie['tytul'].lower():
                print('Tytuł: {}'.format(recipie['tytul']))
                print('Opis: {}'.format(recipie['opis']))


def recipie_print(index, recipies):
    if recipies:
        print('Tytuł: {}'.format(recipies[index]['tytul']))
        print('Opis: {}'.format(recipies[index]['opis']))


def fun():
    print("")


def recipies_show():
    if recipies:
        for recipie in recipies:
            print('Tytuł: {}'.format(recipie['tytul']))
            print('Opis: {}'.format(recipie['opis']))


def recipie_add():
    new = {}
    new['tytul'] = input('Tytuł: ')
    new['opis'] = input('Opis: ')
    recipies.append(new)


def recipie_remove():
    global curr_recipie
    if -1 < curr_recipie < len(recipies):
        del recipies[curr_recipie]


def recipie_nextt():
    global curr_recipie
    curr_recipie += 1
    if curr_recipie >= len(recipies):
        curr_recipie = len(recipies) - 1
    print('Aktualna porada:')
    recipie_print(curr_recipie, recipies)


def recipie_prev():
    global curr_recipie
    curr_recipie -= 1
    if curr_recipie < 0:
        curr_recipie = 0
    print('Aktualna porada:')
    recipie_print(curr_recipie, recipies)