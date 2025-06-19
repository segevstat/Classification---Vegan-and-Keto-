VEGAN_INGREDIENTS = [
    "tofu", "lentils", "beans", "chickpeas", "quinoa", "seeds", "nuts",
    "broccoli", "spinach", "kale", "carrots", "potatoes", "rice", "pasta"
]

NON_VEGAN_INGREDIENTS = [
    "chicken", "beef", "fish", "egg", "cheese", "milk", "butter", "honey", "yogurt"
]

KETO_INGREDIENTS = [
    "chicken", "beef", "fish", "eggs", "cheese", "butter", "olive oil", "avocado",
    "almonds", "spinach", "broccoli", "zucchini", "cauliflower"
]

HIGH_CARB_INGREDIENTS = [
    "sugar", "rice", "bread", "pasta", "potatoes", "corn", "beans", "bananas", "dates"
]

def is_ingredient_vegan(ingredient):
    ingredient = ingredient.lower()
    return not any(animal in ingredient for animal in NON_VEGAN_INGREDIENTS)

def is_ingredient_keto(ingredient):
    ingredient = ingredient.lower()
    return not any(carb in ingredient for carb in HIGH_CARB_INGREDIENTS)

def classify_recipe(ingredients):
    is_vegan = all(is_ingredient_vegan(ing) for ing in ingredients)
    is_keto = all(is_ingredient_keto(ing) for ing in ingredients)

    if is_vegan and is_keto:
        return "Vegan & Keto"
    elif is_vegan:
        return "Vegan"
    elif is_keto:
        return "Keto"
    else:
        return "Neither"
