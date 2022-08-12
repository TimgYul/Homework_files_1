from pprint import pprint
from re import L

cook_book = {}

def read_file(f, count):
    i = 0
    
    list_book = []
    while i <= count:
        line = f.readline().strip('\n').split('|')
        #print(line)
        i += 1
        if len(line) == 3:
            book = {}
            book['ingredient_name'] = line[0]#.strip('\n')
            book['quantity'] = line[1]#.strip('\n')
            book['measure'] = line[2]#.strip('\n')
            list_book.append(book)
            #pprint(list_book)
                    
    return list_book

with open('recipes.txt', encoding='utf-8') as f:
    a = True
    while a:
        name = f.readline().strip('\n')
        #print(name)
        if name:
            count = int(f.readline())
            cook_book[name] = read_file(f,count)
        else:
            a = False

    pprint(cook_book)


    
