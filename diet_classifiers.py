

VEGAN_INGREDIENTS = {
    "tofu", "lentils", "beans", "chickpeas", "quinoa", "seeds", "nuts",
    "broccoli", "spinach", "kale", "carrots", "potatoes", "rice", "pasta"
}

NON_VEGAN_INGREDIENTS = {
    "chicken", "beef", "fish", "egg", "eggs", "cheese", "milk", "butter", "honey", "yogurt"
}

KETO_INGREDIENTS = {
    "chicken", "beef", "fish", "egg", "eggs", "cheese", "butter", "olive oil", "avocado",
    "almonds", "spinach", "broccoli", "zucchini", "cauliflower"
}

HIGH_CARB_INGREDIENTS = {
    "sugar", "rice", "bread", "pasta", "potatoes", "potato", "corn", "beans", "bananas",
    "dates", "chickpeas", "quinoa", "lentils"
}


def is_ingredient_vegan(ingredient):
    ingredient = ingredient.lower().strip()
    return not any(non_vegan in ingredient for non_vegan in NON_VEGAN_INGREDIENTS)

def is_ingredient_keto(ingredient):
    ingredient = ingredient.lower().strip()
    return not any(high_carb in ingredient for high_carb in HIGH_CARB_INGREDIENTS)


def is_vegan_recipe(ingredients):
    return all(is_ingredient_vegan(ing) for ing in ingredients)

def is_keto_recipe(ingredients):
    return all(is_ingredient_keto(ing) for ing in ingredients)

def classify_recipe(ingredients):
    normalized_ingredients = [ing.lower().strip() for ing in ingredients]

    vegan = is_vegan_recipe(normalized_ingredients)
    keto = is_keto_recipe(normalized_ingredients)

    if vegan and keto:
        return "Vegan & Keto"
    elif vegan:
        return "Vegan"
    elif keto:
        return "Keto"
    else:
        return "Neither"


