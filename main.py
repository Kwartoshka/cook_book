
def logger_with_path(path):
    def logger(func):
        def wrapper(*args, **kwargs):
            from time import asctime as time
            cur_time = time()
            name = (func.__name__)
            result = func(*args, **kwargs)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(f'Time of call is {cur_time}\n')
                f.write(f'Name of function is "{name}"\n')
                f.write(f'Arguments are {args} and {kwargs}\n')
                f.write(f'Result is {result}')
            return result
        return wrapper
    return logger

path = input('Enter the saving path: ')

@logger_with_path(path)
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingridient_name'] not in shop_list:
                shop_list[ingridient['ingridient_name']] = {
                    'quantity': ingridient['quantity'] * person_count,
                    'measure': ingridient['measure']
                }
            else:
                quantity = ingridient['quantity']
                (shop_list[ingridient['ingridient_name']]['quantity']) += ingridient['quantity'] * person_count
    return shop_list



cook_book = {}

with open('recipes.txt', encoding='utf-8') as recipes:
    recipes_list = recipes.read().splitlines()

next_line = 0
for index in range(len(recipes_list)):
    if index != next_line:
        continue
    lines = int(recipes_list[index+1])
    current_list = []
    for ingrid in range(lines):
        current_dict = {}
        current_dict['ingridient_name'], current_dict['quantity'], current_dict['measure'] = \
            recipes_list[index + 2 + ingrid].split(' | ')
        current_dict['quantity'] = int(current_dict['quantity'])
        current_list.append(current_dict)
    next_line = index + 3 + lines
    cook_book[recipes_list[index]] = current_list


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 1)


