from pprint import pprint
from re import L

cook_book = {}

def read_file(f, count):
    i = 0
    
    list_book = []
    while i <= count:
        line = f.readline().split('|')
        #print(line)
        i += 1
        if len(line) == 3:
            book = {}
            book['ingredient_name'] = line[0].strip('\n')
            book['quantity'] = line[1].strip('\n')
            book['measure'] = line[2].strip('\n')
            #print(book)
            list_book.append(book)
            #print(list_book)
                    
    return list_book

with open('recipes.txt', encoding='utf-8') as f:
    f.seek(0)
    name = f.readline().strip('\n')
    #print(name)
    count = int(f.readline())
    cook_book[name] = read_file(f,count)
    #pprint(cook_book)
    
    name = f.readline().strip('\n')
    #print(name)
    count = int(f.readline())
    cook_book[name] = read_file(f,count)
    pprint(cook_book)


    
