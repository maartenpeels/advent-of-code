from collections import defaultdict

if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt').readlines()]

    foods = []
    for line in lines:
        tokens = line.split(' (contains ')
        ingredients = set(tokens[0].split(' '))
        allergens = set(tokens[1][:-1].split(', '))
        foods.append((ingredients, allergens))

    # print(foods)

    ingredient_count = defaultdict(lambda: 0)
    possible = {}
    for ingredients, allergens in foods:
        for ingredient in ingredients:
            ingredient_count[ingredient] += 1
        for allergen in allergens:
            if allergen not in possible:
                possible[allergen] = ingredients.copy()
            else:
                possible[allergen] &= ingredients

    # print(possible)

    allergic = set()
    for allergens in possible.values():
        allergic.update(allergens)

    # print(allergic)

    save_count = sum([ingredient_count[ingredient] for ingredient in (ingredient_count.keys() - allergic)])
    print(f'Answer for part 1: {save_count}')

    dangerous_ingredients = set()
    allergens = []
    while len(allergens) < len(possible.keys()):
        for allergen, ingredients in possible.items():
            if len(ingredients - dangerous_ingredients) == 1:
                ingredient = list(ingredients - dangerous_ingredients)[0]
                allergens.append((allergen, ingredient))
                dangerous_ingredients.add(ingredient)
                break

    print(f'Answer for part 2: {",".join(allergen[1] for allergen in sorted(allergens))}')
