from pprint import pprint
from re import L

def read_file(f, count):
    i = 0
    
    list_book = []
    while i <= count:
        line = f.readline().strip('\n').split('|')
        #print(line)
        i += 1
        if len(line) == 3:
            book = {}
            book['ingredient_name'] = line[0]
            book['quantity'] = line[1]
            book['measure'] = line[2]
            list_book.append(book)
                    
    return list_book

def wish_list(dishes, person_count, cook_book):
    list_menu = {}
    for dish in dishes:
        for list in cook_book[dish]:            
            ingredient = {}
            if list['ingredient_name'] in list_menu:
                temp = {}
                temp = list_menu[list['ingredient_name']]
                ingredient['quantity'] = ( int(list['quantity'] ) * person_count) + temp['quantity']
            else:
                ingredient['quantity'] = int(list['quantity']) * person_count
            
            ingredient['measure'] = list['measure']
            list_menu[list['ingredient_name']] = ingredient
    return list_menu



with open('recipes.txt', encoding='utf-8') as f:
    a = True
    cook_book = {}
    while a:
        name = f.readline().strip('\n')
        if name:
            count = int(f.readline())
            cook_book[name] = read_file(f,count)
        else:
            a = False

    print('\nСостав меню:')
    pprint(cook_book)

    menu = wish_list([ 'Омлет', 'Омлет'], 3 , cook_book)
    print('\nКоличество ингредиентов:')
    pprint(menu)



    
