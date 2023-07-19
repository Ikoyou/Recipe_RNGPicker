import json
import random


def recipe():
    with open('recipes.json') as raw_data:
        load_data = raw_data.read()
        new_data = json.loads(str(load_data))
        random_data = random.choice(new_data)
        return print(f"Name: {random_data['Name']}\nurl: {random_data['url']}"
                     f"\nIngredients: {str(random_data['Ingredients'])}"
                     f"\nInstructions: {str(random_data['Method'])}")


if __name__ == '__main__':
    recipe()
