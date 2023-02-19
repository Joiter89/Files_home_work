import os
current = os.getcwd()
folder_name = 'Files_home_work'
file_name = 'recipes.txt'
full_path = os.path.join(current, folder_name, file_name)


with open('recipes.txt', 'rt', encoding ='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredient_count = int(f.readline())
        ingredients = []
        for i in range(ingredient_count):
            ing = f.readline().strip()
            name, quantity, measure = ing.split(' | ')
            ingredients.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure                             
            })
        f.readline()
        cook_book[dish_name] = ingredients 

from pprint import pprint        
pprint(cook_book)  

print()
print()

def get_shop_list_by_dishes(dishes, person_count):
    dish_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridients in cook_book[dish]:
                dish_dict[ingridients['ingredient_name']] = {'quantity': int(ingridients['quantity']) * person_count, 'measure': ingridients['measure']}
    return dish_dict             
           
pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))