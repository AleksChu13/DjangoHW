import copy
import re
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'ruff': {
        'пиво, мл': 500,
        'водка, мл': 40,
    }
    # можете добавить свои рецепты ;)
}


# View that will be activated for any of the recipes in DATA dict
# And would forward the recipe from the url to index.html (after updating values based on servings)
def recipes(request):
    servings = int(request.GET.get("servings", 1))
    path = request.get_full_path()
    recipe = copy.copy(DATA[re.search('/(.*)/', path).group(1)])
    recipe.update((x, y * servings) for x, y in recipe.items())

    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)


# View for unknown recipe
def error_404_view(request, exception):
    print('here')
    context = {
        'recipe': {}
    }
    return render(request, 'calculator/index.html', context)