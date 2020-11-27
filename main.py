cook_book = {}

with open('recipes.txt', encoding='utf-8') as recipes:
    recipes_list = recipes.read().splitlines()

# for line in recipes_list:
#     line = line.strip()
next_line = 0
for index in range(len(recipes_list)):
    if index != next_line:
        continue
    lines = int(recipes_list[index+1])
    current_list = []
    for ingrid in range(lines):
        current_dict = {}
        current_dict['ingridient_name'], current_dict['quantity'], current_dict['measure'] = recipes_list[index + 2 + ingrid].split(' | ')
        current_list.append(current_dict)
    next_line = index + 3 + lines
    cook_book[recipes_list[index]] = current_list

# print(cook_book)
