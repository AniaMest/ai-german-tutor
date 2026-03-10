import json
import random

def exercise_loader():
    with open("data/connectors.json") as file:
        return json.load(file)

def exercise_chooser(exercises):
    return random.choice(exercises)