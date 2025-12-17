
from Visual_settings import run_pygame_window


class Ingredient:
    def __init__(self, name, value, description=""):
        self.name = name
        self.value = value
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.value})"


class Recipe:
    def __init__(self, name, ingredients, result_value, comment=""):
        self.name = name
        self.ingredients = ingredients
        self.result_value = result_value
        self.comment = comment

    def matches(self, ingredient_list):
        return sorted(self.ingredients) == sorted(ingredient_list)


class AlchemyGame:
    def __init__(self):
        # ---- GAME STATE ----
        self.selected_ingridients_ = None
        self.state = "menu"

        # ---- INGREDIENTS ----
        self.ingredients = {
            "Water": Ingredient("Water", 0.1),
            "Honey": Ingredient("Honey", 4),
            "Vinegar": Ingredient("Vinegar", 6),
            "Sugar": Ingredient("Sugar", 7),
        }

        # ---- RECIPES ----
        self.recipes = [
            Recipe(
                "Bitter-sweet potion",
                ["Water", "Honey", "Vinegar"],
                16,
                "Sharp, sweet, and unstable."
            ),
            Recipe(
                "Sweet water",
                ["Water", "Sugar"],
                7.1,
                "Simple but pleasant."
            ),
        ]


        self.selected_ingredients = []
        self.last_result = None



    def start_game(self):
        self.state = "playing"
        self.selected_ingridient__
