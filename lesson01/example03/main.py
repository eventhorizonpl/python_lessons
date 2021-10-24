def eggs_whit_bacon():
    print('eggs with bacon')
    recipe_ingredients = {
        'bacon': 1,
        'eggs': 4,
    }
    recipe_times = {
        'bacon': 5,
        'eggs': 4,
    }
    pull_out_of_the_refrigerator(recipe_ingredients)
    prepare_ingridients(recipe_ingredients)
    putting_prepared_ingredient_on_the_pan('bacon')
    frying_on_a_pan('bacon', recipe_times['bacon'])
    frying_on_a_pan('eggs', recipe_times['eggs'])
    ready()

def eggs_whit_onion():
    print('eggs with onion')
    recipe_ingredients = {
        'eggs': 4,
        'onion': 1,
    }
    recipe_times = {
        'eggs': 4,
        'onion': 4,
    }
    pull_out_of_the_refrigerator(recipe_ingredients)
    prepare_ingridients(recipe_ingredients)
    putting_prepared_ingredient_on_the_pan('onion')
    frying_on_a_pan('onion', recipe_times['onion'])
    frying_on_a_pan('eggs', recipe_times['eggs'])
    ready()

def frying_on_a_pan(ingredient, minutes):
    print('Frying', ingredient, 'on a pan for', minutes, 'minutes')

def prepare_ingridients(recipe_ingredients):
    for ecipe_ingredient_key, ecipe_ingredient_value in recipe_ingredients.items():
        if ecipe_ingredient_key == 'bacon' or ecipe_ingredient_key == 'onion':
            print('Cutting', ecipe_ingredient_value, ecipe_ingredient_key)
        elif ecipe_ingredient_key == 'eggs':
            print('Breaking', ecipe_ingredient_value, ecipe_ingredient_key)

def pull_out_of_the_refrigerator(recipe_ingredients):
    for ecipe_ingredient_key, ecipe_ingredient_value in recipe_ingredients.items():
        print('Pulling out of the refridgerator', ecipe_ingredient_value, ecipe_ingredient_key)

def putting_prepared_ingredient_on_the_pan(ingredient):
    print('Putting prepared', ingredient, 'on the pan')

def ready():
    print('The meal is ready')

if __name__ == '__main__':
    print('Available recipes:')
    print('1 - eggs with bacon')
    print('2 - eggs with onion')
    recipe_number = int(input())

    if recipe_number == 1:
        eggs_whit_bacon()
    elif recipe_number == 2:
        eggs_whit_onion()
    else:
        print('Unknow recipe')
